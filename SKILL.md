---
name: blender-tutorial-scout
description: 先查本地教程深读库与已有索引，缺细分做法时用 opencli 定向检索 B 站高质量中文原创教程与公开课，并按版本新旧与可信度分级登记。遇到陌生 Blender 工艺、需要补充中文实战参考，或更新 UP 主名录与资源索引时使用。
metadata:
  version: "1.0.0"
---

# Blender 中文教程检索与分级

本技能属于 [前期参考部门](https://github.com/tsist/blender-ai-workflow/blob/main/skills/blender-work-methodology/references/departments/reference.md)，负责帮制作环节快速找到能直接照着复现的中文 Blender 教程，并持续维护项目里的 UP 主名录与主题资源索引。动手搜网前先查本地沉淀，把查到的高质量新资源按版本和可信度入库，后面做同类作品就能直接取用。

## 怎么做

### 第一步：先查本地深读库、共享 Wiki 与已有索引

先翻已有积累，再决定要不要联网找新片。本地已经整理透的工艺直接拿来用，省下重复翻视频的时间。

1. **查本地教程深读库**：打开 `<PROJECT_ROOT>/tutorial-library/_INDEX.md` 和对应专题目录，看目标工艺是否已有完整步骤笔记。
2. **查共享 Wiki**：对常用规范和已验节点参数，顺手查共享 Wiki 里的沉淀条目。
3. **查本技能主索引**：读 [资源索引](references/resource-index.md) 和 [UP 主名录](references/up-directory.md)。命中 A 级或 B 级且近半年内核验过的条目，直接挑出 1–3 条交给下游，用完顺手补一行核验注记。
4. **查公共研究路由**：需要确认当前宿主版本或同部门关联技能时，运行一次公共目录命令：

```powershell
& './blenderctl.ps1' discover --product research
```

### 第二步：用 `opencli bilibili` 定向检索 B 站缺口

本地库和主索引缺某道细分中文工艺时，用「软件词 + 工艺中文词 + 英文术语原词或深度词」组合检索。中文区高水平教学的标题常保留英文节点名或术语原词，混搜更容易落到硬核实操。

```powershell
# 按关键词搜视频或作者
opencli bilibili search "Blender 5 几何节点 散布 实操" --type video --limit 20 -f json
opencli bilibili search "目标UP主名" --type user --limit 10 -f json

# 查视频元数据：作者、分P结构、时长、播放与收藏数
opencli bilibili video BVxxxxxxxxxx --page 1 -f json

# 读字幕或官方分段大纲，快速判断步骤完整性与演示版本
opencli bilibili subtitle BVxxxxxxxxxx --page 1 -f plain
opencli bilibili summary BVxxxxxxxxxx -f yaml

# 查高赞和置顶评论：找工程文件链接、插件清单与版本勘误
opencli bilibili comments BVxxxxxxxxxx --limit 20 -f json

# 命中好老师后，按收藏排序翻他的系列合集（单次控量查一两位重点作者）
opencli bilibili user-videos <UID> --order stow --limit 20 -f json
```

遇到单条页面限流或搜索卡片缺少 BV 号时，转用通用搜索引擎按 `site:bilibili.com` 或「BV 号 + 标题片段」反查作者名、分 P 集数与互动数据。找公开课或到期免费开放课程时，优先选官方账号或原作者主页发布的免费全集。更多搜词矩阵和细分领域选词法见 [检索策略手册](references/search-playbook.md)。

### 第三步：按版本新旧、原创可信度与免费工具原则分级

拿到候选视频后，先排版本新旧，再评原创可信度，同时筛查工具依赖：

1. **版本新旧排第一**：优先选 `Blender 5.x` 教程，其次选 `4.x` 教程。更早版本留在对应细分领域尚无新版时补位，并在备注栏标清和 `5.x` 的差异点（如新阵列修改器、法线修改器顺序或节点改名）。
2. **免费开源优先，商业付费插件显式隔离**：优先推荐靠 Blender 原生功能或免费开源插件完成的教程。遇到依赖商业付费插件的教程，在备注栏写清插件名称并标注「含商业付费插件，已隔离」，提示下游改走原生或免费开源替代方案。
3. **原创可信度分级**：结合收藏播放比（高于 5% 是强信号）、步骤完整度、工程文件与作者实绩归档：

| 分级 | 判定标准 | 使用方式 |
| --- | --- | --- |
| **A 级** | 原作者或职业讲师的完整系列课或系统实操，步骤可复现、附工程文件或参数全露出、适配 `5.x` 或写清版本差异（官方标杆与顶级工作室完整课可记为 **S 级**） | 作为主参考交下游直接复现，经实机验证后可写入共享 Wiki |
| **B 级** | 原创单集实操，步骤连贯、参数清晰，能跟着跑通某一道具体工序或排错技巧 | 作为单点辅助参考，配合主工艺对照使用 |
| **C 级** | 片段展示、版本跨度大且缺适配说明、未授权汉化搬运或强依赖付费商业插件的教程 | 作为线索留存：备注栏写明原作者与原课程出处，或标注付费插件隔离说明，方便后续追查原版或免费替代做法 |

核验满半年的旧条目，再次选用前跑一次 `opencli bilibili video` 确认链接有效与版本适配，更新核验日期。

### 第四步：登记回主索引与 UP 主名录

每条新登记资源备齐 URL 或 BV 号、核验日期和至少两项验证依据（时长、分 P 数、收藏比、工程文件有无、版本说明或置顶评论要点），再追加写入现有数据文件：

1. **写入主题资源索引**：打开 [references/resource-index.md](references/resource-index.md)，按顶部既定列格式追加到对应主题分节（材质纹理、UV 与烘焙、雕刻、几何节点、灯光渲染、绑定动画、剪辑合成、全流程与其他）。
2. **写入 UP 主名录**：打开 [references/up-directory.md](references/up-directory.md)，补充新发现作者的主页链接、专长领域、代表作、分级、核验依据与核验日期；已有作者跨领域产出新好课，在原卡片下追加一条领域增补记录。
3. **保留历史轨迹**：遇到失效或搬家链接，在原条目补记 `dead` 或 `moved` 状态标签并保留原行；作者分级升降时保留旧记录并补一行变化原因。
4. **控制单轮研究边界**：一轮检索筛出 1–3 篇可直接照做的优质教程就收手，把时间留给实机复现。

## 交给下游

向 [前期参考部门](https://github.com/tsist/blender-ai-workflow/blob/main/skills/blender-work-methodology/references/departments/reference.md) 或对应制作部门交付一份精简的**教程参考清单**，每条包含：

- 教程标题、UP 主、BV 号或直链、适用 Blender 版本与评级（S/A/B/C）。
- 从字幕或分段大纲提炼出的核心工序要点与关键时间段。
- 涉及的免费开源工具说明；含搬运出处或商业付费插件隔离项的，在条目旁醒目标注。

下游拿到清单后，先在项目当前宿主里挑一个最小样例复现，同机位对照参考图确认效果。值得长期反复查阅的长课，按深读模板整理进 `<PROJECT_ROOT>/tutorial-library/`；经过实机复现验证的稳定工艺，再沉淀到共享 Wiki。

## 例子：为机械表拉丝表盘补找 5.x 中文材质教程

接到前期参考请求：建模和材质部门准备做一件复古机械表，想确认表盘同心拉丝各向异性材质在 `Blender 5.x` 下的原生节点接法。

1. **先查本地**：翻看 `<PROJECT_ROOT>/tutorial-library/_INDEX.md` 和 [references/resource-index.md](references/resource-index.md)，硬表面加权法线已有现成深读笔记，但缺「同心拉丝各向异性节点」的 `5.x` 中文实操。
2. **定向检索**：运行 `opencli bilibili search "Blender 5 拉丝金属 各向异性 材质节点" --type video --limit 20 -f json`，筛出 3 条时长超过 15 分钟的候选视频。
3. **核验取证**：对最贴题的一条依次运行 `opencli bilibili video <BV> -f json`、`opencli bilibili subtitle <BV> -f plain` 和 `opencli bilibili comments <BV> -f json`。确认作者为原创 UP 主，全程使用原生 `Principled BSDF` 与 `Radial` 梯度贴图，无付费插件，收藏播放比 8.2%，置顶评论附有工程文件网盘链接。
4. **分级登记**：按版本与原创可信度评为 **A 级**，将新条目追加进 `references/resource-index.md` 的「材质纹理」节，并把作者信息与代表作登记到 `references/up-directory.md`。
5. **交接复现**：把本地硬表面法线深读笔记与这条新登记的 A 级教程（附关键节点参数时间段）一并交给材质部门。材质代理按步骤在工作副本里搭完节点并渲染对照图，验证通过后推进下一步。

## 参考

- [主题资源索引（活跃数据）](references/resource-index.md)
- [UP 主名录（活跃数据）](references/up-directory.md)
- [检索策略手册（关键词矩阵与细分领域技巧）](references/search-playbook.md)
- [工具演进与规范来源](references/sources.md)

维护：唯一维护源是 `./.agents/skills/blender-tutorial-scout/`，改完同步各镜像目录。
