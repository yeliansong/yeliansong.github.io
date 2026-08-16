#!/usr/bin/env python3
"""Build the whole blog from the Markdown files without Hugo or a theme."""
from __future__ import annotations

import datetime as dt
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {"drafts", ".git", "node_modules"}


def clean_output(value: str) -> str:
    return "\n".join(line.replace("\t", "    ").rstrip() for line in value.splitlines()) + "\n"


def inline(value: str) -> str:
    value = html.escape(value, quote=False)
    value = re.sub(r"!\[([^]]*)\]\(([^ )]+)(?:\s+&quot;.*?&quot;)?\)", r'<img src="\2" alt="\1" loading="lazy">', value)
    value = re.sub(r"\[([^]]+)\]\(([^ )]+)(?:\s+&quot;.*?&quot;)?\)", r'<a href="\2">\1</a>', value)
    value = re.sub(r"&lt;(https?://[^&]+)&gt;", r'<a href="\1">\1</a>', value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", value)
    return value


def markdown(md: str) -> str:
    lines = md.replace("\r\n", "\n").splitlines()
    out, paragraph, quote, list_kind = [], [], [], None
    in_code, code_lang, code = False, "", []

    def flush_paragraph():
        if paragraph:
            out.append("<p>" + inline(" ".join(x.strip() for x in paragraph)) + "</p>")
            paragraph.clear()

    def flush_quote():
        if quote:
            out.append("<blockquote>" + "<br>".join(inline(x) for x in quote) + "</blockquote>")
            quote.clear()

    def close_list():
        nonlocal list_kind
        if list_kind:
            out.append(f"</{list_kind}>")
            list_kind = None

    for raw in lines:
        line = raw.rstrip()
        fence = re.match(r"^```\s*([\w+-]*)", line)
        if fence:
            flush_paragraph(); flush_quote(); close_list()
            if in_code:
                out.append(f'<pre><code class="language-{html.escape(code_lang)}">{html.escape(chr(10).join(code))}</code></pre>')
                code.clear(); in_code = False
            else:
                in_code = True; code_lang = fence.group(1)
            continue
        if in_code:
            code.append(line); continue
        if not line.strip() or line.strip().lower() == "<br>":
            flush_paragraph(); flush_quote(); close_list(); continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_paragraph(); flush_quote(); close_list()
            level = len(heading.group(1)); label = heading.group(2).strip()
            anchor = re.sub(r"[^\w\u4e00-\u9fff]+", "-", label.lower()).strip("-")
            out.append(f'<h{level} id="{anchor}">{inline(label)}</h{level}>'); continue
        item = re.match(r"^\s*[-*+]\s+(.+)$", line)
        numbered = re.match(r"^\s*\d+[.)]\s+(.+)$", line)
        if item or numbered:
            flush_paragraph(); flush_quote()
            desired = "ul" if item else "ol"
            if list_kind != desired:
                close_list(); out.append(f"<{desired}>"); list_kind = desired
            out.append(f"<li>{inline((item or numbered).group(1))}</li>"); continue
        if line.startswith(">"):
            flush_paragraph(); close_list(); quote.append(line.lstrip("> ")); continue
        if re.match(r"^(-{3,}|\*{3,})$", line.strip()):
            flush_paragraph(); flush_quote(); close_list(); out.append("<hr>"); continue
        if line.lstrip().startswith("<img "):
            flush_paragraph(); flush_quote(); close_list()
            cleaned = re.sub(r'\sstyle="[^"]*"', "", line.strip())
            cleaned = cleaned.replace("<img ", '<img loading="lazy" ')
            out.append(f'<figure>{cleaned}</figure>'); continue
        if line.lstrip().startswith(("<div", "</div", "<table", "</table", "<thead", "</thead", "<tbody", "</tbody", "<tr", "</tr", "<th", "</th", "<td", "</td")):
            flush_paragraph(); flush_quote(); close_list(); out.append(line); continue
        paragraph.append(line)
    flush_paragraph(); flush_quote(); close_list()
    if in_code:
        out.append(f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
    return "\n".join(out)


def plain(md: str) -> str:
    value = re.sub(r"```.*?```", " ", md, flags=re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"!?(\[([^]]*)\])\([^)]*\)", r"\2", value)
    value = re.sub(r"[#>*_`~-]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def front_matter(md: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", md, re.S)
    if not match:
        return {}, md
    metadata = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip().lower()] = value.strip()
    return metadata, md[match.end():]


def get_title(md: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", md, re.M)
    return match.group(1).strip() if match else fallback


def get_date(path: Path) -> dt.date:
    match = re.match(r"(20\d{2})[-_](\d{1,2})[-_](\d{1,2})", path.parent.name)
    if match:
        try: return dt.date(*map(int, match.groups()))
        except ValueError: pass
    return dt.date(2020, 1, 1)


def topic(title: str, path: str) -> tuple[str, str]:
    text = (title + " " + path).lower()
    if any(x in text for x in ["日本", "旅游", "旅行", "三体", "月亮和六便士", "平凡的世界", "健康", "住房"]):
        return "生活与阅读", "Life"
    if any(x in text for x in ["k8s", "kubernetes", "docker", "容器", "pod", "deployment", "configmap", "secret", "volume", "cka"]):
        return "云原生", "Cloud Native"
    if any(x in text for x in ["linux", "inode", "lsof", "网络", "http", "nginx", "prometheus", "grafana", "ansible", "运维"]):
        return "系统与运维", "Systems"
    return "工具与编程", "Tools"


def shell(title: str, description: str, body: str, page_class="", lang="zh-CN") -> str:
    safe_title, safe_desc = html.escape(title), html.escape(description[:160], quote=True)
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{safe_title} · 叶连松</title><meta name="description" content="{safe_desc}">
<meta property="og:title" content="{safe_title}"><meta property="og:description" content="{safe_desc}"><meta property="og:type" content="article">
<link rel="stylesheet" href="/css/blog.css"><script defer src="/js/blog.js"></script></head>
<body class="{page_class}"><header class="topbar"><a class="wordmark identity" href="/" aria-label="Liansong Ye's blog"><span class="identity-mark">LY</span><span class="identity-copy"><b>LIANSONG YE</b><small>WORK / LIFE / BOOKS</small></span></a>
<nav><a href="/posts/">文章</a><a href="/categories/">主题</a><a href="/about/">关于</a></nav>
<button class="theme-toggle" type="button" aria-label="切换明暗模式">◐</button></header>
{body}
<footer class="site-footer"><div><b>LIANSONG YE</b><p>记录工作、生活与读书。</p></div><div class="footer-network"><div><span>CONNECT</span><nav><a href="https://github.com/yeliansong">GitHub</a><a href="https://www.linkedin.com/in/liansongye">LinkedIn</a><a href="mailto:ylsccnu@hotmail.com">Email</a></nav></div><div><span>ELSEWHERE</span><nav><a href="https://www.youtube.com/@xiaoye_SG/featured">YouTube</a><a href="https://space.bilibili.com/454920574">Bilibili</a><a href="https://juejin.cn/user/3659627025959112">掘金</a></nav></div></div><small>© 2026 · Keep writing.</small></footer></body></html>'''


def article_page(item: dict) -> str:
    content = markdown(item["md"])
    content = re.sub(r"<h1[^>]*>.*?</h1>", "", content, count=1, flags=re.S)
    tags = "".join(f"<span>{html.escape(tag)}</span>" for tag in item.get("tags", []))
    tag_row = f'<div class="article-tags">{tags}</div>' if tags else ""
    hero = f'''<main class="article-layout"><aside class="article-rail"><a href="/posts/">← 全部文章</a><span>{item['date'].year}</span></aside>
<article class="prose"><header class="article-head"><p class="kicker">{item['topic_en']} / {item['date'].isoformat()}</p><h1>{html.escape(item['title'])}</h1><p class="dek">{html.escape(item['excerpt'])}</p>{tag_row}</header>{content}
<div class="article-end"><span>END</span><a href="/posts/">继续阅读 →</a></div></article></main>'''
    return shell(item["title"], item["excerpt"], hero, "article-page")


def cards(items: list[dict]) -> str:
    return "\n".join(f'''<a class="post-card" href="/{x['url']}/" data-search="{html.escape((x['title']+' '+x['topic']).lower(), quote=True)}"><span class="post-date">{x['date'].strftime('%Y.%m.%d')}</span><div><small>{x['topic_en']}</small><h2>{html.escape(x['title'])}</h2><p>{html.escape(x['excerpt'])}</p></div><b>↗</b></a>''' for x in items)


def redirect_page(target: str) -> str:
    safe = html.escape(target, quote=True)
    return clean_output(f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url={safe}"><link rel="canonical" href="{safe}"><title>正在前往新页面 · 叶连松</title><link rel="stylesheet" href="/css/blog.css"></head><body><main class="not-found"><p class="kicker">PAGE MOVED / 页面已迁移</p><h1>正在前往新页面。</h1><p>博客已经完成改版，这个旧入口会带你前往新的内容页面。</p><a class="button" href="{safe}">立即前往 →</a></main></body></html>''')


def replace_legacy_pages():
    replaced = 0
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts: continue
        current = path.read_text(encoding="utf-8", errors="replace")
        if "LoveIt" not in current and "theme.min.js" not in current: continue
        parts = set(rel.parts)
        if "categories" in parts or "tags" in parts: target = "/categories/"
        elif "posts" in parts or "page" in parts or rel.parts[0] == "en": target = "/posts/"
        else: target = "/"
        path.write_text(redirect_page(target), encoding="utf-8"); replaced += 1
    for rel, target in [("en/about/index.html", "/about/"), ("en/start/index.html", "/start/")]:
        path = ROOT / rel; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(redirect_page(target), encoding="utf-8")
    return replaced


def build():
    items = []
    for path in ROOT.rglob("index.md"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_PARTS for part in rel.parts) or rel.parts[0] in {"about", "start"}: continue
        raw_md = path.read_text(encoding="utf-8", errors="replace")
        metadata, md = front_matter(raw_md)
        title = get_title(md, path.parent.name)
        inferred_category, inferred_category_en = topic(title, str(rel))
        category = metadata.get("category", inferred_category)
        category_en = "Work & Life" if category == "工作与生活" else inferred_category_en
        summary_source = re.sub(r"^#{1,6}\s+.*$", "", md, flags=re.M)
        quoted_summary = re.search(r"^>\s*(.+)$", md, re.M)
        summary = metadata.get("summary") or (plain(quoted_summary.group(1)) if quoted_summary else plain(summary_source)[:145].rstrip("，。； ") + "。")
        tags = [x.strip() for x in re.split(r"[,，、]", metadata.get("tags", "")) if x.strip()]
        url = str(path.parent.relative_to(ROOT))
        item = {"path": path, "md": md, "title": title, "date": get_date(path), "topic": category, "topic_en": category_en, "tags": tags, "excerpt": summary, "url": url}
        items.append(item)
        path.with_name("index.html").write_text(clean_output(article_page(item)), encoding="utf-8")
    zh_items = sorted([x for x in items if not x["url"].startswith("en/")], key=lambda x: x["date"], reverse=True)

    intro = '''<main class="listing"><header class="listing-head"><p class="kicker">ARCHIVE / 文章归档</p><h1>写下来的，<br><em>才真正留下来。</em></h1><p>技术实践、阅读笔记、旅途见闻，以及那些值得回头再看的思考。</p></header><div class="filter"><label for="post-search">搜索文章</label><input id="post-search" type="search" placeholder="输入标题或主题…" autocomplete="off"><span id="post-count"></span></div><section class="post-grid" id="post-grid">'''
    posts = intro + cards(zh_items) + "</section></main>"
    (ROOT/"posts").mkdir(exist_ok=True); (ROOT/"posts/index.html").write_text(clean_output(shell("所有文章", "叶连松的全部文章", posts, "listing-page")), encoding="utf-8")

    groups = {}
    for item in zh_items: groups.setdefault(item["topic"], []).append(item)
    topic_blocks = "".join(f'''<section class="topic-block"><div><span>{i:02d}</span><h2>{html.escape(name)}</h2><p>{len(group)} 篇文章</p></div><div>{cards(group)}</div></section>''' for i,(name,group) in enumerate(groups.items(),1))
    topics_body = f'''<main class="topics"><header class="listing-head"><p class="kicker">TOPICS / 主题</p><h1>沿着兴趣，<br><em>建立自己的知识地图。</em></h1></header>{topic_blocks}</main>'''
    for folder in ["categories", "tags"]:
        (ROOT/folder).mkdir(exist_ok=True); (ROOT/folder/"index.html").write_text(clean_output(shell("主题", "按主题浏览文章", topics_body, "topics-page")), encoding="utf-8")

    for folder, eyebrow in [("about", "ABOUT / 关于"), ("start", "START HERE / 开始阅读")]:
        md_path = ROOT/folder/"index.md"
        if md_path.exists():
            md = md_path.read_text(encoding="utf-8"); title = get_title(md, folder)
            rendered = re.sub(r"<h1[^>]*>.*?</h1>", "", markdown(md), count=1, flags=re.S)
            body = f'''<main class="page-layout"><header><p class="kicker">{eyebrow}</p><h1>{html.escape(title)}</h1></header><article class="prose">{rendered}</article></main>'''
            (md_path.with_name("index.html")).write_text(clean_output(shell(title, plain(md)[:150], body, "content-page")), encoding="utf-8")

    not_found = '''<main class="not-found"><p class="kicker">ERROR / 404</p><strong>404</strong><h1>这一页不在这里。</h1><p>也许链接已经改变，或者它还没有被写下来。</p><a class="button" href="/">返回首页 →</a></main>'''
    (ROOT/"404.html").write_text(clean_output(shell("页面未找到", "页面未找到", not_found, "error-page")), encoding="utf-8")
    (ROOT/"site-index.json").write_text(json.dumps([{k:(v.isoformat() if isinstance(v,dt.date) else v) for k,v in x.items() if k not in {"md","path"}} for x in zh_items], ensure_ascii=False, indent=2), encoding="utf-8")
    replaced = replace_legacy_pages()
    print(f"Built {len(items)} article pages, {len(zh_items)} Chinese archive entries, and replaced {replaced} legacy pages")


if __name__ == "__main__": build()
