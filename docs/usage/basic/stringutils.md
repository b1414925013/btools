# StringUtils 使用指南

`StringUtils` 是一个字符串处理工具类，提供了丰富的字符串操作、格式化、验证等功能，帮助开发者更方便地处理字符串。

## 导入

```python
from btools import StringUtils
```

## 核心功能

### 字符串操作

#### 1. 字符串修剪

```python
# 修剪字符串两端的空白字符
text = "  Hello World  "
trimmed = StringUtils.trim(text)
print(trimmed)  # 输出: "Hello World"

# 修剪字符串左侧的空白字符
left_trimmed = StringUtils.ltrim(text)
print(left_trimmed)  # 输出: "Hello World  "

# 修剪字符串右侧的空白字符
right_trimmed = StringUtils.rtrim(text)
print(right_trimmed)  # 输出: "  Hello World"
```

#### 2. 字符串大小写转换

```python
text = "Hello World"

# 转换为全大写
uppercase = StringUtils.upper(text)
print(uppercase)  # 输出: "HELLO WORLD"

# 转换为全小写
lowercase = StringUtils.lower(text)
print(lowercase)  # 输出: "hello world"

# 转换为首字母大写
capitalized = StringUtils.capitalize(text)
print(capitalized)  # 输出: "Hello world"

# 转换为每个单词首字母大写
titled = StringUtils.title(text)
print(titled)  # 输出: "Hello World"
```

#### 3. 字符串替换

```python
text = "Hello World"

# 替换指定子字符串
replaced = StringUtils.replace(text, "World", "Python")
print(replaced)  # 输出: "Hello Python"

# 替换所有匹配的子字符串
text = "Hello Hello Hello"
replaced_all = StringUtils.replace_all(text, "Hello", "Hi")
print(replaced_all)  # 输出: "Hi Hi Hi"
```

#### 4. 字符串分割和连接

```python
# 分割字符串
text = "Hello,World,Python"
parts = StringUtils.split(text, ",")
print(parts)  # 输出: ["Hello", "World", "Python"]

# 连接字符串列表
words = ["Hello", "World", "Python"]
joined = StringUtils.join(words, " ")
print(joined)  # 输出: "Hello World Python"
```

#### 5. 字符串填充

```python
# 左侧填充
text = "123"
padded_left = StringUtils.pad_left(text, 5, "0")
print(padded_left)  # 输出: "00123"

# 右侧填充
padded_right = StringUtils.pad_right(text, 5, "0")
print(padded_right)  # 输出: "12300"

# 两侧填充
padded_both = StringUtils.pad_both(text, 7, "-")
print(padded_both)  # 输出: "--123--"
```

### 字符串验证

```python
# 检查字符串是否为空
empty_text = ""
is_empty = StringUtils.is_empty(empty_text)
print(is_empty)  # 输出: True

# 检查字符串是否为空白
blank_text = "   "
is_blank = StringUtils.is_blank(blank_text)
print(is_blank)  # 输出: True

# 检查字符串是否包含指定子字符串
text = "Hello World"
contains = StringUtils.contains(text, "World")
print(contains)  # 输出: True

# 检查字符串是否以指定前缀开头
starts_with = StringUtils.starts_with(text, "Hello")
print(starts_with)  # 输出: True

# 检查字符串是否以指定后缀结尾
ends_with = StringUtils.ends_with(text, "World")
print(ends_with)  # 输出: True
```

### 字符串格式化

```python
# 格式化字符串
name = "John"
age = 30
formatted = StringUtils.format("Name: {}, Age: {}", name, age)
print(formatted)  # 输出: "Name: John, Age: 30"

# 使用命名参数格式化
user = {"name": "John", "age": 30}
formatted_named = StringUtils.format_map("Name: {name}, Age: {age}", user)
print(formatted_named)  # 输出: "Name: John, Age: 30"
```

### 字符串生成

```python
# 生成指定长度的随机字符串
random_str = StringUtils.random_string(10)
print(random_str)  # 输出: 例如 "aB3cDeFgHi"

# 生成指定长度的随机数字字符串
random_digits = StringUtils.random_digits(6)
print(random_digits)  # 输出: 例如 "123456"

# 生成指定长度的随机字母字符串
random_letters = StringUtils.random_letters(8)
print(random_letters)  # 输出: 例如 "AbCdEfGh"
```

### 字符串加密和哈希

```python
# 计算字符串的MD5哈希值
text = "Hello World"
md5_hash = StringUtils.md5(text)
print(md5_hash)  # 输出: "5eb63bbbe01eeed093cb22bb8f5acdc3"

# 计算字符串的SHA-1哈希值
sha1_hash = StringUtils.sha1(text)
print(sha1_hash)  # 输出: "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"

# 计算字符串的SHA-256哈希值
sha256_hash = StringUtils.sha256(text)
print(sha256_hash)  # 输出: "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
```

## 高级用法

### 字符串处理工具链

```python
# 组合多个字符串操作
text = "   hello world   "
result = StringUtils.trim(text).upper().replace("WORLD", "PYTHON")
print(result)  # 输出: "HELLO PYTHON"

# 或者使用函数式方法
result = StringUtils.pipe(
    text,
    StringUtils.trim,
    StringUtils.upper,
    lambda s: StringUtils.replace(s, "WORLD", "PYTHON")
)
print(result)  # 输出: "HELLO PYTHON"
```

### 字符串模板

```python
# 使用字符串模板
from string import Template

template = Template("Hello, $name! You are $age years old.")
result = StringUtils.template(template, name="John", age=30)
print(result)  # 输出: "Hello, John! You are 30 years old."

# 或者直接使用字符串作为模板
result = StringUtils.template_string(
    "Hello, $name! You are $age years old.",
    name="John",
    age=30
)
print(result)  # 输出: "Hello, John! You are 30 years old."
```

## 性能提示

- 对于频繁的字符串操作，建议使用 `join()` 而不是 `+` 来连接字符串，因为 `join()` 更高效
- 对于大字符串的替换操作，考虑使用正则表达式以获得更好的性能
- 对于需要重复使用的字符串模板，建议预编译模板以提高性能

## 示例：实际应用场景

### 1. 处理用户输入

```python
def process_user_input(input_str):
    """处理用户输入"""
    # 修剪空白字符
    input_str = StringUtils.trim(input_str)
    
    # 检查是否为空
    if StringUtils.is_empty(input_str):
        return "输入不能为空"
    
    # 转换为小写
    input_str = StringUtils.lower(input_str)
    
    return input_str

# 使用示例
user_input = "  Hello World  "
processed = process_user_input(user_input)
print(processed)  # 输出: "hello world"
```

### 2. 生成唯一标识符

```python
def generate_unique_id(prefix="id"):
    """生成唯一标识符"""
    timestamp = StringUtils.format("{:.0f}", StringUtils.current_timestamp())
    random_str = StringUtils.random_string(8)
    return f"{prefix}_{timestamp}_{random_str}"

# 使用示例
unique_id = generate_unique_id()
print(unique_id)  # 输出: 例如 "id_1620000000_aB3cDeFg"
```

### 3. 格式化数据输出

```python
def format_user_info(user):
    """格式化用户信息"""
    template = """用户信息:
姓名: {name}
年龄: {age}
邮箱: {email}
地址: {address}"""
    
    return StringUtils.format_map(template, user)

# 使用示例
user = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "address": "123 Main St, New York"
}

formatted_info = format_user_info(user)
print(formatted_info)
# 输出:
# 用户信息:
# 姓名: John Doe
# 年龄: 30
# 邮箱: john@example.com
# 地址: 123 Main St, New York
```

## 总结

`StringUtils` 提供了全面的字符串处理功能，从基本的修剪、大小写转换到高级的字符串模板和哈希计算，涵盖了日常开发中大部分字符串处理需求。通过合理使用这些功能，可以大大简化字符串处理代码，提高开发效率。