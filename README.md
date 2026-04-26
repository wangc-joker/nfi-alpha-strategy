# NFI Alpha Strategy

这是一个独立于 `NostalgiaForInfinity` 和 `real_trade` 的长期策略研发工程。

当前路线已经调整：先以 NFI 为参考实现进行模块化重构，第一目标是尽量对齐原版 NFI 回测结果，然后再在重构版基础上改造和调优。

## 工程定位

- `NostalgiaForInfinity`：上游参考策略仓库，不在里面直接开发新策略。
- `real_trade`：实盘运行仓库，只放稳定配置、启动脚本和部署相关内容。
- `nfi-alpha-strategy`：新策略研发主仓库，负责研究、设计、实现、测试、文档和长期演进。

## 先读文档

1. [工程设计总纲](D:\test\nfi-alpha-strategy\docs\工程设计总纲.md)
2. [AI协作与长期维护规范](D:\test\nfi-alpha-strategy\docs\AI协作与长期维护规范.md)
3. [NFI重构与改造路线图](D:\test\nfi-alpha-strategy\docs\NFI重构与改造路线图.md)

## 目录说明

- `docs`：工程总纲、架构设计、迭代计划、复盘记录。
- `strategies`：Freqtrade 策略文件和可插拔信号模块。
- `configs`：回测、模拟盘、实盘配置模板。
- `scripts`：数据下载、回测、报告生成、部署辅助脚本。
- `research`：实验记录、指标研究、策略假设和分析报告。
- `tests`：单元测试、策略组件测试、回归验证。
