# Validator 使用指南

`Validator` 类提供了验证各种类型数据的静态方法。

## 基本使用

### 邮箱验证

```python
from btools import Validator

# 验证邮箱
print(Validator.is_email("user@example.com"))  # True
print(Validator.is_email("invalid-email"))      # False
```

### 手机号验证

```python
# 验证手机号（中国大陆）
print(Validator.is_phone("13812345678"))  # True
print(Validator.is_phone("1234567890"))   # False
```

### URL验证

```python
# 验证URL
print(Validator.is_url("https://example.com"))  # True
print(Validator.is_url("invalid-url"))          # False
```

### IP地址验证

```python
# 验证IPv4地址
print(Validator.is_ipv4("192.168.1.1"))   # True
print(Validator.is_ipv4("999.999.999.999"))  # False

# 验证IPv6地址
print(Validator.is_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # True
print(Validator.is_ipv6("invalid-ipv6"))                           # False
```

### 日期验证

```python
# 验证日期
print(Validator.is_date("2023-12-25"))  # True
print(Validator.is_date("2023/12/25"))  # False（默认格式为YYYY-MM-DD）
print(Validator.is_date("2023/12/25", "%Y/%m/%d"))  # True
```

### 数字验证

```python
# 验证数字
print(Validator.is_number("123"))      # True
print(Validator.is_number("123.45"))    # True
print(Validator.is_number("abc"))       # False

# 验证整数
print(Validator.is_integer("123"))      # True
print(Validator.is_integer("123.45"))  # False

# 验证浮点数
print(Validator.is_float("123.45"))     # True
print(Validator.is_float("123"))       # False

# 验证正数
print(Validator.is_positive("10"))     # True
print(Validator.is_positive("-10"))    # False

# 验证负数
print(Validator.is_negative("-10"))    # True
print(Validator.is_negative("10"))     # False

# 验证非负数
print(Validator.is_non_negative("10"))  # True
print(Validator.is_non_negative("0"))   # True
print(Validator.is_non_negative("-10")) # False
```

### 空值验证

```python
# 验证空值
print(Validator.is_empty(None))        # True
print(Validator.is_empty(""))          # True
print(Validator.is_empty("   "))        # True
print(Validator.is_empty([]))           # True
print(Validator.is_empty({}))           # True
print(Validator.is_empty("hello"))      # False
print(Validator.is_empty([1, 2, 3]))    # False
print(Validator.is_empty({"a": 1}))     # False

# 验证非空值
print(Validator.is_not_empty("hello"))  # True
print(Validator.is_not_empty([]))       # False
```

### 字符串验证

```python
# 验证字符串长度
print(Validator.is_length_between("hello", 3, 10))  # True
print(Validator.is_length_between("hi", 3, 10))      # False
print(Validator.is_length_equal("hello", 5))          # True
print(Validator.is_length_less_than("hello", 10))     # True
print(Validator.is_length_greater_than("hello", 3))   # True

# 验证字符串格式
print(Validator.is_alpha("hello"))         # True
print(Validator.is_alpha("hello123"))      # False
print(Validator.is_alphanumeric("hello123")) # True
print(Validator.is_alphanumeric("hello-123")) # False
print(Validator.is_digit("123"))            # True
print(Validator.is_digit("123.45"))         # False
print(Validator.is_lowercase("hello"))       # True
print(Validator.is_lowercase("Hello"))       # False
print(Validator.is_uppercase("HELLO"))       # True
print(Validator.is_uppercase("Hello"))       # False
print(Validator.is_titlecase("Hello World")) # True
print(Validator.is_titlecase("hello world")) # False
```

### 集合验证

```python
# 验证列表长度
print(Validator.is_list_length_between([1, 2, 3], 1, 5))  # True
print(Validator.is_list_length_equal([1, 2, 3], 3))        # True

# 验证字典长度
print(Validator.is_dict_length_between({"a": 1, "b": 2}, 1, 5))  # True
print(Validator.is_dict_length_equal({"a": 1, "b": 2}, 2))        # True
```

## 高级功能

### 自定义验证规则

```python
# 使用自定义正则表达式验证
print(Validator.matches_regex("123-456-7890", r"^\d{3}-\d{3}-\d{4}$"))  # True
print(Validator.matches_regex("1234567890", r"^\d{3}-\d{3}-\d{4}$"))    # False

# 使用自定义验证函数
def is_even_number(value):
    try:
        return int(value) % 2 == 0
    except:
        return False

print(Validator.validate_with_function("4", is_even_number))  # True
print(Validator.validate_with_function("5", is_even_number))  # False
```

### 复合验证

```python
# 验证字符串是否为有效的邮箱且长度小于50
email = "user@example.com"
is_valid = Validator.is_email(email) and Validator.is_length_less_than(email, 50)
print(f"邮箱验证: {is_valid}")

# 验证手机号是否为中国大陆手机号且非空
phone = "13812345678"
is_valid = Validator.is_not_empty(phone) and Validator.is_phone(phone)
print(f"手机号验证: {is_valid}")
```

### 密码强度验证

```python
# 验证密码强度
def is_strong_password(password):
    """验证密码强度：至少8个字符，包含字母和数字"""
    if not Validator.is_length_greater_than(password, 7):
        return False
    if not Validator.has_letters(password):
        return False
    if not Validator.has_digits(password):
        return False
    return True

print(is_strong_password("password123"))  # True
print(is_strong_password("password"))     # False（缺少数字）
print(is_strong_password("12345678"))     # False（缺少字母）
print(is_strong_password("pass123"))      # False（长度不足）
```

### 身份证号验证

```python
# 验证中国大陆身份证号
def is_chinese_id_card(id_card):
    """验证中国大陆身份证号：18位，最后一位可以是X"""
    pattern = r"^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]$"
    return Validator.matches_regex(id_card, pattern)

print(is_chinese_id_card("110101199001011234"))  # True
print(is_chinese_id_card("11010119900101123X"))  # True
print(is_chinese_id_card("11010119900101123"))   # False（长度不足）
print(is_chinese_id_card("1101011990010112345")) # False（长度过长）
```

## 实用工具方法

### 字符串检查

```python
# 检查字符串是否包含字母
print(Validator.has_letters("hello123"))  # True
print(Validator.has_letters("123456"))    # False

# 检查字符串是否包含数字
print(Validator.has_digits("hello123"))  # True
print(Validator.has_digits("hello"))      # False

# 检查字符串是否包含特殊字符
print(Validator.has_special_chars("hello@123"))  # True
print(Validator.has_special_chars("hello123"))    # False

# 检查字符串是否包含空格
print(Validator.has_spaces("hello world"))  # True
print(Validator.has_spaces("helloworld"))    # False
```

### 数值范围检查

```python
# 检查数值是否在范围内
print(Validator.is_between(5, 1, 10))   # True
print(Validator.is_between(15, 1, 10))  # False

# 检查数值是否大于
print(Validator.is_greater_than(10, 5))  # True
print(Validator.is_greater_than(5, 10))   # False

# 检查数值是否小于
print(Validator.is_less_than(5, 10))  # True
print(Validator.is_less_than(10, 5))   # False

# 检查数值是否等于
print(Validator.is_equal(5, 5))   # True
print(Validator.is_equal(5, 10))  # False
```

## 与其他模块集成

### 与 Config 模块集成

```python
from btools import Config, Validator

# 加载配置
config = Config("config.yaml")

# 验证配置值
email = config.get("user.email")
if email and Validator.is_email(email):
    print(f"邮箱有效: {email}")
else:
    print("邮箱无效或未设置")

phone = config.get("user.phone")
if phone and Validator.is_phone(phone):
    print(f"手机号有效: {phone}")
else:
    print("手机号无效或未设置")
```

### 与 TestUtils 模块集成

```python
from btools import TestUtils, Validator

# 生成测试数据
test_data = TestUtils.generate_test_data({
    "username": "${random_string}",
    "email": "${random_email}",
    "phone": "${random_phone}"
})

# 验证生成的数据
print(f"用户名有效: {Validator.is_not_empty(test_data['username'])}")
print(f"邮箱有效: {Validator.is_email(test_data['email'])}")
print(f"手机号有效: {Validator.is_phone(test_data['phone'])}")
```

## 常见问题

### 类型转换问题

`Validator` 类的方法通常接受字符串输入。如果需要验证其他类型的数据，建议先转换为字符串：

```python
# 验证整数
print(Validator.is_number(str(123)))  # True

# 验证浮点数
print(Validator.is_number(str(123.45)))  # True
```

### 正则表达式性能

对于复杂的正则表达式，验证可能会比较慢。建议：

1. 使用简单的验证方法优先
2. 对于频繁验证的模式，考虑编译正则表达式
3. 避免使用过于复杂的正则表达式

### 国际化支持

`Validator` 类的某些方法（如 `is_phone`、`is_chinese_id_card`）是针对特定地区的。对于国际化应用，可能需要根据地区调整验证规则。

### 自定义验证规则

对于复杂的验证场景，可以组合使用 `Validator` 的方法，或者使用 `validate_with_function` 方法创建自定义验证函数。