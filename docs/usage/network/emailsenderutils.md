# EmailSenderUtils 邮件发送工具类

`EmailSenderUtils` 是 BTools 提供的邮件发送工具类，用于发送邮件，支持批量发送、附件处理等功能。

## 功能特性

- 发送普通文本邮件和HTML邮件
- 支持抄送（CC）和密送（BCC）
- 支持添加附件和内嵌图片
- 批量发送邮件（多线程）
- 发送模板邮件
- 自动选择SMTP服务器端口和SSL设置
- 验证邮件配置有效性
- 发送测试邮件

## 使用示例

### 1. 发送简单邮件

```python
from btools.core.network.emailsenderutils import EmailSenderUtils

# 发送简单邮件
result = EmailSenderUtils.send_email_simple(
    smtp_server="smtp.qq.com",
    from_addr="your_email@qq.com",
    password="your_authorization_code",  # QQ邮箱需要使用授权码
    to_addr="recipient@example.com",
    subject="测试邮件",
    content="这是一封测试邮件"
)

print(f"邮件发送{'成功' if result else '失败'}")
```

### 2. 发送HTML邮件

```python
from btools.core.network.emailsenderutils import EmailSenderUtils

# HTML邮件内容
html_content = """
<!DOCTYPE html>
<html>
<body>
    <h1>Hello!</h1>
    <p>这是一封 <b>HTML</b> 测试邮件。</p>
    <p>来自 BTools</p>
</body>
</html>
"""

# 发送HTML邮件
result = EmailSenderUtils.send_html_email(
    smtp_server="smtp.qq.com",
    smtp_port=465,
    from_addr="your_email@qq.com",
    password="your_authorization_code",
    to_addrs=["recipient1@example.com", "recipient2@example.com"],
    subject="HTML测试邮件",
    html_content=html_content
)

print(f"邮件发送{'成功' if result else '失败'}")
```

### 3. 发送带附件的邮件

```python
from btools.core.network.emailsenderutils import EmailSenderUtils

# 发送带附件的邮件
result = EmailSenderUtils.send_email_with_attachment(
    smtp_server="smtp.qq.com",
    smtp_port=465,
    from_addr="your_email@qq.com",
    password="your_authorization_code",
    to_addrs=["recipient@example.com"],
    subject="带附件的测试邮件",
    content="这是一封带附件的测试邮件",
    attachment_paths=["path/to/file1.txt", "path/to/file2.pdf"]
)

print(f"邮件发送{'成功' if result else '失败'}")
```

### 4. 发送模板邮件

```python
from btools.core.network.emailsenderutils import EmailSenderUtils
from btools.core.network.emailtemplateutils import EmailTemplateUtils

# 获取欢迎模板
welcome_template = EmailTemplateUtils.create_welcome_template()

# 模板变量
variables = {
    "username": "John",
    "service_name": "BTools",
    "email": "john@example.com",
    "registration_date": "2024-01-01",
    "service_url": "https://btools.example.com",
    "year": "2024"
}

# 发送模板邮件
result = EmailSenderUtils.send_template_email(
    smtp_server="smtp.qq.com",
    smtp_port=465,
    from_addr="your_email@qq.com",
    password="your_authorization_code",
    to_addrs=["john@example.com"],
    subject="欢迎使用 BTools",
    template_content=welcome_template,
    variables=variables,
    content_type="html"
)

print(f"邮件发送{'成功' if result else '失败'}")
```

### 5. 批量发送邮件

```python
from btools.core.network.emailsenderutils import EmailSenderUtils

# 准备邮件列表
emails = [
    {
        "to_addrs": ["user1@example.com"],
        "subject": "通知：系统更新",
        "content": "系统将于明天进行更新维护",
        "content_type": "plain"
    },
    {
        "to_addrs": ["user2@example.com"],
        "subject": "通知：系统更新",
        "content": "系统将于明天进行更新维护",
        "content_type": "plain"
    },
    {
        "to_addrs": ["user3@example.com"],
        "subject": "通知：系统更新",
        "content": "系统将于明天进行更新维护",
        "content_type": "plain"
    }
]

# 批量发送邮件（使用5个线程）
results = EmailSenderUtils.send_batch_emails(
    smtp_server="smtp.qq.com",
    smtp_port=465,
    from_addr="your_email@qq.com",
    password="your_authorization_code",
    emails=emails,
    max_workers=5
)

# 打印发送结果
for email, success in results.items():
    print(f"向 {email} 发送邮件{'成功' if success else '失败'}")
```

### 6. 验证邮件配置

```python
from btools.core.network.emailsenderutils import EmailSenderUtils

# 验证邮件配置
is_valid = EmailSenderUtils.validate_email_config(
    smtp_server="smtp.qq.com",
    smtp_port=465,
    from_addr="your_email@qq.com",
    password="your_authorization_code"
)

print(f"邮件配置{'有效' if is_valid else '无效'}")
```

### 7. 发送测试邮件

```python
from btools.core.network.emailsenderutils import EmailSenderUtils

# 发送测试邮件（用于验证配置）
result = EmailSenderUtils.send_test_email(
    smtp_server="smtp.qq.com",
    smtp_port=465,
    from_addr="your_email@qq.com",
    password="your_authorization_code",
    test_to_addr="your_email@qq.com"  # 发送给自己
)

print(f"测试邮件发送{'成功' if result else '失败'}")
```

### 8. 获取SMTP服务器

```python
from btools.core.network.emailsenderutils import EmailSenderUtils

# 根据域名获取SMTP服务器
smtp_server = EmailSenderUtils.get_smtp_server("qq.com")
print(f"QQ邮箱的SMTP服务器: {smtp_server}")  # 输出: smtp.qq.com

smtp_server = EmailSenderUtils.get_smtp_server("163.com")
print(f"163邮箱的SMTP服务器: {smtp_server}")  # 输出: smtp.163.com
```

## API 文档

### 核心方法

#### `send_email(smtp_server: str, smtp_port: int, from_addr: str, password: str, to_addrs: List[str], subject: str, content: str, content_type: str = 'plain', cc_addrs: Optional[List[str]] = None, bcc_addrs: Optional[List[str]] = None, attachments: Optional[List[str]] = None, images: Optional[Dict[str, str]] = None, use_ssl: bool = True) -> bool`
发送邮件

- **参数**：
  - `smtp_server` - SMTP服务器
  - `smtp_port` - SMTP端口
  - `from_addr` - 发件人地址
  - `password` - 发件人密码或授权码
  - `to_addrs` - 收件人地址列表
  - `subject` - 邮件主题
  - `content` - 邮件内容
  - `content_type` - 内容类型（plain或html）
  - `cc_addrs` - 抄送地址列表
  - `bcc_addrs` - 密送地址列表
  - `attachments` - 附件路径列表
  - `images` - 内嵌图片字典，键为图片ID，值为图片路径
  - `use_ssl` - 是否使用SSL
- **返回**：如果发送成功则返回True，否则返回False

#### `send_email_simple(smtp_server: str, from_addr: str, password: str, to_addr: str, subject: str, content: str) -> bool`
发送简单邮件

- **参数**：
  - `smtp_server` - SMTP服务器
  - `from_addr` - 发件人地址
  - `password` - 发件人密码或授权码
  - `to_addr` - 收件人地址
  - `subject` - 邮件主题
  - `content` - 邮件内容
- **返回**：如果发送成功则返回True，否则返回False

#### `send_html_email(smtp_server: str, smtp_port: int, from_addr: str, password: str, to_addrs: List[str], subject: str, html_content: str, cc_addrs: Optional[List[str]] = None, bcc_addrs: Optional[List[str]] = None, attachments: Optional[List[str]] = None, use_ssl: bool = True) -> bool`
发送HTML邮件

- **参数**：
  - `smtp_server` - SMTP服务器
  - `smtp_port` - SMTP端口
  - `from_addr` - 发件人地址
  - `password` - 发件人密码或授权码
  - `to_addrs` - 收件人地址列表
  - `subject` - 邮件主题
  - `html_content` - HTML内容
  - `cc_addrs` - 抄送地址列表
  - `bcc_addrs` - 密送地址列表
  - `attachments` - 附件路径列表
  - `use_ssl` - 是否使用SSL
- **返回**：如果发送成功则返回True，否则返回False

#### `send_email_with_attachment(smtp_server: str, smtp_port: int, from_addr: str, password: str, to_addrs: List[str], subject: str, content: str, attachment_paths: List[str], use_ssl: bool = True) -> bool`
发送带附件的邮件

- **参数**：
  - `smtp_server` - SMTP服务器
  - `smtp_port` - SMTP端口
  - `from_addr` - 发件人地址
  - `password` - 发件人密码或授权码
  - `to_addrs` - 收件人地址列表
  - `subject` - 邮件主题
  - `content` - 邮件内容
  - `attachment_paths` - 附件路径列表
  - `use_ssl` - 是否使用SSL
- **返回**：如果发送成功则返回True，否则返回False

#### `send_template_email(smtp_server: str, smtp_port: int, from_addr: str, password: str, to_addrs: List[str], subject: str, template_content: str, variables: Dict[str, Any], content_type: str = 'html', cc_addrs: Optional[List[str]] = None, bcc_addrs: Optional[List[str]] = None, attachments: Optional[List[str]] = None, use_ssl: bool = True) -> bool`
发送模板邮件

- **参数**：
  - `smtp_server` - SMTP服务器
  - `smtp_port` - SMTP端口
  - `from_addr` - 发件人地址
  - `password` - 发件人密码或授权码
  - `to_addrs` - 收件人地址列表
  - `subject` - 邮件主题
  - `template_content` - 模板内容
  - `variables` - 模板变量
  - `content_type` - 内容类型
  - `cc_addrs` - 抄送地址列表
  - `bcc_addrs` - 密送地址列表
  - `attachments` - 附件路径列表
  - `use_ssl` - 是否使用SSL
- **返回**：如果发送成功则返回True，否则返回False

#### `send_batch_emails(smtp_server: str, smtp_port: int, from_addr: str, password: str, emails: List[Dict[str, Any]], use_ssl: bool = True, max_workers: int = 5) -> Dict[str, bool]`
批量发送邮件

- **参数**：
  - `smtp_server` - SMTP服务器
  - `smtp_port` - SMTP端口
  - `from_addr` - 发件人地址
  - `password` - 发件人密码或授权码
  - `emails` - 邮件列表，每个邮件包含to_addrs, subject, content等字段
  - `use_ssl` - 是否使用SSL
  - `max_workers` - 最大工作线程数
- **返回**：每个收件人地址的发送结果

#### `validate_email_config(smtp_server: str, smtp_port: int, from_addr: str, password: str, use_ssl: bool = True) -> bool`
验证邮件配置

- **参数**：
  - `smtp_server` - SMTP服务器
  - `smtp_port` - SMTP端口
  - `from_addr` - 发件人地址
  - `password` - 发件人密码或授权码
  - `use_ssl` - 是否使用SSL
- **返回**：配置是否有效

#### `send_test_email(smtp_server: str, smtp_port: int, from_addr: str, password: str, test_to_addr: str, use_ssl: bool = True) -> bool`
发送测试邮件

- **参数**：
  - `smtp_server` - SMTP服务器
  - `smtp_port` - SMTP端口
  - `from_addr` - 发件人地址
  - `password` - 发件人密码或授权码
  - `test_to_addr` - 测试收件人地址
  - `use_ssl` - 是否使用SSL
- **返回**：测试是否成功

#### `get_smtp_server(domain: str) -> Optional[str]`
根据域名获取SMTP服务器

- **参数**：`domain` - 域名
- **返回**：SMTP服务器地址

## 依赖项

- **smtplib**：Python标准库，用于发送邮件
- **email**：Python标准库，用于构建邮件内容
- **concurrent.futures**：Python标准库，用于多线程批量发送

## 注意事项

1. **授权码**：某些邮箱（如QQ邮箱、163邮箱）需要使用授权码而不是登录密码发送邮件
2. **SSL设置**：大部分现代邮箱服务器都要求使用SSL连接
3. **端口设置**：常见的SMTP端口：
   - QQ邮箱：465（SSL）
   - 163邮箱：465（SSL）
   - Gmail：465（SSL）
   - 企业邮箱：根据邮件服务商提供的信息
4. **批量发送**：批量发送邮件时，建议控制发送速度，避免被邮件服务器视为垃圾邮件
5. **附件大小**：不同的邮件服务器对附件大小有不同的限制
6. **反垃圾邮件**：确保邮件内容符合反垃圾邮件规则，避免使用敏感词汇
7. **错误处理**：发送邮件可能会遇到网络问题、认证失败等错误，建议在实际应用中添加适当的错误处理

## 常见问题

### Q: 邮件发送失败，提示认证失败
A: 请检查以下几点：
- 用户名和密码（授权码）是否正确
- 是否开启了SMTP服务
- 是否使用了正确的端口和SSL设置

### Q: 批量发送邮件时部分失败
A: 可能的原因：
- 邮件服务器限制了发送频率
- 部分收件人邮箱地址无效
- 网络不稳定

### Q: 邮件被标记为垃圾邮件
A: 建议：
- 确保邮件内容正规，避免使用敏感词汇
- 添加退订链接（如果是批量发送）
- 确保发件人地址真实有效
- 建立良好的发信信誉
