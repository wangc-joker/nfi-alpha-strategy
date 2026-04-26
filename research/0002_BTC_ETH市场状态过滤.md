# 0002 BTC 市场状态过滤

## 目标

把 NFI 中很重要的“参考大盘环境再交易”的思想接入 AlphaRegimeStrategy。

## 实现内容

- 增加 `informative_pairs`：
  - `BTC/USDT:USDT` 1h
- 在主策略中合并 BTC 1h 指标。
- 计算参考市场状态：
  - close > EMA200
  - EMA50 > EMA200
  - RSI14 > 42
- BTC 的 1h 状态通过时，`alpha_market_ok = 1`。
- `RiskManager` 将 `alpha_market_ok` 纳入统一入场过滤。

## 设计意图

这个过滤器不是为了让策略更“聪明”，而是先让它更少犯低级错误。

第一版趋势回调信号只看单个币自己的走势，容易在大盘走弱时误判局部反弹。加入 BTC 过滤后，策略会更偏向在整体环境健康时交易。

ETH 暂时不作为硬过滤条件。原因是 ETH 很多时候跟随 BTC 变化，并放大 BTC 的波动。如果把 ETH 也作为一票否决条件，可能会过度过滤交易机会。后续可以把 ETH 用作风险强度或仓位调整参考，而不是作为硬开关。

## 和 NFI 的关系

参考 NFI 的多周期和 BTC 市场过滤思想，但采用更简单、可解释的规则。后续可以继续加入 4h/1d 环境，不急着堆很多条件。

## 2026-04-25 烟测对比

测试命令：

```powershell
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.backtest.alpha.futures.smoke.json --strategy-path /freqtrade/user_data/strategies --strategy AlphaRegimeStrategy --timerange 20260401-20260410 --timeframe 5m
```

加入 BTC 1h 过滤前：

```text
交易数：10
收益：-1.670 USDT
收益率：-0.56%
胜率：30.0%
最大回撤：0.96%
```

加入 BTC 1h 过滤后：

```text
交易数：4
收益：+0.262 USDT
收益率：+0.09%
胜率：50.0%
最大回撤：0.32%
```

补充调整：

最初版本曾短暂同时使用 BTC 和 ETH 作为硬过滤条件。后来判断 ETH 很多时候只是跟随并放大 BTC，因此移除 ETH 硬过滤，只保留 BTC。2026-04-25 同区间复测后，BTC-only 的结果与 BTC+ETH 硬过滤一致，因此保留更简单的 BTC-only 设计。

阶段结论：

这个过滤器在烟测区间减少了低质量交易，并降低了回撤。样本还很小，不能说明长期有效，但方向符合项目目标：先控制错误交易，再追求收益放大。
