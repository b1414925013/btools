# DictUtil 使用指南

`DictUtil` 是一个字典工具类，提供了字典相关的便捷操作，类似 Hutool 中的 MapUtil。

## 功能特性

- 字典空值判断
- 类型安全的值获取（int、float、bool、str、list、dict）
- 字典键值操作（添加、删除、更新）
- 字典合并、反转、比较
- 字典过滤、映射、排序
- 嵌套字典操作
- 列表分组、统计
- 深拷贝和浅拷贝

## 基本用法

### 导入 DictUtil

```python
from btools.core.basic.dictutils import DictUtil
```

### 字典空值判断

```python
from btools.core.basic.dictutils import DictUtil

# 判断字典是否为空
print(DictUtil.is_empty(None))  # True
print(DictUtil.is_empty({}))  # True
print(DictUtil.is_empty({'a': 1}))  # False

# 判断字典是否不为空
print(DictUtil.is_not_empty({'a': 1}))  # True

# 获取字典大小
print(DictUtil.size({'a': 1, 'b': 2}))  # 2
```

### 获取值（类型安全）

```python
from btools.core.basic.dictutils import DictUtil

d = {
    'int_val': 42,
    'float_val': 3.14,
    'bool_val': True,
    'str_val': 'hello',
    'list_val': [1, 2, 3],
    'dict_val': {'x': 10}
}

# 获取普通值
print(DictUtil.get(d, 'int_val'))  # 42
print(DictUtil.get(d, 'not_exist', 'default'))  # 'default'

# 获取整数值
print(DictUtil.get_int(d, 'int_val'))  # 42
print(DictUtil.get_int(d, 'not_exist', 0))  # 0

# 获取浮点数值
print(DictUtil.get_float(d, 'float_val'))  # 3.14
print(DictUtil.get_float(d, 'not_exist', 0.0))  # 0.0

# 获取布尔值
print(DictUtil.get_bool(d, 'bool_val'))  # True
print(DictUtil.get_bool(d, 'not_exist', False))  # False

# 获取字符串值
print(DictUtil.get_str(d, 'str_val'))  # 'hello'
print(DictUtil.get_str(d, 'not_exist', ''))  # ''

# 获取列表值
print(DictUtil.get_list(d, 'list_val'))  # [1, 2, 3]

# 获取字典值
print(DictUtil.get_dict(d, 'dict_val'))  # {'x': 10}
```

### 键值操作

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': 1}

# 添加键值对
DictUtil.put(d, 'b', 2)
print(d)  # {'a': 1, 'b': 2}

# 批量添加
DictUtil.put_all(d, {'c': 3, 'd': 4})
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 不存在时添加
DictUtil.put_if_absent(d, 'a', 100)  # 'a'已存在，不更新
DictUtil.put_if_absent(d, 'e', 5)  # 'e'不存在，添加
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 删除键
DictUtil.remove(d, 'e')
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 批量删除
DictUtil.remove_all(d, ['c', 'd'])
print(d)  # {'a': 1, 'b': 2}

# 清空字典
DictUtil.clear(d)
print(d)  # {}
```

### 键值检查

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': 1, 'b': 2}

# 检查键是否存在
print(DictUtil.contains_key(d, 'a'))  # True
print(DictUtil.contains_key(d, 'c'))  # False

# 检查值是否存在
print(DictUtil.contains_value(d, 1))  # True
print(DictUtil.contains_value(d, 3))  # False
```

### 获取键、值、项

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': 1, 'b': 2, 'c': 3}

# 获取所有键
print(DictUtil.keys(d))  # ['a', 'b', 'c']

# 获取所有值
print(DictUtil.values(d))  # [1, 2, 3]

# 获取所有键值对
print(DictUtil.items(d))  # [('a', 1), ('b', 2), ('c', 3)]
```

### 字典反转

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': 1, 'b': 2, 'c': 3}
inverted = DictUtil.invert(d)
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

### 字典合并

```python
from btools.core.basic.dictutils import DictUtil

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# 合并（覆盖重复键）
merged = DictUtil.merge(d1, d2)
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# 合并（不覆盖重复键）
merged_no_overwrite = DictUtil.merge(d1, d2, overwrite=False)
print(merged_no_overwrite)  # {'a': 1, 'b': 2, 'c': 4}
```

## 高级用法

### 字典过滤

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 按键值对过滤
filtered = DictUtil.filter(d, lambda k, v: v > 2)
print(filtered)  # {'c': 3, 'd': 4}

# 按键过滤
filtered_keys = DictUtil.filter_keys(d, lambda k: k in ['a', 'c'])
print(filtered_keys)  # {'a': 1, 'c': 3}

# 按值过滤
filtered_values = DictUtil.filter_values(d, lambda v: v % 2 == 0)
print(filtered_values)  # {'b': 2, 'd': 4}
```

### 字典映射

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': 1, 'b': 2}

# 映射键
mapped_keys = DictUtil.map_keys(d, lambda k: k.upper())
print(mapped_keys)  # {'A': 1, 'B': 2}

# 映射值
mapped_values = DictUtil.map_values(d, lambda v: v * 2)
print(mapped_values)  # {'a': 2, 'b': 4}

# 映射键值对
mapped_items = DictUtil.map_items(d, lambda k, v: (k.upper(), v * 2))
print(mapped_items)  # {'A': 2, 'B': 4}
```

### 字典排序

```python
from btools.core.basic.dictutils import DictUtil

d = {'b': 2, 'a': 1, 'd': 4, 'c': 3}

# 按键排序
sorted_by_key = DictUtil.sort_by_key(d)
print(sorted_by_key)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 按键倒序排序
sorted_by_key_reverse = DictUtil.sort_by_key(d, reverse=True)
print(sorted_by_key_reverse)  # {'d': 4, 'c': 3, 'b': 2, 'a': 1}

# 按值排序
sorted_by_value = DictUtil.sort_by_value(d)
print(sorted_by_value)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### 字典切片和忽略

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 提取指定键
sliced = DictUtil.slice(d, ['a', 'c'])
print(sliced)  # {'a': 1, 'c': 3}

# 忽略指定键
omitted = DictUtil.omit(d, ['a', 'c'])
print(omitted)  # {'b': 2, 'd': 4}
```

### 与列表转换

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': 1, 'b': 2}

# 字典转列表
lst = DictUtil.to_list(d)
print(lst)  # [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]

# 列表转字典
new_dict = DictUtil.from_list(lst)
print(new_dict)  # {'a': 1, 'b': 2}
```

### 拷贝

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': 1, 'b': {'x': 10}}

# 浅拷贝（嵌套对象共享引用）
shallow_copy = DictUtil.shallow_copy(d)
shallow_copy['b']['x'] = 20
print(d['b']['x'])  # 20（原字典也被修改）

# 深拷贝（完全独立）
deep_copy = DictUtil.deep_copy(d)
deep_copy['b']['x'] = 30
print(d['b']['x'])  # 20（原字典不受影响）
```

### 嵌套字典操作

```python
from btools.core.basic.dictutils import DictUtil

d = {'a': {'b': {'c': 1}}}

# 检查嵌套键是否存在
print(DictUtil.has_nested(d, ['a', 'b', 'c']))  # True
print(DictUtil.has_nested(d, ['a', 'x', 'c']))  # False

# 获取嵌套值
nested_value = DictUtil.get_nested(d, ['a', 'b', 'c'])
print(nested_value)  # 1

# 设置嵌套值
new_dict = {}
DictUtil.set_nested(new_dict, ['x', 'y', 'z'], 100)
print(new_dict)  # {'x': {'y': {'z': 100}}}
```

### 列表分组和统计

```python
from btools.core.basic.dictutils import DictUtil

users = [
    {'name': 'Alice', 'age': 20, 'gender': 'female'},
    {'name': 'Bob', 'age': 25, 'gender': 'male'},
    {'name': 'Charlie', 'age': 20, 'gender': 'male'},
    {'name': 'Diana', 'age': 25, 'gender': 'female'},
    {'name': 'Eve', 'age': 30, 'gender': 'female'}
]

# 按年龄分组
grouped_by_age = DictUtil.group_by(users, lambda u: u['age'])
print(grouped_by_age)
# {
#     20: [{'name': 'Alice', ...}, {'name': 'Charlie', ...}],
#     25: [{'name': 'Bob', ...}, {'name': 'Diana', ...}],
#     30: [{'name': 'Eve', ...}]
# }

# 按性别统计
counted_by_gender = DictUtil.count_by(users, lambda u: u['gender'])
print(counted_by_gender)  # {'female': 3, 'male': 2}
```

## 完整示例

```python
from btools.core.basic.dictutils import DictUtil

# 创建字典
data = {
    'user': {
        'name': '张三',
        'age': 30,
        'active': True
    },
    'scores': [85, 90, 78],
    'metadata': {
        'created_at': '2024-01-01',
        'updated_at': '2024-01-02'
    }
}

# 安全获取值
name = DictUtil.get_str(data, 'user', {}).get('name', '')
age = DictUtil.get_int(DictUtil.get_dict(data, 'user'), 'age', 0)
print(f"姓名: {name}, 年龄: {age}")

# 获取嵌套值
created_at = DictUtil.get_nested(data, ['metadata', 'created_at'], '')
print(f"创建时间: {created_at}")

# 过滤和转换
filtered_data = DictUtil.filter(data, lambda k, v: k != 'metadata')
print(f"过滤后: {filtered_data}")

# 分组统计
items = [
    {'category': 'A', 'price': 100},
    {'category': 'A', 'price': 200},
    {'category': 'B', 'price': 150}
]
grouped = DictUtil.group_by(items, lambda x: x['category'])
counted = DictUtil.count_by(items, lambda x: x['category'])
print(f"分组: {grouped}")
print(f"统计: {counted}")
```

## 注意事项

1. **类型转换**：`get_int`、`get_float` 等方法在类型转换失败时会返回默认值，不会抛出异常。

2. **空值处理**：所有方法都对 `None` 进行了安全处理，传入 `None` 作为字典参数时会返回合理的默认值。

3. **深拷贝**：`deep_copy` 使用 `copy.deepcopy`，对于包含自定义对象的字典，需要确保对象支持深拷贝。

4. **排序字典**：Python 3.7+ 的字典保持插入顺序，`sort_by_key` 和 `sort_by_value` 返回的是新的有序字典。

5. **嵌套字典**：使用 `get_nested`、`set_nested`、`has_nested` 操作嵌套字典时，如果中间路径的键不是字典类型，会返回默认值或创建空字典。
