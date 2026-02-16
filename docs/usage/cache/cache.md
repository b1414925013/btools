# CacheUtils 使用指南

`CacheUtils` 是一个缓存工具类，提供了丰富的缓存操作方法，包括内存缓存、文件缓存等功能。

## 功能特性

- 内存缓存
- 文件缓存
- 缓存设置
- 缓存获取
- 缓存删除
- 缓存清空
- 缓存过期设置

## 基本用法

### 导入

```python
from btools import CacheUtils
```

### 示例

#### 内存缓存

```python
# 设置内存缓存
CacheUtils.set("key1", "value1")
CacheUtils.set("key2", "value2", expire=3600)  # 设置1小时过期

# 获取内存缓存
print(CacheUtils.get("key1"))  # 输出: value1
print(CacheUtils.get("key2"))  # 输出: value2

# 检查缓存是否存在
print(CacheUtils.exists("key1"))  # 输出: True
print(CacheUtils.exists("nonexistent"))  # 输出: False

# 删除内存缓存
CacheUtils.delete("key1")
print(CacheUtils.get("key1"))  # 输出: None

# 清空所有内存缓存
CacheUtils.clear()
print(CacheUtils.get("key2"))  # 输出: None
```

#### 文件缓存

```python
# 设置文件缓存
CacheUtils.set_file("file_key1", "file_value1")
CacheUtils.set_file("file_key2", "file_value2", expire=3600)  # 设置1小时过期

# 获取文件缓存
print(CacheUtils.get_file("file_key1"))  # 输出: file_value1
print(CacheUtils.get_file("file_key2"))  # 输出: file_value2

# 检查文件缓存是否存在
print(CacheUtils.exists_file("file_key1"))  # 输出: True
print(CacheUtils.exists_file("nonexistent"))  # 输出: False

# 删除文件缓存
CacheUtils.delete_file("file_key1")
print(CacheUtils.get_file("file_key1"))  # 输出: None

# 清空所有文件缓存
CacheUtils.clear_file()
print(CacheUtils.get_file("file_key2"))  # 输出: None
```

## 高级用法

### 缓存配置

```python
# 配置缓存目录
CacheUtils.set_cache_dir("/path/to/cache/dir")

# 获取缓存目录
print(CacheUtils.get_cache_dir())  # 输出: /path/to/cache/dir
```

### 复杂数据缓存

```python
# 缓存复杂数据
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "traveling"]
}

# 设置缓存
CacheUtils.set("user_data", data)

# 获取缓存
user_data = CacheUtils.get("user_data")
print(user_data["name"])  # 输出: John
print(user_data["hobbies"])  # 输出: ['reading', 'coding', 'traveling']

# 文件缓存复杂数据
CacheUtils.set_file("complex_data", data)
complex_data = CacheUtils.get_file("complex_data")
print(complex_data["city"])  # 输出: New York
```

### 批量操作

```python
# 批量设置缓存
items = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
CacheUtils.set_many(items)

# 批量获取缓存
keys = ["key1", "key2", "key3"]
values = CacheUtils.get_many(keys)
print(values)  # 输出: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# 批量删除缓存
CacheUtils.delete_many(keys)
print(CacheUtils.get("key1"))  # 输出: None
print(CacheUtils.get("key2"))  # 输出: None
print(CacheUtils.get("key3"))  # 输出: None
```

## 注意事项

1. 文件缓存会在磁盘上创建文件，因此需要确保有足够的磁盘空间。
2. 缓存过期时间是基于系统时间的，因此系统时间的变化可能会影响缓存的过期行为。
3. 对于大型数据，内存缓存可能会占用较多内存，建议使用文件缓存。

## 总结

`CacheUtils` 提供了全面的缓存操作功能，简化了缓存处理的复杂度，使代码更加简洁易读。无论是基本的内存缓存还是高级的文件缓存，`CacheUtils` 都能满足你的需求。