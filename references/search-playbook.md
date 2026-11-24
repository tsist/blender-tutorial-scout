# 检索策略手册（search-playbook）

配套 `SKILL.md` 使用，帮你在本地库缺口处更快搜到高可信度中文教程，并一路下探到细分工艺。

## 1. 关键词矩阵

按「软件与版本词 + 工艺中文词 + 深度质量词 + 英文术语原词」拼词：

- **软件与版本词**：`Blender`、`Blender 5`、`Blender 4`（涉及修改器或节点迭代的主题加上版本号，优先找 `5.x` 教程）。
- **工艺中文词**：材质节点、PBR、贴图、纹理、烘焙、UV 展开、程序化材质、雕刻、重拓扑、硬表面、卡线、加权法线、几何节点、灯光、渲染、Cycles、EEVEE、绑定、蒙皮、权重、动画、三渲二、剪辑、合成。
- **深度质量词**：全流程、实操、进阶、系统教学、工程文件、避坑、底层原理、商业级。
- **细分下探词**：英文术语原词（`UDIM`、`ORM`、`trim sheet`、`texel density`、`bevel node`、`Rigify`、`NLA`、`SDF`）、具体节点名（如 `Principled BSDF`、`Data Transfer`）、报错原句。

常用组合示例：

- **材质与 UV**：`Blender 5 PBR 烘焙 全流程`、`Blender UDIM 实操`、`Blender trim sheet 制作`、`Blender 程序化材质 进阶 原理`
- **绑定与动画**：`Blender 绑定教程`、`Blender 权重绘制 蒙皮`、`Blender Rigify 教程 中文`、`Blender 驱动器 教程`、`Blender NLA 非线性动画`、`Blender 表情绑定 facial rig`、`Blender 弹性骨骼 jiggle bones`、`Blender 四足动物 绑定`
- **三渲二风格化**：优先搜「三渲二」「卡通渲染」「卡通材质」「动漫着色器」，其次再试「NPR」「toon shading」「赛璐璐」。搜描边时用「描边 + 方法名（实体化 / 菲涅尔 / Freestyle / 合成器 / 几何节点）」；搜着色时用「动漫阴影 / 动漫着色器 / 阴影平滑 / SDF」。

## 2. 用 `opencli bilibili` 筛出高含金量教程

1. **宽搜初筛**：运行 `opencli bilibili search "<关键词>" --type video --limit 20 -f json`，优先挑时长大于 15 分钟、标题结构清晰的教程。
2. **核验数据与收藏比**：对候选跑 `opencli bilibili video <BV> -f json`，重点看收藏数与播放量之比（高于 5% 是强信号）以及分 P 总集数。
3. **快速看清干货密度**：跑 `opencli bilibili subtitle <BV> -f plain` 或 `opencli bilibili summary <BV> -f yaml`，直接确认讲到了哪些具体节点、参数和 Blender 版本。
4. **挖评论区宝藏**：跑 `opencli bilibili comments <BV> -f json`，从置顶评论和高赞回复里找工程文件链接、插件清单和版本勘误。
5. **顺藤摸瓜查 UP 主系列课**：遇到讲得透的作者，跑 `opencli bilibili user-videos <UID> --order stow --limit 20 -f json` 翻他的高收藏合集，单次会话控量查一两位重点作者即可，顺手把专长领域写进 `up-directory.md`。

## 3. 公开课、双语教程与工具依赖核查

- **公开课与到期免费开放课程**：重点留意官方账号或作者本人主页发布的完整版、全集、限时免费或公开课，记录免费性质与核验日期。
- **双语与中字教程**：优先选 Blender Studio 官方中字，以及在简介或置顶评论写明原作者授权和原频道链接的授权中字版。遇到未注明授权的搬运视频，按 C 级留存线索，写清原作者与原课程出处，方便溯源查找原版。
- **商业付费插件隔离**：核对字幕和评论区的插件清单。靠 Blender 原生功能或免费开源插件（如 Rigify、LoopTools、Bool Tool）完成的教程优先推荐；依赖付费商业插件的视频标为 C 级线索，并在备注栏写清插件名与「含商业付费插件，已隔离」，提醒下游改走原生或免费替代方案。
- **英文线索补充**：中文区尚无覆盖的刁钻工艺，可顺手查 Blender 官方手册、Blender Studio 博客、Polycount Wiki 或 YouTube 原作者频道，用来核对底层参数并记下中文教程缺口。

## 4. 受限或无 BV 号时的反查兜底

- **页面限流或无 BV 号课程卡**：改用通用搜索引擎跑 `site:bilibili.com <关键词> 教程` 或 `「BV号 + 标题片段」` 反查，从结果摘要里补齐作者名、分 P 集数、发布日期与互动数据。
- **核验身份与系列集数**：命中优质单集后，用「UP 主名 + 系列名」或「系列名 + 集数标题」反查其余分集，补全系列结构。
- **信息暂缺处理**：泛名账号或暂时拿不到作者名的条目，标清「UP 待核」留作待复核线索，凑齐两条以上验证依据后再升入正式索引分级。
