# Reversal216 真实双顺接入结果

## 背景

用户确认此前最佳双顺版本来自：

- `D:\test\ft_userdata\user_data\strategies\myStrage\Top9MainReversal216ShortAggressiveStrategy.py`

该文件实际包装的是 `Top9RegimeMainReversal216NoLongAggressiveStrategy`，核心行为是：

- 继承 `Top9RegimeMainReversal216Strategy`
- 禁用多头反转分支：`long_reversal_pairs = set()`
- 保留空头反转候选池：BTC、TRX、ADA、ETH、XRP、DOGE、ZEC
- 对 `short_reversal_breakdown` 做更激进仓位倍率：父类 `1.12`，子类再乘 `1.5`，合计 `1.68`

## 本次实现

新增模块：

- `strategies/nfi_refactor/alpha_hybrid/reversal216.py`

新增策略：

- `NFIReversal216ShortAggressiveHybridStrategy`

设计取舍：

- 不修改 NFI 原始指标管线。
- Reversal216 需要 `1d` 的 OHLC 和趋势列，而 NFI 默认会删除 informative OHLC，所以新模块单独合并 Reversal216 专用 `1d` 数据。
- 将 `long_reversal_breakout`、`short_reversal_breakdown` 加入 NFI grind 标签列表，让新信号成交后可以走 NFI 的复杂仓位管理。
- 复刻原短空分支仓位倍率：`short_reversal_breakdown` 在 NFI 原 stake 基础上乘 `1.68`。
- 复刻原反转退出保护：反转标签持仓在 `current_profit < 0.08` 时不提前走父类 custom_exit。

## 半年前测

配置：

- `D:\test\ft_userdata\user_data\config.backtest.dynamic.top40.302u.max2.halfyear.balanced.json`
- timerange：`20251016-20260415`
- 起始资金：`302.6 USDT`
- `max_open_trades = 2`
- strategy：`NFIReversal216ShortAggressiveHybridStrategy`

结果：

| 指标 | 结果 |
| --- | ---: |
| 交易数 | 61 |
| 最终资金 | 2060.4 USDT |
| 绝对收益 | 1757.8 USDT |
| 总收益率 | 580.90% |
| 胜率 | 100% |
| 多 / 空交易 | 60 / 1 |
| 账面最大回撤 | 0.00% |
| 最大浮亏 MAE | -73.08% |
| 最大浮亏交易 | ZEC/USDT:USDT, tag `120` |
| 最久持仓 | CRV/USDT:USDT, 93d 18h 25m |

## 关键结论

这次半年前测的真实成交中，`reversal` 标签成交数为 `0`。

因此该版本的回测收益、交易数、胜率与 NFI 基线完全一致。原因不是代码未生效，而是在该 top40 / 半年 / max_open_trades=2 样本里，Reversal216 没有产生最终可成交的新标签，或者产生的候选信号没有抢到实际仓位。

这说明：

- Reversal216 已经被工程化接入，可以作为后续可拔插信号继续调试。
- 这组测试无法证明 Reversal216 对 NFI 有收益改善。
- 如果要验证 Reversal216 的贡献，需要进一步跑更适合它的实验，例如 top9 原币池、放宽 `max_open_trades`、单独统计信号出现次数，或按原 Top9 的 timeframe/候选池做对齐测试。
