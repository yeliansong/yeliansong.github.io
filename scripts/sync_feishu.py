#!/usr/bin/env python3
"""Sync one Feishu document into this static blog without third-party packages."""
from __future__ import annotations
import argparse, datetime as dt, json, os, re, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def request(url: str, data=None, token=None):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    if token: headers["Authorization"] = f"Bearer {token}"
    body = json.dumps(data).encode() if data else None
    with urllib.request.urlopen(urllib.request.Request(url, body, headers), timeout=30) as r:
        payload = json.load(r)
    if payload.get("code", 0) != 0:
        raise RuntimeError(payload.get("msg", "Feishu API error"))
    return payload

def tenant_token():
    payload = request("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal", {
        "app_id": os.environ["FEISHU_APP_ID"], "app_secret": os.environ["FEISHU_APP_SECRET"]})
    return payload["tenant_access_token"]

def document_text(document_id: str, token: str) -> str:
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{document_id}/raw_content?lang=0"
    return request(url, token=token)["data"]["content"]

def slugify(value: str) -> str:
    readable_slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value.lower()).strip("-")
    return readable_slug or "untitled"

def inline_md(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    return text

def main():
    p=argparse.ArgumentParser(); p.add_argument("--document-id", default=os.getenv("FEISHU_DOCUMENT_ID")); p.add_argument("--slug"); p.add_argument("--draft", action="store_true"); args=p.parse_args()
    if not args.document_id: raise SystemExit("Missing --document-id or FEISHU_DOCUMENT_ID")
    content=inline_md(document_text(args.document_id, tenant_token()))
    lines=content.splitlines()
    title=next((x.strip().lstrip("# ") for x in lines if x.strip()), "未命名文章")
    first=next((i for i,x in enumerate(lines) if x.strip()), 0)
    body="\n".join(lines[first+1:]).strip()
    slug=args.slug or f"{dt.date.today().isoformat()}-{slugify(title)}"
    target=ROOT / ("drafts" if args.draft else slug); target.mkdir(parents=True, exist_ok=True)
    markdown_content=f"# {title}\n\n{body}\n"
    (target/"index.md").write_text(markdown_content, encoding="utf-8")
    print(target.relative_to(ROOT))
if __name__ == "__main__": main()
