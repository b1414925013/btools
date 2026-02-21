# LoadTestUtils 使用指南

`LoadTestUtils` 类提供了负载测试工具，用于模拟并发请求。

## 基本使用

### 简单负载测试

```python
from btools import LoadTestUtils

# 定义测试函数
def test_request():
    import requests
    response = requests.get("https://example.com")
    return response.status_code == 200

# 运行负载测试
results = LoadTestUtils.run_load_test(
    func=test_request,
    concurrent_users=10,  # 并发用户数
    duration=30,  # 持续时间（秒）
    ramp_up=5  # 预热时间（秒）
)

print(f"总请求数: {results['total_requests']}")
print(f"成功率: {results['success_rate']}%")
print(f"平均响应时间: {results['average_response_time']}s")
```

### 多阶段负载测试

```python
from btools import LoadTestUtils

# 定义测试阶段
stages = [
    {"duration": 30, "users": 10},   # 30秒 10个用户
    {"duration": 60, "users": 50},   # 60秒 50个用户
    {"duration": 30, "users": 100},  # 30秒 100个用户
    {"duration": 30, "users": 0},    # 30秒 0个用户（冷却）
]

# 运行多阶段测试
results = LoadTestUtils.run_staged_load_test(
    func=test_request,
    stages=stages
)
```

## 高级功能

### 自定义测试场景

```python
from btools import LoadTestUtils

# 自定义测试场景
def my_test_scenario(user_id):
    # 每个用户执行的场景
    import time
    import requests
    
    # 步骤1: 首页
    requests.get("https://example.com")
    time.sleep(0.5)
    
    # 步骤2: 登录
    requests.post("https://example.com/login", json={"user": f"user{user_id}"})
    time.sleep(0.3)
    
    # 步骤3: 浏览产品
    requests.get("https://example.com/products")
    return True

# 运行场景测试
results = LoadTestUtils.run_scenario_test(
    scenario=my_test_scenario,
    concurrent_users=20,
    duration=60
)
```

### 结果分析

```python
from btools import LoadTestUtils

# 生成详细报告
report = LoadTestUtils.generate_load_test_report(results)
print(report)

# 保存报告
LoadTestUtils.save_report(report, "load_test_report.json")

# 可视化结果
LoadTestUtils.plot_results(results, "load_test_chart.png")
```

### 阈值检查

```python
from btools import LoadTestUtils

# 定义性能阈值
thresholds = {
    "max_response_time": 2.0,  # 最大响应时间 2秒
    "min_success_rate": 95.0,   # 最小成功率 95%
    "max_error_rate": 5.0        # 最大错误率 5%
}

# 检查阈值
check_result = LoadTestUtils.check_thresholds(results, thresholds)
print(f"是否通过: {check_result['passed']}")
print(f"失败原因: {check_result['failures']}")
```

## HTTP 请求测试

```python
from btools import LoadTestUtils

# 使用内置的 HTTP 测试
results = LoadTestUtils.test_http_endpoint(
    url="https://example.com/api",
    method="GET",
    concurrent_users=50,
    duration=60
)

# POST 请求测试
results = LoadTestUtils.test_http_endpoint(
    url="https://example.com/api",
    method="POST",
    json={"data": "test"},
    concurrent_users=30,
    duration=30
)
```

## 渐进式负载测试

```python
from btools import LoadTestUtils

# 渐进式增加负载
results = LoadTestUtils.run_ramp_up_test(
    func=test_request,
    initial_users=5,
    max_users=100,
    step=10,
    step_duration=30
)
```

## 测试指标

负载测试结果包含以下指标：

| 指标 | 说明 |
|------|------|
| `total_requests` | 总请求数 |
| `successful_requests` | 成功请求数 |
| `failed_requests` | 失败请求数 |
| `success_rate` | 成功率 (%) |
| `error_rate` | 错误率 (%) |
| `average_response_time` | 平均响应时间 (秒) |
| `min_response_time` | 最小响应时间 (秒) |
| `max_response_time` | 最大响应时间 (秒) |
| `median_response_time` | 中位响应时间 (秒) |
| `p95_response_time` | 95分位响应时间 (秒) |
| `p99_response_time` | 99分位响应时间 (秒) |
| `requests_per_second` | 每秒请求数 (RPS) |
| `concurrent_users` | 并发用户数 |
| `duration` | 测试持续时间 (秒) |
