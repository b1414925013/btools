# RandomUtil - 随机工具类

## 功能特性

`RandomUtil` 是一个随机工具类，提供了丰富的随机数生成功能，包括：

- 生成随机整数、浮点数、布尔值
- 生成随机字符串（支持大小写字母、数字、十六进制等）
- 从序列中随机选择元素
- 打乱序列
- 生成随机字节串、UUID、颜色
- 生成随机邮箱地址、手机号、密码
- 生成随机日期、时间
- 设置随机种子
- 生成高斯分布、三角形分布、指数分布的随机数

## 基本用法

### 导入模块

```python
from btools.core.basic import RandomUtil
```

### 1. 生成随机整数

```python
# 生成默认范围的随机整数（0-999999999）
random_int = RandomUtil.randomInt()
print(f"随机整数: {random_int}")

# 生成指定范围的随机整数（1-100）
random_int = RandomUtil.randomInt(1, 100)
print(f"1-100的随机整数: {random_int}")
```

### 2. 生成随机浮点数

```python
# 生成默认范围的随机浮点数（0.0-1.0）
random_float = RandomUtil.randomFloat()
print(f"随机浮点数: {random_float}")

# 生成指定范围的随机浮点数（1.0-10.0）
random_float = RandomUtil.randomFloat(1.0, 10.0)
print(f"1.0-10.0的随机浮点数: {random_float}")
```

### 3. 生成随机布尔值

```python
# 生成随机布尔值
random_bool = RandomUtil.randomBool()
print(f"随机布尔值: {random_bool}")
```

### 4. 生成随机字符串

```python
# 生成默认长度的随机字符串（8位，包含大小写字母和数字）
random_str = RandomUtil.randomStr()
print(f"随机字符串: {random_str}")

# 生成指定长度的随机字符串（16位）
random_str = RandomUtil.randomStr(16)
print(f"16位随机字符串: {random_str}")

# 生成指定字符集的随机字符串（只包含小写字母）
random_str = RandomUtil.randomStr(10, "abcdefghijklmnopqrstuvwxyz")
print(f"10位小写随机字符串: {random_str}")
```

### 5. 生成特定类型的随机字符串

```python
# 生成随机小写字符串
lower_str = RandomUtil.randomLowerStr(10)
print(f"随机小写字符串: {lower_str}")

# 生成随机大写字符串
upper_str = RandomUtil.randomUpperStr(10)
print(f"随机大写字符串: {upper_str}")

# 生成随机数字字符串
number_str = RandomUtil.randomNumberStr(10)
print(f"随机数字字符串: {number_str}")

# 生成随机十六进制字符串
hex_str = RandomUtil.randomHexStr(10)
print(f"随机十六进制字符串: {hex_str}")
```

### 6. 生成随机字符

```python
# 生成随机字符（包含大小写字母和数字）
random_char = RandomUtil.randomChar()
print(f"随机字符: {random_char}")

# 生成指定字符集的随机字符（只包含小写字母）
random_char = RandomUtil.randomChar("abcdefghijklmnopqrstuvwxyz")
print(f"随机小写字符: {random_char}")
```

### 7. 从序列中随机选择元素

```python
# 从序列中随机选择一个元素
sequence = ["apple", "banana", "orange", "grape", "watermelon"]
random_element = RandomUtil.randomChoice(sequence)
print(f"随机选择的元素: {random_element}")

# 从序列中随机选择多个元素（可重复）
random_elements = RandomUtil.randomChoices(sequence, k=3)
print(f"随机选择的多个元素（可重复）: {random_elements}")

# 从序列中随机选择多个元素（不可重复）
random_elements = RandomUtil.randomSample(sequence, k=3)
print(f"随机选择的多个元素（不可重复）: {random_elements}")
```

### 8. 打乱序列

```python
# 打乱序列
sequence = [1, 2, 3, 4, 5]
print(f"打乱前: {sequence}")
RandomUtil.shuffle(sequence)
print(f"打乱后: {sequence}")
```

### 9. 生成随机字节串

```python
# 生成随机字节串（8字节）
random_bytes = RandomUtil.randomBytes(8)
print(f"随机字节串: {random_bytes}")
```

### 10. 生成随机UUID

```python
# 生成随机UUID
random_uuid = RandomUtil.randomUUID()
print(f"随机UUID: {random_uuid}")
```

### 11. 生成随机颜色

```python
# 生成随机颜色（不包含透明度）
random_color = RandomUtil.randomColor()
print(f"随机颜色: {random_color}")

# 生成随机颜色（包含透明度）
random_color_with_alpha = RandomUtil.randomColor(alpha=True)
print(f"随机颜色（带透明度）: {random_color_with_alpha}")
```

### 12. 生成随机邮箱地址

```python
# 生成随机邮箱地址（默认域名）
random_email = RandomUtil.randomEmail()
print(f"随机邮箱地址: {random_email}")

# 生成指定域名的随机邮箱地址
random_email = RandomUtil.randomEmail("test.com")
print(f"指定域名的随机邮箱地址: {random_email}")
```

### 13. 生成随机手机号

```python
# 生成随机手机号（默认前缀）
random_phone = RandomUtil.randomPhone()
print(f"随机手机号: {random_phone}")

# 生成指定前缀的随机手机号
random_phone = RandomUtil.randomPhone("139")
print(f"指定前缀的随机手机号: {random_phone}")
```

### 14. 生成随机密码

```python
# 生成随机密码（默认长度12位，包含大小写字母、数字和特殊字符）
random_password = RandomUtil.randomPassword()
print(f"随机密码: {random_password}")

# 生成指定长度的随机密码
random_password = RandomUtil.randomPassword(16)
print(f"16位随机密码: {random_password}")
```

### 15. 生成随机日期

```python
# 生成随机日期（默认范围1970-2030）
year, month, day = RandomUtil.randomDate()
print(f"随机日期: {year}-{month:02d}-{day:02d}")

# 生成指定范围的随机日期
year, month, day = RandomUtil.randomDate(2000, 2020)
print(f"2000-2020的随机日期: {year}-{month:02d}-{day:02d}")
```

### 16. 生成随机时间

```python
# 生成随机时间
hour, minute, second = RandomUtil.randomTime()
print(f"随机时间: {hour:02d}:{minute:02d}:{second:02d}")
```

### 17. 设置随机种子

```python
# 设置随机种子（设置后，生成的随机数会固定）
RandomUtil.setSeed(12345)

# 生成随机整数
random_int1 = RandomUtil.randomInt()
print(f"设置种子后的随机整数: {random_int1}")

# 重新设置相同的种子
RandomUtil.setSeed(12345)

# 生成的随机整数应该与之前相同
random_int2 = RandomUtil.randomInt()
print(f"重新设置种子后的随机整数: {random_int2}")
print(f"两个随机数是否相同: {random_int1 == random_int2}")
```

### 18. 获取随机数生成器实例

```python
# 获取随机数生成器实例
random_instance = RandomUtil.getRandom()
print(f"随机数生成器实例: {random_instance}")

# 使用实例生成随机数
random_value = random_instance.randint(1, 100)
print(f"使用实例生成的随机整数: {random_value}")
```

### 19. 生成特殊分布的随机数

```python
# 生成高斯分布的随机数（均值0.0，标准差1.0）
gaussian_value = RandomUtil.randomGaussian()
print(f"高斯分布的随机数: {gaussian_value}")

# 生成三角形分布的随机数（最小值1.0，最大值3.0，众数2.0）
triangular_value = RandomUtil.randomTriangular(1.0, 3.0, 2.0)
print(f"三角形分布的随机数: {triangular_value}")

# 生成指数分布的随机数（速率参数1.0）
expovariate_value = RandomUtil.randomExpovariate(1.0)
print(f"指数分布的随机数: {expovariate_value}")
```

## 高级用法

### 1. 生成指定格式的随机数据

```python
# 生成随机身份证号（简化版）
def generate_id_card():
    # 前6位地区码（这里使用固定值）
    area_code = "110101"
    # 生成随机出生日期
    year, month, day = RandomUtil.randomDate(1970, 2000)
    birth_date = f"{year}{month:02d}{day:02d}"
    # 生成随机顺序码
    sequence_code = RandomUtil.randomNumberStr(3)
    # 生成随机校验码
    check_code = RandomUtil.randomChar("0123456789X")
    return f"{area_code}{birth_date}{sequence_code}{check_code}"

# 测试生成身份证号
id_card = generate_id_card()
print(f"随机身份证号: {id_card}")
```

### 2. 生成随机用户信息

```python
# 生成随机用户信息
def generate_user_info():
    return {
        "username": RandomUtil.randomStr(10, string.ascii_lowercase + string.digits),
        "password": RandomUtil.randomPassword(),
        "email": RandomUtil.randomEmail(),
        "phone": RandomUtil.randomPhone(),
        "birth_date": f"{RandomUtil.randomDate(1970, 2000)}",
        "avatar_color": RandomUtil.randomColor()
    }

# 测试生成用户信息
import string
user_info = generate_user_info()
print(f"随机用户信息: {user_info}")
```

### 3. 生成随机测试数据

```python
# 生成随机测试数据
def generate_test_data(count=10):
    data = []
    for i in range(count):
        data.append({
            "id": i + 1,
            "name": RandomUtil.randomStr(10, string.ascii_lowercase),
            "age": RandomUtil.randomInt(18, 60),
            "score": RandomUtil.randomFloat(0, 100),
            "passed": RandomUtil.randomBool(),
            "email": RandomUtil.randomEmail(),
            "phone": RandomUtil.randomPhone()
        })
    return data

# 测试生成测试数据
import string
test_data = generate_test_data(5)
print(f"随机测试数据: {test_data}")
```

### 4. 随机排序

```python
# 随机排序
def random_sort(items):
    """随机排序列表"""
    items_copy = items.copy()
    RandomUtil.shuffle(items_copy)
    return items_copy

# 测试随机排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始列表: {items}")
sorted_items = random_sort(items)
print(f"随机排序后: {sorted_items}")
```

## 注意事项

1. **随机性**：`RandomUtil` 使用 Python 标准库的 `random` 模块，生成的是伪随机数。如果需要加密级别的随机性，请使用 `secrets` 模块。

2. **种子设置**：设置随机种子后，生成的随机数序列会固定，这在需要可重复的随机结果时非常有用。

3. **性能考虑**：对于大量生成随机数的场景，建议直接使用 `getRandom()` 获取随机数生成器实例，然后重复使用该实例。

4. **密码安全性**：`randomPassword()` 生成的密码包含大小写字母、数字和特殊字符，适合一般场景使用，但如果需要更高安全性的密码，建议使用 `secrets` 模块。

5. **数据范围**：生成随机日期时，会自动处理不同月份的天数，确保生成的日期是有效的。

6. **字符集**：生成随机字符串时，默认字符集为大小写字母和数字，如果需要包含特殊字符，请自定义字符集。

## 总结

`RandomUtil` 提供了全面的随机数生成功能，简化了随机数据的生成过程。通过这些工具方法，您可以更方便地生成各种类型的随机数据，适用于测试、模拟、密码生成等多种场景。