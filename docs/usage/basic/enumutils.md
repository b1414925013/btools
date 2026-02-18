# EnumUtil - 枚举工具类

## 功能特性

`EnumUtil` 是一个枚举工具类，提供了丰富的枚举相关操作功能，包括：

- 获取枚举列表、名称列表、值列表
- 根据名称或值获取枚举
- 检查枚举类是否包含指定名称或值
- 获取枚举数量
- 枚举对象与字典之间的转换
- 检查对象是否为枚举
- 获取枚举对象所属的枚举类
- 获取枚举对象的序号

## 基本用法

### 导入模块

```python
from btools.core.basic import EnumUtil
import enum
```

### 示例枚举类

```python
class TestEnum(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
```

### 1. 获取枚举列表

```python
# 获取所有枚举值列表
enum_list = EnumUtil.get_enum_list(TestEnum)
print(enum_list)  # 输出: [<TestEnum.FIRST: 1>, <TestEnum.SECOND: 2>, <TestEnum.THIRD: 3>]
```

### 2. 获取枚举名称列表

```python
# 获取所有枚举名称列表
names = EnumUtil.get_enum_names(TestEnum)
print(names)  # 输出: ['FIRST', 'SECOND', 'THIRD']
```

### 3. 获取枚举值列表

```python
# 获取所有枚举值列表
values = EnumUtil.get_enum_values(TestEnum)
print(values)  # 输出: [1, 2, 3]
```

### 4. 获取枚举映射

```python
# 获取名称到值的映射
enum_map = EnumUtil.get_enum_map(TestEnum)
print(enum_map)  # 输出: {'FIRST': 1, 'SECOND': 2, 'THIRD': 3}
```

### 5. 根据名称获取枚举

```python
# 根据名称获取枚举（存在的名称）
enum_obj = EnumUtil.get_enum_by_name(TestEnum, "FIRST")
print(enum_obj)  # 输出: TestEnum.FIRST

# 根据名称获取枚举（不存在的名称，使用默认值）
enum_obj = EnumUtil.get_enum_by_name(TestEnum, "NOT_EXIST", TestEnum.FIRST)
print(enum_obj)  # 输出: TestEnum.FIRST

# 根据名称获取枚举（不存在的名称，不使用默认值）
enum_obj = EnumUtil.get_enum_by_name(TestEnum, "NOT_EXIST")
print(enum_obj)  # 输出: None
```

### 6. 根据值获取枚举

```python
# 根据值获取枚举（存在的值）
enum_obj = EnumUtil.get_enum_by_value(TestEnum, 1)
print(enum_obj)  # 输出: TestEnum.FIRST

# 根据值获取枚举（不存在的值，使用默认值）
enum_obj = EnumUtil.get_enum_by_value(TestEnum, 999, TestEnum.FIRST)
print(enum_obj)  # 输出: TestEnum.FIRST

# 根据值获取枚举（不存在的值，不使用默认值）
enum_obj = EnumUtil.get_enum_by_value(TestEnum, 999)
print(enum_obj)  # 输出: None
```

### 7. 检查是否包含指定名称或值

```python
# 检查是否包含指定名称
contains_name = EnumUtil.contains_name(TestEnum, "FIRST")
print(contains_name)  # 输出: True

contains_name = EnumUtil.contains_name(TestEnum, "NOT_EXIST")
print(contains_name)  # 输出: False

# 检查是否包含指定值
contains_value = EnumUtil.contains_value(TestEnum, 1)
print(contains_value)  # 输出: True

contains_value = EnumUtil.contains_value(TestEnum, 999)
print(contains_value)  # 输出: False
```

### 8. 获取枚举数量

```python
# 获取枚举数量
count = EnumUtil.get_enum_count(TestEnum)
print(count)  # 输出: 3
```

### 9. 枚举与字典转换

```python
# 枚举转字典
enum_dict = EnumUtil.to_dict(TestEnum.FIRST)
print(enum_dict)  # 输出: {'name': 'FIRST', 'value': 1}

# 从字典创建枚举（通过名称）
enum_obj = EnumUtil.from_dict(TestEnum, {"name": "FIRST"})
print(enum_obj)  # 输出: TestEnum.FIRST

# 从字典创建枚举（通过值）
enum_obj = EnumUtil.from_dict(TestEnum, {"value": 1})
print(enum_obj)  # 输出: TestEnum.FIRST
```

### 10. 其他操作

```python
# 检查对象是否为枚举
is_enum = EnumUtil.is_enum(TestEnum.FIRST)
print(is_enum)  # 输出: True

is_enum = EnumUtil.is_enum(TestEnum)
print(is_enum)  # 输出: True

is_enum = EnumUtil.is_enum(1)
print(is_enum)  # 输出: False

# 获取枚举对象所属的枚举类
enum_class = EnumUtil.get_enum_class(TestEnum.FIRST)
print(enum_class)  # 输出: <enum 'TestEnum'>

# 获取枚举对象的序号
ordinal = EnumUtil.get_enum_ordinal(TestEnum.FIRST)
print(ordinal)  # 输出: 0

ordinal = EnumUtil.get_enum_ordinal(TestEnum.SECOND)
print(ordinal)  # 输出: 1
```

## 高级用法

### 1. 枚举遍历

```python
# 使用 get_enum_list 遍历所有枚举
for enum_member in EnumUtil.get_enum_list(TestEnum):
    print(f"名称: {enum_member.name}, 值: {enum_member.value}")

# 输出:
# 名称: FIRST, 值: 1
# 名称: SECOND, 值: 2
# 名称: THIRD, 值: 3
```

### 2. 枚举映射转换

```python
# 将枚举映射转换为值到名称的映射
enum_map = EnumUtil.get_enum_map(TestEnum)
value_to_name_map = {v: k for k, v in enum_map.items()}
print(value_to_name_map)  # 输出: {1: 'FIRST', 2: 'SECOND', 3: 'THIRD'}
```

### 3. 枚举值验证

```python
def validate_enum_value(enum_class, value):
    """验证值是否为有效的枚举值"""
    if not EnumUtil.contains_value(enum_class, value):
        raise ValueError(f"无效的枚举值: {value}")
    return EnumUtil.get_enum_by_value(enum_class, value)

# 测试验证
try:
    enum_obj = validate_enum_value(TestEnum, 1)
    print(f"验证通过: {enum_obj}")
except ValueError as e:
    print(f"验证失败: {e}")

# 输出: 验证通过: TestEnum.FIRST
```

## 注意事项

1. **枚举类型**：`EnumUtil` 仅支持 Python 标准库中的 `enum.Enum` 类型及其子类。

2. **性能考虑**：对于频繁调用的场景，建议缓存 `get_enum_list`、`get_enum_names`、`get_enum_values` 和 `get_enum_map` 的结果，以提高性能。

3. **默认值**：当使用 `get_enum_by_name` 和 `get_enum_by_value` 方法时，如果找不到对应的枚举，可以提供默认值，避免返回 `None` 导致的潜在问题。

4. **序号计算**：`get_enum_ordinal` 方法的序号是基于枚举在枚举类中定义的顺序，从 0 开始计数。如果枚举类的定义顺序发生变化，序号也会相应变化。

## 总结

`EnumUtil` 提供了全面的枚举操作功能，简化了枚举的使用和管理。通过这些工具方法，您可以更方便地处理枚举相关的任务，提高代码的可读性和可维护性。