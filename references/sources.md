# 工具演进与规范来源

本文件集中记录 `blender-tutorial-scout` 的路由契约、教程深读库配套约定、活跃索引的建立背景与检索工具演进脉络，供查溯时核对。

## 公共路由与部门依据

- **公共目录入口**：运行 `& './blenderctl.ps1' discover --product research` 实时查看研究类产品配置、当前支持宿主版本、`scope_reference`（`tutorial-library`）以及关联技能（`blender-modeling-reference`、`simready-hard-surface-research`）。
- **所属部门卡**：[前期参考部门](https://github.com/tsist/blender-ai-workflow/blob/main/skills/blender-work-methodology/references/departments/reference.md)。
- **项目总纲约定**：`<PROJECT_ROOT>/AGENTS.md` 中的「参考复现四步法（先查本地 → 挑 1–3 个成熟教程 → 实机复现 → 同机位对照）」与「免费开源工具优先阶梯」。

## 本地教程深读库与活跃数据索引

- **本地教程深读库**：`<PROJECT_ROOT>/tutorial-library/README.md` 与 `<PROJECT_ROOT>/tutorial-library/_INDEX.md`（2026-11-06 建立）。深读库存放完整精读后的步骤笔记，确立了「Blender 5.x 新版本优先、4.x 其次、更早版本补位标差」以及「明确标注原作者出处与授权边界」的收录纪律。
- **主索引与名录演进**：`references/resource-index.md` 与 `references/up-directory.md` 属于项目活跃主索引数据，自 2026-10-24 首轮材质域普查起持续增补，目前已陆续覆盖材质纹理、UV 与烘焙、几何节点、绑定动画、三渲二与硬表面等多个制作领域。

## B 站检索工具演进记录

- **早期批次经验（2026-10-24 至 2026-10-26）**：材质域、几何节点域、绑定动画域与三渲二域普查期间，曾通过 `bili-cli` 与直连接口检索，连续访问作者页与视频详情接口时遇到 B 站 412 风控拦截，由此沉淀出「单次会话控量查重点作者主页」和「通用搜索引擎按 BV 号与标题片段双模反查」两套实证对策。
- **当前统一检索通道**：B 站公开视频与作者检索现统一走 `opencli bilibili` 子命令族（`search`、`video`、`subtitle`、`summary`、`comments`、`user-videos`），经浏览器会话读取页面元数据与字幕；遇到单端限流或课程卡片缺 BV 号时，配合通用搜索引擎反查补齐核验依据。
