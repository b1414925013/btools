# MathUtils 使用指南

`MathUtils` 是一个数学工具类，提供了丰富的数学计算方法，包括基本数学运算、随机数生成、统计计算等功能。

## 功能特性

- 基本数学运算（绝对值、平方根、幂运算、指数运算、对数运算）
- 三角函数（正弦、余弦、正切、角度弧度转换）
- 取整函数（向上取整、向下取整、四舍五入、截断）
- 符号函数
- 最大值、最小值、求和、平均值、中位数计算
- 最大公约数、最小公倍数计算
- 随机数生成（整数、浮点数、随机选择、随机采样）
- 洗牌功能
- 随机种子设置
- 距离计算
- 钳制功能
- 线性插值
- 阶乘、组合数、排列数计算

## 基本用法

### 导入

```python
from btools import MathUtils
```

### 示例

#### 基本数学运算

```python
# 绝对值
print(MathUtils.abs(-1))  # 输出: 1
print(MathUtils.abs(1))   # 输出: 1

# 平方根
print(MathUtils.sqrt(4))  # 输出: 2.0

# 幂运算
print(MathUtils.pow(2, 3))  # 输出: 8

# 指数运算
print(MathUtils.exp(1))  # 输出: 2.718281828459045

# 自然对数
print(MathUtils.log(1))  # 输出: 0.0

# 以10为底的对数
print(MathUtils.log10(10))  # 输出: 1.0
```

#### 三角函数

```python
# 正弦
print(MathUtils.sin(0))  # 输出: 0.0

# 余弦
print(MathUtils.cos(0))  # 输出: 1.0

# 正切
print(MathUtils.tan(0))  # 输出: 0.0

# 角度转弧度
print(MathUtils.radians(180))  # 输出: 3.141592653589793

# 弧度转角度
print(MathUtils.degrees(3.141592653589793))  # 输出: 180.0
```

#### 取整函数

```python
# 向上取整
print(MathUtils.ceil(1.2))  # 输出: 2

# 向下取整
print(MathUtils.floor(1.8))  # 输出: 1

# 四舍五入
print(MathUtils.round(1.2))  # 输出: 1
print(MathUtils.round(1.8))  # 输出: 2

# 截断
print(MathUtils.trunc(1.8))   # 输出: 1
print(MathUtils.trunc(-1.8))  # 输出: -1
```

#### 统计计算

```python
# 最大值
print(MathUtils.max(1, 2, 3))  # 输出: 3

# 最小值
print(MathUtils.min(1, 2, 3))  # 输出: 1

# 求和
print(MathUtils.sum(1, 2, 3))  # 输出: 6

# 平均值
print(MathUtils.average(1, 2, 3))  # 输出: 2.0

# 中位数
print(MathUtils.median(1, 2, 3))    # 输出: 2
print(MathUtils.median(1, 2, 3, 4))  # 输出: 2.5

# 最大公约数
print(MathUtils.gcd(4, 6))  # 输出: 2

# 最小公倍数
print(MathUtils.lcm(4, 6))  # 输出: 12
```

#### 随机数生成

```python
# 生成随机整数（1-10）
print(MathUtils.generate_random_integer(1, 10))

# 生成随机浮点数（1-10）
print(MathUtils.generate_random_float(1, 10))

# 随机选择
choices = [1, 2, 3, 4, 5]
print(MathUtils.generate_random_choice(choices))

# 随机采样（从列表中随机选择3个元素）
population = [1, 2, 3, 4, 5]
print(MathUtils.generate_random_sample(population, 3))

# 洗牌
arr = [1, 2, 3, 4, 5]
MathUtils.shuffle(arr)
print(arr)  # 输出: 随机排序的列表

# 设置随机种子
MathUtils.set_random_seed(42)
result1 = MathUtils.generate_random_integer(1, 10)
MathUtils.set_random_seed(42)
result2 = MathUtils.generate_random_integer(1, 10)
print(result1 == result2)  # 输出: True
```

## 高级用法

### 距离计算

```python
# 计算两点之间的距离
print(MathUtils.distance(0, 0, 3, 4))  # 输出: 5.0
```

### 钳制功能

```python
# 钳制值在指定范围内
print(MathUtils.clamp(5, 1, 10))   # 输出: 5
print(MathUtils.clamp(0, 1, 10))   # 输出: 1
print(MathUtils.clamp(15, 1, 10))  # 输出: 10
```

### 线性插值

```python
# 线性插值
print(MathUtils.lerp(0, 10, 0.5))  # 输出: 5
```

### 阶乘、组合数、排列数计算

```python
# 阶乘
print(MathUtils.factorial(5))  # 输出: 120

# 组合数
print(MathUtils.combinations(5, 2))  # 输出: 10

# 排列数
print(MathUtils.permutations(5, 2))  # 输出: 20
```

## 注意事项

1. 对于三角函数，所有角度参数都是以弧度为单位的。如果需要使用角度，请先使用 `radians()` 方法转换。
2. 对于随机数生成，如需重现相同的随机序列，请使用 `set_random_seed()` 方法设置种子。
3. 对于阶乘、组合数和排列数计算，输入值不宜过大，否则可能会导致计算结果溢出。

## 总结

`MathUtils` 提供了全面的数学计算功能，简化了数学运算的复杂度，使代码更加简洁易读。无论是基本的数学运算还是高级的统计计算，`MathUtils` 都能满足你的需求。