# Validator 使用指南

`Validator` 是一个数据验证工具类，提供了丰富的数据验证功能，帮助开发者更方便地验证各种类型和格式的数据，确保数据的有效性和一致性。

## 导入

```python
from btools import Validator
# 或
from btools.core import Validator
```

## 核心功能

### 常用格式验证

#### 1. 邮箱验证

```python
# 验证邮箱地址格式
email = "test@example.com"
is_valid = Validator.is_email(email)
print(f"Is valid email: {is_valid}")  # 输出: True

# 验证无效邮箱
invalid_email = "invalid-email"
is_valid = Validator.is_email(invalid_email)
print(f"Is valid email: {is_valid}")  # 输出: False

# 验证带特殊字符的邮箱
special_email = "user.name+tag@example.co.uk"
is_valid = Validator.is_email(special_email)
print(f"Is valid email: {is_valid}")  # 输出: True
```

#### 2. 手机号码验证

```python
# 验证中国大陆手机号码
phone = "13812345678"
is_valid = Validator.is_phone(phone)
print(f"Is valid phone: {is_valid}")  # 输出: True

# 验证无效手机号码
invalid_phone = "1234567890"
is_valid = Validator.is_phone(invalid_phone)
print(f"Is valid phone: {is_valid}")  # 输出: False

# 验证固定电话号码（需要自定义验证函数）
def is_landline(phone):
    """验证固定电话号码"""
    pattern = r'^0\d{2,3}-?\d{7,8}$'
    import re
    return re.match(pattern, phone) is not None

landline = "010-12345678"
is_valid = is_landline(landline)
print(f"Is valid landline: {is_valid}")  # 输出: True
```

#### 3. URL验证

```python
# 验证URL格式
url = "https://www.example.com"
is_valid = Validator.is_url(url)
print(f"Is valid URL: {is_valid}")  # 输出: True

# 验证带路径的URL
url_with_path = "https://www.example.com/path/to/page"
is_valid = Validator.is_url(url_with_path)
print(f"Is valid URL with path: {is_valid}")  # 输出: True

# 验证带查询参数的URL
url_with_query = "https://www.example.com/search?q=python"
is_valid = Validator.is_url(url_with_query)
print(f"Is valid URL with query: {is_valid}")  # 输出: True

# 验证无效URL
invalid_url = "example.com"
is_valid = Validator.is_url(invalid_url)
print(f"Is valid URL: {is_valid}")  # 输出: False
```

#### 4. IPv4地址验证

```python
# 验证IPv4地址
ip = "192.168.1.1"
is_valid = Validator.is_ipv4(ip)
print(f"Is valid IPv4: {is_valid}")  # 输出: True

# 验证无效IPv4地址
invalid_ip = "256.256.256.256"
is_valid = Validator.is_ipv4(invalid_ip)
print(f"Is valid IPv4: {is_valid}")  # 输出: False

# 验证网络保留地址
reserved_ip = "10.0.0.1"
is_valid = Validator.is_ipv4(reserved_ip)
print(f"Is valid IPv4 (reserved): {is_valid}")  # 输出: True
```

### 数据类型验证

#### 1. 数字验证

```python
# 验证是否为数字
value = "123"
is_valid = Validator.is_number(value)
print(f"Is number: {is_valid}")  # 输出: True

# 验证浮点数
value = "123.45"
is_valid = Validator.is_number(value)
print(f"Is number: {is_valid}")  # 输出: True

# 验证负数
value = "-123"
is_valid = Validator.is_number(value)
print(f"Is number: {is_valid}")  # 输出: True

# 验证无效数字
value = "abc"
is_valid = Validator.is_number(value)
print(f"Is number: {is_valid}")  # 输出: False

# 验证是否为整数
value = "123"
is_valid = Validator.is_integer(value)
print(f"Is integer: {is_valid}")  # 输出: True

# 验证是否为正数
value = "123"
is_valid = Validator.is_positive(value)
print(f"Is positive: {is_valid}")  # 输出: True

# 验证是否为负数
value = "-123"
is_valid = Validator.is_negative(value)
print(f"Is negative: {is_valid}")  # 输出: True
```

#### 2. 日期验证

```python
# 验证日期格式
 date_str = "2023-01-01"
is_valid = Validator.is_date(date_str)
print(f"Is valid date: {is_valid}")  # 输出: True

# 验证带时间的日期
 date_str = "2023-01-01 12:00:00"
is_valid = Validator.is_date(date_str, format="%Y-%m-%d %H:%M:%S")
print(f"Is valid date with time: {is_valid}")  # 输出: True

# 验证无效日期
 invalid_date = "2023-02-30"  # 2月没有30天
is_valid = Validator.is_date(invalid_date)
print(f"Is valid date: {is_valid}")  # 输出: False
```

#### 3. 空值验证

```python
# 验证是否为空
empty_values = [None, "", [], {}, set()]
for value in empty_values:
    is_empty = Validator.is_empty(value)
    print(f"{repr(value)} is empty: {is_empty}")
# 输出:
# None is empty: True
# "" is empty: True
# [] is empty: True
# {} is empty: True
# set() is empty: True

# 验证非空值
non_empty_values = ["Hello", [1, 2, 3], {"key": "value"}, {1, 2, 3}, 0, False]
for value in non_empty_values:
    is_empty = Validator.is_empty(value)
    print(f"{repr(value)} is empty: {is_empty}")
# 输出:
# "Hello" is empty: False
# [1, 2, 3] is empty: False
# {"key": "value"} is empty: False
# {1, 2, 3} is empty: False
# 0 is empty: False
# False is empty: False
```

### 长度验证

```python
# 验证字符串长度是否在指定范围内
text = "Hello"
is_valid = Validator.is_length_between(text, 3, 10)
print(f"Is length between 3 and 10: {is_valid}")  # 输出: True

# 验证长度不足
short_text = "Hi"
is_valid = Validator.is_length_between(short_text, 3, 10)
print(f"Is length between 3 and 10: {is_valid}")  # 输出: False

# 验证长度过长
long_text = "This text is too long"
is_valid = Validator.is_length_between(long_text, 3, 10)
print(f"Is length between 3 and 10: {is_valid}")  # 输出: False

# 验证列表长度
items = [1, 2, 3, 4, 5]
is_valid = len(items) >= 3 and len(items) <= 10
print(f"Is list length between 3 and 10: {is_valid}")  # 输出: True
```

## 高级用法

### 自定义验证函数

```python
# 自定义验证函数
def is_strong_password(password):
    """验证密码强度"""
    # 至少8个字符，包含至少一个大写字母，一个小写字母和一个数字
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

# 使用自定义验证函数
password = "StrongPass123"
is_valid = is_strong_password(password)
print(f"Is strong password: {is_valid}")  # 输出: True

weak_password = "weak"
is_valid = is_strong_password(weak_password)
print(f"Is strong password: {is_valid}")  # 输出: False
```

### 组合验证

```python
# 组合多个验证条件
def validate_user_registration(data):
    """验证用户注册数据"""
    errors = []
    
    # 验证用户名
    username = data.get("username")
    if Validator.is_empty(username):
        errors.append("Username is required")
    elif not Validator.is_length_between(username, 3, 20):
        errors.append("Username must be between 3 and 20 characters")
    
    # 验证邮箱
    email = data.get("email")
    if Validator.is_empty(email):
        errors.append("Email is required")
    elif not Validator.is_email(email):
        errors.append("Email format is invalid")
    
    # 验证密码
    password = data.get("password")
    if Validator.is_empty(password):
        errors.append("Password is required")
    elif len(password) < 8:
        errors.append("Password must be at least 8 characters")
    
    # 验证手机号码
    phone = data.get("phone")
    if phone and not Validator.is_phone(phone):
        errors.append("Phone number format is invalid")
    
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

# 使用组合验证
user_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "StrongPass123",
    "phone": "13812345678"
}

validation_result = validate_user_registration(user_data)
print(f"Is valid: {validation_result['is_valid']}")
print(f"Errors: {validation_result['errors']}")

# 测试无效数据
invalid_data = {
    "username": "jo",  # 太短
    "email": "invalid-email",  # 无效邮箱
    "password": "weak",  # 太短
    "phone": "1234567890"  # 无效手机号
}

validation_result = validate_user_registration(invalid_data)
print(f"Is valid: {validation_result['is_valid']}")
print(f"Errors: {validation_result['errors']}")
```

### 验证器链

```python
# 创建验证器链
class ValidationChain:
    """验证器链"""
    
    def __init__(self, value):
        self.value = value
        self.errors = []
    
    def not_empty(self, message="Value cannot be empty"):
        if Validator.is_empty(self.value):
            self.errors.append(message)
        return self
    
    def is_email(self, message="Invalid email format"):
        if not Validator.is_email(self.value):
            self.errors.append(message)
        return self
    
    def is_phone(self, message="Invalid phone format"):
        if not Validator.is_phone(self.value):
            self.errors.append(message)
        return self
    
    def min_length(self, min_len, message=None):
        if message is None:
            message = f"Value must be at least {min_len} characters"
        if len(self.value) < min_len:
            self.errors.append(message)
        return self
    
    def max_length(self, max_len, message=None):
        if message is None:
            message = f"Value must be at most {max_len} characters"
        if len(self.value) > max_len:
            self.errors.append(message)
        return self
    
    def validate(self):
        return {
            "is_valid": len(self.errors) == 0,
            "errors": self.errors
        }

# 使用验证器链
email = "test@example.com"
result = ValidationChain(email)\
    .not_empty()\
    .is_email()\
    .validate()
print(f"Email validation: {result}")

phone = "13812345678"
result = ValidationChain(phone)\
    .not_empty()\
    .is_phone()\
    .validate()
print(f"Phone validation: {result}")

username = "john"
result = ValidationChain(username)\
    .not_empty()\
    .min_length(3)\
    .max_length(20)\
    .validate()
print(f"Username validation: {result}")
```

## 性能提示

- 对于频繁的验证操作，考虑缓存验证结果，以减少重复验证的开销
- 对于复杂的验证逻辑，考虑将其封装为自定义验证函数或验证器类，以提高代码可读性和可维护性
- 对于大型数据集的验证，考虑使用生成器表达式或列表推导式，以提高性能
- 对于前端提交的数据，始终在后端进行验证，不要依赖前端验证
- 对于敏感数据的验证，考虑使用更严格的验证规则，以提高安全性

## 示例：实际应用场景

### 1. 表单验证

```python
def validate_contact_form(form_data):
    """验证联系表单数据"""
    validation_results = {
        "name": {
            "value": form_data.get("name"),
            "is_valid": not Validator.is_empty(form_data.get("name")),
            "error": "Name is required" if Validator.is_empty(form_data.get("name")) else ""
        },
        "email": {
            "value": form_data.get("email"),
            "is_valid": not Validator.is_empty(form_data.get("email")) and Validator.is_email(form_data.get("email")),
            "error": "" if (not Validator.is_empty(form_data.get("email")) and Validator.is_email(form_data.get("email"))) else "Please enter a valid email address"
        },
        "subject": {
            "value": form_data.get("subject"),
            "is_valid": not Validator.is_empty(form_data.get("subject")),
            "error": "Subject is required" if Validator.is_empty(form_data.get("subject")) else ""
        },
        "message": {
            "value": form_data.get("message"),
            "is_valid": not Validator.is_empty(form_data.get("message")) and len(form_data.get("message", "")) >= 10,
            "error": "Message must be at least 10 characters" if (Validator.is_empty(form_data.get("message")) or len(form_data.get("message", "")) < 10) else ""
        }
    }
    
    # 检查是否所有字段都有效
    is_valid = all(field["is_valid"] for field in validation_results.values())
    
    return {
        "is_valid": is_valid,
        "fields": validation_results
    }

# 使用示例
form_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "subject": "Inquiry",
    "message": "Hello, I have a question about your product."
}

validation_result = validate_contact_form(form_data)
print(f"Form is valid: {validation_result['is_valid']}")
for field_name, field_data in validation_result['fields'].items():
    print(f"{field_name}: {field_data['is_valid']} - {field_data['error']}")
```

### 2. API请求验证

```python
def validate_api_request(request_data):
    """验证API请求数据"""
    # 验证必填字段
    required_fields = ["user_id", "action", "timestamp"]
    missing_fields = [field for field in required_fields if field not in request_data]
    
    if missing_fields:
        return {
            "status": "error",
            "message": f"Missing required fields: {', '.join(missing_fields)}"
        }
    
    # 验证user_id格式
    user_id = request_data.get("user_id")
    if not isinstance(user_id, int) or user_id <= 0:
        return {
            "status": "error",
            "message": "Invalid user_id"
        }
    
    # 验证action值
    valid_actions = ["create", "update", "delete", "get"]
    action = request_data.get("action")
    if action not in valid_actions:
        return {
            "status": "error",
            "message": f"Invalid action. Valid actions are: {', '.join(valid_actions)}"
        }
    
    # 验证timestamp
    timestamp = request_data.get("timestamp")
    if not isinstance(timestamp, int) or timestamp < 0:
        return {
            "status": "error",
            "message": "Invalid timestamp"
        }
    
    # 验证可选字段
    if "email" in request_data and not Validator.is_email(request_data["email"]):
        return {
            "status": "error",
            "message": "Invalid email format"
        }
    
    if "phone" in request_data and not Validator.is_phone(request_data["phone"]):
        return {
            "status": "error",
            "message": "Invalid phone format"
        }
    
    return {
        "status": "success",
        "message": "Request is valid"
    }

# 使用示例
valid_request = {
    "user_id": 123,
    "action": "create",
    "timestamp": 1672531200,
    "email": "john@example.com",
    "phone": "13812345678"
}

response = validate_api_request(valid_request)
print(f"Valid request response: {response}")

invalid_request = {
    "user_id": "invalid",  # 无效的user_id
    "action": "invalid-action",  # 无效的action
    "timestamp": -1  # 无效的timestamp
}

response = validate_api_request(invalid_request)
print(f"Invalid request response: {response}")
```

### 3. 配置验证

```python
def validate_config(config):
    """验证配置数据"""
    errors = []
    
    # 验证服务器配置
    server_config = config.get("server", {})
    if "host" not in server_config or Validator.is_empty(server_config["host"]):
        errors.append("Server host is required")
    
    if "port" not in server_config:
        errors.append("Server port is required")
    elif not isinstance(server_config["port"], int) or server_config["port"] <= 0 or server_config["port"] > 65535:
        errors.append("Server port must be a valid port number (1-65535)")
    
    # 验证数据库配置
    db_config = config.get("database", {})
    if "url" not in db_config or Validator.is_empty(db_config["url"]):
        errors.append("Database URL is required")
    
    # 验证日志配置
    log_config = config.get("logging", {})
    valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    if "level" in log_config and log_config["level"] not in valid_log_levels:
        errors.append(f"Invalid log level. Valid levels are: {', '.join(valid_log_levels)}")
    
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

# 使用示例
valid_config = {
    "server": {
        "host": "localhost",
        "port": 8080
    },
    "database": {
        "url": "mysql://localhost:3306/db"
    },
    "logging": {
        "level": "INFO"
    }
}

validation_result = validate_config(valid_config)
print(f"Config is valid: {validation_result['is_valid']}")
print(f"Errors: {validation_result['errors']}")

invalid_config = {
    "server": {
        "host": "",  # 空主机名
        "port": 99999  # 无效端口
    },
    "logging": {
        "level": "INVALID_LEVEL"  # 无效日志级别
    }
}

validation_result = validate_config(invalid_config)
print(f"Config is valid: {validation_result['is_valid']}")
print(f"Errors: {validation_result['errors']}")
```

### 4. 数据导入验证

```python
def validate_import_data(data):
    """验证导入数据"""
    valid_records = []
    invalid_records = []
    
    for i, record in enumerate(data):
        record_errors = []
        
        # 验证必填字段
        if Validator.is_empty(record.get("name")):
            record_errors.append("Name is required")
        
        if Validator.is_empty(record.get("email")):
            record_errors.append("Email is required")
        elif not Validator.is_email(record.get("email")):
            record_errors.append("Invalid email format")
        
        if Validator.is_empty(record.get("age")):
            record_errors.append("Age is required")
        elif not Validator.is_number(record.get("age")):
            record_errors.append("Age must be a number")
        elif int(record.get("age")) < 0:
            record_errors.append("Age cannot be negative")
        
        # 验证可选字段
        if "phone" in record and record["phone"] and not Validator.is_phone(record["phone"]):
            record_errors.append("Invalid phone format")
        
        if record_errors:
            invalid_records.append({
                "index": i,
                "record": record,
                "errors": record_errors
            })
        else:
            valid_records.append(record)
    
    return {
        "valid_count": len(valid_records),
        "invalid_count": len(invalid_records),
        "valid_records": valid_records,
        "invalid_records": invalid_records
    }

# 使用示例
import_data = [
    {"name": "John Doe", "email": "john@example.com", "age": "30", "phone": "13812345678"},
    {"name": "Jane Smith", "email": "invalid-email", "age": "25"},  # 无效邮箱
    {"name": "", "email": "bob@example.com", "age": "40"},  # 空姓名
    {"name": "Alice Johnson", "email": "alice@example.com", "age": "-5"}  # 无效年龄
]

validation_result = validate_import_data(import_data)
print(f"Valid records: {validation_result['valid_count']}")
print(f"Invalid records: {validation_result['invalid_count']}")
print("\nInvalid records details:")
for record in validation_result['invalid_records']:
    print(f"Index {record['index']}: {record['errors']}")
```

## 总结

`Validator` 提供了全面的数据验证功能，从基本的邮箱、手机号码验证到复杂的自定义验证，涵盖了日常开发中大部分数据验证需求。通过合理使用这些功能，可以大大简化数据验证代码，提高代码的可读性和可维护性。

无论是表单验证、API请求验证，还是配置验证和数据导入验证，`Validator` 都能提供简洁、高效的解决方案，确保数据的有效性和一致性。