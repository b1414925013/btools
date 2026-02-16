# ArrayUtils 使用指南

`ArrayUtils` 是一个数组处理工具类，提供了丰富的数组操作方法，包括添加、删除、排序、查找等功能。

## 功能特性

- 数组基本操作（添加、删除、获取、设置）
- 数组排序和反转
- 数组复制和连接
- 数组扁平化和去重
- 数组分块和填充
- 数组转换（列表、元组、numpy数组）
- 数组统计（最大值、最小值、求和、平均值、中位数）
- 数组过滤和映射
- 数组遍历和匹配

## 基本用法

### 导入

```python
from btools import ArrayUtils
```

### 示例

#### 数组基本操作

```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 添加元素
ArrayUtils.add(arr, 6)
print(arr)  # 输出: [1, 2, 3, 4, 5, 6]

# 添加多个元素
ArrayUtils.add_all(arr, [7, 8, 9])
print(arr)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 删除元素
ArrayUtils.remove(arr, 3)
print(arr)  # 输出: [1, 2, 4, 5, 6, 7, 8, 9]

# 删除指定位置元素
ArrayUtils.remove_at(arr, 0)
print(arr)  # 输出: [2, 4, 5, 6, 7, 8, 9]

# 获取元素
print(ArrayUtils.get(arr, 2))  # 输出: 5

# 设置元素
ArrayUtils.set(arr, 2, 10)
print(arr)  # 输出: [2, 4, 10, 6, 7, 8, 9]
```

#### 数组排序和反转

```python
# 创建数组
arr = [3, 1, 4, 2, 5]

# 排序
ArrayUtils.sort(arr)
print(arr)  # 输出: [1, 2, 3, 4, 5]

# 反转
ArrayUtils.reverse(arr)
print(arr)  # 输出: [5, 4, 3, 2, 1]
```

#### 数组复制和连接

```python
# 创建数组
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# 复制数组
arr3 = ArrayUtils.copy(arr1)
print(arr3)  # 输出: [1, 2, 3]

# 连接数组
arr4 = ArrayUtils.concat(arr1, arr2)
print(arr4)  # 输出: [1, 2, 3, 4, 5, 6]
```

#### 数组扁平化和去重

```python
# 创建嵌套数组
nested_arr = [[1, 2], [3, 4], [5, 6]]

# 扁平化
flat_arr = ArrayUtils.flatten(nested_arr)
print(flat_arr)  # 输出: [1, 2, 3, 4, 5, 6]

# 创建带重复元素的数组
duplicate_arr = [1, 2, 2, 3, 4, 4, 5]

# 去重
unique_arr = ArrayUtils.distinct(duplicate_arr)
print(unique_arr)  # 输出: [1, 2, 3, 4, 5]
```

#### 数组统计

```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 最大值
print(ArrayUtils.max(arr))  # 输出: 5

# 最小值
print(ArrayUtils.min(arr))  # 输出: 1

# 求和
print(ArrayUtils.sum(arr))  # 输出: 15

# 平均值
print(ArrayUtils.average(arr))  # 输出: 3.0

# 中位数
print(ArrayUtils.median(arr))  # 输出: 3
```

#### 数组过滤和映射

```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 过滤（大于2的元素）
filtered = ArrayUtils.filter(arr, lambda x: x > 2)
print(filtered)  # 输出: [3, 4, 5]

# 映射（每个元素乘以2）
mapped = ArrayUtils.map(arr, lambda x: x * 2)
print(mapped)  # 输出: [2, 4, 6, 8, 10]
```

## 高级用法

### 数组分块

```python
# 创建数组
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 分块（每个块大小为3）
chunks = ArrayUtils.chunk(arr, 3)
print(chunks)  # 输出: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 数组填充

```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 填充（用0替换所有元素）
ArrayUtils.fill(arr, 0)
print(arr)  # 输出: [0, 0, 0, 0, 0]
```

### 数组转换

```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 转换为元组
tuple_arr = ArrayUtils.to_tuple(arr)
print(tuple_arr)  # 输出: (1, 2, 3, 4, 5)

# 转换为numpy数组
import numpy as np
numpy_arr = ArrayUtils.to_numpy(arr)
print(numpy_arr)  # 输出: [1 2 3 4 5]
print(type(numpy_arr))  # 输出: <class 'numpy.ndarray'>
```

### 数组匹配

```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 任意匹配（是否有元素大于3）
any_match = ArrayUtils.any_match(arr, lambda x: x > 3)
print(any_match)  # 输出: True

# 所有匹配（是否所有元素都大于0）
all_match = ArrayUtils.all_match(arr, lambda x: x > 0)
print(all_match)  # 输出: True

# 无匹配（是否没有元素大于10）
none_match = ArrayUtils.none_match(arr, lambda x: x > 10)
print(none_match)  # 输出: True
```

## 注意事项

1. 大多数方法会直接修改原数组，如需保持原数组不变，请使用 `copy()` 方法创建副本。
2. 对于 `to_numpy()` 方法，需要确保已安装 numpy 库。
3. 对于大型数组，某些操作可能会影响性能，请根据实际情况选择合适的方法。

## 总结

`ArrayUtils` 提供了全面的数组操作功能，简化了数组处理的复杂度，使代码更加简洁易读。无论是基本的数组操作还是高级的数组处理，`ArrayUtils` 都能满足你的需求。