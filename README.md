# NFI Alpha Strategy

这是一个独立于 `NostalgiaForInfinity` 和 `real_trade` 的长期策略研发工程。

当前主线已经收口为：**原版 NFI X7 + RecoveryCutGentle 风控包装层**。

也就是说，本仓库不再把完全重构 NFI 作为当前主线，而是通过包装原版 `NostalgiaForInfinityX7.py` 的方式维护优化策略。以后上游 NFI 更新时，优先替换原版 NFI 文件，再验证包装层是否正常。

## 当前主线文件

- `strategies/NFIRiskDurationStrategy.py`：当前主策略，继承原版 `NostalgiaForInfinityX7` 并叠加 RecoveryCutGentle 风控。
- `scripts/sync_recovery_cut_gentle_wrapper.ps1`：把上游 NFI 原策略和当前包装策略同步到 Freqtrade `user_data/strategies`。
- `docs/当前进度说明.md`：当前状态、关键回测结果和下一步计划。

## 旧路线归档

早期的从零设计路线和 NFI 完全重构路线已归档到：

`archive/重构旧路线/`

归档内容包括：

- `AlphaRegimeStrategy.py`
- `alpha_modules/`
- `NFIRefactorStrategy.py`
- `nfi_refactor/`
- 旧路线专用脚本、配置和测试

这些文件不再作为当前主线运行，但保留用于学习 NFI 结构、查阅历史实验和未来可能的模块迁移。

## 同步当前主线到 Freqtrade

```powershell
powershell -ExecutionPolicy Bypass -File D:\test\nfi-alpha-strategy\scripts\sync_recovery_cut_gentle_wrapper.ps1
```

默认会复制：

- `D:\test\NostalgiaForInfinity\NostalgiaForInfinityX7.py`
- `D:\test\nfi-alpha-strategy\strategies\NFIRiskDurationStrategy.py`

到：

- `D:\test\ft_userdata\user_data\strategies`

## 推荐阅读顺序

1. `docs/当前进度说明.md`
2. `strategies/NFIRiskDurationStrategy.py`
3. `scripts/sync_recovery_cut_gentle_wrapper.ps1`
4. `docs/工程设计总纲.md`
5. `archive/重构旧路线/README.md`

## 当前判断

当前最值得继续验证的是 RecoveryCutGentle 包装版，尤其是：

- `max_open_trades=4`：更稳，回撤和最大水下比例更健康。
- `max_open_trades=2`：收益爆发更强，但单仓资金占比更大，风险更集中。

后续 FreqAI 接入也建议作为包装层增强，而不是直接侵入 NFI 主流程。
