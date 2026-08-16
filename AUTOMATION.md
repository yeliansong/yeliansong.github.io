# 博客写作与发布流程

## 飞书文档一键发布

1. 在飞书开放平台创建企业自建应用，开通 `docx:document:readonly` 权限并发布应用。
2. 把要发布的文档分享给该应用，记下文档 URL 中的 document ID。
3. 在 GitHub 仓库 `Settings → Secrets and variables → Actions` 新增 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET`。
4. 打开 GitHub Actions 的 **Sync Feishu article**，点击 **Run workflow**，填入 document ID。

流水线会保留一份 `index.md` 内容源，调用全站生成器创建文章页并更新文章归档。建议飞书第一行直接写文章标题，正文使用普通段落；需要明确层级时，可以直接输入 `## 二级标题`、`### 三级标题`、`- 列表` 和 Markdown 代码块。

当前同步使用飞书/Lark 文档块接口，可以保留正文、标题、列表、引用和代码块；飞书中直接粘贴的图片暂时不会被下载。含图片的文章请先使用公开图床 URL，以 Markdown 图片语法插入，或发布前在仓库中补充图片。

## Lark Wiki 每日反思日记

仓库中的 **Sync daily reflections** 工作流会在每周日 09:00（新加坡时间）同步 Lark Wiki 节点 `Z32cwpqSdiyhmSkLTnVlmP4zgUd`，并持续更新同一个博客页面。需要在 GitHub Actions Secrets 中配置 `LARK_APP_ID` 和 `LARK_APP_SECRET`，应用需拥有 Wiki 节点读取权限与 `docx:document:readonly` 权限。

日记属于高隐私内容。推荐将工作流的 Wiki token 指向单独的“每日反思日记（公开版）”，仅放入确认可以公开的内容。当前文档内的图片会写入待同步标记，不会自动公开或下载。

## 每周文章机制

推荐每周生成“候选草稿”，不要自动发布。选题应来自真实积累：一次故障、一个架构取舍、一个工具的使用边界、一本书或一段旅途感受。自动生成后先检查事实、删除空泛表述、补充自己的判断，再通过上面的飞书流程发布。

推荐结构：真实场景 → 问题与约束 → 排查/决策过程 → 方案 → 结果与复盘 → 可复用清单。

## 内容分类

只保留三个一级入口，避免重新产生标签债务：

- Engineering：SRE、云原生、Linux、网络、自动化
- Career：职业经历、面试、技能成长
- Life：旅行、阅读和新加坡生活
