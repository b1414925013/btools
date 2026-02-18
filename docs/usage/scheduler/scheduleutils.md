# ScheduleUtils 使用指南

`ScheduleUtils` 类提供了定时任务的创建、管理和执行功能，支持一次性任务、周期性任务等多种调度方式。

## 基本使用

### 导入方式

```python
from btools import ScheduleUtils, global_scheduler

# 或使用便捷函数
from btools import (
    schedule_once, schedule_interval, schedule_at_fixed_rate,
    schedule_with_fixed_delay, cancel_task, cancel_all,
    start_scheduler, stop_scheduler
)
```

## 一次性任务

### 安排一次性任务

```python
from btools import schedule_once
import time

def greet(name):
    """问候函数"""
    print(f"你好, {name}! 当前时间: {time.strftime('%H:%M:%S')}")

print(f"开始时间: {time.strftime('%H:%M:%S')}")

# 安排2秒后执行的任务
task_id = schedule_once(2, greet, "张三")
print(f"任务已安排, ID: {task_id}")

# 等待任务执行
time.sleep(3)
```

### 使用ScheduleUtils类

```python
from btools import ScheduleUtils
import time

scheduler = ScheduleUtils()

def task():
    print("一次性任务执行")

# 启动调度器
scheduler.start()

# 安排任务
task_id = scheduler.schedule_once(1, task)
print(f"任务ID: {task_id}")

# 检查调度器状态
print(f"调度器运行中: {scheduler.is_running()}")
print(f"当前任务数: {scheduler.get_task_count()}")

time.sleep(2)

# 停止调度器
scheduler.stop()
```

## 周期性任务

### 按固定间隔执行任务

```python
from btools import schedule_interval
import time

counter = 0

def count():
    """计数函数"""
    global counter
    counter += 1
    print(f"第 {counter} 次执行, 时间: {time.strftime('%H:%M:%S')}")

# 每1秒执行一次
task_id = schedule_interval(1, count)
print(f"周期性任务已安排, ID: {task_id}")

# 执行5秒后停止
time.sleep(5)

# 取消任务
from btools import cancel_task
cancel_task(task_id)
print("任务已取消")

time.sleep(2)
```

### 固定速率与固定延迟

```python
from btools import schedule_at_fixed_rate, schedule_with_fixed_delay
import time

def slow_task(name):
    """耗时任务"""
    print(f"{name} 开始执行: {time.strftime('%H:%M:%S')}")
    time.sleep(1.5)  # 模拟耗时操作
    print(f"{name} 执行完成: {time.strftime('%H:%M:%S')}")

print("=== 固定速率示例 ===")
# 固定速率：不考虑任务执行时间，每2秒触发一次
rate_id = schedule_at_fixed_rate(2, slow_task, "固定速率任务")
time.sleep(6)
from btools import cancel_task
cancel_task(rate_id)

print("\n=== 固定延迟示例 ===")
# 固定延迟：考虑任务执行时间，任务完成后延迟2秒再执行
delay_id = schedule_with_fixed_delay(2, slow_task, "固定延迟任务")
time.sleep(6)
cancel_task(delay_id)
```

## 任务管理

### 取消任务

```python
from btools import ScheduleUtils
import time

scheduler = ScheduleUtils()
scheduler.start()

def task1():
    print("任务1执行")

def task2():
    print("任务2执行")

# 安排两个任务
id1 = scheduler.schedule_once(2, task1)
id2 = scheduler.schedule_once(3, task2)

print(f"当前任务数: {scheduler.get_task_count()}")

# 取消任务1
scheduler.cancel_task(id1)
print(f"取消任务1后, 任务数: {scheduler.get_task_count()}")

time.sleep(4)

# 取消所有任务
scheduler.cancel_all()
print(f"取消所有任务后, 任务数: {scheduler.get_task_count()}")

scheduler.stop()
```

### 使用全局调度器

```python
from btools import (
    schedule_once, schedule_interval, cancel_task, cancel_all,
    start_scheduler, stop_scheduler
)
import time

def task_a():
    print("任务A执行")

def task_b():
    print("任务B执行")

# 启动调度器
start_scheduler()

# 安排任务
id_a = schedule_once(1, task_a)
id_b = schedule_interval(2, task_b)

print("任务已安排")
time.sleep(5)

# 取消单个任务
cancel_task(id_b)
print("任务B已取消")

time.sleep(2)

# 取消所有任务并停止调度器
cancel_all()
stop_scheduler()
print("调度器已停止")
```

## 完整示例

### 数据备份调度器

```python
from btools import ScheduleUtils
import time
import os

class BackupManager:
    """数据备份管理器"""
    
    def __init__(self):
        self.scheduler = ScheduleUtils()
        self.backup_count = 0
    
    def backup_data(self, source_dir, backup_dir):
        """备份数据"""
        self.backup_count += 1
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        print(f"[{timestamp}] 开始备份: {source_dir} -> {backup_dir}")
        print(f"这是第 {self.backup_count} 次备份")
        # 模拟备份过程
        time.sleep(0.5)
        print(f"[{timestamp}] 备份完成")
    
    def start(self):
        """启动备份调度器"""
        self.scheduler.start()
        # 每10秒备份一次
        self.scheduler.schedule_interval(
            10, 
            self.backup_data, 
            "/data/source", 
            "/data/backup"
        )
        print("备份调度器已启动")
    
    def stop(self):
        """停止备份调度器"""
        self.scheduler.stop()
        print("备份调度器已停止")

# 使用示例
manager = BackupManager()
manager.start()

# 运行35秒
time.sleep(35)

manager.stop()
```

### 定时提醒系统

```python
from btools import schedule_once, schedule_interval
import time

class ReminderSystem:
    """定时提醒系统"""
    
    def __init__(self):
        self.reminders = []
    
    def add_reminder(self, message, delay_seconds):
        """添加一次性提醒"""
        def remind():
            print(f"\n⏰ 提醒: {message}")
        
        task_id = schedule_once(delay_seconds, remind)
        self.reminders.append(task_id)
        print(f"已添加提醒: '{message}', 将在 {delay_seconds} 秒后提醒")
    
    def add_periodic_reminder(self, message, interval_seconds):
        """添加周期性提醒"""
        def remind():
            print(f"\n🔔 周期性提醒: {message}")
        
        task_id = schedule_interval(interval_seconds, remind)
        self.reminders.append(task_id)
        print(f"已添加周期性提醒: '{message}', 每 {interval_seconds} 秒提醒一次")

# 使用示例
system = ReminderSystem()

print("=== 定时提醒系统 ===")
print(f"当前时间: {time.strftime('%H:%M:%S')}")

# 添加一次性提醒
system.add_reminder("5秒后喝水", 5)
system.add_reminder("10秒后休息", 10)

# 添加周期性提醒
system.add_periodic_reminder("每3秒眨眼", 3)

# 运行15秒
time.sleep(15)

# 取消所有提醒
from btools import cancel_all
cancel_all()
print("\n所有提醒已取消")
```

### 健康检查系统

```python
from btools import ScheduleUtils
import time
import random

class HealthChecker:
    """健康检查系统"""
    
    def __init__(self):
        self.scheduler = ScheduleUtils()
        self.services = {
            "database": "ok",
            "api": "ok",
            "cache": "ok"
        }
    
    def check_service(self, service_name):
        """检查服务状态"""
        # 模拟随机故障
        status = "error" if random.random() < 0.1 else "ok"
        self.services[service_name] = status
        
        timestamp = time.strftime('%H:%M:%S')
        if status == "ok":
            print(f"[{timestamp}] ✓ {service_name}: 正常")
        else:
            print(f"[{timestamp}] ✗ {service_name}: 异常!")
    
    def start(self):
        """启动健康检查"""
        self.scheduler.start()
        
        # 每2秒检查数据库
        self.scheduler.schedule_interval(2, self.check_service, "database")
        
        # 每3秒检查API
        self.scheduler.schedule_interval(3, self.check_service, "api")
        
        # 每5秒检查缓存
        self.scheduler.schedule_interval(5, self.check_service, "cache")
        
        print("健康检查已启动")
    
    def stop(self):
        """停止健康检查"""
        self.scheduler.stop()
        print("健康检查已停止")

# 使用示例
checker = HealthChecker()
checker.start()

# 运行15秒
time.sleep(15)

checker.stop()

# 打印最终状态
print("\n最终服务状态:")
for service, status in checker.services.items():
    print(f"  {service}: {status}")
```

## 常见问题

### Q: 如何在任务执行时传递参数？

A: 可以通过 `*args` 和 `**kwargs` 传递参数：

```python
from btools import schedule_once

def task_with_args(a, b, c=None):
    print(f"a={a}, b={b}, c={c}")

# 位置参数
schedule_once(1, task_with_args, 1, 2)

# 关键字参数
schedule_once(2, task_with_args, 1, 2, c=3)
```

### Q: 如何处理任务中的异常？

A: 建议在任务函数内部处理异常：

```python
from btools import schedule_interval
import time

def safe_task():
    """安全的任务函数"""
    try:
        # 可能出错的代码
        result = 1 / 0  # 会触发异常
        print(f"结果: {result}")
    except Exception as e:
        print(f"任务执行出错: {e}")

# 即使出错，后续任务也会继续执行
schedule_interval(2, safe_task)
time.sleep(6)
```

### Q: 如何确保程序退出时清理调度器？

A: 可以使用 try-finally 或 atexit 模块：

```python
from btools import ScheduleUtils
import time
import atexit

scheduler = ScheduleUtils()

def cleanup():
    """清理函数"""
    print("\n正在清理...")
    scheduler.stop()
    print("清理完成")

# 注册退出时的清理函数
atexit.register(cleanup)

# 启动调度器
scheduler.start()
scheduler.schedule_interval(1, lambda: print("任务执行"))

print("按 Ctrl+C 退出")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n收到中断信号")
```
