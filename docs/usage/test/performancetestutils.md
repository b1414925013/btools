# PerformanceTestUtils 使用指南

`PerformanceTestUtils` 类提供了性能测试工具，包括测量执行时间、内存使用等功能。

## 基本使用

### 测量执行时间

```python
from btools import PerformanceTestUtils

# 测量函数执行时间
def my_function():
    sum(range(1000000))

# 单次测量
result = PerformanceTestUtils.measure_time(my_function)
print(f"执行时间: {result['time} 秒")

# 多次测量取平均值
result = PerformanceTestUtils.measure_time(
    my_function,
    iterations=10,
    warmup=2
)
print(f"平均执行时间: {result['average_time']} 秒")
```

### 装饰器使用

```python
from btools import PerformanceTestUtils

# 使用装饰器测量函数执行时间
@PerformanceTestUtils.timed
def slow_function():
    sum(range(1000000))

result = slow_function()
# 函数会正常执行，同时会打印执行时间
```

### 测量内存使用

```python
from btools import PerformanceTestUtils

# 测量内存使用
def memory_heavy_function():
    data = [i for i in range(1000000)]
    return data

result = PerformanceTestUtils.measure_memory(memory_heavy_function)
print(f"内存使用: {result['memory_used']} MB")
```

## 高级功能

### 基准测试

```python
from btools import PerformanceTestUtils

# 运行基准测试
def function_a():
    pass

def function_b():
    pass

results = PerformanceTestUtils.benchmark(
    functions=[function_a, function_b],
    names=["Function A", "Function B"],
    iterations=100
)

for name, result in results.items():
    print(f"{name}: {result['average_time']}s")
```

### 性能分析

```python
from btools import PerformanceTestUtils

# 性能分析
def complex_function():
    pass

profile = PerformanceTestUtils.profile(complex_function)
print(profile)

# 保存性能分析结果
PerformanceTestUtils.save_profile(
    complex_function,
    "profile_stats.prof"
)
```

### 生成性能报告

```python
from btools import PerformanceTestUtils

# 生成性能报告
report = PerformanceTestUtils.generate_performance_report(
    functions=[function_a, function_b],
    names=["Function A", "Function B"]
)
print(report)

# 保存性能报告
PerformanceTestUtils.save_performance_report(
    report,
    "performance_report.json"
)
```

## 监控工具

### CPU 使用监控

```python
from btools import PerformanceTestUtils
import time

# 监控 CPU 使用
with PerformanceTestUtils.monitor_cpu() as monitor:
    # 执行代码
    time.sleep(1)

stats = monitor.get_stats()
print(f"平均 CPU 使用: {stats['cpu_percent']}%")
```

### 内存使用监控

```python
from btools import PerformanceTestUtils
import time

# 监控内存使用
with PerformanceTestUtils.monitor_memory() as monitor:
    # 执行代码
    time.sleep(1)

stats = monitor.get_stats()
print(f"峰值内存使用: {stats['peak_memory']} MB")
```

### 组合监控

```python
from btools import PerformanceTestUtils

# 同时监控 CPU 和内存
with PerformanceTestUtils.monitor_resources() as monitor:
    # 执行代码
    pass

stats = monitor.get_stats()
print(stats)
```

## 性能阈值检查

```python
from btools import PerformanceTestUtils

# 检查性能阈值
def test_result = PerformanceTestUtils.check_performance_threshold(
    function=my_function,
    max_time=1.0,  # 最大允许时间（秒）
    max_memory=100  # 最大允许内存（MB）
)

print(f"是否通过: {test_result['passed']}")
```

## 性能对比

```python
from btools import PerformanceTestUtils

# 对比两个函数的性能
comparison = PerformanceTestUtils.compare_performance(
    function1=old_function,
    function2=new_function,
    iterations=10
)

print(f"改进: {comparison['improvement_percent']}%")
print(f"新函数更快: {comparison['new_is_faster']}")
```
