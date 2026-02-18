# RuntimeUtil - 命令行工具类

## 功能特性

`RuntimeUtil` 是一个命令行工具类，提供了丰富的命令行执行功能，包括：

- 执行命令并返回执行结果
- 执行命令并返回标准输出
- 执行命令并返回标准输出的行列表
- 执行命令并等待完成，返回是否执行成功
- 异步执行命令，返回进程对象
- 获取进程的输出
- 获取系统信息
- 获取运行时信息
- 环境变量操作（获取、设置、移除）
- 操作系统检测（Windows、Linux、Mac）
- 运行脚本文件
- 终止指定进程
- 线程休眠

## 基本用法

### 导入模块

```python
from btools.core.basic import RuntimeUtil
```

### 1. 执行命令并返回结果

```python
# 执行命令并返回 (返回码, 标准输出, 标准错误)
returncode, stdout, stderr = RuntimeUtil.exec("echo hello")
print(f"返回码: {returncode}")  # 输出: 返回码: 0
print(f"标准输出: {stdout}")  # 输出: 标准输出: hello
print(f"标准错误: {stderr}")  # 输出: 标准错误: 
```

### 2. 执行命令并返回标准输出

```python
# 执行命令并返回标准输出
output = RuntimeUtil.execForStr("echo hello")
print(output)  # 输出: hello
```

### 3. 执行命令并返回标准输出的行列表

```python
# 执行命令并返回标准输出的行列表
lines = RuntimeUtil.execForLines("echo hello && echo world")
print(lines)  # 输出: ['hello', 'world']
```

### 4. 执行命令并等待完成，返回是否执行成功

```python
# 执行命令并等待完成，返回是否执行成功
success = RuntimeUtil.execWait("echo hello")
print(success)  # 输出: True
```

### 5. 异步执行命令，返回进程对象

```python
# 异步执行命令，返回进程对象
process = RuntimeUtil.execAsync("echo hello")

# 等待进程完成
process.wait()

# 获取进程的返回码
returncode = process.returncode
print(f"返回码: {returncode}")  # 输出: 返回码: 0
```

### 6. 获取进程的输出

```python
# 异步执行命令
process = RuntimeUtil.execAsync("echo hello")

# 获取进程的输出
stdout, stderr = RuntimeUtil.getProcessOutput(process)
print(f"标准输出: {stdout}")  # 输出: 标准输出: hello
print(f"标准错误: {stderr}")  # 输出: 标准错误: 
```

### 7. 获取系统信息

```python
# 获取系统信息
system_info = RuntimeUtil.getSystemInfo()
print(system_info)

# 输出示例:
# {
#     'system': 'Windows',
#     'release': '10',
#     'version': '10.0.19045',
#     'machine': 'AMD64',
#     'processor': 'Intel64 Family 6 Model 142 Stepping 12, GenuineIntel',
#     'python_version': '3.10.11',
#     'python_implementation': 'CPython',
#     'python_compiler': 'MSC v.1934 64 bit (AMD64)',
#     'os_name': 'nt'
# }
```

### 8. 获取运行时信息

```python
# 获取运行时信息
runtime_info = RuntimeUtil.getRuntimeInfo()
print(f"当前工作目录: {runtime_info['cwd']}")
print(f"进程ID: {runtime_info['pid']}")
print(f"父进程ID: {runtime_info['ppid']}")
print(f"Python解释器路径: {runtime_info['python_path']}")
print(f"Python版本: {runtime_info['python_version']}")
print(f"系统平台: {runtime_info['sys_platform']}")
```

### 9. 环境变量操作

```python
# 获取环境变量
path = RuntimeUtil.getEnv("PATH")
print(f"PATH环境变量: {path}")

# 获取不存在的环境变量，使用默认值
test_var = RuntimeUtil.getEnv("TEST_VAR", "default_value")
print(f"TEST_VAR环境变量: {test_var}")  # 输出: TEST_VAR环境变量: default_value

# 设置环境变量
RuntimeUtil.setEnv("TEST_VAR", "test_value")
test_var = RuntimeUtil.getEnv("TEST_VAR")
print(f"TEST_VAR环境变量: {test_var}")  # 输出: TEST_VAR环境变量: test_value

# 移除环境变量
RuntimeUtil.unsetEnv("TEST_VAR")
test_var = RuntimeUtil.getEnv("TEST_VAR")
print(f"TEST_VAR环境变量: {test_var}")  # 输出: TEST_VAR环境变量: None
```

### 10. 操作系统检测

```python
# 获取操作系统名称
os_name = RuntimeUtil.getOsName()
print(f"操作系统名称: {os_name}")

# 检测是否为Windows系统
is_windows = RuntimeUtil.isWindows()
print(f"是否为Windows系统: {is_windows}")

# 检测是否为Linux系统
is_linux = RuntimeUtil.isLinux()
print(f"是否为Linux系统: {is_linux}")

# 检测是否为Mac系统
is_mac = RuntimeUtil.isMac()
print(f"是否为Mac系统: {is_mac}")
```

### 11. 运行脚本文件

```python
# 创建临时Python脚本
with open("test_script.py", "w") as f:
    f.write("print('Hello from script')")

# 运行脚本文件
returncode, stdout, stderr = RuntimeUtil.runScript("test_script.py")
print(f"返回码: {returncode}")  # 输出: 返回码: 0
print(f"标准输出: {stdout}")  # 输出: 标准输出: Hello from script
print(f"标准错误: {stderr}")  # 输出: 标准错误: 

# 清理临时文件
import os
os.remove("test_script.py")
```

### 12. 终止指定进程

```python
# 异步执行一个会休眠的命令
import time
process = RuntimeUtil.execAsync("timeout 5")  # Windows系统
# 或 process = RuntimeUtil.execAsync("sleep 5")  # Linux/Mac系统

# 等待一小段时间确保进程已启动
time.sleep(0.5)

# 终止进程
success = RuntimeUtil.killProcess(process.pid)
print(f"是否终止成功: {success}")  # 输出: 是否终止成功: True

# 等待进程终止
process.wait()
print(f"进程返回码: {process.returncode}")
```

### 13. 线程休眠

```python
# 线程休眠
print("开始休眠")
RuntimeUtil.sleep(1)  # 休眠1秒
print("休眠结束")
```

## 高级用法

### 1. 执行复杂命令

```python
# 执行复杂命令，例如列出当前目录的文件
if RuntimeUtil.isWindows():
    cmd = "dir"
else:
    cmd = "ls -la"

returncode, stdout, stderr = RuntimeUtil.exec(cmd)
print(stdout)
```

### 2. 执行带参数的命令

```python
# 执行带参数的命令
if RuntimeUtil.isWindows():
    cmd = "echo Hello, %USERNAME%"
else:
    cmd = "echo Hello, $USER"

output = RuntimeUtil.execForStr(cmd)
print(output)  # 输出: Hello, 用户名
```

### 3. 执行带超时的命令

```python
# 执行带超时的命令
cmd = "timeout 10" if RuntimeUtil.isWindows() else "sleep 10"

# 设置超时为2秒
returncode, stdout, stderr = RuntimeUtil.exec(cmd, timeout=2)
print(f"返回码: {returncode}")  # 输出: 返回码: -1
print(f"标准错误: {stderr}")  # 输出: 标准错误: 命令执行超时: 2秒
```

### 4. 在指定目录执行命令

```python
# 在指定目录执行命令
import os

test_dir = "test_dir"
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# 在test_dir目录中创建一个文件
with open(os.path.join(test_dir, "test.txt"), "w") as f:
    f.write("test content")

# 在指定目录执行命令
if RuntimeUtil.isWindows():
    cmd = "dir"
else:
    cmd = "ls -la"

returncode, stdout, stderr = RuntimeUtil.exec(cmd, cwd=test_dir)
print(stdout)
```

### 5. 运行带参数的脚本

```python
# 创建带参数的脚本
with open("args_script.py", "w") as f:
    f.write("""
import sys
print(f"参数数量: {len(sys.argv) - 1}")
print(f"参数: {sys.argv[1:]}")
""")

# 运行带参数的脚本
returncode, stdout, stderr = RuntimeUtil.runScript("args_script.py", "arg1", "arg2", "arg3")
print(stdout)
# 输出:
# 参数数量: 3
# 参数: ['arg1', 'arg2', 'arg3']

# 清理临时文件
import os
os.remove("args_script.py")
```

## 注意事项

1. **安全考虑**：使用 `exec`、`execAsync` 等方法执行命令时，应避免直接拼接用户输入的命令，以防命令注入攻击。

2. **超时设置**：对于可能长时间运行的命令，建议设置合理的 `timeout` 参数，避免程序无限期等待。

3. **跨平台兼容性**：不同操作系统的命令格式可能不同，建议使用 `isWindows()`、`isLinux()`、`isMac()` 等方法进行判断，执行适合当前系统的命令。

4. **进程管理**：使用 `execAsync` 启动的进程，应确保在不需要时正确终止，避免产生僵尸进程。

5. **环境变量**：修改环境变量时，只会影响当前进程及其子进程，不会影响父进程或系统全局环境变量。

6. **权限问题**：执行某些命令可能需要管理员/root 权限，请注意权限设置。

7. **脚本执行**：运行脚本文件时，确保脚本文件有执行权限（Linux/Mac系统）。

## 总结

`RuntimeUtil` 提供了全面的命令行执行功能，简化了命令行操作的复杂度。通过这些工具方法，您可以更方便地执行命令、管理进程、获取系统信息等，提高代码的可读性和可维护性。