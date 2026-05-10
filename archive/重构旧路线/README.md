# 重构旧路线归档说明

更新时间：2026-05-10

这个目录保存 `nfi-alpha-strategy` 早期两条路线的历史成果：

1. 从零设计的新策略路线：`AlphaRegimeStrategy`。
2. 完全模块化重构 NFI 的路线：`NFIRefactorStrategy`。

它们现在不再是当前主线。

当前主线已经切换为：

`原版 NostalgiaForInfinityX7 + NFIRiskDurationStrategy 包装层`

## 为什么归档

完全重构 NFI 能帮助理解源码，但维护成本很高。NFI 原版持续更新时，逐个模块同步非常容易产生行为偏移。

包装方式更稳：

- 原版 NFI 更新时，只需要替换 `NostalgiaForInfinityX7.py`。
- 我们自己的优化集中在包装策略里。
- 回测对齐和故障定位更简单。

## 目录说明

- `strategies/AlphaRegimeStrategy.py`：早期从零构建的新策略主文件。
- `strategies/alpha_modules/`：AlphaRegimeStrategy 的插件化模块。
- `strategies/NFIRefactorStrategy.py`：NFI 完全重构路线的适配器。
- `strategies/nfi_refactor/`：从 NFI 拆出的指标、入场、退出、仓位、状态模块。
- `scripts/`：旧路线专用同步、回测、回归脚本。
- `configs/`：旧 Alpha 路线的回测配置。
- `tests/`：旧 NFI 重构模块的单元测试。

## 什么时候还会用到

- 学习 NFI 的入场、退出、补仓、grind 逻辑时。
- 想把某段 NFI 逻辑独立抽出来研究时。
- 未来如果决定重新推进完全重构路线时。

## 当前不要做什么

- 不要把这里的旧同步脚本作为实盘同步入口。
- 不要把 `NFIRefactorStrategy` 当作当前收益对比基线。
- 不要在没有 parity 回测的情况下，把归档模块重新接回主策略。

当前主线请看：

- `../../strategies/NFIRiskDurationStrategy.py`
- `../../scripts/sync_recovery_cut_gentle_wrapper.ps1`
- `../../docs/当前进度说明.md`
