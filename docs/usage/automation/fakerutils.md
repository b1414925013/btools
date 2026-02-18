# FakerUtils 使用指南

`FakerUtils` 类提供了类似于Faker库的测试数据生成功能，支持生成各种类型的测试数据，包括基础类型、个人信息、企业信息、金融信息、网络信息等。

## 基本使用

### 导入方式

```python
# 方式一：通过类名使用
from btools import FakerUtils

# 方式二：使用便捷函数
from btools import (
    random_string, random_integer, random_float, random_boolean,
    random_date, random_datetime, random_email, random_phone,
    random_name, random_address, random_company, random_position,
    random_id_card, random_bank_card, random_ip, random_url,
    random_user_agent, random_credit_card, random_user,
    random_product, random_order, generate_test_data
)
```

## 基础数据类型生成

### 生成随机字符串

```python
from btools import random_string

# 生成默认长度(10)的随机字符串
str1 = random_string()
print(f"随机字符串: {str1}")

# 生成指定长度的随机字符串
str2 = random_string(20)
print(f"20位随机字符串: {str2}")

# 生成包含特殊字符的随机字符串
str3 = random_string(15, include_special=True)
print(f"包含特殊字符的字符串: {str3}")
```

### 生成随机整数

```python
from btools import random_integer

# 生成默认范围(0-1000)的随机整数
num1 = random_integer()
print(f"随机整数: {num1}")

# 生成指定范围的随机整数
num2 = random_integer(1, 100)
print(f"1-100之间的随机整数: {num2}")
```

### 生成随机浮点数

```python
from btools import random_float

# 生成默认范围(0.0-1000.0)和小数位数(2)的随机浮点数
float1 = random_float()
print(f"随机浮点数: {float1}")

# 生成指定范围和小数位数的随机浮点数
float2 = random_float(1.0, 10.0, 3)
print(f"1.0-10.0之间3位小数的浮点数: {float2}")
```

### 生成随机布尔值

```python
from btools import random_boolean

bool_val = random_boolean()
print(f"随机布尔值: {bool_val}")
```

### 生成随机日期

```python
from btools import random_date
import datetime

# 生成默认范围(1970-01-01到今天)的随机日期
date1 = random_date()
print(f"随机日期: {date1}")

# 生成指定范围的随机日期
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2023, 12, 31)
date2 = random_date(start_date, end_date)
print(f"2020-2023年间的随机日期: {date2}")
```

### 生成随机日期时间

```python
from btools import random_datetime
import datetime

# 生成默认范围(1970-01-01到现在)的随机日期时间
dt1 = random_datetime()
print(f"随机日期时间: {dt1}")

# 生成指定范围的随机日期时间
start_dt = datetime.datetime(2023, 1, 1, 0, 0, 0)
end_dt = datetime.datetime(2023, 12, 31, 23, 59, 59)
dt2 = random_datetime(start_dt, end_dt)
print(f"2023年间的随机日期时间: {dt2}")
```

## 个人信息生成

### 生成随机姓名

```python
from btools import random_name

name = random_name()
print(f"随机姓名: {name}")
```

### 生成随机邮箱

```python
from btools import random_email

# 生成随机域名的邮箱
email1 = random_email()
print(f"随机邮箱: {email1}")

# 生成指定域名的邮箱
email2 = random_email('test.com')
print(f"指定域名邮箱: {email2}")
```

### 生成随机手机号

```python
from btools import random_phone

# 生成随机前缀的手机号
phone1 = random_phone()
print(f"随机手机号: {phone1}")

# 生成指定前缀的手机号
phone2 = random_phone('138')
print(f"138开头的手机号: {phone2}")
```

### 生成随机地址

```python
from btools import random_address

address = random_address()
print(f"随机地址: {address}")
```

### 生成随机身份证号

```python
from btools import random_id_card

id_card = random_id_card()
print(f"随机身份证号: {id_card}")
```

## 企业信息生成

### 生成随机公司名称

```python
from btools import random_company

company = random_company()
print(f"随机公司名称: {company}")
```

### 生成随机职位

```python
from btools import random_position

position = random_position()
print(f"随机职位: {position}")
```

## 金融信息生成

### 生成随机银行卡号

```python
from btools import random_bank_card

bank_card = random_bank_card()
print(f"随机银行卡号: {bank_card}")
```

### 生成随机信用卡信息

```python
from btools import random_credit_card

credit_card = random_credit_card()
print(f"信用卡信息: {credit_card}")
# 输出示例: {'number': '6222021234567890', 'expiry': '12/26', 'cvv': '123'}
```

## 网络信息生成

### 生成随机IP地址

```python
from btools import random_ip

ip = random_ip()
print(f"随机IP地址: {ip}")
```

### 生成随机URL

```python
from btools import random_url

url = random_url()
print(f"随机URL: {url}")
```

### 生成随机User-Agent

```python
from btools import random_user_agent

user_agent = random_user_agent()
print(f"随机User-Agent: {user_agent}")
```

## 复合信息生成

### 生成随机用户信息

```python
from btools import random_user

user = random_user()
print(f"用户信息: {user}")
# 输出包含: name, email, phone, address, company, position, id_card, bank_card, ip
```

### 生成随机产品信息

```python
from btools import random_product

product = random_product()
print(f"产品信息: {product}")
# 输出包含: name, price, stock, sku, category, description
```

### 生成随机订单信息

```python
from btools import random_order

order = random_order()
print(f"订单信息: {order}")
# 输出包含: order_id, user_id, total_amount, order_time, status, payment_method
```

## 模板生成测试数据

### 根据模板生成测试数据

```python
from btools import generate_test_data

template = {
    "name": "name",
    "email": "email",
    "phone": "phone",
    "age": "integer",
    "salary": "float",
    "active": "boolean",
    "address": "address",
    "company": "company",
    "position": "position",
    "id_card": "id_card",
    "bank_card": "bank_card",
    "ip": "ip",
    "url": "url",
    "user_agent": "user_agent",
    "date": "date",
    "datetime": "datetime",
    "user": "user",
    "product": "product",
    "order": "order"
}

data = generate_test_data(template)
print(f"生成的测试数据: {data}")
```

### 模板支持的数据类型

| 类型 | 描述 |
|------|------|
| string | 随机字符串 |
| integer | 随机整数 |
| float | 随机浮点数 |
| boolean | 随机布尔值 |
| email | 随机邮箱 |
| phone | 随机手机号 |
| name | 随机姓名 |
| address | 随机地址 |
| company | 随机公司名称 |
| position | 随机职位 |
| id_card | 随机身份证号 |
| bank_card | 随机银行卡号 |
| ip | 随机IP地址 |
| url | 随机URL |
| user_agent | 随机User-Agent |
| date | 随机日期(字符串格式) |
| datetime | 随机日期时间(字符串格式) |
| user | 随机用户信息(字典) |
| product | 随机产品信息(字典) |
| order | 随机订单信息(字典) |

## 使用FakerUtils类

如果需要通过类名使用所有方法，可以直接使用FakerUtils类：

```python
from btools import FakerUtils

# 使用类方法
name = FakerUtils.random_name()
email = FakerUtils.random_email()
phone = FakerUtils.random_phone()

# 使用模板生成
template = {"name": "name", "email": "email"}
data = FakerUtils.generate_test_data(template)

print(f"{name}, {email}, {phone}")
print(f"模板数据: {data}")
```

## 与测试框架集成

### 与unittest集成

```python
import unittest
from btools import random_user, random_product

class TestUserRegistration(unittest.TestCase):
    def test_user_creation(self):
        """测试用户创建"""
        user = random_user()
        print(f"测试用户: {user}")
        self.assertIsNotNone(user['name'])
        self.assertIsNotNone(user['email'])
        self.assertIsNotNone(user['phone'])
    
    def test_product_order(self):
        """测试产品订单"""
        product = random_product()
        order = random_order()
        print(f"产品: {product}")
        print(f"订单: {order}")
        self.assertIsNotNone(product['sku'])
        self.assertIsNotNone(order['order_id'])

if __name__ == '__main__':
    unittest.main()
```

### 与pytest集成

```python
import pytest
from btools import random_user, random_email, random_phone

@pytest.fixture
def test_user():
    """测试用户数据"""
    return random_user()

@pytest.fixture
def test_contacts():
    """生成多个联系人"""
    contacts = []
    for _ in range(5):
        contacts.append({
            "email": random_email(),
            "phone": random_phone()
        })
    return contacts

def test_user_valid(test_user):
    """测试用户数据有效性"""
    assert test_user['name'] is not None
    assert '@' in test_user['email']
    assert len(test_user['phone']) == 11

def test_contacts_count(test_contacts):
    """测试联系人数目"""
    assert len(test_contacts) == 5
    for contact in test_contacts:
        assert '@' in contact['email']
```

## 常见使用场景

### 数据库测试数据填充

```python
from btools import random_user, random_product, random_order
import sqlite3

# 连接数据库
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT
    )
''')

# 插入测试用户数据
for _ in range(10):
    user = random_user()
    cursor.execute(
        'INSERT INTO users (name, email, phone) VALUES (?, ?, ?)',
        (user['name'], user['email'], user['phone'])
    )

conn.commit()
conn.close()
print("测试数据已插入数据库")
```

### API测试数据生成

```python
from btools import random_user, generate_test_data
import requests

# 生成用户注册数据
template = {
    "username": "name",
    "email": "email",
    "password": "string",
    "phone": "phone"
}
register_data = generate_test_data(template)

# 发送注册请求
response = requests.post(
    'https://api.example.com/register',
    json=register_data
)
print(f"注册请求数据: {register_data}")
print(f"响应状态码: {response.status_code}")
```

## 常见问题

### Q: 如何生成更多不同类型的测试数据？

A: 可以通过组合不同的生成方法来创建自定义的数据结构，例如：

```python
from btools import random_name, random_email, random_integer, random_date

custom_data = {
    "profile": {
        "name": random_name(),
        "email": random_email(),
        "age": random_integer(18, 65)
    },
    "registration_date": random_date().strftime("%Y-%m-%d")
}
print(custom_data)
```

### Q: 身份证号是否是真实有效的？

A: 当前生成的身份证号是模拟格式的，用于测试数据填充，不具备真实的校验码。如果需要真实的校验算法，可以扩展该功能。

### Q: 如何生成大量的测试数据？

A: 可以使用循环批量生成：

```python
from btools import random_user

users = [random_user() for _ in range(100)]
print(f"已生成 {len(users)} 个用户数据")
```
