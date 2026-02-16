# MailUtils 使用指南

`MailUtils` 是一个邮件工具类，提供了丰富的邮件操作方法，包括邮件验证、邮件解析等功能。

## 功能特性

- 验证邮箱格式
- 解析邮箱地址

## 基本用法

### 导入

```python
from btools import MailUtils
```

### 示例

#### 验证邮箱格式

```python
# 验证邮箱格式
print(MailUtils.validate_email("test@example.com"))  # 输出: True
print(MailUtils.validate_email("test@"))  # 输出: False
print(MailUtils.validate_email("testexample.com"))  # 输出: False
```

#### 解析邮箱地址

```python
# 解析邮箱地址
email = "Test User <test@example.com>"
name, address = MailUtils.parse_email(email)
print(f"Name: {name}")  # 输出: Name: Test User
print(f"Address: {address}")  # 输出: Address: test@example.com

# 解析只有地址的邮箱
email = "test@example.com"
name, address = MailUtils.parse_email(email)
print(f"Name: {name}")  # 输出: Name: None
print(f"Address: {address}")  # 输出: Address: test@example.com
```

## 高级用法

### 批量验证邮箱

```python
# 批量验证邮箱
emails = ["test1@example.com", "test2@", "test3example.com", "test4@example.com"]
for email in emails:
    print(f"{email}: {MailUtils.validate_email(email)}")
    # 输出:
    # test1@example.com: True
    # test2@: False
    # test3example.com: False
    # test4@example.com: True
```

### 批量解析邮箱

```python
# 批量解析邮箱
emails = [
    "Test User 1 <test1@example.com>",
    "Test User 2 <test2@example.com>",
    "test3@example.com"
]
for email in emails:
    name, address = MailUtils.parse_email(email)
    print(f"Email: {email}")
    print(f"  Name: {name}")
    print(f"  Address: {address}")
    # 输出:
    # Email: Test User 1 <test1@example.com>
    #   Name: Test User 1
    #   Address: test1@example.com
    # Email: Test User 2 <test2@example.com>
    #   Name: Test User 2
    #   Address: test2@example.com
    # Email: test3@example.com
    #   Name: None
    #   Address: test3@example.com
```

## 注意事项

1. `validate_email()` 方法使用正则表达式验证邮箱格式，可能无法覆盖所有有效的邮箱格式，但可以验证大多数常见的邮箱格式。

## 总结

`MailUtils` 提供了基本的邮件操作功能，简化了邮件处理的复杂度，使代码更加简洁易读。无论是基本的邮箱验证还是高级的邮箱解析，`MailUtils` 都能满足你的需求。