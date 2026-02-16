# Converter 使用指南

`Converter` 类提供了在不同数据类型之间转换的静态方法。

## 基本使用

### 转换为基本类型

```python
from btools import Converter

# 转换为整数
print(Converter.to_int("123"))       # 123
print(Converter.to_int(123))         # 123
print(Converter.to_int("abc", 0))    # 0（转换失败返回默认值）

# 转换为浮点数
print(Converter.to_float("123.45"))  # 123.45
print(Converter.to_float(123))       # 123.0
print(Converter.to_float("abc", 0.0)) # 0.0（转换失败返回默认值）

# 转换为布尔值
print(Converter.to_bool("true"))      # True
print(Converter.to_bool("1"))         # True
print(Converter.to_bool("false"))     # False
print(Converter.to_bool("0"))         # False
print(Converter.to_bool(None))        # False

# 转换为字符串
print(Converter.to_str(123))          # "123"
print(Converter.to_str(123.45))       # "123.45"
print(Converter.to_str(True))         # "True"
print(Converter.to_str(None))         # ""
```

### 转换为集合

```python
# 转换为列表
print(Converter.to_list("hello"))     # ["hello"]
print(Converter.to_list((1, 2, 3)))   # [1, 2, 3]
print(Converter.to_list({"a": 1}))    # [{"a": 1}]
print(Converter.to_list(None))         # []

# 转换为元组
print(Converter.to_tuple("hello"))     # ("hello",)
print(Converter.to_tuple([1, 2, 3]))   # (1, 2, 3)
print(Converter.to_tuple({"a": 1}))    # ({"a": 1},)
print(Converter.to_tuple(None))         # ()

# 转换为集合
print(Converter.to_set([1, 2, 3, 2]))  # {1, 2, 3}
print(Converter.to_set((1, 2, 3)))    # {1, 2, 3}
print(Converter.to_set(None))          # set()

# 转换为字典
print(Converter.to_dict({"a": 1}))    # {"a": 1}
print(Converter.to_dict([("a", 1), ("b", 2)]))  # {"a": 1, "b": 2}
print(Converter.to_dict(None))         # {}
```

### 转换为 datetime

```python
from datetime import datetime

# 转换为datetime
print(Converter.to_datetime("2023-12-25"))  # datetime对象
print(Converter.to_datetime("2023/12/25", "%Y/%m/%d"))  # datetime对象
print(Converter.to_datetime(None))  # None

# 从datetime转换
now = datetime.now()
print(Converter.datetime_to_str(now))  # "2023-12-25 14:30:00"
print(Converter.datetime_to_str(now, "%Y-%m-%d"))  # "2023-12-25"
print(Converter.datetime_to_str(now, "%H:%M:%S"))  # "14:30:00"
```

### 转换为日期字符串

```python
# 转换日期字符串格式
print(Converter.convert_date_format("2023/12/25", "%Y/%m/%d", "%Y-%m-%d"))  # "2023-12-25"
print(Converter.convert_date_format("25-12-2023", "%d-%m-%Y", "%Y-%m-%d"))  # "2023-12-25"
```

## 高级功能

### 命名规范转换

```python
# 驼峰命名转蛇形命名
print(Converter.camel_to_snake("camelCase"))  # "camel_case"
print(Converter.camel_to_snake("CamelCase"))  # "camel_case"
print(Converter.camel_to_snake("HTTPRequest"))  # "http_request"

# 蛇形命名转驼峰命名
print(Converter.snake_to_camel("snake_case"))  # "snakeCase"
print(Converter.snake_to_camel("snake_case", capitalize_first=True))  # "SnakeCase"
print(Converter.snake_to_camel("http_request"))  # "httpRequest"

# 帕斯卡命名转蛇形命名
print(Converter.pascal_to_snake("PascalCase"))  # "pascal_case"

# 蛇形命名转帕斯卡命名
print(Converter.snake_to_pascal("snake_case"))  # "SnakeCase"
```

### 字符串转换

```python
# 转换为小写
print(Converter.to_lowercase("HELLO WORLD"))  # "hello world"

# 转换为大写
print(Converter.to_uppercase("hello world"))  # "HELLO WORLD"

# 转换为首字母大写
print(Converter.to_titlecase("hello world"))  # "Hello World"

# 转换为驼峰命名
print(Converter.to_camel_case("hello world"))  # "helloWorld"
print(Converter.to_camel_case("hello_world"))  # "helloWorld"

# 转换为蛇形命名
print(Converter.to_snake_case("HelloWorld"))  # "hello_world"
print(Converter.to_snake_case("hello world"))  # "hello_world"
```

### 数字转换

```python
# 转换为百分比
print(Converter.to_percentage(0.123))  # "12.3%"
print(Converter.to_percentage(0.123, 1))  # "12.3%"
print(Converter.to_percentage(0.1234, 2))  # "12.34%"

# 转换为货币格式
print(Converter.to_currency(1234.56))  # "¥1,234.56"
print(Converter.to_currency(1234.56, currency_symbol="$"))  # "$1,234.56"

# 转换为千分位格式
print(Converter.to_thousands(1234567))  # "1,234,567"
print(Converter.to_thousands(1234567.89))  # "1,234,567.89"
```

### 列表和字典转换

```python
# 列表转换为逗号分隔字符串
print(Converter.list_to_csv([1, 2, 3, 4]))  # "1,2,3,4"
print(Converter.list_to_csv(["a", "b", "c"]))  # "a,b,c"

# 逗号分隔字符串转换为列表
print(Converter.csv_to_list("1,2,3,4"))  # ["1", "2", "3", "4"]
print(Converter.csv_to_list("a,b,c"))  # ["a", "b", "c"]
print(Converter.csv_to_list("1,2,3,4", convert_to_int=True))  # [1, 2, 3, 4]

# 字典转换为查询字符串
print(Converter.dict_to_query_string({"a": 1, "b": 2}))  # "a=1&b=2"
print(Converter.dict_to_query_string({"a": "hello world", "b": "test"}))  # "a=hello+world&b=test"

# 查询字符串转换为字典
print(Converter.query_string_to_dict("a=1&b=2"))  # {"a": "1", "b": "2"}
print(Converter.query_string_to_dict("a=hello+world&b=test"))  # {"a": "hello world", "b": "test"}
print(Converter.query_string_to_dict("a=1&b=2", convert_numeric=True))  # {"a": 1, "b": 2}
```

### 进制转换

```python
# 十进制转二进制
print(Converter.decimal_to_binary(10))  # "1010"

# 二进制转十进制
print(Converter.binary_to_decimal("1010"))  # 10

# 十进制转八进制
print(Converter.decimal_to_octal(10))  # "12"

# 八进制转十进制
print(Converter.octal_to_decimal("12"))  # 10

# 十进制转十六进制
print(Converter.decimal_to_hex(10))  # "a"
print(Converter.decimal_to_hex(255))  # "ff"

# 十六进制转十进制
print(Converter.hex_to_decimal("a"))  # 10
print(Converter.hex_to_decimal("ff"))  # 255
```

### 编码转换

```python
# 字符串转Base64
print(Converter.to_base64("hello world"))  # "aGVsbG8gd29ybGQ="

# Base64转字符串
print(Converter.from_base64("aGVsbG8gd29ybGQ="))  # "hello world"

# URL编码
print(Converter.url_encode("hello world"))  # "hello+world"
print(Converter.url_encode("https://example.com"))  # "https%3A%2F%2Fexample.com"

# URL解码
print(Converter.url_decode("hello+world"))  # "hello world"
print(Converter.url_decode("https%3A%2F%2Fexample.com"))  # "https://example.com"
```

## 实用工具方法

### 数据清理

```python
# 清理字符串
print(Converter.clean_string("  hello world  \n"))  # "hello world"
print(Converter.clean_string("  123  \n"))  # "123"

# 清理列表
print(Converter.clean_list(["  hello  ", "", "  world  ", None]))  # ["hello", "world"]

# 清理字典
print(Converter.clean_dict({"a": "  hello  ", "b": "", "c": None}))  # {"a": "hello"}
```

### 数据格式化

```python
# 格式化数字
print(Converter.format_number(1234567, decimal_places=2))  # "1,234,567.00"
print(Converter.format_number(1234.5678, decimal_places=2))  # "1,234.57"

# 格式化文件大小
print(Converter.format_file_size(1024))  # "1.00 KB"
print(Converter.format_file_size(1048576))  # "1.00 MB"
print(Converter.format_file_size(1073741824))  # "1.00 GB"

# 格式化时间间隔
print(Converter.format_duration(3661))  # "1h 1m 1s"
print(Converter.format_duration(61))  # "1m 1s"
print(Converter.format_duration(1))  # "1s"
```

### 类型检查和转换

```python
# 检查并转换类型
def process_data(data):
    # 确保data是列表
    data_list = Converter.to_list(data)
    # 确保每个元素都是字符串
    return [Converter.to_str(item) for item in data_list]

print(process_data("hello"))  # ["hello"]
print(process_data([1, 2, 3]))  # ["1", "2", "3"]
print(process_data(None))  # []

# 安全地获取嵌套字典值
def get_nested_value(data, keys, default=None):
    """安全地获取嵌套字典值"""
    result = data
    for key in Converter.to_list(keys):
        if isinstance(result, dict) and key in result:
            result = result[key]
        else:
            return default
    return result

# 使用示例
data = {"user": {"profile": {"name": "John", "age": 30}}}
print(get_nested_value(data, ["user", "profile", "name"]))  # "John"
print(get_nested_value(data, ["user", "profile", "email"], "default@example.com"))  # "default@example.com"
print(get_nested_value(data, "user.profile.name"))  # "John"
```

## 与其他模块集成

### 与 Config 模块集成

```python
from btools import Config, Converter

# 加载配置
config = Config("config.yaml")

# 获取并转换配置值
# 获取整数配置
port = Converter.to_int(config.get("server.port"), 8080)
print(f"服务器端口: {port}")

# 获取布尔配置
debug = Converter.to_bool(config.get("server.debug"), False)
print(f"调试模式: {debug}")

# 获取列表配置
allowed_hosts = Converter.to_list(config.get("server.allowed_hosts"), ["localhost"])
print(f"允许的主机: {allowed_hosts}")
```

### 与 Validator 模块集成

```python
from btools import Validator, Converter

# 验证并转换数据
def process_input(input_value):
    # 清理输入
    cleaned = Converter.clean_string(input_value)
    
    # 验证并转换为整数
    if Validator.is_integer(cleaned):
        return Converter.to_int(cleaned)
    else:
        return None

print(process_input("  123  "))  # 123
print(process_input("  abc  "))  # None
print(process_input(None))  # None
```

## 常见问题

### 转换失败处理

`Converter` 类的方法通常提供默认值参数，当转换失败时会返回默认值：

```python
# 转换失败时返回默认值
print(Converter.to_int("abc", 0))  # 0
print(Converter.to_float("abc", 0.0))  # 0.0
print(Converter.to_bool("abc", True))  # True
print(Converter.to_list(None, ["default"]))  # ["default"]
```

### 类型推断

`Converter` 类会尝试根据输入类型进行智能转换：

```python
# 智能转换
print(Converter.to_int(123.45))  # 123（从浮点数转换）
print(Converter.to_float(123))  # 123.0（从整数转换）
print(Converter.to_str(True))  # "True"（从布尔值转换）
print(Converter.to_bool(1))  # True（从整数转换）
print(Converter.to_bool(0))  # False（从整数转换）
```

### 空值处理

`Converter` 类对 `None` 值有合理的处理：

```python
# 空值处理
print(Converter.to_str(None))  # ""
print(Converter.to_list(None))  # []
print(Converter.to_dict(None))  # {}
print(Converter.to_bool(None))  # False
print(Converter.to_int(None, 0))  # 0
print(Converter.to_float(None, 0.0))  # 0.0
```

### 性能考虑

对于大量数据的转换，应注意性能影响：

1. 对于简单类型转换，`Converter` 类的方法性能很好
2. 对于复杂类型转换（如深层嵌套结构），可能会有性能开销
3. 对于频繁的转换操作，考虑缓存转换结果

### 自定义转换

对于特殊的转换需求，可以组合使用 `Converter` 的方法或创建自定义转换函数：

```python
# 自定义转换函数
def convert_to_age_group(age):
    """将年龄转换为年龄组"""
    age = Converter.to_int(age, 0)
    if age < 18:
        return "未成年人"
    elif age < 60:
        return "成年人"
    else:
        return "老年人"

print(convert_to_age_group(15))  # "未成年人"
print(convert_to_age_group(30))  # "成年人"
print(convert_to_age_group(65))  # "老年人"
print(convert_to_age_group("abc"))  # "未成年人"（转换失败默认为0）
```