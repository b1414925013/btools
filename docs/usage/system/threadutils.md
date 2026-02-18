# ThreadUtils 使用指南

`ThreadUtils` 类提供了线程操作的便捷方法，包括线程创建、线程池、超时执行、线程本地存储等功能。

## 基本使用

### 导入方式

```python
from btools import ThreadUtils, ThreadPool, ThreadLocal, thread_local

# 或使用便捷函数
from btools import (
    create_thread, start_thread, wait_for_threads,
    run_in_threadpool, run_with_timeout,
    get_current_thread_name, get_current_thread_id, sleep
)
```

## 线程创建与管理

### 创建线程

```python
from btools import ThreadUtils
import time

def print_message(message):
    """打印消息的示例函数"""
    time.sleep(1)
    print(f"线程: {ThreadUtils.get_current_thread_name()}, 消息: {message}")

# 创建线程（不启动）
thread = ThreadUtils.create_thread(
    target=print_message,
    args=("Hello World",),
    name="MyThread"
)

print(f"线程创建: {thread.name}")

# 启动线程
thread.start()
thread.join()
```

### 创建并启动线程

```python
from btools import start_thread
import time

def task(name, delay):
    """带延迟的任务"""
    time.sleep(delay)
    print(f"任务 {name} 完成")

# 直接启动线程
thread = start_thread(
    target=task,
    args=("Task1", 1),
    kwargs={"delay": 2},
    name="WorkerThread"
)

print(f"线程已启动: {thread.name}")
thread.join()
```

### 等待多个线程完成

```python
from btools import start_thread, wait_for_threads
import time

def worker(number):
    """工作线程"""
    time.sleep(0.5)
    print(f"Worker {number} 完成")

# 创建并启动多个线程
threads = []
for i in range(5):
    thread = start_thread(
        target=worker,
        args=(i,),
        name=f"Worker-{i}"
    )
    threads.append(thread)

print("等待所有线程完成...")
# 等待所有线程完成
all_done = wait_for_threads(threads, timeout=10)
print(f"所有线程完成: {all_done}")
```

## 线程池使用

### 在线程池中运行多个函数

```python
from btools import run_in_threadpool
import time

def compute(x):
    """计算函数"""
    time.sleep(0.5)
    return x * x

# 准备函数列表和参数列表
funcs = [compute, compute, compute, compute, compute]
args_list = [(1,), (2,), (3,), (4,), (5,)]

# 在线程池中运行
results = run_in_threadpool(funcs, args_list, max_workers=3)
print(f"计算结果: {results}")
```

### 使用ThreadPool类

```python
from btools import ThreadPool
import time

def download_file(url):
    """模拟下载文件"""
    print(f"开始下载: {url}")
    time.sleep(1)
    print(f"下载完成: {url}")
    return f"文件内容: {url}"

# 创建线程池
pool = ThreadPool(max_workers=3)

# 提交任务
future1 = pool.submit(download_file, "https://example.com/file1")
future2 = pool.submit(download_file, "https://example.com/file2")
future3 = pool.submit(download_file, "https://example.com/file3")
future4 = pool.submit(download_file, "https://example.com/file4")

# 获取结果
print(f"File1 结果: {future1.result()}")
print(f"File2 结果: {future2.result()}")

# 使用map方法
urls = ["https://example.com/a", "https://example.com/b", "https://example.com/c"]
map_results = pool.map(download_file, urls)
print(f"Map 结果: {map_results}")

# 等待所有任务完成
pool.wait_completion(timeout=10)

# 关闭线程池
pool.shutdown()
```

## 超时执行

### 带超时的函数执行

```python
from btools import run_with_timeout
import time

def fast_function():
    """快速函数"""
    time.sleep(1)
    return "快速函数完成"

def slow_function():
    """慢速函数"""
    time.sleep(5)
    return "慢速函数完成"

try:
    # 执行快速函数（不会超时）
    result1 = run_with_timeout(fast_function, timeout=3)
    print(f"快速函数结果: {result1}")
    
    # 执行慢速函数（会超时）
    result2 = run_with_timeout(slow_function, timeout=3)
    print(f"慢速函数结果: {result2}")
except TimeoutError as e:
    print(f"超时错误: {e}")
```

### 带参数的超时执行

```python
from btools import run_with_timeout
import time

def process_data(data, multiplier):
    """处理数据的函数"""
    time.sleep(2)
    return [x * multiplier for x in data]

try:
    data = [1, 2, 3, 4, 5]
    result = run_with_timeout(
        process_data,
        args=(data,),
        kwargs={"multiplier": 2},
        timeout=5
    )
    print(f"处理结果: {result}")
except TimeoutError as e:
    print(f"处理超时: {e}")
```

## 线程本地存储

### 使用ThreadLocal类

```python
from btools import ThreadLocal
import threading
import time

# 创建线程本地存储实例
local_storage = ThreadLocal()

def set_user_id(user_id):
    """设置用户ID"""
    local_storage.set("user_id", user_id)
    time.sleep(0.5)
    # 获取用户ID
    stored_id = local_storage.get("user_id")
    print(f"线程 {threading.current_thread().name}: 用户ID = {stored_id}")

# 在多个线程中使用
threads = []
for i in range(3):
    t = threading.Thread(
        target=set_user_id,
        args=(f"USER-{i}",),
        name=f"Thread-{i}"
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### 使用全局thread_local

```python
from btools import thread_local, start_thread
import time

def worker_task(task_id):
    """工作任务"""
    thread_local.set("task_id", task_id)
    thread_local.set("status", "running")
    
    time.sleep(0.5)
    
    current_task = thread_local.get("task_id")
    current_status = thread_local.get("status")
    
    print(f"任务 {current_task} 状态: {current_status}")
    
    # 清除特定变量
    thread_local.remove("status")
    
    # 验证清除
    status_after = thread_local.get("status", "默认状态")
    print(f"清除后状态: {status_after}")

# 启动多个线程
for i in range(3):
    start_thread(worker_task, args=(f"Task-{i}",), name=f"Worker-{i}")

time.sleep(1)

# 清空主线程的本地存储
thread_local.clear()
```

## 获取线程信息

### 获取当前线程信息

```python
from btools import get_current_thread_name, get_current_thread_id, start_thread
import threading

def print_thread_info():
    """打印当前线程信息"""
    name = get_current_thread_name()
    thread_id = get_current_thread_id()
    print(f"线程名称: {name}")
    print(f"线程ID: {thread_id}")

# 主线程信息
print("=== 主线程信息 ===")
print_thread_info()

# 子线程信息
print("\n=== 子线程信息 ===")
thread = start_thread(print_thread_info, name="InfoThread")
thread.join()
```

### 线程睡眠

```python
from btools import sleep
import time

start_time = time.time()

print("开始睡眠...")
sleep(2)  # 睡眠2秒
print(f"睡眠结束，耗时: {time.time() - start_time:.2f} 秒")
```

## 完整示例

### 并发下载示例

```python
from btools import ThreadPool, get_current_thread_name
import time

def download(url, filename):
    """下载文件"""
    thread_name = get_current_thread_name()
    print(f"[{thread_name}] 开始下载: {filename}")
    time.sleep(1)  # 模拟下载
    print(f"[{thread_name}] 下载完成: {filename}")
    return f"{filename} 的内容"

# 创建线程池
pool = ThreadPool(max_workers=3)

# 准备下载任务
downloads = [
    ("https://example.com/file1.txt", "file1.txt"),
    ("https://example.com/file2.txt", "file2.txt"),
    ("https://example.com/file3.txt", "file3.txt"),
    ("https://example.com/file4.txt", "file4.txt"),
    ("https://example.com/file5.txt", "file5.txt"),
]

# 提交任务
futures = []
for url, filename in downloads:
    future = pool.submit(download, url, filename)
    futures.append(future)

# 获取结果
print("\n=== 下载结果 ===")
for i, future in enumerate(futures):
    result = future.result()
    print(f"文件 {i+1}: {result}")

# 关闭线程池
pool.shutdown()
print("\n所有任务完成！")
```

### Web爬虫示例

```python
from btools import ThreadPool, thread_local
import time
import random

def crawl_page(url):
    """爬取页面"""
    # 设置线程本地变量
    thread_local.set("current_url", url)
    
    # 模拟爬取
    time.sleep(random.uniform(0.5, 1.5))
    
    # 获取本地变量
    current_url = thread_local.get("current_url")
    print(f"爬取完成: {current_url}")
    
    return {
        "url": url,
        "title": f"页面标题 - {url.split('/')[-1]}",
        "content": f"页面内容 - {url}"
    }

# 创建线程池
pool = ThreadPool(max_workers=4)

# 准备URL列表
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
    "https://example.com/page4",
    "https://example.com/page5",
    "https://example.com/page6",
]

# 使用map方法
results = pool.map(crawl_page, urls)

# 处理结果
print("\n=== 爬取结果 ===")
for result in results:
    print(f"URL: {result['url']}")
    print(f"标题: {result['title']}")
    print("---")

pool.shutdown()
```

## 常见问题

### Q: 守护线程和非守护线程有什么区别？

A: 守护线程会在主线程结束时自动终止，而非守护线程会继续执行直到完成。示例：

```python
from btools import start_thread
import time

def daemon_task():
    """守护线程任务"""
    for i in range(5):
        time.sleep(1)
        print(f"守护线程: {i}")

def normal_task():
    """非守护线程任务"""
    for i in range(3):
        time.sleep(1)
        print(f"非守护线程: {i}")

# 启动守护线程
start_thread(daemon_task, daemon=True, name="Daemon")

# 启动非守护线程
start_thread(normal_task, daemon=False, name="Normal")

print("主线程结束")
```

### Q: 如何处理线程池中的异常？

A: 可以通过future对象捕获异常：

```python
from btools import ThreadPool

def risky_task(x):
    """有风险的任务"""
    if x == 3:
        raise ValueError("x 不能是 3")
    return x * 2

pool = ThreadPool()
futures = []

for i in range(5):
    future = pool.submit(risky_task, i)
    futures.append(future)

for i, future in enumerate(futures):
    try:
        result = future.result()
        print(f"任务 {i} 结果: {result}")
    except Exception as e:
        print(f"任务 {i} 异常: {e}")

pool.shutdown()
```
