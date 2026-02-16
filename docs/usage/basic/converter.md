# Converter 使用指南

`Converter` 是一个数据转换工具类，提供了丰富的数据类型转换功能，帮助开发者更方便地在不同数据类型之间进行转换，同时处理转换过程中的异常情况。

## 导入

```python
from btools import Converter
# 或
from btools.core import Converter
```

## 核心功能

### 基本数据类型转换

#### 1. 转换为整数

```python
# 转换为整数
value = "123"
result = Converter.to_int(value)
print(f"Converted to int: {result}")  # 输出: 123

# 转换失败时返回默认值
value = "abc"
result = Converter.to_int(value, default=0)
print(f"Converted to int (with default): {result}")  # 输出: 0

# 处理浮点数
value = 123.99
result = Converter.to_int(value)
print(f"Converted float to int: {result}")  # 输出: 123
```

#### 2. 转换为浮点数

```python
# 转换为浮点数
value = "123.45"
result = Converter.to_float(value)
print(f"Converted to float: {result}")  # 输出: 123.45

# 转换失败时返回默认值
value = "abc"
result = Converter.to_float(value, default=0.0)
print(f"Converted to float (with default): {result}")  # 输出: 0.0

# 处理整数
value = 123
result = Converter.to_float(value)
print(f"Converted int to float: {result}")  # 输出: 123.0
```

#### 3. 转换为布尔值

```python
# 转换为布尔值
value = "true"
result = Converter.to_bool(value)
print(f"Converted to bool: {result}")  # 输出: True

# 处理不同形式的真值
values = ["yes", "y", "1", "t", "True", True, 1, 1.0]
for v in values:
    result = Converter.to_bool(v)
    print(f"{repr(v)} -> {result}")  # 所有值都输出: True

# 处理不同形式的假值
values = ["false", "no", "n", "0", "f", "False", False, 0, 0.0, None]
for v in values:
    result = Converter.to_bool(v)
    print(f"{repr(v)} -> {result}")  # 所有值都输出: False

# 转换失败时返回默认值
value = "abc"
result = Converter.to_bool(value, default=True)
print(f"Converted to bool (with default): {result}")  # 输出: True
```

#### 4. 转换为字符串

```python
# 转换为字符串
value = 123
result = Converter.to_str(value)
print(f"Converted to str: '{result}'")  # 输出: '123'

# 处理None值
value = None
result = Converter.to_str(value, default="")
print(f"Converted None to str: '{result}'")  # 输出: ''

# 处理复杂对象
value = {"name": "John", "age": 30}
result = Converter.to_str(value)
print(f"Converted dict to str: {result}")  # 输出: "{'name': 'John', 'age': 30}"
```

### 集合类型转换

#### 1. 转换为列表

```python
# 转换为列表
value = "hello"
result = Converter.to_list(value)
print(f"Converted str to list: {result}")  # 输出: ['hello']

# 处理元组
value = (1, 2, 3)
result = Converter.to_list(value)
print(f"Converted tuple to list: {result}")  # 输出: [1, 2, 3]

# 处理集合
value = {1, 2, 3}
result = Converter.to_list(value)
print(f"Converted set to list: {result}")  # 输出: [1, 2, 3]

# 处理None值
value = None
result = Converter.to_list(value, default=[1, 2, 3])
print(f"Converted None to list: {result}")  # 输出: [1, 2, 3]

# 处理已经是列表的值
value = [1, 2, 3]
result = Converter.to_list(value)
print(f"Converted list to list: {result}")  # 输出: [1, 2, 3]
```

#### 2. 转换为字典

```python
# 转换为字典
value = "{\"name\": \"John\", \"age\": 30}"
result = Converter.to_dict(value)
print(f"Converted str to dict: {result}")  # 输出: {'name': 'John', 'age': 30}

# 处理None值
value = None
result = Converter.to_dict(value, default={"name": "Default"})
print(f"Converted None to dict: {result}")  # 输出: {'name': 'Default'}

# 处理已经是字典的值
value = {"name": "John", "age": 30}
result = Converter.to_dict(value)
print(f"Converted dict to dict: {result}")  # 输出: {'name': 'John', 'age': 30}
```

### 日期时间转换

#### 1. 转换为datetime对象

```python
# 转换为datetime对象
value = "2023-01-01"
result = Converter.to_datetime(value)
print(f"Converted str to datetime: {result}")  # 输出: 2023-01-01 00:00:00

# 指定日期格式
value = "01/01/2023"
result = Converter.to_datetime(value, format="%m/%d/%Y")
print(f"Converted str to datetime (with format): {result}")  # 输出: 2023-01-01 00:00:00

# 处理时间戳
value = 1672531200  # 2023-01-01 00:00:00 UTC
result = Converter.to_datetime(value)
print(f"Converted timestamp to datetime: {result}")  # 输出: 2023-01-01 00:00:00

# 转换失败时返回默认值
value = "abc"
result = Converter.to_datetime(value, default=None)
print(f"Converted invalid str to datetime: {result}")  # 输出: None

# 处理已经是datetime对象的值
from datetime import datetime
value = datetime.now()
result = Converter.to_datetime(value)
print(f"Converted datetime to datetime: {result}")  # 输出: 当前时间
```

#### 2. 日期时间转换为字符串

```python
# 将datetime对象转换为字符串
from datetime import datetime
value = datetime.now()
result = Converter.datetime_to_str(value)
print(f"Converted datetime to str: {result}")  # 输出: 例如 "2023-01-01 12:00:00"

# 指定日期格式
result = Converter.datetime_to_str(value, format="%Y/%m/%d %H:%M:%S")
print(f"Converted datetime to str (with format): {result}")  # 输出: 例如 "2023/01/01 12:00:00"

# 处理None值
value = None
result = Converter.datetime_to_str(value)
print(f"Converted None to str: '{result}'")  # 输出: ''
```

### 命名风格转换

#### 1. 驼峰命名转换为蛇形命名

```python
# 将驼峰命名转换为蛇形命名
value = "camelCase"
result = Converter.camel_to_snake(value)
print(f"Converted camelCase to snake_case: {result}")  # 输出: "camel_case"

# 处理 PascalCase
value = "PascalCase"
result = Converter.camel_to_snake(value)
print(f"Converted PascalCase to snake_case: {result}")  # 输出: "pascal_case"

# 处理连续大写字母
value = "HTTPRequest"
result = Converter.camel_to_snake(value)
print(f"Converted HTTPRequest to snake_case: {result}")  # 输出: "http_request"
```

#### 2. 蛇形命名转换为驼峰命名

```python
# 将蛇形命名转换为驼峰命名
value = "snake_case"
result = Converter.snake_to_camel(value)
print(f"Converted snake_case to camelCase: {result}")  # 输出: "snakeCase"

# 转换为 PascalCase
value = "snake_case"
result = Converter.snake_to_camel(value, capitalize_first=True)
print(f"Converted snake_case to PascalCase: {result}")  # 输出: "SnakeCase"

# 处理多个下划线
value = "long_snake_case_name"
result = Converter.snake_to_camel(value)
print(f"Converted long_snake_case_name to camelCase: {result}")  # 输出: "longSnakeCaseName"
```

## 高级用法

### 链式转换

```python
# 链式转换
data = "123"
result = Converter.to_int(data)  # 转换为整数
result = Converter.to_str(result)  # 转换回字符串
result = Converter.to_list(result)  # 转换为列表
print(f"Chained conversion result: {result}")  # 输出: ["123"]

# 更复杂的链式转换
user_input = "1,2,3,4,5"
numbers = Converter.to_list(user_input, default=[])
numbers = [Converter.to_int(num) for num in numbers]
sum_numbers = sum(numbers)
print(f"Sum of numbers: {sum_numbers}")  # 输出: 15
```

### 批量转换

```python
# 批量转换列表中的元素
data = ["1", "2", "3", "4", "5"]
numbers = [Converter.to_int(item) for item in data]
print(f"Batch converted to int: {numbers}")  # 输出: [1, 2, 3, 4, 5]

# 批量转换字典中的值
data = {
    "age": "30",
    "score": "95.5",
    "is_active": "true",
    "registered_at": "2023-01-01"
}

converted_data = {
    "age": Converter.to_int(data["age"]),
    "score": Converter.to_float(data["score"]),
    "is_active": Converter.to_bool(data["is_active"]),
    "registered_at": Converter.to_datetime(data["registered_at"])
}

print(f"Batch converted dict: {converted_data}")
# 输出: {"age": 30, "score": 95.5, "is_active": True, "registered_at": datetime.datetime(2023, 1, 1, 0, 0)}
```

### 自定义转换函数

```python
# 自定义转换函数
def custom_converter(value, default=None):
    """自定义转换函数：将字符串转换为标题格式"""
    try:
        if value is None:
            return default
        return Converter.to_str(value).title()
    except:
        return default

# 使用自定义转换函数
values = ["john doe", "jane smith", None, 123]
converted_values = [custom_converter(v, default="Unknown") for v in values]
print(f"Custom converted values: {converted_values}")  # 输出: ["John Doe", "Jane Smith", "Unknown", "123"]
```

### 类型安全转换

```python
# 类型安全转换
def get_user_age(user_data):
    """获取用户年龄，确保返回整数"""
    return Converter.to_int(user_data.get("age"), default=0)

# 使用示例
user1 = {"name": "John", "age": "30"}
user2 = {"name": "Jane"}  # 缺少age字段
user3 = {"name": "Bob", "age": "abc"}  # 无效的age值

age1 = get_user_age(user1)
age2 = get_user_age(user2)
age3 = get_user_age(user3)

print(f"User 1 age: {age1} (type: {type(age1).__name__})")  # 输出: "User 1 age: 30 (type: int)"
print(f"User 2 age: {age2} (type: {type(age2).__name__})")  # 输出: "User 2 age: 0 (type: int)"
print(f"User 3 age: {age3} (type: {type(age3).__name__})")  # 输出: "User 3 age: 0 (type: int)"
```

## 性能提示

- 对于频繁的转换操作，考虑缓存转换结果，以减少重复转换的开销
- 对于大型数据集的转换，考虑使用生成器表达式或列表推导式，以提高性能
- 对于复杂的转换逻辑，考虑将其封装为自定义转换函数，以提高代码可读性和可维护性
- 对于可能为None的值，始终提供默认值，以避免后续代码中的NoneType错误

## 示例：实际应用场景

### 1. 处理用户输入数据

```python
def process_user_input(input_data):
    """处理用户输入数据"""
    processed = {
        "name": Converter.to_str(input_data.get("name"), default=""),
        "age": Converter.to_int(input_data.get("age"), default=0),
        "email": Converter.to_str(input_data.get("email"), default=""),
        "is_subscribed": Converter.to_bool(input_data.get("is_subscribed"), default=False),
        "interests": Converter.to_list(input_data.get("interests"), default=[]),
        "registered_at": Converter.to_datetime(input_data.get("registered_at"))
    }
    
    return processed

# 使用示例
user_input = {
    "name": "John Doe",
    "age": "30",
    "email": "john@example.com",
    "is_subscribed": "true",
    "interests": "programming,reading,travel"
}

processed_data = process_user_input(user_input)
print(processed_data)
# 输出:
# {
#     "name": "John Doe",
#     "age": 30,
#     "email": "john@example.com",
#     "is_subscribed": True,
#     "interests": ["programming,reading,travel"],
#     "registered_at": None
# }
```

### 2. 处理API响应数据

```python
def process_api_response(response):
    """处理API响应数据"""
    if not response or not isinstance(response, dict):
        return {"success": False, "data": None, "error": "Invalid response"}
    
    return {
        "success": Converter.to_bool(response.get("success"), default=False),
        "data": response.get("data"),
        "error": Converter.to_str(response.get("error"), default=""),
        "total": Converter.to_int(response.get("total"), default=0),
        "page": Converter.to_int(response.get("page"), default=1),
        "page_size": Converter.to_int(response.get("page_size"), default=10)
    }

# 使用示例
api_response = {
    "success": "true",
    "data": {"id": 1, "name": "John"},
    "total": "100",
    "page": "1",
    "page_size": "20"
}

processed_response = process_api_response(api_response)
print(processed_response)
# 输出:
# {
#     "success": True,
#     "data": {"id": 1, "name": "John"},
#     "error": "",
#     "total": 100,
#     "page": 1,
#     "page_size": 20
# }
```

### 3. 配置数据转换

```python
def load_config(config_data):
    """加载配置数据"""
    config = {
        "server": {
            "host": Converter.to_str(config_data.get("server.host"), default="localhost"),
            "port": Converter.to_int(config_data.get("server.port"), default=8080),
            "debug": Converter.to_bool(config_data.get("server.debug"), default=False)
        },
        "database": {
            "url": Converter.to_str(config_data.get("database.url"), default=""),
            "timeout": Converter.to_int(config_data.get("database.timeout"), default=30),
            "retries": Converter.to_int(config_data.get("database.retries"), default=3)
        },
        "logging": {
            "level": Converter.to_str(config_data.get("logging.level"), default="INFO"),
            "file": Converter.to_str(config_data.get("logging.file"), default="")
        }
    }
    
    return config

# 使用示例
config_data = {
    "server.host": "example.com",
    "server.port": "9090",
    "server.debug": "false",
    "database.url": "mysql://localhost:3306/db",
    "database.timeout": "60",
    "logging.level": "DEBUG"
}

config = load_config(config_data)
print(config)
# 输出:
# {
#     "server": {
#         "host": "example.com",
#         "port": 9090,
#         "debug": False
#     },
#     "database": {
#         "url": "mysql://localhost:3306/db",
#         "timeout": 60,
#         "retries": 3
#     },
#     "logging": {
#         "level": "DEBUG",
#         "file": ""
#     }
# }
```

### 4. 数据导出准备

```python
def prepare_data_for_export(data):
    """准备数据用于导出"""
    export_data = []
    
    for item in data:
        export_item = {
            "id": Converter.to_str(item.get("id"), default=""),
            "name": Converter.to_str(item.get("name"), default=""),
            "value": Converter.to_str(item.get("value"), default="0"),
            "is_active": "Yes" if Converter.to_bool(item.get("is_active")) else "No",
            "created_at": Converter.datetime_to_str(item.get("created_at"), format="%Y-%m-%d")
        }
        export_data.append(export_item)
    
    return export_data

# 使用示例
from datetime import datetime
data = [
    {"id": 1, "name": "Item 1", "value": 100, "is_active": True, "created_at": datetime.now()},
    {"id": 2, "name": "Item 2", "value": "200", "is_active": "false", "created_at": datetime.now()}
]

export_data = prepare_data_for_export(data)
print(export_data)
# 输出:
# [
#     {
#         "id": "1",
#         "name": "Item 1",
#         "value": "100",
#         "is_active": "Yes",
#         "created_at": "2023-01-01"
#     },
#     {
#         "id": "2",
#         "name": "Item 2",
#         "value": "200",
#         "is_active": "No",
#         "created_at": "2023-01-01"
#     }
# ]
```

## 总结

`Converter` 提供了全面的数据类型转换功能，从基本的整数、浮点数、布尔值转换到复杂的日期时间、集合类型转换，涵盖了日常开发中大部分数据转换需求。通过合理使用这些功能，可以大大简化数据转换代码，提高代码的可读性和可维护性。

无论是处理用户输入、API响应数据，还是配置数据和导出数据，`Converter` 都能提供简洁、高效的解决方案，同时处理转换过程中的异常情况，确保代码的健壮性。