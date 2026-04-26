# 0012 NFI Parity 基线

## 目标

建立原版 `NostalgiaForInfinityX7` 和重构版 `NFIRefactorStrategy` 的第一条对照回测。

第一版 `NFIRefactorStrategy` 是 parity adapter：

```text
NFIRefactorStrategy extends NostalgiaForInfinityX7
```

这不是最终结构，但它能先建立一个稳定入口：

```text
类名独立；
配置可独立指定；
回测行为应与原版一致；
后续每拆出一个模块，都和这个结果对照；
```

## 固定对照配置

```text
config: /freqtrade/user_data/config.backtest.dynamic.top40.302u.max2.halfyear.balanced.json
timerange: 20251016-20260415
timeframe: 5m
starting balance: 302.6 USDT
max_open_trades: 2
```

## 有效基线结果

```text
原版 NostalgiaForInfinityX7 回测结果：
交易数：61
收益：+1757.800 USDT
收益率：+580.90%
胜率：100%
最大回撤：0%
Long / Short：60 / 1

NFIRefactorStrategy 回测结果：
交易数：61
收益：+1757.800 USDT
收益率：+580.90%
胜率：100%
最大回撤：0%
Long / Short：60 / 1

差异说明：
无差异。第一版 parity adapter 与原版 NFI 行为对齐。
```

## 无效基线记录

曾尝试使用：

```text
config: /freqtrade/user_data/config.backtest.nfi.top40clean.300u.max2.json
timerange: 20260401-20260410
```

结果原版 NFI 和重构版都是 0 笔交易，所以不能作为有效 parity 基线。

## 当前结论

`NFIRefactorStrategy` 的第一版 adapter 可以作为重构入口。

下一步不是继续继承，而是从原版 NFI 中逐步抽取模块。每抽一块，都用这条半年度基线回归验证。
