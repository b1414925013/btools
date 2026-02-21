# ProcessUtils 使用指南

`ProcessUtils` 类提供了跨平台进程管理功能，用于启动、监控、终止进程。

## 基本使用

### 启动进程

```python
from btools import ProcessUtils

# 启动进程
process = ProcessUtils.start_process(
    command=["python", "script.py"],
    cwd="/working/dir",
    env={"VAR": "value"}
)

# 获取进程 ID
pid = process.pid
print(f"进程 ID: {pid}")
```

### 等待进程完成

```python
from btools import ProcessUtils

# 运行并等待进程完成
result = ProcessUtils.run_process(
    command=["python", "script.py"],
    capture_output=True,
    timeout=30
)

print(f"返回码: {result.returncode}")
print(f"标准输出: {result.stdout}")
print(f"标准错误: {result.stderr}")
```

### 检查进程状态

```python
from btools import ProcessUtils

# 检查进程是否正在运行
is_running = ProcessUtils.is_process_running(pid)

# 获取进程信息
info = ProcessUtils.get_process_info(pid)
print(f"进程名: {info['name']}")
print(f"内存使用: {info['memory']}")
print(f"CPU 使用: {info['cpu']}")
```

## 进程管理

### 列出进程

```python
from btools import ProcessUtils

# 列出所有进程
all_processes = ProcessUtils.list_processes()
for proc in all_processes:
    print(f"{proc['pid']}: {proc['name']}")

# 按名称搜索进程
matching = ProcessUtils.find_processes_by_name("python")
print(matching)

# 按命令行搜索
matching = ProcessUtils.find_processes_by_cmdline("script.py")
print(matching)
```

### 终止进程

```python
from btools import ProcessUtils

# 优雅终止进程
success = ProcessUtils.terminate_process(pid)

# 强制终止进程
success = ProcessUtils.kill_process(pid)

# 终止进程树（包括子进程）
success = ProcessUtils.terminate_process_tree(pid)
```

### 进程信号

```python
from btools import ProcessUtils

# 发送信号到进程
success = ProcessUtils.send_signal(pid, signal.SIGTERM)

# 暂停进程
success = ProcessUtils.suspend_process(pid)

# 恢复进程
success = ProcessUtils.resume_process(pid)
```

## 高级功能

### 进程监控

```python
from btools import ProcessUtils
import time

# 监控进程
with ProcessUtils.monitor_process(pid) as monitor:
    time.sleep(5)
    stats = monitor.get_stats()
    print(f"CPU: {stats['cpu_percent']}%")
    print(f"内存: {stats['memory_mb']}MB")
```

### 异步进程执行

```python
from btools import ProcessUtils

# 异步执行进程
async def run_async():
    result = await ProcessUtils.run_process_async(
        command=["python", "script.py"]
    )
    print(result.returncode)
```

### 进程池

```python
from btools import ProcessUtils

# 创建进程池
with ProcessUtils.create_process_pool(max_workers=4) as pool:
    # 提交任务
    futures = [
        pool.submit(ProcessUtils.run_process, ["python", f"script_{i}.py"])
        for i in range(10)
    ]
    
    # 获取结果
    for future in futures:
        result = future.result()
        print(result.returncode)
```

### 进程通信

```python
from btools import ProcessUtils

# 使用管道通信
process = ProcessUtils.start_process(
    command=["python", "script.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# 发送输入
stdout, stderr = process.communicate(input=b"input data")
```

### 超时控制

```python
from btools import ProcessUtils

# 带超时执行
try:
    result = ProcessUtils.run_process(
        command=["python", "slow_script.py"],
        timeout=10
    )
except subprocess.TimeoutExpired:
    print("进程超时")
    ProcessUtils.kill_process(pid)
```

## 子进程管理

```python
from btools import ProcessUtils

# 获取子进程
children = ProcessUtils.get_child_processes(pid)
print(children)

# 等待所有子进程
ProcessUtils.wait_for_children(pid)
```

## 资源使用监控

```python
from btools import ProcessUtils

# 获取进程资源使用
usage = ProcessUtils.get_resource_usage(pid)
print(f"CPU 时间: {usage['cpu_time']}")
print(f"内存使用: {usage['memory']}")
print(f"IO 读取: {usage['io_read']}")
print(f"IO 写入: {usage['io_write']}")
```

## 进程优先级

```python
from btools import ProcessUtils

# 获取进程优先级
priority = ProcessUtils.get_priority(pid)
print(priority)

# 设置进程优先级
success = ProcessUtils.set_priority(pid, 10)  # 10 = 低优先级

# 设置为高优先级
success = ProcessUtils.set_high_priority(pid)

# 设置为低优先级
success = ProcessUtils.set_low_priority(pid)
```

## 守护进程

```python
from btools import ProcessUtils

# 创建守护进程
ProcessUtils.daemonize()

# 或者作为上下文管理器
with ProcessUtils.daemon_context():
    # 这里的代码在守护进程中运行
    pass
```

## 平台特定注意事项

### Windows 进程

```python
from btools import ProcessUtils

if PlatformUtils.is_windows():
    # Windows 特定的进程操作
    info = ProcessUtils.get_windows_process_info(pid)
    print(info)
```

### Linux 进程

```python
from btools import ProcessUtils

if PlatformUtils.is_linux():
    # Linux 特定的进程操作
    info = ProcessUtils.get_linux_process_info(pid)
    print(info)
    
    # 读取 /proc 信息
    proc_info = ProcessUtils.read_proc_info(pid)
    print(proc_info)
```

### macOS 进程

```python
from btools import ProcessUtils

if PlatformUtils.is_macos():
    # macOS 特定的进程操作
    info = ProcessUtils.get_macos_process_info(pid)
    print(info)
```

## 最佳实践

1. **总是处理超时**
   ```python
   try:
       result = ProcessUtils.run_process(cmd, timeout=30)
   except subprocess.TimeoutExpired:
       ProcessUtils.kill_process(pid)
   ```

2. **捕获输出用于调试**
   ```python
   result = ProcessUtils.run_process(cmd, capture_output=True)
   if result.returncode != 0:
       print(result.stderr)
   ```

3. **优雅终止后强制终止**
   ```python
   ProcessUtils.terminate_process(pid)
   time.sleep(5)
   if ProcessUtils.is_process_running(pid):
       ProcessUtils.kill_process(pid)
   ```
