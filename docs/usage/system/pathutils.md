# PathUtils 使用指南

`PathUtils` 类提供了跨平台路径处理功能，统一路径格式。

## 基本使用

### 路径规范化

```python
from btools import PathUtils

# 规范化路径
path = PathUtils.normalize("path/to//file.txt")
print(path)  # "path/to/file.txt" (Unix) 或 "path\\to\\file.txt" (Windows)

# 转换为 Unix 格式
unix_path = PathUtils.to_unix("path\\to\\file.txt")
print(unix_path)  # "path/to/file.txt"

# 转换为 Windows 格式
win_path = PathUtils.to_windows("path/to/file.txt")
print(win_path)  # "path\\to\\file.txt"
```

### 路径拼接

```python
from btools import PathUtils

# 拼接路径
path = PathUtils.join("path", "to", "file.txt")
print(path)  # "path/to/file.txt" 或 "path\\to\\file.txt"

# 安全拼接
path = PathUtils.safe_join("/base", "..", "etc", "passwd")
# 返回 "/base/etc/passwd"（防止路径遍历攻击）
```

### 路径信息

```python
from btools import PathUtils

# 获取文件名
filename = PathUtils.get_filename("/path/to/file.txt")
print(filename)  # "file.txt"

# 获取文件扩展名
ext = PathUtils.get_extension("/path/to/file.txt")
print(ext)  # "txt"

# 获取目录名
dirname = PathUtils.get_dirname("/path/to/file.txt")
print(dirname)  # "/path/to"

# 获取文件名（不含扩展名）
basename = PathUtils.get_basename("/path/to/file.txt")
print(basename)  # "file"
```

### 路径检查

```python
from btools import PathUtils

# 检查是否为绝对路径
is_absolute = PathUtils.is_absolute("/path/to/file.txt")
print(is_absolute)  # True

# 检查是否为相对路径
is_relative = PathUtils.is_relative("path/to/file.txt")
print(is_relative)  # True

# 检查路径是否存在
exists = PathUtils.exists("/path/to/file.txt")

# 检查是否为文件
is_file = PathUtils.is_file("/path/to/file.txt")

# 检查是否为目录
is_dir = PathUtils.is_dir("/path/to/directory")
```

## 高级功能

### 路径操作

```python
from btools import PathUtils

# 获取绝对路径
abs_path = PathUtils.abspath("relative/path")

# 获取相对路径
rel_path = PathUtils.relpath("/absolute/path", "/base/path")

# 获取父目录
parent = PathUtils.parent("/path/to/dir/file.txt")
print(parent)  # "/path/to/dir"

# 获取根目录
root = PathUtils.root("/path/to/file.txt")
print(root)  # "/" (Unix) 或 "C:\\" (Windows)
```

### 路径修改

```python
from btools import PathUtils

# 修改扩展名
new_path = PathUtils.change_extension("/path/to/file.txt", "md")
print(new_path)  # "/path/to/file.md"

# 添加前缀
prefixed = PathUtils.add_prefix("/path/to/file.txt", "prefix_")
print(prefixed)  # "/path/to/prefix_file.txt"

# 添加后缀
suffixed = PathUtils.add_suffix("/path/to/file.txt", "_suffix")
print(suffixed)  # "/path/to/file_suffix.txt"
```

### 路径列表操作

```python
from btools import PathUtils

# 分割路径
parts = PathUtils.split("/path/to/file.txt")
print(parts)  # ["", "path", "to", "file.txt"]

# 展开用户目录
expanded = PathUtils.expand_user("~/Documents/file.txt")
print(expanded)  # "/home/user/Documents/file.txt"

# 展开环境变量
expanded = PathUtils.expand_vars("$HOME/Documents/$FILE")
```

### 临时路径

```python
from btools import PathUtils

# 获取临时目录
temp_dir = PathUtils.get_temp_dir()
print(temp_dir)

# 创建临时文件路径
temp_file = PathUtils.get_temp_file(suffix=".txt")
print(temp_file)

# 创建临时目录路径
temp_dir_path = PathUtils.get_temp_directory(prefix="mytemp_")
print(temp_dir_path)
```

### 特殊路径

```python
from btools import PathUtils

# 获取用户主目录
home = PathUtils.get_home_dir()
print(home)

# 获取当前工作目录
cwd = PathUtils.get_cwd()
print(cwd)

# 获取应用数据目录
app_data = PathUtils.get_app_data_dir("MyApp")
print(app_data)

# 获取配置目录
config_dir = PathUtils.get_config_dir("MyApp")
print(config_dir)
```

## 路径验证

```python
from btools import PathUtils

# 验证路径格式
is_valid = PathUtils.is_valid_path("/path/to/file.txt")

# 检查是否包含非法字符
has_illegal = PathUtils.has_illegal_chars("file?name.txt")
print(has_illegal)  # True

# 清理路径名
clean_name = PathUtils.sanitize_filename("file?name*.txt")
print(clean_name)  # "filename.txt"
```

## 通配符匹配

```python
from btools import PathUtils

# 通配符匹配
is_match = PathUtils.match("*.txt", "file.txt")
print(is_match)  # True

is_match = PathUtils.match("path/*/*.py", "path/to/file.py")
print(is_match)  # True
```

## 跨平台注意事项

| 操作 | Windows | Unix/Linux/macOS |
|------|---------|-------------------|
| 路径分隔符 | `\\` | `/` |
| 根目录 | `C:\\` | `/` |
| 用户目录 | `C:\\Users\\User` | `/home/user` |
| 临时目录 | `C:\\Users\\User\\AppData\\Local\\Temp` | `/tmp` |
