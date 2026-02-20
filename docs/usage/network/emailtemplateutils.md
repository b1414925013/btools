# EmailTemplateUtils 邮件模板工具类

`EmailTemplateUtils` 是 BTools 提供的邮件模板管理工具类，用于创建、管理和渲染邮件模板，生成HTML邮件内容。

## 功能特性

- 创建和管理邮件模板
- 支持 Jinja2 模板引擎
- 提供多种预设邮件模板
- 从文件加载模板
- 模板渲染和变量替换
- 模板语法验证

## 预设模板

- **基本HTML模板**：通用HTML邮件模板
- **通知邮件模板**：系统通知邮件模板
- **欢迎邮件模板**：用户注册欢迎邮件模板
- **密码重置模板**：密码重置请求邮件模板

## 使用示例

### 1. 创建和渲染模板

```python
from btools.core.network.emailtemplateutils import EmailTemplateUtils

# 创建HTML模板
template_content = """
<!DOCTYPE html>
<html>
<body>
    <h1>Hello {{ name }}!</h1>
    <p>Welcome to {{ service }}.</p>
</body>
</html>
"""

# 渲染模板
variables = {"name": "John", "service": "BTools"}
rendered_html = EmailTemplateUtils.render_template_string(template_content, variables)
print(rendered_html)
```

### 2. 使用预设模板

```python
from btools.core.network.emailtemplateutils import EmailTemplateUtils

# 获取基本HTML模板
basic_template = EmailTemplateUtils.create_basic_html_template()

# 渲染模板
variables = {
    "title": "测试邮件",
    "content": "这是一封测试邮件内容",
    "footer": "© 2024 BTools"
}
rendered_html = EmailTemplateUtils.render_template_string(basic_template, variables)
print(rendered_html)
```

### 3. 使用通知模板

```python
from btools.core.network.emailtemplateutils import EmailTemplateUtils

# 获取通知模板
notification_template = EmailTemplateUtils.create_notification_template()

# 渲染模板
variables = {
    "subject": "系统通知",
    "message": "您的任务已完成",
    "timestamp": "2024-01-01 12:00:00"
}
rendered_html = EmailTemplateUtils.render_template_string(notification_template, variables)
print(rendered_html)
```

### 4. 使用欢迎模板

```python
from btools.core.network.emailtemplateutils import EmailTemplateUtils

# 获取欢迎模板
welcome_template = EmailTemplateUtils.create_welcome_template()

# 渲染模板
variables = {
    "username": "John",
    "service_name": "BTools",
    "email": "john@example.com",
    "registration_date": "2024-01-01",
    "service_url": "https://btools.example.com",
    "year": "2024"
}
rendered_html = EmailTemplateUtils.render_template_string(welcome_template, variables)
print(rendered_html)
```

### 5. 使用密码重置模板

```python
from btools.core.network.emailtemplateutils import EmailTemplateUtils

# 获取密码重置模板
reset_template = EmailTemplateUtils.create_password_reset_template()

# 渲染模板
variables = {
    "username": "John",
    "reset_url": "https://btools.example.com/reset-password?token=123456",
    "expiry_time": "24小时"
}
rendered_html = EmailTemplateUtils.render_template_string(reset_template, variables)
print(rendered_html)
```

### 6. 从文件加载模板

```python
from btools.core.network.emailtemplateutils import EmailTemplateUtils

# 保存模板到文件
template_content = "<h1>{{ title }}</h1><p>{{ content }}</p>"
EmailTemplateUtils.save_template(template_content, "templates/email_template.html")

# 从文件加载模板
template = EmailTemplateUtils.load_template("templates/email_template.html")

# 渲染模板
variables = {"title": "测试邮件", "content": "这是一封测试邮件"}
rendered_html = EmailTemplateUtils.render_template(template, variables)
print(rendered_html)
```

### 7. 验证模板语法

```python
from btools.core.network.emailtemplateutils import EmailTemplateUtils

# 验证有效的模板
valid_template = "Hello {{ name }}"
is_valid = EmailTemplateUtils.validate_template(valid_template)
print(f"模板是否有效: {is_valid}")  # 输出: True

# 验证无效的模板
invalid_template = "Hello {{ name"  # 缺少结束标记
is_valid = EmailTemplateUtils.validate_template(invalid_template)
print(f"模板是否有效: {is_valid}")  # 输出: False
```

## API 文档

### 核心方法

#### `create_html_template(content: str) -> Template`
创建HTML邮件模板

- **参数**：`content` - HTML模板内容
- **返回**：Jinja2模板对象

#### `render_template(template: Template, variables: Dict[str, any]) -> str`
渲染邮件模板

- **参数**：
  - `template` - Jinja2模板对象
  - `variables` - 模板变量字典
- **返回**：渲染后的HTML内容

#### `render_template_string(template_str: str, variables: Dict[str, any]) -> str`
渲染模板字符串

- **参数**：
  - `template_str` - 模板字符串
  - `variables` - 模板变量字典
- **返回**：渲染后的内容

#### `load_template_from_file(file_path: str) -> Template`
从文件加载模板

- **参数**：`file_path` - 模板文件路径
- **返回**：Jinja2模板对象

#### `save_template(template_content: str, file_path: str) -> None`
保存模板到文件

- **参数**：
  - `template_content` - 模板内容
  - `file_path` - 文件路径

#### `validate_template(template_str: str) -> bool`
验证模板语法

- **参数**：`template_str` - 模板字符串
- **返回**：模板语法是否正确

### 预设模板方法

#### `create_basic_html_template() -> str`
创建基本的HTML邮件模板

- **返回**：基本HTML模板字符串

#### `create_notification_template() -> str`
创建通知邮件模板

- **返回**：通知邮件模板字符串

#### `create_welcome_template() -> str`
创建欢迎邮件模板

- **返回**：欢迎邮件模板字符串

#### `create_password_reset_template() -> str`
创建密码重置邮件模板

- **返回**：密码重置邮件模板字符串

## 依赖项

- **jinja2**：用于模板渲染和管理

## 注意事项

1. 模板中的变量使用双大括号 `{{ variable }}` 表示
2. 复杂模板建议使用文件存储，便于维护
3. 发送渲染后的HTML邮件时，建议使用 `EmailSenderUtils` 类
4. 对于大量邮件发送，建议使用批量发送功能以提高效率
