# ArrayUtils 使用指南

`ArrayUtils` 是一个数组处理工具类，提供了丰富的数组操作方法，包括添加、删除、排序、查找等功能。

## 导入

```python
from btools import ArrayUtils
```

## 方法详解

### 1. is_empty

**功能**：判断数组是否为空。

**方法签名**：
```python
@staticmethod
def is_empty(array: Any) -> bool
```

**参数**：
- `array` (Any): 要判断的数组

**返回值**：
- `bool`: 如果为空则返回 True，否则返回 False

**使用场景**：
- 验证数组是否为空
- 作为条件判断
- 防止空数组操作

**使用示例**：
```python
# 检查空数组
print(ArrayUtils.is_empty([]))  # 输出: True

# 检查非空数组
print(ArrayUtils.is_empty([1, 2, 3]))  # 输出: False

# 检查 None
print(ArrayUtils.is_empty(None))  # 输出: True
```

### 2. is_not_empty

**功能**：判断数组是否不为空。

**方法签名**：
```python
@staticmethod
def is_not_empty(array: Any) -> bool
```

**参数**：
- `array` (Any): 要判断的数组

**返回值**：
- `bool`: 如果不为空则返回 True，否则返回 False

**使用场景**：
- 验证数组是否有效
- 作为条件判断
- 确保数组操作的安全性

**使用示例**：
```python
# 检查非空数组
print(ArrayUtils.is_not_empty([1, 2, 3]))  # 输出: True

# 检查空数组
print(ArrayUtils.is_not_empty([]))  # 输出: False
```

### 3. size

**功能**：获取数组大小。

**方法签名**：
```python
@staticmethod
def size(array: Any) -> int
```

**参数**：
- `array` (Any): 要获取大小的数组

**返回值**：
- `int`: 数组大小

**使用场景**：
- 检查数组长度
- 分配资源
- 循环处理

**使用示例**：
```python
# 获取数组大小
print(ArrayUtils.size([1, 2, 3, 4, 5]))  # 输出: 5

# 处理 None
print(ArrayUtils.size(None))  # 输出: 0
```

### 4. add

**功能**：向数组添加元素。

**方法签名**：
```python
@staticmethod
def add(array: List, element: Any) -> None
```

**参数**：
- `array` (List): 要添加元素的数组
- `element` (Any): 要添加的元素

**返回值**：
- `None`

**使用场景**：
- 动态构建数组
- 向现有数组添加元素
- 收集数据

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 添加元素
ArrayUtils.add(arr, 6)
print(arr)  # 输出: [1, 2, 3, 4, 5, 6]
```

### 5. add_all

**功能**：向数组添加多个元素。

**方法签名**：
```python
@staticmethod
def add_all(array: List, elements: Union[List, Tuple]) -> None
```

**参数**：
- `array` (List): 要添加元素的数组
- `elements` (Union[List, Tuple]): 要添加的元素集合

**返回值**：
- `None`

**使用场景**：
- 批量添加元素
- 合并数组
- 一次性添加多个元素

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 添加多个元素
ArrayUtils.add_all(arr, [7, 8, 9])
print(arr)  # 输出: [1, 2, 3, 4, 5, 7, 8, 9]
```

### 6. remove

**功能**：从数组中移除元素。

**方法签名**：
```python
@staticmethod
def remove(array: List, element: Any) -> bool
```

**参数**：
- `array` (List): 要移除元素的数组
- `element` (Any): 要移除的元素

**返回值**：
- `bool`: 如果移除成功则返回 True，否则返回 False

**使用场景**：
- 移除特定元素
- 清理数组
- 条件性移除

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 移除元素
ArrayUtils.remove(arr, 3)
print(arr)  # 输出: [1, 2, 4, 5]
```

### 7. remove_at

**功能**：从数组中移除指定位置的元素。

**方法签名**：
```python
@staticmethod
def remove_at(array: List, index: int) -> Any
```

**参数**：
- `array` (List): 要移除元素的数组
- `index` (int): 要移除的元素位置

**返回值**：
- `Any`: 被移除的元素，如果移除失败则返回 None

**使用场景**：
- 移除指定位置的元素
- 按索引删除
- 处理有序数组

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 移除指定位置元素
removed = ArrayUtils.remove_at(arr, 0)
print(removed)  # 输出: 1
print(arr)  # 输出: [2, 3, 4, 5]
```

### 8. get

**功能**：获取数组指定位置的元素。

**方法签名**：
```python
@staticmethod
def get(array: Union[List, Tuple], index: int) -> Any
```

**参数**：
- `array` (Union[List, Tuple]): 要获取元素的数组
- `index` (int): 元素位置

**返回值**：
- `Any`: 数组元素，如果位置无效则返回 None

**使用场景**：
- 安全地获取数组元素
- 避免索引越界异常
- 条件性访问

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 获取元素
print(ArrayUtils.get(arr, 2))  # 输出: 3

# 获取无效位置
print(ArrayUtils.get(arr, 10))  # 输出: None
```

### 9. set

**功能**：设置数组指定位置的元素。

**方法签名**：
```python
@staticmethod
def set(array: List, index: int, element: Any) -> bool
```

**参数**：
- `array` (List): 要设置元素的数组
- `index` (int): 元素位置
- `element` (Any): 要设置的元素

**返回值**：
- `bool`: 如果设置成功则返回 True，否则返回 False

**使用场景**：
- 修改数组元素
- 更新特定位置的值
- 安全地设置元素

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 设置元素
ArrayUtils.set(arr, 2, 10)
print(arr)  # 输出: [1, 2, 10, 4, 5]
```

### 10. index_of

**功能**：查找元素在数组中第一次出现的位置。

**方法签名**：
```python
@staticmethod
def index_of(array: Union[List, Tuple], element: Any) -> int
```

**参数**：
- `array` (Union[List, Tuple]): 要查找的数组
- `element` (Any): 要查找的元素

**返回值**：
- `int`: 元素在数组中第一次出现的位置，如果没有找到则返回 -1

**使用场景**：
- 查找元素位置
- 检查元素是否存在
- 定位元素

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5, 3]

# 查找元素位置
print(ArrayUtils.index_of(arr, 3))  # 输出: 2

# 查找不存在的元素
print(ArrayUtils.index_of(arr, 10))  # 输出: -1
```

### 11. last_index_of

**功能**：查找元素在数组中最后一次出现的位置。

**方法签名**：
```python
@staticmethod
def last_index_of(array: Union[List, Tuple], element: Any) -> int
```

**参数**：
- `array` (Union[List, Tuple]): 要查找的数组
- `element` (Any): 要查找的元素

**返回值**：
- `int`: 元素在数组中最后一次出现的位置，如果没有找到则返回 -1

**使用场景**：
- 查找元素最后出现的位置
- 处理重复元素
- 从后向前查找

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5, 3]

# 查找元素最后出现的位置
print(ArrayUtils.last_index_of(arr, 3))  # 输出: 5
```

### 12. contains

**功能**：判断数组是否包含指定元素。

**方法签名**：
```python
@staticmethod
def contains(array: Union[List, Tuple], element: Any) -> bool
```

**参数**：
- `array` (Union[List, Tuple]): 要判断的数组
- `element` (Any): 要检查的元素

**返回值**：
- `bool`: 如果包含指定元素则返回 True，否则返回 False

**使用场景**：
- 检查元素是否存在
- 条件判断
- 验证输入

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 检查元素是否存在
print(ArrayUtils.contains(arr, 3))  # 输出: True
print(ArrayUtils.contains(arr, 10))  # 输出: False
```

### 13. sort

**功能**：排序数组。

**方法签名**：
```python
@staticmethod
def sort(array: List, key: Optional[Callable[[Any], Any]] = None, reverse: bool = False) -> None
```

**参数**：
- `array` (List): 要排序的数组
- `key` (Optional[Callable[[Any], Any]]): 排序键函数
- `reverse` (bool): 是否倒序

**返回值**：
- `None`

**使用场景**：
- 对数组进行排序
- 自定义排序规则
- 按特定键排序

**使用示例**：
```python
# 创建数组
arr = [3, 1, 4, 2, 5]

# 排序
ArrayUtils.sort(arr)
print(arr)  # 输出: [1, 2, 3, 4, 5]

# 倒序排序
ArrayUtils.sort(arr, reverse=True)
print(arr)  # 输出: [5, 4, 3, 2, 1]

# 按绝对值排序
arr = [-3, 1, -4, 2, 5]
ArrayUtils.sort(arr, key=abs)
print(arr)  # 输出: [1, 2, -3, -4, 5]
```

### 14. sorted

**功能**：排序数组并返回新数组。

**方法签名**：
```python
@staticmethod
def sorted(array: Union[List, Tuple], key: Optional[Callable[[Any], Any]] = None, reverse: bool = False) -> List
```

**参数**：
- `array` (Union[List, Tuple]): 要排序的数组
- `key` (Optional[Callable[[Any], Any]]): 排序键函数
- `reverse` (bool): 是否倒序

**返回值**：
- `List`: 排序后的新数组

**使用场景**：
- 排序数组并保持原数组不变
- 链式操作
- 临时排序

**使用示例**：
```python
# 创建数组
arr = [3, 1, 4, 2, 5]

# 排序并返回新数组
sorted_arr = ArrayUtils.sorted(arr)
print(sorted_arr)  # 输出: [1, 2, 3, 4, 5]
print(arr)  # 输出: [3, 1, 4, 2, 5] (原数组不变)
```

### 15. reverse

**功能**：反转数组。

**方法签名**：
```python
@staticmethod
def reverse(array: List) -> None
```

**参数**：
- `array` (List): 要反转的数组

**返回值**：
- `None`

**使用场景**：
- 反转数组顺序
- 逆序处理
- 颠倒元素顺序

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 反转数组
ArrayUtils.reverse(arr)
print(arr)  # 输出: [5, 4, 3, 2, 1]
```

### 16. reversed

**功能**：反转数组并返回新数组。

**方法签名**：
```python
@staticmethod
def reversed(array: Union[List, Tuple]) -> List
```

**参数**：
- `array` (Union[List, Tuple]): 要反转的数组

**返回值**：
- `List`: 反转后的新数组

**使用场景**：
- 反转数组并保持原数组不变
- 链式操作
- 临时反转

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 反转并返回新数组
reversed_arr = ArrayUtils.reversed(arr)
print(reversed_arr)  # 输出: [5, 4, 3, 2, 1]
print(arr)  # 输出: [1, 2, 3, 4, 5] (原数组不变)
```

### 17. copy

**功能**：复制数组。

**方法签名**：
```python
@staticmethod
def copy(array: Union[List, Tuple]) -> List
```

**参数**：
- `array` (Union[List, Tuple]): 要复制的数组

**返回值**：
- `List`: 复制后的新数组

**使用场景**：
- 创建数组副本
- 避免修改原数组
- 安全操作

**使用示例**：
```python
# 创建数组
arr1 = [1, 2, 3]

# 复制数组
arr2 = ArrayUtils.copy(arr1)
print(arr2)  # 输出: [1, 2, 3]

# 修改副本不影响原数组
arr2.append(4)
print(arr1)  # 输出: [1, 2, 3]
print(arr2)  # 输出: [1, 2, 3, 4]
```

### 18. sub_array

**功能**：截取数组。

**方法签名**：
```python
@staticmethod
def sub_array(array: Union[List, Tuple], start: int, end: Optional[int] = None) -> List
```

**参数**：
- `array` (Union[List, Tuple]): 要截取的数组
- `start` (int): 起始位置
- `end` (Optional[int]): 结束位置

**返回值**：
- `List`: 截取后的新数组

**使用场景**：
- 获取数组的一部分
- 分页处理
- 范围操作

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 截取从索引2开始的子数组
sub = ArrayUtils.sub_array(arr, 2)
print(sub)  # 输出: [3, 4, 5, 6, 7, 8, 9]

# 截取指定范围
sub = ArrayUtils.sub_array(arr, 2, 5)
print(sub)  # 输出: [3, 4, 5]
```

### 19. concat

**功能**：合并多个数组。

**方法签名**：
```python
@staticmethod
def concat(*arrays: Union[List, Tuple]) -> List
```

**参数**：
- `*arrays` (Union[List, Tuple]): 要合并的数组

**返回值**：
- `List`: 合并后的新数组

**使用场景**：
- 合并多个数组
- 组合数据
- 拼接数组

**使用示例**：
```python
# 创建数组
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = [7, 8, 9]

# 合并数组
merged = ArrayUtils.concat(arr1, arr2, arr3)
print(merged)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 20. flatten

**功能**：扁平化数组。

**方法签名**：
```python
@staticmethod
def flatten(array: Union[List, Tuple]) -> List
```

**参数**：
- `array` (Union[List, Tuple]): 要扁平化的数组

**返回值**：
- `List`: 扁平化后的新数组

**使用场景**：
- 处理嵌套数组
- 扁平化多维数组
- 简化数据结构

**使用示例**：
```python
# 创建嵌套数组
nested_arr = [[1, 2], [3, 4], [5, 6]]

# 扁平化
flat_arr = ArrayUtils.flatten(nested_arr)
print(flat_arr)  # 输出: [1, 2, 3, 4, 5, 6]

# 处理深度嵌套
deep_nested = [[1, [2, 3]], [4, [5, 6]]]
flat_deep = ArrayUtils.flatten(deep_nested)
print(flat_deep)  # 输出: [1, 2, 3, 4, 5, 6]
```

### 21. distinct

**功能**：去重数组。

**方法签名**：
```python
@staticmethod
def distinct(array: Union[List, Tuple]) -> List
```

**参数**：
- `array` (Union[List, Tuple]): 要去重的数组

**返回值**：
- `List`: 去重后的新数组

**使用场景**：
- 去除重复元素
- 数据去重
- 保持唯一性

**使用示例**：
```python
# 创建带重复元素的数组
duplicate_arr = [1, 2, 2, 3, 4, 4, 5]

# 去重
unique_arr = ArrayUtils.distinct(duplicate_arr)
print(unique_arr)  # 输出: [1, 2, 3, 4, 5]
```

### 22. chunk

**功能**：将数组分块。

**方法签名**：
```python
@staticmethod
def chunk(array: Union[List, Tuple], size: int) -> List[List]
```

**参数**：
- `array` (Union[List, Tuple]): 要分块的数组
- `size` (int): 块大小

**返回值**：
- `List[List]`: 分块后的新数组

**使用场景**：
- 分批处理数据
- 分页显示
- 批量操作

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 分块（每个块大小为3）
chunks = ArrayUtils.chunk(arr, 3)
print(chunks)  # 输出: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 分块（每个块大小为2）
chunks = ArrayUtils.chunk(arr, 2)
print(chunks)  # 输出: [[1, 2], [3, 4], [5, 6], [7, 8], [9]]
```

### 23. fill

**功能**：填充数组。

**方法签名**：
```python
@staticmethod
def fill(array: List, value: Any, start: int = 0, end: Optional[int] = None) -> None
```

**参数**：
- `array` (List): 要填充的数组
- `value` (Any): 填充值
- `start` (int): 起始位置
- `end` (Optional[int]): 结束位置

**返回值**：
- `None`

**使用场景**：
- 初始化数组
- 重置数组值
- 填充特定范围

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 填充（用0替换所有元素）
ArrayUtils.fill(arr, 0)
print(arr)  # 输出: [0, 0, 0, 0, 0]

# 填充指定范围
arr = [1, 2, 3, 4, 5]
ArrayUtils.fill(arr, 9, 1, 4)
print(arr)  # 输出: [1, 9, 9, 9, 5]
```

### 24. to_list

**功能**：将对象转换为数组。

**方法签名**：
```python
@staticmethod
def to_list(array: Any) -> List
```

**参数**：
- `array` (Any): 要转换的对象

**返回值**：
- `List`: 转换后的数组

**使用场景**：
- 统一数据类型
- 处理不同类型的输入
- 确保返回列表

**使用示例**：
```python
# 转换元组为列表
tuple_data = (1, 2, 3, 4, 5)
list_data = ArrayUtils.to_list(tuple_data)
print(list_data)  # 输出: [1, 2, 3, 4, 5]

# 转换单个元素为列表
single_item = 42
list_data = ArrayUtils.to_list(single_item)
print(list_data)  # 输出: [42]
```

### 25. to_tuple

**功能**：将对象转换为元组。

**方法签名**：
```python
@staticmethod
def to_tuple(array: Any) -> Tuple
```

**参数**：
- `array` (Any): 要转换的对象

**返回值**：
- `Tuple`: 转换后的元组

**使用场景**：
- 统一数据类型
- 处理不同类型的输入
- 确保返回元组

**使用示例**：
```python
# 转换列表为元组
list_data = [1, 2, 3, 4, 5]
tuple_data = ArrayUtils.to_tuple(list_data)
print(tuple_data)  # 输出: (1, 2, 3, 4, 5)
```

### 26. to_numpy

**功能**：将对象转换为NumPy数组。

**方法签名**：
```python
@staticmethod
def to_numpy(array: Any) -> np.ndarray
```

**参数**：
- `array` (Any): 要转换的对象

**返回值**：
- `np.ndarray`: 转换后的NumPy数组

**使用场景**：
- 科学计算
- 数据分析
- 与NumPy库集成

**使用示例**：
```python
# 转换列表为NumPy数组
import numpy as np
list_data = [1, 2, 3, 4, 5]
numpy_data = ArrayUtils.to_numpy(list_data)
print(numpy_data)  # 输出: [1 2 3 4 5]
print(type(numpy_data))  # 输出: <class 'numpy.ndarray'>
```

### 27. max

**功能**：获取数组中的最大值。

**方法签名**：
```python
@staticmethod
def max(array: Union[List, Tuple]) -> Any
```

**参数**：
- `array` (Union[List, Tuple]): 要获取最大值的数组

**返回值**：
- `Any`: 最大值，如果数组为空则返回 None

**使用场景**：
- 查找最大值
- 数据分析
- 统计计算

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 获取最大值
print(ArrayUtils.max(arr))  # 输出: 5

# 处理空数组
print(ArrayUtils.max([]))  # 输出: None
```

### 28. min

**功能**：获取数组中的最小值。

**方法签名**：
```python
@staticmethod
def min(array: Union[List, Tuple]) -> Any
```

**参数**：
- `array` (Union[List, Tuple]): 要获取最小值的数组

**返回值**：
- `Any`: 最小值，如果数组为空则返回 None

**使用场景**：
- 查找最小值
- 数据分析
- 统计计算

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 获取最小值
print(ArrayUtils.min(arr))  # 输出: 1
```

### 29. sum

**功能**：计算数组中元素的和。

**方法签名**：
```python
@staticmethod
def sum(array: Union[List, Tuple]) -> Any
```

**参数**：
- `array` (Union[List, Tuple]): 要计算和的数组

**返回值**：
- `Any`: 元素的和，如果数组为空则返回 0

**使用场景**：
- 计算总和
- 数据分析
- 统计计算

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 计算和
print(ArrayUtils.sum(arr))  # 输出: 15
```

### 30. average

**功能**：计算数组中元素的平均值。

**方法签名**：
```python
@staticmethod
def average(array: Union[List, Tuple]) -> float
```

**参数**：
- `array` (Union[List, Tuple]): 要计算平均值的数组

**返回值**：
- `float`: 元素的平均值，如果数组为空则返回 0.0

**使用场景**：
- 计算平均值
- 数据分析
- 统计计算

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 计算平均值
print(ArrayUtils.average(arr))  # 输出: 3.0
```

### 31. median

**功能**：计算数组中元素的中位数。

**方法签名**：
```python
@staticmethod
def median(array: Union[List, Tuple]) -> float
```

**参数**：
- `array` (Union[List, Tuple]): 要计算中位数的数组

**返回值**：
- `float`: 元素的中位数，如果数组为空则返回 0.0

**使用场景**：
- 计算中位数
- 数据分析
- 统计计算

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 计算中位数
print(ArrayUtils.median(arr))  # 输出: 3.0

# 处理偶数长度数组
arr = [1, 2, 3, 4, 5, 6]
print(ArrayUtils.median(arr))  # 输出: 3.5
```

### 32. frequency

**功能**：计算元素在数组中出现的频率。

**方法签名**：
```python
@staticmethod
def frequency(array: Union[List, Tuple], element: Any) -> int
```

**参数**：
- `array` (Union[List, Tuple]): 要计算的数组
- `element` (Any): 要计算频率的元素

**返回值**：
- `int`: 元素出现的频率

**使用场景**：
- 统计元素出现次数
- 数据分析
- 频率计算

**使用示例**：
```python
# 创建数组
arr = [1, 2, 2, 3, 4, 4, 4, 5]

# 计算元素频率
print(ArrayUtils.frequency(arr, 4))  # 输出: 3
print(ArrayUtils.frequency(arr, 10))  # 输出: 0
```

### 33. filter

**功能**：过滤数组中符合条件的元素。

**方法签名**：
```python
@staticmethod
def filter(array: Union[List, Tuple], predicate: Callable[[Any], bool]) -> List
```

**参数**：
- `array` (Union[List, Tuple]): 要过滤的数组
- `predicate` (Callable[[Any], bool]): 条件函数

**返回值**：
- `List`: 符合条件的元素数组

**使用场景**：
- 过滤数据
- 条件筛选
- 数据清洗

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 过滤大于5的元素
filtered = ArrayUtils.filter(arr, lambda x: x > 5)
print(filtered)  # 输出: [6, 7, 8, 9, 10]

# 过滤偶数
filtered = ArrayUtils.filter(arr, lambda x: x % 2 == 0)
print(filtered)  # 输出: [2, 4, 6, 8, 10]
```

### 34. map

**功能**：映射数组中的元素。

**方法签名**：
```python
@staticmethod
def map(array: Union[List, Tuple], mapper: Callable[[Any], Any]) -> List
```

**参数**：
- `array` (Union[List, Tuple]): 要映射的数组
- `mapper` (Callable[[Any], Any]): 映射函数

**返回值**：
- `List`: 映射后的元素数组

**使用场景**：
- 转换数组元素
- 数据变换
- 元素处理

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 每个元素乘以2
mapped = ArrayUtils.map(arr, lambda x: x * 2)
print(mapped)  # 输出: [2, 4, 6, 8, 10]

# 转换为字符串
mapped = ArrayUtils.map(arr, lambda x: f"Item {x}")
print(mapped)  # 输出: ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
```

### 35. for_each

**功能**：遍历数组中的元素并执行操作。

**方法签名**：
```python
@staticmethod
def for_each(array: Union[List, Tuple], action: Callable[[Any], None]) -> None
```

**参数**：
- `array` (Union[List, Tuple]): 要遍历的数组
- `action` (Callable[[Any], None]): 操作函数

**返回值**：
- `None`

**使用场景**：
- 遍历数组执行操作
- 打印元素
- 副作用操作

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 打印每个元素
ArrayUtils.for_each(arr, lambda x: print(f"Element: {x}"))
# 输出:
# Element: 1
# Element: 2
# Element: 3
# Element: 4
# Element: 5
```

### 36. any_match

**功能**：判断数组中是否存在符合条件的元素。

**方法签名**：
```python
@staticmethod
def any_match(array: Union[List, Tuple], predicate: Callable[[Any], bool]) -> bool
```

**参数**：
- `array` (Union[List, Tuple]): 要判断的数组
- `predicate` (Callable[[Any], bool]): 条件函数

**返回值**：
- `bool`: 如果存在符合条件的元素则返回 True，否则返回 False

**使用场景**：
- 检查是否存在符合条件的元素
- 条件判断
- 快速验证

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 检查是否有元素大于3
print(ArrayUtils.any_match(arr, lambda x: x > 3))  # 输出: True

# 检查是否有元素大于10
print(ArrayUtils.any_match(arr, lambda x: x > 10))  # 输出: False
```

### 37. all_match

**功能**：判断数组中是否所有元素都符合条件。

**方法签名**：
```python
@staticmethod
def all_match(array: Union[List, Tuple], predicate: Callable[[Any], bool]) -> bool
```

**参数**：
- `array` (Union[List, Tuple]): 要判断的数组
- `predicate` (Callable[[Any], bool]): 条件函数

**返回值**：
- `bool`: 如果所有元素都符合条件则返回 True，否则返回 False

**使用场景**：
- 检查所有元素是否符合条件
- 数据验证
- 整体判断

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 检查是否所有元素都大于0
print(ArrayUtils.all_match(arr, lambda x: x > 0))  # 输出: True

# 检查是否所有元素都大于3
print(ArrayUtils.all_match(arr, lambda x: x > 3))  # 输出: False
```

### 38. none_match

**功能**：判断数组中是否没有符合条件的元素。

**方法签名**：
```python
@staticmethod
def none_match(array: Union[List, Tuple], predicate: Callable[[Any], bool]) -> bool
```

**参数**：
- `array` (Union[List, Tuple]): 要判断的数组
- `predicate` (Callable[[Any], bool]): 条件函数

**返回值**：
- `bool`: 如果没有符合条件的元素则返回 True，否则返回 False

**使用场景**：
- 检查是否没有符合条件的元素
- 数据验证
- 整体判断

**使用示例**：
```python
# 创建数组
arr = [1, 2, 3, 4, 5]

# 检查是否没有元素大于10
print(ArrayUtils.none_match(arr, lambda x: x > 10))  # 输出: True

# 检查是否没有元素大于3
print(ArrayUtils.none_match(arr, lambda x: x > 3))  # 输出: False
```

## 综合使用示例

### 1. 数据处理流程

```python
def process_data(data):
    """处理数据"""
    # 检查数据是否为空
    if ArrayUtils.is_empty(data):
        return []
    
    # 去重
    unique_data = ArrayUtils.distinct(data)
    
    # 排序
    ArrayUtils.sort(unique_data)
    
    # 过滤大于5的元素
    filtered_data = ArrayUtils.filter(unique_data, lambda x: x > 5)
    
    # 映射每个元素为其平方
    mapped_data = ArrayUtils.map(filtered_data, lambda x: x ** 2)
    
    return mapped_data

# 使用示例
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = process_data(data)
print(result)  # 输出: [36, 81]
```

### 2. 分页处理

```python
def paginate(data, page_size):
    """分页处理数据"""
    # 分块
    chunks = ArrayUtils.chunk(data, page_size)
    
    # 遍历每一页
    for i, page in enumerate(chunks):
        print(f"Page {i + 1}: {page}")

# 使用示例
data = list(range(1, 21))  # [1, 2, 3, ..., 20]
paginate(data, 5)
# 输出:
# Page 1: [1, 2, 3, 4, 5]
# Page 2: [6, 7, 8, 9, 10]
# Page 3: [11, 12, 13, 14, 15]
# Page 4: [16, 17, 18, 19, 20]
```

### 3. 统计分析

```python
def analyze_data(data):
    """分析数据"""
    if ArrayUtils.is_empty(data):
        return {}
    
    return {
        "count": ArrayUtils.size(data),
        "max": ArrayUtils.max(data),
        "min": ArrayUtils.min(data),
        "sum": ArrayUtils.sum(data),
        "average": ArrayUtils.average(data),
        "median": ArrayUtils.median(data)
    }

# 使用示例
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
analysis = analyze_data(data)
print(analysis)
# 输出:
# {
#     "count": 10,
#     "max": 10,
#     "min": 1,
#     "sum": 55,
#     "average": 5.5,
#     "median": 5.5
# }
```

## 性能提示

- 对于频繁的数组操作，建议使用 `copy()` 方法创建副本，避免修改原数组
- 对于大型数组，某些操作（如 `flatten`）可能会影响性能，请根据实际情况选择合适的方法
- 对于需要频繁访问的数组元素，建议使用索引访问而不是 `get()` 方法
- 对于需要排序的大型数组，考虑使用 `sorted()` 方法并指定合适的 `key` 函数

## 注意事项

1. 大多数方法会直接修改原数组，如需保持原数组不变，请使用 `copy()` 方法创建副本。
2. 对于 `to_numpy()` 方法，需要确保已安装 numpy 库。
3. 对于大型数组，某些操作可能会影响性能，请根据实际情况选择合适的方法。
4. 所有方法都提供了对 `None` 值的安全处理，确保在处理可能为 `None` 的数组时不会抛出异常。

## 总结

`ArrayUtils` 提供了全面的数组操作功能，从基本的添加、删除、获取元素到高级的排序、过滤、映射等操作，涵盖了日常开发中大部分数组处理需求。通过合理使用这些功能，可以大大简化数组处理代码，提高开发效率。

所有方法都提供了对 `None` 值的安全处理，确保在处理可能为 `None` 的数组时不会抛出异常。这使得 `ArrayUtils` 成为处理数组的可靠工具类。