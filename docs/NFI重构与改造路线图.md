# NFI 重构与改造路线图

## 0. 路线调整

之前我们是从零设计 `AlphaRegimeStrategy`，优点是结构干净，缺点是进展慢，而且很难短期达到 NFI 的成熟度。

现在调整路线：

```text
以 NostalgiaForInfinityX7 为蓝本
  -> 按我们的模块化框架重构
  -> 先追求回测结果对齐
  -> 再做结构改造
  -> 再做调优
  -> 未来接入 FreqAI
```

这条路线更像软件工程里的“重构遗留系统”：

```text
先保证行为一致，再改变内部结构。
```

## 1. 总目标

最终目标不是复制一个新的 7 万行文件，而是把 NFI 的有效逻辑拆成可维护模块。

目标顺序：

```text
第一目标：重构版尽量达到原版 NFI 的回测结果。
第二目标：在保持结果接近的前提下，拆分结构、增强可维护性。
第三目标：在重构版基础上调优。
第四目标：未来接入 FreqAI。
```

当前阶段先做到第三目标之前，也就是：

```text
完成第一目标和第二目标的工程基础；
为第三目标准备可验证的调优环境。
```

## 2. 核心原则

### 2.1 不手工猜策略

NFI 已经是一个复杂成熟策略。我们不能只看几段代码就凭感觉重写，否则会失去它真正有效的部分。

正确方式：

```text
原版 NFI 是参考实现；
每拆出一个模块，都要和原版回测结果对比；
结果偏差必须可解释。
```

### 2.2 先行为对齐，再结构优化

重构顺序：

```text
冻结原版参考结果
  -> 建立重构版骨架
  -> 一个模块一个模块迁移
  -> 每一步都跑回归回测
```

不能一口气重写所有逻辑。

### 2.3 模块边界必须比 NFI 更清楚

NFI 的优势是策略逻辑丰富，劣势是巨型单文件。

重构版需要拆成：

```text
nfi_core/
  indicators/
  market_context/
  protections/
  entries/
  exits/
  position/
  modes/
  state/
```

## 3. 四步路线

### 第一步：NFI Parity，对齐原版回测

目标：

```text
重构版在固定配置、固定币种、固定时间区间下，尽量接近原版 NFI 回测结果。
```

完成标准：

```text
相同数据
相同 config
相同 pairlist
相同 timerange
相同 max_open_trades
相同 stake
收益率、交易数、回撤基本接近
```

允许差异：

```text
由于 Freqtrade 版本、缓存、浮点、订单撮合细节导致的小误差。
```

不允许差异：

```text
交易数大幅不同；
收益方向不同；
回撤数量级不同；
明显少了一类模式；
```

第一步拆解顺序：

```text
1. 指标计算迁移
2. BTC informative 迁移
3. pair informative 迁移
4. global protections 迁移
5. long entry modes 迁移
6. short entry modes 迁移
7. custom stake / leverage 迁移
8. custom exit / position adjustment 迁移
```

### 第二步：结构化改造，但不改变策略含义

目标：

```text
把 NFI 的逻辑拆成模块，但尽量不改变交易行为。
```

这一阶段不是优化收益，而是让代码可维护。

拆分目标：

```text
指标层：只负责计算指标
市场层：只负责 BTC / 高周期 / 市场状态
保护层：只负责能不能开仓
信号层：只负责产生候选信号
模式层：负责 normal / quick / grind / top coins / btc 等模式
仓位层：负责 stake、leverage、rebuy、grind
退出层：负责 custom_exit、止盈、止损、derisk
状态层：负责运行时缓存和持久化
```

第二步完成标准：

```text
重构版不再是单个巨型文件；
每个模式能单独开关；
每个信号保留 tag；
每个模块有说明文档；
回测结果仍接近原版；
```

### 第三步：在重构版上调优

调优方向：

```text
降低过度补仓依赖；
减少低质量入场；
减少深回撤；
优化 max_open_trades / stake 分配；
改进动态币池；
重新设计空头模块；
```

第三步必须遵守：

```text
任何调优都必须和第二步的 parity 版本对比。
```

否则不知道是优化有效，还是重构时已经改变行为。

### 第四步：未来接入 FreqAI

FreqAI 的定位：

```text
候选信号评分；
风险过滤；
波动率预测；
趋势延续概率；
```

暂时不让 AI 直接决定买卖。

## 4. 现在要做什么

当前立即执行：

```text
1. 建立 NFI 重构专用目录。
2. 建立原版 NFI 黄金回测记录。
3. 建立模块拆分清单。
4. 建立 parity 检查文档。
5. 开始迁移“指标层 + BTC informative + protections”。
```

## 5. 我的建议

不要直接把 NFI 复制后手工改成模块。

更稳的方式是：

```text
先做 NFIReferenceStrategy：只用于保存原始行为。
再做 NFIRefactorStrategy：逐步模块化迁移。
每迁移一块，就跑一次和 Reference 的对照回测。
```

这会比从零调试快很多，也比直接大改 NFI 安全。

## 6. 风险提醒

NFI 有大量运行时状态、补仓、grind、derisk、缓存和模式判断。

如果没有 parity 回归，直接重构很容易出现：

```text
入场 tag 对不上；
custom_exit 行为不同；
position_adjustment 顺序不同；
reload 后缓存行为不同；
回测收益看似相近但实盘行为不同；
```

所以第 1 步一定要像搭测试网一样认真做。
