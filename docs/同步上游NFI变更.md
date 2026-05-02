# 同步上游 NFI X7 变更操作手册

## 适用场景

`NostalgiaForInfinityX7.py` 上游更新了新版本（如 v17.4.15 → v17.4.43），需要将变更同步到 `nfi-alpha-strategy` 项目的 `NFIRefactorStrategy` 及其模块化代码。

## 整体流程

```text
1. 生成上游 diff
2. 分析 diff 分类
3. 按分类同步到模块
4. 回归验证
5. 跨分支同步
```

---

## Step 1: 生成上游 diff

```powershell
# 确保上游文件已替换为新版本
# 然后在项目根目录执行：
git diff --no-color D:\test\NostalgiaForInfinity\NostalgiaForInfinityX7.py > generated\nfi_x7_diff.patch
```

将 diff 加到 `generated/` 目录归档，命名格式：`nfi_x7_v{old}_to_v{new}.patch`

## Step 2: 分析 diff 分类

阅读 patch，将变更归入以下类别：

| 类别 | 变更特征 | 处理方式 |
|------|---------|---------|
| **类常量** | class-level 属性新增/修改 | 更新 `nfi_refactor/state/initialization.py` 的 `NFI_SAFE_PARAMETERS` |
| **简单方法变更** | 1-5 行的安全守卫、类型转换 | 直接更新对应模块 |
| **模块阈值调整** | 已有模块中的 RSI/EMA/ROC 等数值变化 | 逐项更新模块中对应表达式 |
| **大范围重写** | 方法体整体替换（如 `long_grind_entry_v3`） | 保留 `super()` 回退 |
| **populate_entry_trend保护条件** | 几百处分散的保护条件阈值调整 | 保留 `super()` 回退 |
| **exit 条件阈值** | populate_exit_trend 中的信号变化 | 更新对应 exit 模块 |

### 模块与策略方法的映射表

| NFIRefactorStrategy 方法 | 对应模块 | 当前同步状态 |
|-------------------------|---------|------------|
| `custom_exit()` | `nfi_refactor/exits/custom_exit.py` | 已模块化 |
| `populate_entry_trend()` | `nfi_refactor/entries/trend.py` | super() 回退 |
| `populate_exit_trend()` | `nfi_refactor/exits/trend.py` | 已模块化 |
| `adjust_trade_position()` | `nfi_refactor/position/adjustment.py` | super() 回退 |
| `long_exit_rebuy()` | `nfi_refactor/exits/mode_rebuy_long.py` | super() 回退 |
| `short_exit_rebuy()` | `nfi_refactor/exits/mode_rebuy_short.py` | 已模块化 |
| `long_grind_entry_v3()` | `nfi_refactor/position/adjustment_helpers_long.py` | super() 回退 |
| `short_grind_entry_v3()` | `nfi_refactor/position/adjustment_helpers_short.py` | super() 回退 |
| `long_rebuy_adjust_trade_position_v3()` | `nfi_refactor/position/rebuy_adjustment.py` | super() 回退 |
| `short_rebuy_adjust_trade_position_v3()` | `nfi_refactor/position/rebuy_adjustment.py` | super() 回退 |
| `leverage()` | `nfi_refactor/position/leverage.py` | 已模块化 |
| `custom_stake_amount()` | `nfi_refactor/position/stake.py` | 已模块化 |
| `confirm_trade_entry()` | `nfi_refactor/entries/confirm_entry.py` | 已模块化 |
| `confirm_trade_exit()` | `nfi_refactor/exits/confirm_exit.py` | 已模块化 |
| `populate_indicators()` | `nfi_refactor/indicators/pipeline.py` | 已模块化 |

## Step 3: 按分类同步

### 3a. 同步类常量

上游新增的类常量会自动被 `NFIRefactorStrategy` 继承。只需在 `initialization.py` 检查是否需要加入 `NFI_SAFE_PARAMETERS`。

### 3b. 同步简单方法变更

以 `custom_exit` 的 `len(df) < 6` 安全守卫为例：

1. 找到对应模块文件
2. 阅读上下文，在正确位置插入变更
3. 确保 `custom_exit.py` 中处理可能的 None 返回
4. 在 `NFIRefactorStrategy.py` 中将该方法从 `super()` 改回模块调用

### 3c. 同步模块阈值调整

以 `mode_rebuy_long.py` 的 `system_v3_2_stops_enable` 为例：

1. 在 patch 中找到对应 hunk
2. 阅读模块中对应位置
3. 逐项更新阈值

### 3d. 保留 super() 回退

对于大范围重写的方法，不要在模块中逐行同步。在 `NFIRefactorStrategy.py` 中保持：

```python
def method_name(self, ...):
    # Upstream X7 vX.X.X -> vX.X.X changed ... (keep parity via parent)
    return super().method_name(...)
```

## Step 4: 回归验证

```powershell
# 运行回归检查脚本
powershell -ExecutionPolicy Bypass -File .\scripts\run_nfi_refactor_regression.ps1

# 或手动验证：
# 1. 策略加载成功
# 2. 烟雾回测完成
# 3. 交易数与收益接近预期
# 4. enter tag 分布接近预期
```

## Step 5: 提交 & 跨分支同步

```powershell
git add -A
git commit -m "Sync upstream NFI X7 v{old} -> v{new} changes to refactored modules"

# 合并到其他分支
git checkout codex/refactor-risk-duration-optimization
git merge refactor_base -m "Merge upstream NFI X7 v{old}->v{new} sync from refactor_base"

git checkout codex/alpha-strategy-foundation
git merge refactor_base -m "Merge upstream NFI X7 v{old}->v{new} sync from refactor_base"

git checkout refactor_base
git push origin refactor_base codex/refactor-risk-duration-optimization codex/alpha-strategy-foundation
```

## 注意事项

- `NFIRefactorStrategy` 继承自 `NostalgiaForInfinityX7`，父类本身已是最新版本，`super()` 回退得到的是正确的上游行为
- 模块代码和 `super()` 回退混合使用是安全的——两者来源都是正确的上游行为
- 不要为了"拆完"而强行拆分大范围重写的方法，过度拆分引入 bug 的风险大于收益
- 改完模块后运行回归检查，确认交易数和收益偏移在合理范围内（<5%）
