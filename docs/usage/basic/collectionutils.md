# CollectionUtils 使用指南

`CollectionUtils` 是一个集合处理工具类，提供了丰富的字典、列表、集合等集合类型的操作功能，帮助开发者更方便地处理各种集合数据。

## 导入

```python
from btools import CollectionUtils
```

## 核心功能

### 字典操作

#### 1. 字典基本操作

```python
# 创建字典
data = {"name": "John", "age": 30, "city": "New York"}

# 获取字典的键
keys = CollectionUtils.get_keys(data)
print(keys)  # 输出: ["name", "age", "city"]

# 获取字典的值
values = CollectionUtils.get_values(data)
print(values)  # 输出: ["John", 30, "New York"]

# 获取字典的键值对
items = CollectionUtils.get_items(data)
print(items)  # 输出: [("name", "John"), ("age", 30), ("city", "New York")]

# 检查字典是否为空
is_empty = CollectionUtils.is_empty(data)
print(is_empty)  # 输出: False

# 检查字典是否包含指定键
contains_key = CollectionUtils.contains_key(data, "name")
print(contains_key)  # 输出: True

# 检查字典是否包含指定值
contains_value = CollectionUtils.contains_value(data, "John")
print(contains_value)  # 输出: True
```

#### 2. 字典获取操作

```python
# 安全获取字典值（不存在时返回默认值）
data = {"name": "John", "age": 30}

# 获取存在的键
name = CollectionUtils.get(data, "name")
print(name)  # 输出: "John"

# 获取不存在的键，返回默认值
city = CollectionUtils.get(data, "city", "Unknown")
print(city)  # 输出: "Unknown"

# 使用点号分隔的路径获取嵌套字典的值
nested_data = {
    "person": {
        "name": "John",
        "age": 30,
        "address": {
            "city": "New York",
            "zip": "10001"
        }
    }
}

# 获取嵌套值
city = CollectionUtils.get_by_path(nested_data, "person.address.city")
print(city)  # 输出: "New York"

# 获取不存在的嵌套路径，返回默认值
country = CollectionUtils.get_by_path(nested_data, "person.address.country", "USA")
print(country)  # 输出: "USA"
```

#### 3. 字典修改操作

```python
# 合并字典
dict1 = {"name": "John", "age": 30}
dict2 = {"city": "New York", "age": 31}  # 注意：age值会被覆盖

merged = CollectionUtils.merge(dict1, dict2)
print(merged)  # 输出: {"name": "John", "age": 31, "city": "New York"}

# 深度合并字典
nested_dict1 = {
    "person": {
        "name": "John",
        "address": {
            "city": "New York"
        }
    }
}

nested_dict2 = {
    "person": {
        "age": 30,
        "address": {
            "zip": "10001"
        }
    }
}

deep_merged = CollectionUtils.deep_merge(nested_dict1, nested_dict2)
print(deep_merged)
# 输出: {"person": {"name": "John", "age": 30, "address": {"city": "New York", "zip": "10001"}}}

# 从字典中移除指定键
remove_keys = ["age", "city"]
updated = CollectionUtils.remove_keys(data, remove_keys)
print(updated)  # 输出: {"name": "John"}
```

#### 4. 字典转换操作

```python
# 将字典转换为字符串
data = {"name": "John", "age": 30}
dict_str = CollectionUtils.to_string(data)
print(dict_str)  # 输出: "{'name': 'John', 'age': 30}"

# 将字典转换为排序后的字符串（按键排序）
sorted_str = CollectionUtils.to_sorted_string(data)
print(sorted_str)  # 输出: "{'age': 30, 'name': 'John'}"

# 将字典转换为JSON字符串
import json
json_str = CollectionUtils.to_json(data)
print(json_str)  # 输出: '{"name": "John", "age": 30}'

# 将JSON字符串转换为字典
json_str = '{"name": "John", "age": 30}'
dict_from_json = CollectionUtils.from_json(json_str)
print(dict_from_json)  # 输出: {"name": "John", "age": 30}
```

### 列表操作

#### 1. 列表基本操作

```python
# 创建列表
numbers = [1, 2, 3, 4, 5]

# 检查列表是否为空
is_empty = CollectionUtils.is_empty(numbers)
print(is_empty)  # 输出: False

# 获取列表长度
length = CollectionUtils.size(numbers)
print(length)  # 输出: 5

# 获取列表的第一个元素
first = CollectionUtils.first(numbers)
print(first)  # 输出: 1

# 获取列表的最后一个元素
last = CollectionUtils.last(numbers)
print(last)  # 输出: 5

# 检查列表是否包含指定元素
contains = CollectionUtils.contains(numbers, 3)
print(contains)  # 输出: True
```

#### 2. 列表修改操作

```python
# 向列表中添加元素
numbers = [1, 2, 3]
CollectionUtils.add(numbers, 4)
print(numbers)  # 输出: [1, 2, 3, 4]

# 向列表中添加多个元素
CollectionUtils.add_all(numbers, [5, 6, 7])
print(numbers)  # 输出: [1, 2, 3, 4, 5, 6, 7]

# 从列表中移除指定元素
CollectionUtils.remove(numbers, 3)
print(numbers)  # 输出: [1, 2, 4, 5, 6, 7]

# 从列表中移除多个元素
CollectionUtils.remove_all(numbers, [4, 5])
print(numbers)  # 输出: [1, 2, 6, 7]

# 清空列表
CollectionUtils.clear(numbers)
print(numbers)  # 输出: []
```

#### 3. 列表过滤和转换操作

```python
# 过滤列表中的元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = CollectionUtils.filter(numbers, lambda x: x % 2 == 0)
print(even_numbers)  # 输出: [2, 4, 6, 8, 10]

# 转换列表中的元素
squared_numbers = CollectionUtils.map(numbers, lambda x: x ** 2)
print(squared_numbers)  # 输出: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 查找列表中的元素
found = CollectionUtils.find(numbers, lambda x: x > 5)
print(found)  # 输出: 6

# 检查列表中的所有元素是否满足条件
all_even = CollectionUtils.all(numbers, lambda x: x % 2 == 0)
print(all_even)  # 输出: False

# 检查列表中是否有元素满足条件
any_even = CollectionUtils.any(numbers, lambda x: x % 2 == 0)
print(any_even)  # 输出: True
```

#### 4. 列表排序和去重操作

```python
# 排序列表
numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = CollectionUtils.sort(numbers)
print(sorted_numbers)  # 输出: [1, 2, 3, 5, 8, 9]

# 按自定义键排序
students = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]

sorted_students = CollectionUtils.sort_by(students, lambda x: x["age"])
print(sorted_students)
# 输出: [{"name": "Alice", "age": 25}, {"name": "John", "age": 30}, {"name": "Bob", "age": 35}]

# 去重列表
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
distinct_numbers = CollectionUtils.distinct(numbers)
print(distinct_numbers)  # 输出: [1, 2, 3, 4, 5]

# 随机打乱列表
shuffled_numbers = CollectionUtils.shuffle(numbers)
print(shuffled_numbers)  # 输出: 随机顺序的列表
```

### 集合操作

```python
# 创建集合
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 计算集合的交集
intersection = CollectionUtils.intersection(set1, set2)
print(intersection)  # 输出: {4, 5}

# 计算集合的并集
union = CollectionUtils.union(set1, set2)
print(union)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8}

# 计算集合的差集（set1中存在但set2中不存在的元素）
difference = CollectionUtils.difference(set1, set2)
print(difference)  # 输出: {1, 2, 3}

# 计算集合的对称差集（只在其中一个集合中存在的元素）
symmetric_difference = CollectionUtils.symmetric_difference(set1, set2)
print(symmetric_difference)  # 输出: {1, 2, 3, 6, 7, 8}

# 检查集合是否为另一个集合的子集
is_subset = CollectionUtils.is_subset({1, 2, 3}, {1, 2, 3, 4, 5})
print(is_subset)  # 输出: True

# 检查集合是否为另一个集合的超集
is_superset = CollectionUtils.is_superset({1, 2, 3, 4, 5}, {1, 2, 3})
print(is_superset)  # 输出: True
```

### 通用操作

#### 1. 空值处理

```python
# 检查对象是否为空
empty_values = [None, "", [], {}, set()]
for value in empty_values:
    is_empty = CollectionUtils.is_empty(value)
    print(f"{repr(value)} is empty: {is_empty}")
# 输出:
# None is empty: True
# "" is empty: True
# [] is empty: True
# {} is empty: True
# set() is empty: True

# 获取非空值
values = [None, "", "Hello", [], [1, 2, 3]]
non_empty_values = CollectionUtils.get_non_empty(values)
print(non_empty_values)  # 输出: ["Hello", [1, 2, 3]]

# 获取第一个非空值
first_non_empty = CollectionUtils.first_non_empty([None, "", "Hello", "World"])
print(first_non_empty)  # 输出: "Hello"
```

#### 2. 复制操作

```python
# 浅复制字典
data = {"name": "John", "age": 30, "address": {"city": "New York"}}
shallow_copy = CollectionUtils.shallow_copy(data)
print(shallow_copy)  # 输出: {"name": "John", "age": 30, "address": {"city": "New York"}}

# 深复制字典
deep_copy = CollectionUtils.deep_copy(data)
print(deep_copy)  # 输出: {"name": "John", "age": 30, "address": {"city": "New York"}}

# 修改原始字典中的嵌套值，浅复制会受影响，深复制不会
data["address"]["city"] = "London"
print(shallow_copy["address"]["city"])  # 输出: "London"
print(deep_copy["address"]["city"])  # 输出: "New York"
```

#### 3. 计数操作

```python
# 计算元素在列表中出现的次数
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
count = CollectionUtils.count(numbers, 3)
print(count)  # 输出: 3

# 计算满足条件的元素个数
count_even = CollectionUtils.count_if(numbers, lambda x: x % 2 == 0)
print(count_even)  # 输出: 3
```

## 高级用法

### 函数式编程风格

```python
# 使用函数式方法处理数据
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 链式操作
result = CollectionUtils.pipe(
    numbers,
    lambda x: CollectionUtils.filter(x, lambda y: y % 2 == 0),  # 过滤偶数
    lambda x: CollectionUtils.map(x, lambda y: y ** 2),  # 平方
    lambda x: CollectionUtils.sort(x, reverse=True)  # 降序排序
)
print(result)  # 输出: [100, 64, 36, 16, 4]

# 使用reduce操作
from functools import reduce
sum_result = CollectionUtils.reduce(numbers, lambda acc, x: acc + x, 0)
print(sum_result)  # 输出: 55
```

### 数据转换

```python
# 将列表转换为字典
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
dict_from_lists = CollectionUtils.to_dict(keys, values)
print(dict_from_lists)  # 输出: {"name": "John", "age": 30, "city": "New York"}

# 将字典转换为列表（键值对元组）
data = {"name": "John", "age": 30, "city": "New York"}
list_from_dict = CollectionUtils.to_list(data)
print(list_from_dict)  # 输出: [("name", "John"), ("age", 30), ("city", "New York")]

# 将字典转换为列表（仅值）
values_list = CollectionUtils.to_value_list(data)
print(values_list)  # 输出: ["John", 30, "New York"]
```

## 性能提示

- 对于大集合的操作，考虑使用生成器表达式而不是列表推导式，以减少内存使用
- 对于频繁的字典查找，考虑使用 `defaultdict` 或 `get()` 方法以提高性能
- 对于需要频繁修改的列表，考虑使用 `deque` 以提高插入和删除操作的性能
- 对于需要去重的大列表，考虑使用 `set` 转换以获得 O(n) 的时间复杂度

## 示例：实际应用场景

### 1. 处理API响应数据

```python
def process_api_response(response):
    """处理API响应数据"""
    # 安全获取响应数据
    data = CollectionUtils.get(response, "data", {})
    
    # 获取用户信息
    user = CollectionUtils.get(data, "user", {})
    
    # 提取需要的字段
    user_info = {
        "id": CollectionUtils.get(user, "id"),
        "name": CollectionUtils.get(user, "name", "Unknown"),
        "email": CollectionUtils.get(user, "email", "Unknown"),
        "age": CollectionUtils.get(user, "age", 0),
        "city": CollectionUtils.get_by_path(user, "address.city", "Unknown")
    }
    
    # 获取分页信息
    pagination = CollectionUtils.get(data, "pagination", {})
    page_info = {
        "current_page": CollectionUtils.get(pagination, "current_page", 1),
        "total_pages": CollectionUtils.get(pagination, "total_pages", 1),
        "total_items": CollectionUtils.get(pagination, "total_items", 0)
    }
    
    return {
        "user": user_info,
        "pagination": page_info
    }

# 使用示例
api_response = {
    "data": {
        "user": {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com",
            "address": {
                "city": "New York"
            }
        },
        "pagination": {
            "current_page": 1,
            "total_pages": 5,
            "total_items": 100
        }
    }
}

processed_data = process_api_response(api_response)
print(processed_data)
```

### 2. 数据验证和清理

```python
def validate_and_clean_data(data):
    """验证和清理数据"""
    # 移除空值
    cleaned_data = {}
    for key, value in CollectionUtils.get_items(data):
        if not CollectionUtils.is_empty(value):
            cleaned_data[key] = value
    
    # 验证必填字段
    required_fields = ["name", "email", "password"]
    missing_fields = []
    
    for field in required_fields:
        if not CollectionUtils.contains_key(cleaned_data, field):
            missing_fields.append(field)
    
    if missing_fields:
        return {
            "valid": False,
            "message": f"Missing required fields: {', '.join(missing_fields)}",
            "data": cleaned_data
        }
    
    return {
        "valid": True,
        "message": "Data is valid",
        "data": cleaned_data
    }

# 使用示例
user_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "secure123",
    "age": "",  # 空值
    "city": None  # 空值
}

validation_result = validate_and_clean_data(user_data)
print(validation_result)
```

### 3. 数据聚合和统计

```python
def aggregate_user_data(users):
    """聚合用户数据"""
    # 按年龄分组
    users_by_age = {}
    for user in users:
        age = CollectionUtils.get(user, "age", 0)
        if age not in users_by_age:
            users_by_age[age] = []
        users_by_age[age].append(user)
    
    # 计算每个年龄段的用户数量
    age_statistics = {}
    for age, age_users in CollectionUtils.get_items(users_by_age):
        age_statistics[age] = {
            "count": len(age_users),
            "names": CollectionUtils.map(age_users, lambda x: CollectionUtils.get(x, "name"))
        }
    
    # 计算平均年龄
    ages = CollectionUtils.map(users, lambda x: CollectionUtils.get(x, "age", 0))
    average_age = sum(ages) / len(ages) if ages else 0
    
    return {
        "total_users": len(users),
        "average_age": average_age,
        "age_statistics": age_statistics
    }

# 使用示例
users = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 25}
]

aggregated_data = aggregate_user_data(users)
print(aggregated_data)
```

## 总结

`CollectionUtils` 提供了全面的集合处理功能，从基本的字典、列表操作到高级的集合运算和函数式编程风格，涵盖了日常开发中大部分集合处理需求。通过合理使用这些功能，可以大大简化集合处理代码，提高开发效率。

无论是处理API响应数据、验证用户输入，还是进行数据聚合和统计，`CollectionUtils` 都能提供简洁、高效的解决方案。