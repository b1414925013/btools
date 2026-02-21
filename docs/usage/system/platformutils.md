# PlatformUtils 使用指南

`PlatformUtils` 类提供了跨平台兼容工具，用于处理不同操作系统的差异。

## 基本使用

### 获取平台信息

```python
from btools import PlatformUtils

# 获取操作系统名称
os_name = PlatformUtils.get_os_name()
print(os_name)  # "Windows", "Linux", "Darwin" (macOS)

# 获取操作系统版本
os_version = PlatformUtils.get_os_version()
print(os_version)

# 获取架构
architecture = PlatformUtils.get_architecture()
print(architecture)  # "x86_64", "arm64"

# 获取完整平台信息
platform_info = PlatformUtils.get_platform_info()
print(platform_info)
```

### 平台检查

```python
from btools import PlatformUtils

# 检查是否为 Windows
is_windows = PlatformUtils.is_windows()

# 检查是否为 Linux
is_linux = PlatformUtils.is_linux()

# 检查是否为 macOS
is_macos = PlatformUtils.is_macos()

# 检查是否为 Unix-like (Linux/macOS)
is_unix = PlatformUtils.is_unix()
```

## 高级功能

### 路径处理

```python
from btools import PlatformUtils

# 获取路径分隔符
sep = PlatformUtils.get_path_separator()
print(sep)  # "\\" (Windows), "/" (Unix)

# 获取环境变量分隔符
pathsep = PlatformUtils.get_path_separator()
print(pathsep)  # ";" (Windows), ":" (Unix)

# 获取换行符
newline = PlatformUtils.get_newline()
print(newline)  # "\r\n" (Windows), "\n" (Unix)
```

### 环境变量

```python
from btools import PlatformUtils

# 获取 PATH 环境变量
path = PlatformUtils.get_path_env()
print(path)

# 添加到 PATH
PlatformUtils.add_to_path("/new/path")

# 从 PATH 移除
PlatformUtils.remove_from_path("/old/path")

# 检查是否在 PATH 中
in_path = PlatformUtils.is_in_path("/some/path")
```

### 可执行文件扩展名

```python
from btools import PlatformUtils

# 获取可执行文件扩展名
exe_ext = PlatformUtils.get_executable_extension()
print(exe_ext)  # ".exe" (Windows), "" (Unix)

# 获取可执行文件名
exe_name = PlatformUtils.get_executable_name("myapp")
print(exe_name)  # "myapp.exe" (Windows), "myapp" (Unix)
```

### 系统目录

```python
from btools import PlatformUtils

# 获取临时目录
temp_dir = PlatformUtils.get_temp_dir()
print(temp_dir)

# 获取用户主目录
home_dir = PlatformUtils.get_home_dir()
print(home_dir)

# 获取应用数据目录
app_data = PlatformUtils.get_app_data_dir("MyApp")
print(app_data)

# 获取系统配置目录
config_dir = PlatformUtils.get_config_dir("MyApp")
print(config_dir)
```

## 平台特定操作

### Windows 特定

```python
from btools import PlatformUtils

if PlatformUtils.is_windows():
    # 获取 Windows 版本
    win_version = PlatformUtils.get_windows_version()
    
    # 获取 Program Files 目录
    program_files = PlatformUtils.get_program_files_dir()
    
    # 获取 Program Files (x86) 目录
    program_files_x86 = PlatformUtils.get_program_files_x86_dir()
    
    # 获取 AppData 目录
    app_data = PlatformUtils.get_appdata_dir()
    
    # 获取 LocalAppData 目录
    local_app_data = PlatformUtils.get_localappdata_dir()
```

### Linux 特定

```python
from btools import PlatformUtils

if PlatformUtils.is_linux():
    # 获取 Linux 发行版
    distro = PlatformUtils.get_linux_distro()
    print(distro)  # "Ubuntu", "CentOS", "Debian"
    
    # 获取发行版版本
    distro_version = PlatformUtils.get_linux_distro_version()
    
    # 获取 /etc 目录
    etc_dir = PlatformUtils.get_etc_dir()
    
    # 获取 /var 目录
    var_dir = PlatformUtils.get_var_dir()
```

### macOS 特定

```python
from btools import PlatformUtils

if PlatformUtils.is_macos():
    # 获取 macOS 版本
    macos_version = PlatformUtils.get_macos_version()
    
    # 获取应用程序目录
    applications_dir = PlatformUtils.get_applications_dir()
    
    # 获取 Library 目录
    library_dir = PlatformUtils.get_library_dir()
    
    # 获取用户 Library 目录
    user_library_dir = PlatformUtils.get_user_library_dir()
```

## 执行平台特定代码

```python
from btools import PlatformUtils

# 使用装饰器
@PlatformUtils.on_windows
def windows_only():
    print("只在 Windows 上执行")

@PlatformUtils.on_linux
def linux_only():
    print("只在 Linux 上执行")

@PlatformUtils.on_macos
def macos_only():
    print("只在 macOS 上执行")

# 使用条件执行
PlatformUtils.execute_on_platform({
    'windows': lambda: print("Windows"),
    'linux': lambda: print("Linux"),
    'macos': lambda: print("macOS"),
    'default': lambda: print("其他平台")
})
```

## 系统命令

```python
from btools import PlatformUtils

# 获取正确的命令
command = PlatformUtils.get_command('ls')
# Windows: 'dir', Unix: 'ls'

command = PlatformUtils.get_command('clear')
# Windows: 'cls', Unix: 'clear'

command = PlatformUtils.get_command('copy')
# Windows: 'copy', Unix: 'cp'
```

## 权限检查

```python
from btools import PlatformUtils

# 检查是否为管理员/root
is_admin = PlatformUtils.is_admin()

# 检查是否具有写权限
can_write = PlatformUtils.has_write_permission("/path/to/dir")

# 检查是否具有读权限
can_read = PlatformUtils.has_read_permission("/path/to/file")
```

## 平台信息对照表

| 属性 | Windows | Linux | macOS |
|------|---------|-------|-------|
| `is_windows()` | True | False | False |
| `is_linux()` | False | True | False |
| `is_macos()` | False | False | True |
| `is_unix()` | False | True | True |
| 路径分隔符 | `\\` | `/` | `/` |
| 换行符 | `\r\n` | `\n` | `\n` |
| 可执行文件扩展名 | `.exe` | 无 | 无 |
