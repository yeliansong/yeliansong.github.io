# 博客写作与发布流程

## 飞书文档一键发布

1. 在飞书开放平台创建企业自建应用，开通 `docx:document:readonly` 权限并发布应用。
2. 把要发布的文档分享给该应用，记下文档 URL 中的 document ID。
3. 在 GitHub 仓库 `Settings → Secrets and variables → Actions` 新增 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET`。
4. 打开 GitHub Actions 的 **Sync Feishu article**，点击 **Run workflow**，填入 document ID。

流水线会保留一份 `index.md` 内容源，并生成 GitHub Pages 可直接访问的 `index.html`。建议飞书首行为 `# 文章标题`，正文使用标题、段落、列表和代码块。

## 每周文章机制

推荐每周生成“候选草稿”，不要自动发布。选题应来自真实积累：一次故障、一个架构取舍、一个工具的使用边界、一本书或一段旅途感受。自动生成后先检查事实、删除空泛表述、补充自己的判断，再通过上面的飞书流程发布。

推荐结构：真实场景 → 问题与约束 → 排查/决策过程 → 方案 → 结果与复盘 → 可复用清单。

## 内容分类

只保留三个一级入口，避免重新产生标签债务：

- Engineering：SRE、云原生、Linux、网络、自动化
- Career：职业经历、面试、技能成长
- Life：旅行、阅读和新加坡生活
