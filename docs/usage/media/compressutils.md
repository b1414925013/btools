# CompressUtils 使用指南

`CompressUtils` 是一个压缩工具类，提供了丰富的压缩操作方法，包括文件压缩、解压等功能。

## 功能特性

- 文件压缩
- 文件解压
- 目录压缩
- 目录解压

## 基本用法

### 导入

```python
from btools import CompressUtils
```

### 示例

#### 文件压缩

```python
# 压缩单个文件
CompressUtils.compress_file("input.txt", "output.zip")
print("File compressed successfully!")

# 压缩多个文件
files = ["file1.txt", "file2.txt", "file3.txt"]
CompressUtils.compress_files(files, "output.zip")
print("Files compressed successfully!")
```

#### 文件解压

```python
# 解压到当前目录
CompressUtils.extract_file("input.zip")
print("File extracted successfully!")

# 解压到指定目录
CompressUtils.extract_file("input.zip", "extract_dir")
print("File extracted to specified directory successfully!")
```

#### 目录压缩

```python
# 压缩目录
CompressUtils.compress_directory("input_dir", "output.zip")
print("Directory compressed successfully!")

# 压缩目录（包含子目录）
CompressUtils.compress_directory("input_dir", "output.zip", recursive=True)
print("Directory compressed recursively successfully!")
```

#### 目录解压

```python
# 解压目录
CompressUtils.extract_directory("input.zip", "extract_dir")
print("Directory extracted successfully!")
```

## 高级用法

### 压缩格式支持

```python
# 使用不同的压缩格式
# ZIP格式
CompressUtils.compress_file("input.txt", "output.zip")

# TAR格式
CompressUtils.compress_file("input.txt", "output.tar")

# TAR.GZ格式
CompressUtils.compress_file("input.txt", "output.tar.gz")

# TAR.BZ2格式
CompressUtils.compress_file("input.txt", "output.tar.bz2")
```

### 压缩级别

```python
# 设置压缩级别（1-9，9为最高压缩率）
CompressUtils.compress_file("input.txt", "output.zip", compression_level=9)
print("File compressed with highest compression level!")
```

### 密码保护

```python
# 压缩文件并设置密码
CompressUtils.compress_file("input.txt", "output.zip", password="mypassword")
print("File compressed with password protection!")

# 解压带密码的文件
CompressUtils.extract_file("input.zip", "extract_dir", password="mypassword")
print("Password-protected file extracted successfully!")
```

## 注意事项

1. 压缩和解压操作可能会占用较多的系统资源，对于大型文件或目录，可能需要较长时间。
2. 密码保护功能仅支持某些压缩格式，如ZIP。
3. 解压操作会覆盖目标目录中已存在的同名文件，请谨慎操作。

## 总结

`CompressUtils` 提供了全面的压缩操作功能，简化了压缩和解压的复杂度，使代码更加简洁易读。无论是基本的文件压缩还是高级的目录压缩，`CompressUtils` 都能满足你的需求。