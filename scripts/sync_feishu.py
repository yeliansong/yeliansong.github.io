#!/usr/bin/env python3
"""Sync one Feishu document into this static blog without third-party packages."""
from __future__ import annotations
import argparse, datetime as dt, json, os, re, urllib.error, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def request(url: str, data=None, token=None):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    if token: headers["Authorization"] = f"Bearer {token}"
    body = json.dumps(data).encode() if data else None
    try:
        with urllib.request.urlopen(urllib.request.Request(url, body, headers), timeout=30) as r:
            payload = json.load(r)
    except urllib.error.HTTPError as error:
        # Lark returns useful API error details in the response body even for
        # HTTP 4xx responses. Surface them in Actions instead of a bare 400.
        try:
            payload = json.load(error)
        except (json.JSONDecodeError, UnicodeDecodeError):
            raise RuntimeError(f"Lark API HTTP {error.code}: {error.reason}") from error
        raise RuntimeError(
            f"Lark API error {payload.get('code', error.code)}: "
            f"{payload.get('msg', error.reason)}"
        ) from error
    if payload.get("code", 0) != 0:
        raise RuntimeError(payload.get("msg", "Feishu API error"))
    return payload

def api_base(platform: str) -> str:
    return "https://open.larksuite.com" if platform == "lark" else "https://open.feishu.cn"

def tenant_token(platform: str):
    payload = request(f"{api_base(platform)}/open-apis/auth/v3/tenant_access_token/internal", {
        "app_id": os.environ["FEISHU_APP_ID"], "app_secret": os.environ["FEISHU_APP_SECRET"]})
    return payload["tenant_access_token"]

def resolve_wiki_document(wiki_token: str, token: str, platform: str) -> str:
    # Tokens copied from /wiki/<token> URLs must explicitly be identified as
    # Wiki node tokens. Otherwise Lark responds with HTTP 400.
    query = urllib.parse.urlencode({"token": wiki_token, "obj_type": "wiki"})
    url = f"{api_base(platform)}/open-apis/wiki/v2/spaces/get_node?{query}"
    node = request(url, token=token)["data"]["node"]
    if node.get("obj_type") != "docx":
        raise RuntimeError(f"Wiki node is {node.get('obj_type')}, not a docx document")
    return node["obj_token"]

def block_text(value: dict) -> str:
    parts = []
    for element in value.get("elements", []):
        run = element.get("text_run")
        if not run: continue
        content = run.get("content", "")
        link = run.get("text_element_style", {}).get("link", {}).get("url")
        parts.append(f"[{content}]({link})" if link else content)
    return "".join(parts).strip()

def document_markdown(document_id: str, token: str, platform: str) -> tuple[str, str, dict[str, str]]:
    blocks, page_token = [], None
    while True:
        params = {"page_size": 500}
        if page_token: params["page_token"] = page_token
        url = f"{api_base(platform)}/open-apis/docx/v1/documents/{document_id}/blocks?{urllib.parse.urlencode(params)}"
        data = request(url, token=token)["data"]
        blocks.extend(data.get("items", []))
        if not data.get("has_more"): break
        page_token = data["page_token"]
    title, lines, metadata = "未命名文章", [], {}

    def add_text(value: str, prefix: str = ""):
        if not value:
            return
        match = re.match(r"^(分类|标签|摘要|category|tags|summary)\s*[:：]\s*(.+)$", value, re.I)
        if match:
            keys = {"分类": "category", "标签": "tags", "摘要": "summary"}
            metadata[keys.get(match.group(1).lower(), match.group(1).lower())] = match.group(2).strip()
            return
        lines.append(prefix + value)

    for block in blocks:
        kind = block.get("block_type")
        if kind == 1:
            title = block_text(block.get("page", {})) or title
        elif kind == 2:
            value = block_text(block.get("text", {}))
            add_text(value)
        elif 3 <= kind <= 11:
            level = min(kind - 2, 6)
            value = block_text(block.get(f"heading{kind - 2}", {}))
            if value: lines.append(f"{'#' * level} {value}")
        elif kind == 12:
            value = block_text(block.get("bullet", {}))
            if value: lines.append(f"- {value}")
        elif kind == 13:
            value = block_text(block.get("ordered", {}))
            if value: lines.append(f"1. {value}")
        elif kind == 14:
            value = block_text(block.get("code", {}))
            if value: lines.append(f"```\n{value}\n```")
        elif kind == 15:
            value = block_text(block.get("quote", {}))
            add_text(value, "> ")
        elif kind == 22:
            lines.append("---")
        elif kind == 27:
            lines.append("<!-- Lark image: pending media sync -->")
    return title, "\n\n".join(lines).strip(), metadata

def slugify(value: str) -> str:
    readable_slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value.lower()).strip("-")
    return readable_slug or "untitled"

def inline_md(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    return text

def main():
    p=argparse.ArgumentParser(); p.add_argument("--document-id", default=os.getenv("FEISHU_DOCUMENT_ID")); p.add_argument("--wiki-token"); p.add_argument("--platform", choices=["feishu","lark"], default="feishu"); p.add_argument("--slug"); p.add_argument("--category"); p.add_argument("--tags"); p.add_argument("--summary"); p.add_argument("--draft", action="store_true"); args=p.parse_args()
    if not args.document_id and not args.wiki_token: raise SystemExit("Missing --document-id, --wiki-token, or FEISHU_DOCUMENT_ID")
    token=tenant_token(args.platform)
    document_id=resolve_wiki_document(args.wiki_token, token, args.platform) if args.wiki_token else args.document_id
    title, body, metadata=document_markdown(document_id, token, args.platform)
    for key, value in {"category": args.category, "tags": args.tags, "summary": args.summary}.items():
        if value and key not in metadata: metadata[key] = value
    slug=args.slug or f"{dt.date.today().isoformat()}-{slugify(title)}"
    target=ROOT / ("drafts" if args.draft else slug); target.mkdir(parents=True, exist_ok=True)
    front_matter = ""
    if metadata:
        front_matter = "---\n" + "\n".join(f"{key}: {value}" for key, value in metadata.items()) + "\n---\n\n"
    markdown_content=f"{front_matter}# {title}\n\n{body}\n"
    (target/"index.md").write_text(markdown_content, encoding="utf-8")
    print(target.relative_to(ROOT))
if __name__ == "__main__": main()
