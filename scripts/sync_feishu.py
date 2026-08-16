#!/usr/bin/env python3
"""Sync one Feishu document into this static blog without third-party packages."""
from __future__ import annotations
import argparse, datetime as dt, html, json, os, re, urllib.request
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
    ascii_slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return ascii_slug or dt.date.today().isoformat()

def inline_md(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    return text

def render_markdown(md: str, title: str, description: str) -> str:
    lines, out, in_code, list_open = md.splitlines(), [], False, False
    def close_list():
        nonlocal list_open
        if list_open: out.append("</ul>"); list_open = False
    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            close_list(); out.append("</code></pre>" if in_code else "<pre><code>"); in_code = not in_code; continue
        if in_code: out.append(html.escape(line)+"\n"); continue
        if not line: close_list(); continue
        if line.startswith("### "): close_list(); out.append(f"<h3>{html.escape(line[4:])}</h3>")
        elif line.startswith("## "): close_list(); out.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("# "): close_list(); out.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif re.match(r"^[-*] ", line):
            if not list_open: out.append("<ul>"); list_open=True
            out.append(f"<li>{html.escape(line[2:])}</li>")
        else: close_list(); out.append(f"<p>{html.escape(line)}</p>")
    close_list()
    body="\n".join(out)
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · 叶连松</title><meta name="description" content="{html.escape(description)}"><link rel="stylesheet" href="/css/article.css"></head><body><header><a href="/">YL.</a><nav><a href="/posts/">所有文章</a><a href="/about/">关于</a></nav></header><main><article><p class="kicker">ENGINEERING NOTES</p>{body}</article></main><footer>© {dt.date.today().year} 叶连松 · SRE / DevOps Engineer</footer></body></html>'''

def main():
    p=argparse.ArgumentParser(); p.add_argument("--document-id", default=os.getenv("FEISHU_DOCUMENT_ID")); p.add_argument("--slug"); p.add_argument("--draft", action="store_true"); args=p.parse_args()
    if not args.document_id: raise SystemExit("Missing --document-id or FEISHU_DOCUMENT_ID")
    content=inline_md(document_text(args.document_id, tenant_token()))
    title=next((x.lstrip("# ") for x in content.splitlines() if x.strip()), "未命名文章")
    slug=args.slug or f"{dt.date.today().isoformat()}-{slugify(title)}"
    target=ROOT / ("drafts" if args.draft else slug); target.mkdir(parents=True, exist_ok=True)
    front=f'---\ntitle: "{title.replace(chr(34), chr(39))}"\ndate: {dt.date.today().isoformat()}\ndraft: {str(args.draft).lower()}\nsource: feishu\n---\n\n'
    (target/"index.md").write_text(front+content+"\n", encoding="utf-8")
    if not args.draft: (target/"index.html").write_text(render_markdown(content,title,content[:150]),encoding="utf-8")
    print(target.relative_to(ROOT))
if __name__ == "__main__": main()
