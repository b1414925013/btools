# FileUtils 使用指南

`FileUtils` 是一个文件处理工具类，提供了丰富的文件读写、目录操作、文件系统遍历等功能，帮助开发者更方便地处理文件和目录。

## 导入

```python
from btools import FileUtils
# 或
from btools.core import FileUtils
```

## 核心功能

### 文件操作

#### 1. 文件读写

```python
# 写入文件
content = "Hello, World!"
FileUtils.write_file("test.txt", content)

# 读取文件
read_content = FileUtils.read_file("test.txt")
print(read_content)  # 输出: "Hello, World!"

# 追加内容到文件
append_content = "\nAppend this line"
FileUtils.append_file("test.txt", append_content)

# 读取文件的所有行
lines = FileUtils.read_lines("test.txt")
print(lines)  # 输出: ["Hello, World!", "Append this line"]

# 写入多行到文件
new_lines = ["Line 1", "Line 2", "Line 3"]
FileUtils.write_lines("test_lines.txt", new_lines)
```

#### 2. 文件信息

```python
# 检查文件是否存在
file_exists = FileUtils.exists("test.txt")
print(f"File exists: {file_exists}")

# 检查是否是文件
is_file = FileUtils.is_file("test.txt")
print(f"Is file: {is_file}")

# 检查是否是目录
is_dir = FileUtils.is_directory("test.txt")
print(f"Is directory: {is_dir}")

# 获取文件大小（字节）
file_size = FileUtils.get_file_size("test.txt")
print(f"File size: {file_size} bytes")

# 获取文件的绝对路径
absolute_path = FileUtils.get_absolute_path("test.txt")
print(f"Absolute path: {absolute_path}")

# 获取文件的基本名称
base_name = FileUtils.get_base_name("test.txt")
print(f"Base name: {base_name}")  # 输出: "test.txt"

# 获取文件的名称（不含扩展名）
file_name = FileUtils.get_file_name("test.txt")
print(f"File name: {file_name}")  # 输出: "test"

# 获取文件的扩展名
extension = FileUtils.get_extension("test.txt")
print(f"Extension: {extension}")  # 输出: ".txt"
```

#### 3. 文件修改和删除

```python
# 复制文件
FileUtils.copy("test.txt", "test_copy.txt")

# 移动文件
FileUtils.move("test_copy.txt", "copy/test_copy.txt")

# 重命名文件
FileUtils.rename("test.txt", "renamed_test.txt")

# 删除文件
FileUtils.delete("renamed_test.txt")

# 安全删除文件（不存在时不报错）
FileUtils.safe_delete("non_existent_file.txt")
```

### 目录操作

#### 1. 目录创建和删除

```python
# 创建目录
FileUtils.create_directory("new_dir")

# 创建多级目录
FileUtils.create_directory("parent/child/grandchild")

# 删除目录（必须为空）
FileUtils.delete_directory("new_dir")

# 递归删除目录（包括所有内容）
FileUtils.delete_directory_recursive("parent")
```

#### 2. 目录遍历

```python
# 列出目录中的文件和子目录
items = FileUtils.list_directory(".")
print("Directory items:")
for item in items:
    print(f"  - {item}")

# 递归遍历目录
print("\nRecursive directory traversal:")
for root, dirs, files in FileUtils.walk("."):
    print(f"\nRoot: {root}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")

# 查找指定扩展名的文件
python_files = FileUtils.find_files(".", "*.py")
print("\nPython files:")
for file in python_files:
    print(f"  - {file}")
```

#### 3. 目录信息

```python
# 获取目录大小（递归计算所有文件大小）
dir_size = FileUtils.get_directory_size(".")
print(f"Directory size: {dir_size} bytes")

# 检查目录是否为空
is_empty = FileUtils.is_directory_empty(".")
print(f"Is directory empty: {is_empty}")
```

### 路径操作

```python
# 连接路径
path = FileUtils.join_path("parent", "child", "file.txt")
print(f"Joined path: {path}")

# 获取路径的目录部分
dir_part = FileUtils.get_directory_name("parent/child/file.txt")
print(f"Directory part: {dir_part}")  # 输出: "parent/child"

# 规范化路径
normalized_path = FileUtils.normalize_path("parent/../current/file.txt")
print(f"Normalized path: {normalized_path}")  # 输出: "current/file.txt"

# 获取相对路径
relative_path = FileUtils.get_relative_path("parent/child", "parent/other")
print(f"Relative path: {relative_path}")  # 输出: "../other"
```

### 文件系统操作

#### 1. 文件权限

```python
# 检查文件是否可读
is_readable = FileUtils.is_readable("test.txt")
print(f"Is readable: {is_readable}")

# 检查文件是否可写
is_writable = FileUtils.is_writable("test.txt")
print(f"Is writable: {is_writable}")

# 检查文件是否可执行
is_executable = FileUtils.is_executable("test.txt")
print(f"Is executable: {is_executable}")
```

#### 2. 文件时间

```python
# 获取文件的创建时间
create_time = FileUtils.get_creation_time("test.txt")
print(f"Creation time: {create_time}")

# 获取文件的修改时间
modify_time = FileUtils.get_modification_time("test.txt")
print(f"Modification time: {modify_time}")

# 获取文件的访问时间
access_time = FileUtils.get_access_time("test.txt")
print(f"Access time: {access_time}")
```

#### 3. 临时文件和目录

```python
# 创建临时文件
import os
temp_file = FileUtils.create_temp_file(suffix=".txt")
print(f"Temporary file: {temp_file}")

# 写入内容到临时文件
FileUtils.write_file(temp_file, "Temporary content")

# 创建临时目录
temp_dir = FileUtils.create_temp_directory()
print(f"Temporary directory: {temp_dir}")

# 清理临时文件和目录
FileUtils.delete(temp_file)
FileUtils.delete_directory_recursive(temp_dir)
```

## 高级用法

### 文件操作的上下文管理器

```python
# 使用上下文管理器读写文件
with FileUtils.open_file("context_test.txt", "w") as f:
    f.write("Hello from context manager")

with FileUtils.open_file("context_test.txt", "r") as f:
    content = f.read()
    print(f"Content from context manager: {content}")
```

### 文件编码处理

```python
# 指定编码读写文件
unicode_content = "你好，世界！"
FileUtils.write_file("unicode_test.txt", unicode_content, encoding="utf-8")

read_unicode = FileUtils.read_file("unicode_test.txt", encoding="utf-8")
print(f"Unicode content: {read_unicode}")
```

### 文件比较

```python
# 比较两个文件的内容
file1 = "test1.txt"
file2 = "test2.txt"

FileUtils.write_file(file1, "Content")
FileUtils.write_file(file2, "Content")

are_equal = FileUtils.content_equals(file1, file2)
print(f"Files have same content: {are_equal}")  # 输出: True

# 修改其中一个文件
FileUtils.write_file(file2, "Different content")
are_equal = FileUtils.content_equals(file1, file2)
print(f"Files have same content: {are_equal}")  # 输出: False
```

### 文件系统监控

```python
# 监控目录变化（简单实现）
import time

def monitor_directory(path, interval=1):
    """监控目录变化"""
    # 获取初始状态
    initial_state = {}
    for root, dirs, files in FileUtils.walk(path):
        for file in files:
            file_path = FileUtils.join_path(root, file)
            initial_state[file_path] = FileUtils.get_modification_time(file_path)
    
    print(f"Monitoring directory: {path}")
    print(f"Initial files: {len(initial_state)}")
    
    try:
        while True:
            time.sleep(interval)
            current_state = {}
            for root, dirs, files in FileUtils.walk(path):
                for file in files:
                    file_path = FileUtils.join_path(root, file)
                    current_state[file_path] = FileUtils.get_modification_time(file_path)
            
            # 检查新增文件
            new_files = set(current_state.keys()) - set(initial_state.keys())
            if new_files:
                print(f"New files: {new_files}")
            
            # 检查删除的文件
            deleted_files = set(initial_state.keys()) - set(current_state.keys())
            if deleted_files:
                print(f"Deleted files: {deleted_files}")
            
            # 检查修改的文件
            modified_files = []
            for file_path in set(initial_state.keys()) & set(current_state.keys()):
                if initial_state[file_path] != current_state[file_path]:
                    modified_files.append(file_path)
            if modified_files:
                print(f"Modified files: {modified_files}")
            
            # 更新状态
            initial_state = current_state.copy()
    except KeyboardInterrupt:
        print("Monitoring stopped")

# 使用示例（取消注释以运行）
# monitor_directory(".")
```

## 性能提示

- 对于大文件的读写，考虑使用缓冲或分块处理，以减少内存使用
- 对于频繁的文件操作，考虑使用缓存以提高性能
- 对于需要遍历大量文件的场景，使用 `os.scandir()` 或 `FileUtils.walk()` 的生成器方式，以减少内存使用
- 对于需要比较大文件的场景，考虑使用哈希值比较而不是直接比较内容
- 对于临时文件操作，使用 `FileUtils.create_temp_file()` 和 `FileUtils.create_temp_directory()` 以确保文件系统清洁

## 示例：实际应用场景

### 1. 文件备份

```python
def backup_file(file_path, backup_dir="./backup"):
    """备份文件到指定目录"""
    # 确保备份目录存在
    if not FileUtils.exists(backup_dir):
        FileUtils.create_directory(backup_dir)
    
    # 获取文件名和扩展名
    base_name = FileUtils.get_base_name(file_path)
    
    # 添加时间戳到备份文件名
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file_name = f"{FileUtils.get_file_name(base_name)}_{timestamp}{FileUtils.get_extension(base_name)}"
    backup_path = FileUtils.join_path(backup_dir, backup_file_name)
    
    # 复制文件
    FileUtils.copy(file_path, backup_path)
    print(f"File backed up to: {backup_path}")
    
    return backup_path

# 使用示例
# backup_file("important_file.txt")
```

### 2. 批量文件处理

```python
def batch_process_files(directory, pattern="*.txt", processor=None):
    """批量处理目录中的文件"""
    if processor is None:
        # 默认处理器：打印文件内容
        def default_processor(file_path):
            print(f"\nProcessing file: {file_path}")
            content = FileUtils.read_file(file_path)
            print(f"Content: {content[:100]}..." if len(content) > 100 else f"Content: {content}")
        processor = default_processor
    
    # 查找匹配的文件
    files = FileUtils.find_files(directory, pattern)
    print(f"Found {len(files)} files matching pattern '{pattern}'")
    
    # 处理每个文件
    for file_path in files:
        try:
            processor(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

# 使用示例
# batch_process_files(".")

# 自定义处理器
# def custom_processor(file_path):
#     # 例如：统计文件中的单词数
#     content = FileUtils.read_file(file_path)
#     word_count = len(content.split())
#     print(f"{file_path}: {word_count} words")

# batch_process_files(".", "*.txt", custom_processor)
```

### 3. 目录同步

```python
def sync_directories(source_dir, target_dir):
    """同步源目录到目标目录"""
    # 确保目标目录存在
    if not FileUtils.exists(target_dir):
        FileUtils.create_directory(target_dir)
    
    # 遍历源目录
    for root, dirs, files in FileUtils.walk(source_dir):
        # 计算相对路径
        relative_path = FileUtils.get_relative_path(source_dir, root)
        target_root = FileUtils.join_path(target_dir, relative_path)
        
        # 创建目标目录
        if not FileUtils.exists(target_root):
            FileUtils.create_directory(target_root)
        
        # 复制文件
        for file in files:
            source_file = FileUtils.join_path(root, file)
            target_file = FileUtils.join_path(target_root, file)
            
            # 检查文件是否需要更新
            if not FileUtils.exists(target_file) or \
               FileUtils.get_modification_time(source_file) > FileUtils.get_modification_time(target_file):
                print(f"Copying: {source_file} -> {target_file}")
                FileUtils.copy(source_file, target_file)

# 使用示例
# sync_directories("./source", "./target")
```

### 4. 日志文件轮转

```python
def rotate_log_file(log_file, max_size=1024*1024, backup_count=5):
    """轮转日志文件"""
    # 检查文件大小
    if FileUtils.exists(log_file) and FileUtils.get_file_size(log_file) > max_size:
        # 轮转备份文件
        for i in range(backup_count - 1, 0, -1):
            src = f"{log_file}.{i}"
            dst = f"{log_file}.{i + 1}"
            if FileUtils.exists(src):
                if FileUtils.exists(dst):
                    FileUtils.delete(dst)
                FileUtils.rename(src, dst)
        
        # 重命名当前日志文件
        if FileUtils.exists(log_file):
            FileUtils.rename(log_file, f"{log_file}.1")
        
        # 创建新的空日志文件
        FileUtils.write_file(log_file, "")
        print(f"Log file rotated: {log_file}")

# 使用示例
# rotate_log_file("application.log")
```

## 总结

`FileUtils` 提供了全面的文件和目录操作功能，从基本的文件读写、目录创建到高级的文件系统遍历和监控，涵盖了日常开发中大部分文件处理需求。通过合理使用这些功能，可以大大简化文件处理代码，提高开发效率。

无论是备份文件、批量处理文件，还是同步目录和轮转日志文件，`FileUtils` 都能提供简洁、高效的解决方案。