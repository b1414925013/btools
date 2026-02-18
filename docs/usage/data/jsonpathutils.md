# JSONPathUtils 使用指南

`JSONPathUtils` 类提供了JSONPath表达式的解析、查询、更新和删除功能，基于 jsonpath-ng 库实现。

## 基本使用

### 导入方式

```python
from btools import JSONPathUtils

# 或使用便捷函数
from btools import parse, find, find_first, exists, update, delete, extract, apply
```

## 准备测试数据

让我们先准备一些示例数据，用于后续演示：

```python
data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}
```

## 查询数据

### 查找所有匹配结果

```python
from btools import find

# 查找所有书的作者
authors = find(data, "$.store.book[*].author")
print(f"所有作者: {authors}")
# 输出: ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']

# 查找所有书
books = find(data, "$.store.book")
print(f"所有书: {books}")

# 查找第三本书
third_book = find(data, "$.store.book[2]")
print(f"第三本书: {third_book}")

# 查找最后一本书
last_book = find(data, "$.store.book[-1]")
print(f"最后一本书: {last_book}")

# 查找前两本书
first_two_books = find(data, "$.store.book[0,1]")
print(f"前两本书: {first_two_books}")
```

### 查找第一个匹配结果

```python
from btools import find_first

# 查找第一本书的作者
first_author = find_first(data, "$.store.book[0].author")
print(f"第一本书作者: {first_author}")
# 输出: Nigel Rees

# 查找自行车的颜色
bicycle_color = find_first(data, "$.store.bicycle.color")
print(f"自行车颜色: {bicycle_color}")
# 输出: red
```

### 检查路径是否存在

```python
from btools import exists

# 检查是否有书
has_books = exists(data, "$.store.book")
print(f"有书: {has_books}")  # True

# 检查是否有ISBN字段
has_isbn = exists(data, "$.store.book[0].isbn")
print(f"第一本书有ISBN: {has_isbn}")  # False

# 检查第三本书是否有ISBN
has_isbn_3 = exists(data, "$.store.book[2].isbn")
print(f"第三本书有ISBN: {has_isbn_3}")  # True
```

## 更新数据

### 更新单个值

```python
from btools import update
import copy

# 创建数据副本
data_copy = copy.deepcopy(data)

# 更新第一本书的价格
updated_data = update(data_copy, "$.store.book[0].price", 9.99)
print(f"更新后第一本书价格: {updated_data['store']['book'][0]['price']}")
# 输出: 9.99

# 更新自行车的颜色
updated_data = update(updated_data, "$.store.bicycle.color", "blue")
print(f"更新后自行车颜色: {updated_data['store']['bicycle']['color']}")
# 输出: blue
```

## 删除数据

### 删除字段

```python
from btools import delete
import copy

# 创建数据副本
data_copy = copy.deepcopy(data)

# 删除第一本书的价格
deleted_data = delete(data_copy, "$.store.book[0].price")
print(f"删除后第一本书的键: {list(deleted_data['store']['book'][0].keys())}")

# 删除自行车
deleted_data = delete(deleted_data, "$.store.bicycle")
print(f"删除后store的键: {list(deleted_data['store'].keys())}")
```

## 提取数据

### 批量提取数据

```python
from btools import extract

# 定义提取映射
extract_map = {
    "first_author": "$.store.book[0].author",
    "bicycle_color": "$.store.bicycle.color",
    "expensive_threshold": "$.expensive",
    "all_authors": "$.store.book[*].author"
}

# 提取数据
extracted = extract(data, extract_map)
print(f"提取的数据: {extracted}")
# 输出:
# {
#     'first_author': 'Nigel Rees',
#     'bicycle_color': 'red',
#     'expensive_threshold': 10,
#     'all_authors': ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']
# }
```

## 应用函数

### 对匹配数据应用函数

```python
from btools import apply
import copy

# 创建数据副本
data_copy = copy.deepcopy(data)

# 对价格应用折扣函数（打9折）
def apply_discount(price):
    return round(price * 0.9, 2)

# 应用函数到第一本书
applied_data = apply(data_copy, "$.store.book[0].price", apply_discount)
print(f"折扣后第一本书价格: {applied_data['store']['book'][0]['price']}")
# 输出: 8.05

# 转换价格为字符串
def price_to_string(price):
    return f"${price}"

applied_data = apply(applied_data, "$.store.bicycle.price", price_to_string)
print(f"自行车价格: {applied_data['store']['bicycle']['price']}")
# 输出: $19.95
```

## 解析表达式

### 解析JSONPath表达式

```python
from btools import JSONPathUtils, parse

# 解析表达式
jsonpath = parse("$.store.book[*].author")

# 使用解析后的表达式进行查询
authors = JSONPathUtils.find(data, jsonpath)
print(f"使用解析后的表达式查询: {authors}")

# 使用扩展语法解析
extended_jsonpath = parse("$.store.book[?price > 10]", extended=True)
# 注意：扩展语法需要使用 jsonpath_ng.ext
```

## 实际应用示例

### API响应数据处理

```python
from btools import extract, find_first

# 模拟API响应
api_response = {
    "code": 200,
    "message": "success",
    "data": {
        "user": {
            "id": 123,
            "name": "张三",
            "email": "zhangsan@example.com",
            "profile": {
                "age": 25,
                "address": "北京市朝阳区"
            }
        },
        "orders": [
            {
                "id": "ORD001",
                "amount": 99.9,
                "status": "completed"
            },
            {
                "id": "ORD002",
                "amount": 199.9,
                "status": "pending"
            }
        ]
    }
}

# 提取用户信息
user_map = {
    "user_id": "$.data.user.id",
    "user_name": "$.data.user.name",
    "user_email": "$.data.user.email",
    "user_age": "$.data.user.profile.age",
    "first_order_id": "$.data.orders[0].id"
}

user_info = extract(api_response, user_map)
print(f"用户信息: {user_info}")

# 获取第一个订单状态
first_order_status = find_first(api_response, "$.data.orders[0].status")
print(f"第一个订单状态: {first_order_status}")
```

### 配置文件解析

```python
from btools import find, exists, update

# 模拟配置数据
config = {
    "app": {
        "name": "MyApp",
        "version": "1.0.0",
        "debug": True
    },
    "database": {
        "host": "localhost",
        "port": 3306,
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    },
    "features": [
        {"name": "auth", "enabled": True},
        {"name": "logging", "enabled": True},
        {"name": "cache", "enabled": False}
    ]
}

# 检查是否有数据库配置
has_db = exists(config, "$.database")
print(f"有数据库配置: {has_db}")

# 获取所有功能名称
feature_names = find(config, "$.features[*].name")
print(f"功能名称: {feature_names}")

# 更新数据库密码
updated_config = update(config, "$.database.credentials.password", "new_password")
print(f"更新后的密码: {updated_config['database']['credentials']['password']}")
```

## JSONPath语法参考

### 基本语法

| 语法 | 描述 | 示例 |
|------|------|------|
| `$` | 根对象 | `$` |
| `@` | 当前对象 | 在过滤表达式中使用 |
| `.` 或 `[]` | 子元素 | `$.store.book` 或 `$['store']['book']` |
| `..` | 递归下降 | `$..author` - 查找所有author |
| `*` | 通配符 | `$.store.book[*]` - 所有书 |
| `[,]` | 下标选择 | `$.store.book[0,1]` - 第一和第二本书 |
| `[start:end]` | 切片 | `$.store.book[0:2]` - 前两本书 |
| `[?()]` | 过滤表达式 | `$.store.book[?price > 10]` |

### 常用表达式示例

```python
from btools import find

# 查找所有作者
find(data, "$..author")

# 查找store下的所有东西
find(data, "$.store.*")

# 查找store下所有东西的价格
find(data, "$.store..price")

# 查找所有书
find(data, "$..book")

# 查找第三本书
find(data, "$..book[2]")

# 查找最后一本书
find(data, "$..book[-1:]")

# 查找前两本书
find(data, "$..book[0,1]")

# 使用索引范围查找
find(data, "$..book[:2]")

# 查找有isbn的书
find(data, "$..book[?isbn]")

# 查找价格大于10的书
find(data, "$..book[?price > 10]")

# 查找价格小于expensive的书
find(data, "$..book[?price < $.expensive]")
```

## 常见问题

### Q: 如何处理嵌套数组？

A: 使用 `[*]` 通配符可以遍历数组中的所有元素：

```python
from btools import find

nested_data = {
    "users": [
        {
            "name": "张三",
            "hobbies": ["读书", "游泳"]
        },
        {
            "name": "李四",
            "hobbies": ["跑步", "编程"]
        }
    ]
}

# 获取所有爱好
all_hobbies = find(nested_data, "$.users[*].hobbies[*]")
print(f"所有爱好: {all_hobbies}")
```

### Q: 更新操作是否支持复杂的JSONPath？

A: 当前的update方法主要支持简单的点号路径。对于复杂的JSONPath表达式，建议先查询到目标对象，然后直接操作：

```python
from btools import find_first
import copy

data_copy = copy.deepcopy(data)

# 先找到目标对象
books = find_first(data_copy, "$.store.book")
if books and len(books) > 0:
    books[0]["price"] = 9.99

print(f"更新后价格: {data_copy['store']['book'][0]['price']}")
```
