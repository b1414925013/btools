# SystemUtils 使用指南

`SystemUtils` 是一个系统工具类，提供了丰富的系统操作方法，包括获取操作系统信息、获取Python版本、获取系统架构、获取主机名、获取IP地址、获取环境变量、获取当前工作目录、获取临时目录、获取主目录、获取当前进程ID、获取当前进程名称、获取CPU数量、执行命令等功能。

## 功能特性

- 获取操作系统名称
- 获取Python版本
- 获取系统架构
- 获取主机名
- 获取IP地址
- 获取环境变量
- 检查环境变量是否存在
- 获取当前工作目录
- 获取临时目录
- 获取主目录
- 获取当前进程ID
- 获取当前进程名称
- 获取CPU数量
- 执行命令
- 获取系统时间
- 检查是否为Windows
- 检查是否为Linux
- 检查是否为macOS

## 基本用法

### 导入

```python
from btools import SystemUtils
```

### 示例

#### 获取系统信息

```python
# 获取操作系统名称
print(SystemUtils.get_os_name())  # 输出: Windows

# 获取Python版本
print(SystemUtils.get_python_version())  # 输出: 3.11.0

# 获取系统架构
print(SystemUtils.get_system_architecture())  # 输出: AMD64

# 获取主机名
print(SystemUtils.get_hostname())  # 输出: 主机名

# 获取IP地址
print(SystemUtils.get_ip_address())  # 输出: IP地址
```

#### 环境变量操作

```python
# 获取环境变量
path = SystemUtils.get_env("PATH")
print(path)  # 输出: PATH环境变量的值

# 检查环境变量是否存在
print(SystemUtils.has_env("PATH"))  # 输出: True
print(SystemUtils.has_env("NON_EXISTENT_VAR"))  # 输出: False
```

#### 目录操作

```python
# 获取当前工作目录
print(SystemUtils.get_cwd())  # 输出: 当前工作目录路径

# 获取临时目录
print(SystemUtils.get_temp_dir())  # 输出: 临时目录路径

# 获取主目录
print(SystemUtils.get_home_dir())  # 输出: 主目录路径
```

#### 进程操作

```python
# 获取当前进程ID
print(SystemUtils.get_current_process_id())  # 输出: 当前进程ID

# 获取当前进程名称
print(SystemUtils.get_current_process_name())  # 输出: 当前进程名称

# 获取CPU数量
print(SystemUtils.get_cpu_count())  # 输出: CPU数量
```

#### 命令执行

```python
# 执行命令
if SystemUtils.is_windows():
    result = SystemUtils.execute_command("echo hello")
else:
    result = SystemUtils.execute_command("echo 'hello'")
print(result)  # 输出: (返回码, 标准输出, 标准错误)
```

#### 系统时间

```python
# 获取系统时间
print(SystemUtils.get_system_time())  # 输出: 系统时间戳
```

#### 操作系统检查

```python
# 检查是否为Windows
print(SystemUtils.is_windows())  # 输出: True

# 检查是否为Linux
print(SystemUtils.is_linux())  # 输出: False

# 检查是否为macOS
print(SystemUtils.is_macos())  # 输出: False
```

## 高级用法

### 执行复杂命令

```python
# 执行复杂命令
if SystemUtils.is_windows():
    result = SystemUtils.execute_command("dir /s /b")
else:
    result = SystemUtils.execute_command("find . -name '*.py'")
print(result)  # 输出: (返回码, 标准输出, 标准错误)
```

### 检查操作系统类型并执行相应命令

```python
# 检查操作系统类型并执行相应命令
if SystemUtils.is_windows():
    # Windows 命令
    result = SystemUtils.execute_command("ipconfig")
elif SystemUtils.is_linux():
    # Linux 命令
    result = SystemUtils.execute_command("ifconfig")
elif SystemUtils.is_macos():
    # macOS 命令
    result = SystemUtils.execute_command("ifconfig")
print(result)  # 输出: (返回码, 标准输出, 标准错误)
```

## 注意事项

1. `execute_command()` 方法会执行系统命令，因此在使用时需要注意安全性，避免执行恶意命令。
2. 获取IP地址可能会返回多个IP地址，具体取决于系统配置。
3. 执行长时间运行的命令可能会导致程序阻塞，因此在使用时需要注意。

## 总结

`SystemUtils` 提供了全面的系统操作功能，简化了系统操作的复杂度，使代码更加简洁易读。无论是基本的系统信息获取还是高级的命令执行，`SystemUtils` 都能满足你的需求。