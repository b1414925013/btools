# EmailUtils 使用指南

## 简介

EmailUtils 是 BTools 中的邮件处理工具，包含两个主要类：

- **EmailTemplateUtils**：邮件模板管理工具，用于创建和渲染邮件模板
- **EmailSenderUtils**：邮件发送工具，用于发送各种类型的邮件

## 安装依赖

```bash
pip install -r requirements.txt
```

主要依赖：
- `jinja2`：用于模板渲染
- `email`：Python 标准库，用于邮件构建
- `smtplib`：Python 标准库，用于邮件发送

## EmailTemplateUtils 使用

### 1. 创建和渲染模板

```python
from btools.core.network.emailutils import EmailTemplateUtils

# 创建模板
template = EmailTemplateUtils.create_html_template('''
<html>
<body>
    <h1>Hello {{ name }}!</h1>
    <p>Welcome to our service.</p>
</body>
</html>
''')

# 渲染模板
variables = {'name': 'John'}
html_content = EmailTemplateUtils.render_template(template, variables)
print(html_content)

# 直接渲染模板字符串
html_content = EmailTemplateUtils.render_template_string(
    '<h1>Hello {{ name }}!</h1>',
    {'name': 'John'}
)
```

### 2. 使用内置模板

```python
from btools.core.network.emailutils import EmailTemplateUtils

# 创建基本HTML模板
basic_template = EmailTemplateUtils.create_basic_html_template()

# 创建通知模板
notification_template = EmailTemplateUtils.create_notification_template()

# 创建欢迎邮件模板
welcome_template = EmailTemplateUtils.create_welcome_template()

# 创建密码重置模板
reset_template = EmailTemplateUtils.create_password_reset_template()
```

### 3. 模板文件操作

```python
from btools.core.network.emailutils import EmailTemplateUtils

# 保存模板到文件
template_content = EmailTemplateUtils.create_basic_html_template()
EmailTemplateUtils.save_template(template_content, 'templates/basic.html')

# 加载模板
from jinja2 import Template
template: Template = EmailTemplateUtils.load_template('templates/basic.html')

# 验证模板语法
is_valid = EmailTemplateUtils.validate_template('''
<html>
<body>
    <h1>Hello {{ name }}!</h1>
</body>
</html>
''')
print(f"Template is valid: {is_valid}")
```

### 4. 从目录加载模板

```python
from btools.core.network.emailutils import EmailTemplateUtils

# 从目录加载模板
template = EmailTemplateUtils.load_template_from_directory(
    'templates',
    'welcome.html'
)

# 渲染模板
content = EmailTemplateUtils.render_template(template, {'name': 'John'})
```

## EmailSenderUtils 使用

### 1. 发送简单邮件

```python
from btools.core.network.emailutils import EmailSenderUtils

# 发送简单邮件
success = EmailSenderUtils.send_email_simple(
    smtp_server='smtp.qq.com',
    from_addr='your_email@qq.com',
    password='your_authorization_code',  # 注意：使用授权码而不是密码
    to_addr='recipient@example.com',
    subject='Test Email',
    content='This is a test email.'
)

print(f"Email sent: {success}")
```

### 2. 发送详细邮件

```python
from btools.core.network.emailutils import EmailSenderUtils

# 发送带附件和图片的邮件
success = EmailSenderUtils.send_email(
    smtp_server='smtp.qq.com',
    smtp_port=465,
    from_addr='your_email@qq.com',
    password='your_authorization_code',
    to_addrs=['recipient1@example.com', 'recipient2@example.com'],
    subject='Email with Attachments',
    content='Please find the attached files.',
    content_type='plain',
    cc_addrs=['cc@example.com'],
    bcc_addrs=['bcc@example.com'],
    attachments=['path/to/file1.pdf', 'path/to/file2.txt'],
    images={'logo': 'path/to/logo.png'},
    use_ssl=True
)

print(f"Email sent: {success}")
```

### 3. 发送HTML邮件

```python
from btools.core.network.emailutils import EmailSenderUtils, EmailTemplateUtils

# 创建HTML内容
template = EmailTemplateUtils.create_basic_html_template()
html_content = EmailTemplateUtils.render_template(template, {
    'title': 'Welcome Email',
    'content': '<p>Hello!</p><p>Welcome to our service.</p>',
    'footer': 'Best regards, BTools Team'
})

# 发送HTML邮件
success = EmailSenderUtils.send_html_email(
    smtp_server='smtp.qq.com',
    smtp_port=465,
    from_addr='your_email@qq.com',
    password='your_authorization_code',
    to_addrs=['recipient@example.com'],
    subject='Welcome Email',
    html_content=html_content,
    use_ssl=True
)
```

### 4. 发送模板邮件

```python
from btools.core.network.emailutils import EmailSenderUtils, EmailTemplateUtils

# 获取模板
welcome_template = EmailTemplateUtils.create_welcome_template()

# 发送模板邮件
success = EmailSenderUtils.send_template_email(
    smtp_server='smtp.qq.com',
    smtp_port=465,
    from_addr='your_email@qq.com',
    password='your_authorization_code',
    to_addrs=['user@example.com'],
    subject='Welcome to BTools',
    template_content=welcome_template,
    variables={
        'username': 'John',
        'service_name': 'BTools',
        'service_url': 'https://btools.example.com',
        'registration_date': '2024-01-01',
        'year': '2024'
    },
    use_ssl=True
)
```

### 5. 批量发送邮件

```python
from btools.core.network.emailutils import EmailSenderUtils

# 准备邮件列表
emails = [
    {
        'to_addrs': ['user1@example.com'],
        'subject': 'Hello User 1',
        'content': 'This is email for user 1',
        'content_type': 'plain'
    },
    {
        'to_addrs': ['user2@example.com'],
        'subject': 'Hello User 2',
        'content': 'This is email for user 2',
        'content_type': 'plain'
    }
]

# 批量发送
results = EmailSenderUtils.send_batch_emails(
    smtp_server='smtp.qq.com',
    smtp_port=465,
    from_addr='your_email@qq.com',
    password='your_authorization_code',
    emails=emails,
    use_ssl=True,
    max_workers=3  # 并发发送
)

# 查看结果
for email, success in results.items():
    print(f"{email}: {'Success' if success else 'Failed'}")
```

### 6. 发送带附件的邮件

```python
from btools.core.network.emailutils import EmailSenderUtils

# 发送带附件的邮件
success = EmailSenderUtils.send_email_with_attachment(
    smtp_server='smtp.qq.com',
    smtp_port=465,
    from_addr='your_email@qq.com',
    password='your_authorization_code',
    to_addrs=['recipient@example.com'],
    subject='Email with Attachments',
    content='Please find the attached files.',
    attachment_paths=['path/to/report.pdf', 'path/to/data.xlsx'],
    use_ssl=True
)
```

### 7. 配置验证

```python
from btools.core.network.emailutils import EmailSenderUtils

# 验证邮件配置
is_valid = EmailSenderUtils.validate_email_config(
    smtp_server='smtp.qq.com',
    smtp_port=465,
    from_addr='your_email@qq.com',
    password='your_authorization_code',
    use_ssl=True
)

print(f"Email configuration is valid: {is_valid}")

# 发送测试邮件
if is_valid:
    test_success = EmailSenderUtils.send_test_email(
        smtp_server='smtp.qq.com',
        smtp_port=465,
        from_addr='your_email@qq.com',
        password='your_authorization_code',
        test_to_addr='your_email@qq.com',
        use_ssl=True
    )
    print(f"Test email sent: {test_success}")
```

### 8. 获取SMTP服务器

```python
from btools.core.network.emailutils import EmailSenderUtils

# 根据域名获取SMTP服务器
smtp_server = EmailSenderUtils.get_smtp_server('qq.com')
print(f"SMTP server for qq.com: {smtp_server}")  # 输出: smtp.qq.com

smtp_server = EmailSenderUtils.get_smtp_server('gmail.com')
print(f"SMTP server for gmail.com: {smtp_server}")  # 输出: smtp.gmail.com
```

## 高级用法：模板+发送组合

```python
from btools.core.network.emailutils import EmailTemplateUtils, EmailSenderUtils

# 1. 创建模板
welcome_template = EmailTemplateUtils.create_welcome_template()

# 2. 准备邮件数据
email_data = {
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 465,
    'from_addr': 'your_email@qq.com',
    'password': 'your_authorization_code',
    'to_addrs': ['new_user@example.com'],
    'subject': 'Welcome to Our Service',
    'template_content': welcome_template,
    'variables': {
        'username': 'New User',
        'service_name': 'MyService',
        'service_url': 'https://myservice.com',
        'registration_date': '2024-01-01',
        'year': '2024'
    }
}

# 3. 发送模板邮件
success = EmailSenderUtils.send_template_email(**email_data)
print(f"Welcome email sent: {success}")
```

## 常见问题

### 1. SMTP服务器配置

| 邮箱服务 | SMTP服务器 | 端口 | SSL |
|---------|-----------|------|-----|
| QQ邮箱 | smtp.qq.com | 465 | 是 |
| 163邮箱 | smtp.163.com | 465 | 是 |
| Gmail | smtp.gmail.com | 465 | 是 |
| Outlook | smtp.office365.com | 587 | 是 |

### 2. 授权码获取

- **QQ邮箱**：设置 → 账户 → 开启SMTP服务 → 获取授权码
- **163邮箱**：设置 → POP3/SMTP/IMAP → 开启SMTP服务 → 设置授权码
- **Gmail**：需要开启两步验证，然后创建应用专用密码

### 3. 常见错误

- **认证失败**：检查邮箱和授权码是否正确
- **连接超时**：检查网络连接和SMTP服务器地址
- **发送失败**：检查收件人地址是否正确，以及邮箱是否被限制发送

## 代码优化建议

1. **异常处理**：在生产环境中，建议添加详细的异常处理
2. **配置管理**：建议使用配置文件或环境变量存储邮件配置
3. **日志记录**：建议添加日志记录，便于排查问题
4. **异步发送**：对于大量邮件，建议使用异步发送方式
5. **重试机制**：建议添加发送失败的重试机制

## 输入输出示例

#### 输入输出示例

**示例1：发送简单邮件**

输入：
```python
from btools.core.network.emailutils import EmailSenderUtils

result = EmailSenderUtils.send_email_simple(
    smtp_server='smtp.qq.com',
    from_addr='your_email@qq.com',
    password='your_authorization_code',
    to_addr='friend@example.com',
    subject='Test Email',
    content='Hello, this is a test email!'
)
print(f"Email sent: {result}")
```

输出：
```
Email sent: True
```

**示例2：使用模板发送HTML邮件**

输入：
```python
from btools.core.network.emailutils import EmailTemplateUtils, EmailSenderUtils

# 创建模板
template = EmailTemplateUtils.create_html_template('''
<html>
<body style="font-family: Arial, sans-serif;">
    <div style="max-width: 600px; margin: 0 auto;">
        <h1 style="color: #333;">Order Confirmation</h1>
        <p>Hello {{ customer_name }},</p>
        <p>Thank you for your order. Your order #{{ order_id }} has been confirmed.</p>
        <p>Order details:</p>
        <ul>
            <li>Product: {{ product_name }}</li>
            <li>Quantity: {{ quantity }}</li>
            <li>Total: ${{ total }}</li>
        </ul>
        <p>Best regards,<br>Customer Service</p>
    </div>
</body>
</html>
''')

# 渲染模板
html_content = EmailTemplateUtils.render_template(template, {
    'customer_name': 'John Doe',
    'order_id': '12345',
    'product_name': 'BTools Pro',
    'quantity': 1,
    'total': 99.99
})

# 发送邮件
result = EmailSenderUtils.send_html_email(
    smtp_server='smtp.qq.com',
    smtp_port=465,
    from_addr='your_email@qq.com',
    password='your_authorization_code',
    to_addrs=['customer@example.com'],
    subject='Order Confirmation',
    html_content=html_content,
    use_ssl=True
)
print(f"Order confirmation sent: {result}")
```

输出：
```
Order confirmation sent: True
```

**示例3：批量发送通知邮件**

输入：
```python
from btools.core.network.emailutils import EmailSenderUtils, EmailTemplateUtils

# 创建通知模板
notification_template = EmailTemplateUtils.create_notification_template()

# 准备邮件数据
users = [
    {'email': 'user1@example.com', 'name': 'User 1'},
    {'email': 'user2@example.com', 'name': 'User 2'},
    {'email': 'user3@example.com', 'name': 'User 3'}
]

emails = []
for user in users:
    # 渲染模板
    content = EmailTemplateUtils.render_template_string(
        notification_template,
        {
            'subject': 'System Update Notification',
            'message': f"Hello {user['name']},\n\nWe will be performing system maintenance on 2024-01-15 from 2:00 AM to 4:00 AM.\n\nSorry for any inconvenience.",
            'timestamp': '2024-01-10 10:00:00'
        }
    )
    
    emails.append({
        'to_addrs': [user['email']],
        'subject': 'System Update Notification',
        'content': content,
        'content_type': 'html'
    })

# 批量发送
results = EmailSenderUtils.send_batch_emails(
    smtp_server='smtp.qq.com',
    smtp_port=465,
    from_addr='your_email@qq.com',
    password='your_authorization_code',
    emails=emails,
    use_ssl=True,
    max_workers=2
)

# 查看结果
for email, success in results.items():
    print(f"{email}: {'Success' if success else 'Failed'}")
```

输出：
```
user1@example.com: Success
user2@example.com: Success
user3@example.com: Success
```
