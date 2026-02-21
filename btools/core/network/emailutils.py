"""邮件工具类"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr, formataddr
from typing import List, Dict, Optional, Any
import os
import concurrent.futures
from jinja2 import Template, Environment, FileSystemLoader


class EmailTemplateUtils:
    """邮件模板管理工具类
    
    用于管理邮件模板，生成HTML邮件内容
    """

    @staticmethod
    def create_html_template(content: str) -> Template:
        """
        创建HTML邮件模板
        
        Args:
            content: HTML模板内容
            
        Returns:
            Template: Jinja2模板对象
        """
        return Template(content)

    @staticmethod
    def render_template(template: Template, variables: Dict[str, any]) -> str:
        """
        渲染邮件模板
        
        Args:
            template: Jinja2模板对象
            variables: 模板变量字典
            
        Returns:
            str: 渲染后的HTML内容
        """
        return template.render(**variables)

    @staticmethod
    def render_template_string(template_str: str, variables: Dict[str, any]) -> str:
        """
        渲染模板字符串
        
        Args:
            template_str: 模板字符串
            variables: 模板变量字典
            
        Returns:
            str: 渲染后的内容
        """
        template = Template(template_str)
        return template.render(**variables)

    @staticmethod
    def load_template_from_file(file_path: str) -> Template:
        """
        从文件加载模板
        
        Args:
            file_path: 模板文件路径
            
        Returns:
            Template: Jinja2模板对象
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return Template(content)

    @staticmethod
    def load_template_from_directory(directory: str, template_name: str) -> Template:
        """
        从目录加载模板
        
        Args:
            directory: 模板目录
            template_name: 模板文件名
            
        Returns:
            Template: Jinja2模板对象
        """
        env = Environment(loader=FileSystemLoader(directory))
        return env.get_template(template_name)

    @staticmethod
    def create_basic_html_template() -> str:
        """
        创建基本的HTML邮件模板
        
        Returns:
            str: 基本HTML模板
        """
        return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            background-color: #f5f5f5;
            padding: 10px;
            border-bottom: 1px solid #ddd;
            margin-bottom: 20px;
        }
        .content {
            margin-bottom: 20px;
        }
        .footer {
            background-color: #f5f5f5;
            padding: 10px;
            border-top: 1px solid #ddd;
            margin-top: 20px;
            font-size: 12px;
            color: #666;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{ title }}</h1>
    </div>
    <div class="content">
        {{ content }}
    </div>
    <div class="footer">
        <p>{{ footer }}</p>
    </div>
</body>
</html>
        """

    @staticmethod
    def create_notification_template() -> str:
        """
        创建通知邮件模板
        
        Returns:
            str: 通知邮件模板
        """
        return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{{ subject }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        .notification {
            max-width: 500px;
            margin: 20px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .notification-header {
            background-color: #f8f9fa;
            padding: 10px;
            border-bottom: 1px solid #ddd;
            margin-bottom: 15px;
        }
        .notification-content {
            margin-bottom: 15px;
        }
        .notification-footer {
            font-size: 12px;
            color: #666;
            border-top: 1px solid #ddd;
            padding-top: 10px;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="notification">
        <div class="notification-header">
            <h2>{{ subject }}</h2>
        </div>
        <div class="notification-content">
            {{ message }}
        </div>
        <div class="notification-footer">
            <p>此邮件为系统自动发送，请勿回复。</p>
            <p>发送时间: {{ timestamp }}</p>
        </div>
    </div>
</body>
</html>
        """

    @staticmethod
    def create_welcome_template() -> str:
        """
        创建欢迎邮件模板
        
        Returns:
            str: 欢迎邮件模板
        """
        return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>欢迎使用 {{ service_name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        .welcome {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .welcome-header {
            background-color: #e3f2fd;
            padding: 20px;
            border-bottom: 1px solid #bbdefb;
            margin-bottom: 20px;
            text-align: center;
        }
        .welcome-content {
            margin-bottom: 20px;
        }
        .welcome-footer {
            font-size: 12px;
            color: #666;
            border-top: 1px solid #ddd;
            padding-top: 10px;
            margin-top: 20px;
        }
        .cta-button {
            display: inline-block;
            padding: 12px 24px;
            background-color: #2196f3;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <div class="welcome">
        <div class="welcome-header">
            <h1>欢迎，{{ username }}！</h1>
        </div>
        <div class="welcome-content">
            <p>感谢您注册使用 {{ service_name }}！</p>
            <p>您的账号已成功创建，以下是您的账号信息：</p>
            <ul>
                <li>用户名: {{ username }}</li>
                <li>邮箱: {{ email }}</li>
                <li>注册时间: {{ registration_date }}</li>
            </ul>
            <p>点击下方按钮开始使用我们的服务：</p>
            <a href="{{ service_url }}" class="cta-button">立即开始</a>
        </div>
        <div class="welcome-footer">
            <p>如有任何问题，请联系我们的客服团队。</p>
            <p>&copy; {{ year }} {{ service_name }}</p>
        </div>
    </div>
</body>
</html>
        """

    @staticmethod
    def create_password_reset_template() -> str:
        """
        创建密码重置邮件模板
        
        Returns:
            str: 密码重置邮件模板
        """
        return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>密码重置</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        .reset {
            max-width: 500px;
            margin: 20px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .reset-header {
            background-color: #fff3cd;
            padding: 10px;
            border-bottom: 1px solid #ffeaa7;
            margin-bottom: 15px;
        }
        .reset-content {
            margin-bottom: 15px;
        }
        .reset-footer {
            font-size: 12px;
            color: #666;
            border-top: 1px solid #ddd;
            padding-top: 10px;
            margin-top: 15px;
        }
        .reset-button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #dc3545;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="reset">
        <div class="reset-header">
            <h2>密码重置请求</h2>
        </div>
        <div class="reset-content">
            <p>亲爱的 {{ username }}：</p>
            <p>我们收到了您的密码重置请求。请点击下方按钮重置您的密码：</p>
            <a href="{{ reset_url }}" class="reset-button">重置密码</a>
            <p>此链接将在 {{ expiry_time }} 内失效。</p>
            <p>如果您没有发起此请求，请忽略此邮件。</p>
        </div>
        <div class="reset-footer">
            <p>此邮件为系统自动发送，请勿回复。</p>
        </div>
    </div>
</body>
</html>
        """

    @staticmethod
    def save_template(template_content: str, file_path: str) -> None:
        """
        保存模板到文件
        
        Args:
            template_content: 模板内容
            file_path: 文件路径
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(template_content)

    @staticmethod
    def load_template(file_path: str) -> Template:
        """
        从文件加载模板
        
        Args:
            file_path: 文件路径
            
        Returns:
            Template: Jinja2模板对象
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return Template(content)

    @staticmethod
    def validate_template(template_str: str) -> bool:
        """
        验证模板语法
        
        Args:
            template_str: 模板字符串
            
        Returns:
            bool: 模板语法是否正确
        """
        try:
            Template(template_str)
            return True
        except Exception:
            return False


class EmailSenderUtils:
    """邮件发送工具类
    
    用于发送邮件，支持批量发送、附件处理等功能
    """

    @staticmethod
    def _format_addr(s: str) -> str:
        """
        格式化邮件地址
        
        Args:
            s: 邮件地址字符串
            
        Returns:
            str: 格式化后的邮件地址
        """
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    @staticmethod
    def send_email(
        smtp_server: str,
        smtp_port: int,
        from_addr: str,
        password: str,
        to_addrs: List[str],
        subject: str,
        content: str,
        content_type: str = 'plain',
        cc_addrs: Optional[List[str]] = None,
        bcc_addrs: Optional[List[str]] = None,
        attachments: Optional[List[str]] = None,
        images: Optional[Dict[str, str]] = None,
        use_ssl: bool = True
    ) -> bool:
        """
        发送邮件
        
        Args:
            smtp_server: SMTP服务器
            smtp_port: SMTP端口
            from_addr: 发件人地址
            password: 发件人密码或授权码
            to_addrs: 收件人地址列表
            subject: 邮件主题
            content: 邮件内容
            content_type: 内容类型（plain或html）
            cc_addrs: 抄送地址列表
            bcc_addrs: 密送地址列表
            attachments: 附件路径列表
            images: 内嵌图片字典，键为图片ID，值为图片路径
            use_ssl: 是否使用SSL
            
        Returns:
            bool: 如果发送成功则返回True，否则返回False
        """
        try:
            # 创建邮件
            msg = MIMEMultipart()
            msg['From'] = EmailSenderUtils._format_addr(from_addr)
            msg['To'] = ', '.join(to_addrs)
            if cc_addrs:
                msg['Cc'] = ', '.join(cc_addrs)
            msg['Subject'] = Header(subject, 'utf-8').encode()

            # 添加正文
            msg.attach(MIMEText(content, content_type, 'utf-8'))

            # 添加内嵌图片
            if images:
                for img_id, img_path in images.items():
                    with open(img_path, 'rb') as f:
                        img_data = f.read()
                    img = MIMEImage(img_data)
                    img.add_header('Content-ID', f'<{img_id}>')
                    msg.attach(img)

            # 添加附件
            if attachments:
                for attachment_path in attachments:
                    with open(attachment_path, 'rb') as f:
                        attachment = MIMEApplication(f.read())
                        filename = os.path.basename(attachment_path)
                        attachment.add_header('Content-Disposition', 'attachment', 
                                           filename=Header(filename, 'utf-8').encode())
                        msg.attach(attachment)

            # 连接SMTP服务器
            if use_ssl:
                server = smtplib.SMTP_SSL(smtp_server, smtp_port)
            else:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()

            # 登录并发送邮件
            server.login(from_addr, password)
            all_recipients = to_addrs.copy()
            if cc_addrs:
                all_recipients.extend(cc_addrs)
            if bcc_addrs:
                all_recipients.extend(bcc_addrs)
            server.sendmail(from_addr, all_recipients, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"邮件发送失败: {str(e)}")
            return False

    @staticmethod
    def send_email_simple(
        smtp_server: str,
        from_addr: str,
        password: str,
        to_addr: str,
        subject: str,
        content: str
    ) -> bool:
        """
        发送简单邮件
        
        Args:
            smtp_server: SMTP服务器
            from_addr: 发件人地址
            password: 发件人密码或授权码
            to_addr: 收件人地址
            subject: 邮件主题
            content: 邮件内容
            
        Returns:
            bool: 如果发送成功则返回True，否则返回False
        """
        # 自动选择端口和SSL设置
        if 'smtp.qq.com' in smtp_server:
            smtp_port = 465
            use_ssl = True
        elif 'smtp.163.com' in smtp_server:
            smtp_port = 465
            use_ssl = True
        elif 'smtp.gmail.com' in smtp_server:
            smtp_port = 465
            use_ssl = True
        else:
            smtp_port = 25
            use_ssl = False

        return EmailSenderUtils.send_email(
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            from_addr=from_addr,
            password=password,
            to_addrs=[to_addr],
            subject=subject,
            content=content,
            use_ssl=use_ssl
        )

    @staticmethod
    def send_batch_emails(
        smtp_server: str,
        smtp_port: int,
        from_addr: str,
        password: str,
        emails: List[Dict[str, Any]],
        use_ssl: bool = True,
        max_workers: int = 5
    ) -> Dict[str, bool]:
        """
        批量发送邮件
        
        Args:
            smtp_server: SMTP服务器
            smtp_port: SMTP端口
            from_addr: 发件人地址
            password: 发件人密码或授权码
            emails: 邮件列表，每个邮件包含to_addrs, subject, content等字段
            use_ssl: 是否使用SSL
            max_workers: 最大工作线程数
            
        Returns:
            Dict[str, bool]: 每个收件人地址的发送结果
        """
        results = {}

        def send_single_email(email_info):
            to_addrs = email_info.get('to_addrs', [])
            subject = email_info.get('subject', '')
            content = email_info.get('content', '')
            content_type = email_info.get('content_type', 'plain')
            cc_addrs = email_info.get('cc_addrs', None)
            bcc_addrs = email_info.get('bcc_addrs', None)
            attachments = email_info.get('attachments', None)
            images = email_info.get('images', None)

            success = EmailSenderUtils.send_email(
                smtp_server=smtp_server,
                smtp_port=smtp_port,
                from_addr=from_addr,
                password=password,
                to_addrs=to_addrs,
                subject=subject,
                content=content,
                content_type=content_type,
                cc_addrs=cc_addrs,
                bcc_addrs=bcc_addrs,
                attachments=attachments,
                images=images,
                use_ssl=use_ssl
            )

            for addr in to_addrs:
                results[addr] = success

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(send_single_email, emails)

        return results

    @staticmethod
    def send_template_email(
        smtp_server: str,
        smtp_port: int,
        from_addr: str,
        password: str,
        to_addrs: List[str],
        subject: str,
        template_content: str,
        variables: Dict[str, Any],
        content_type: str = 'html',
        cc_addrs: Optional[List[str]] = None,
        bcc_addrs: Optional[List[str]] = None,
        attachments: Optional[List[str]] = None,
        use_ssl: bool = True
    ) -> bool:
        """
        发送模板邮件
        
        Args:
            smtp_server: SMTP服务器
            smtp_port: SMTP端口
            from_addr: 发件人地址
            password: 发件人密码或授权码
            to_addrs: 收件人地址列表
            subject: 邮件主题
            template_content: 模板内容
            variables: 模板变量
            content_type: 内容类型
            cc_addrs: 抄送地址列表
            bcc_addrs: 密送地址列表
            attachments: 附件路径列表
            use_ssl: 是否使用SSL
            
        Returns:
            bool: 如果发送成功则返回True，否则返回False
        """
        # 使用EmailTemplateUtils渲染模板
        rendered_content = EmailTemplateUtils.render_template_string(
            template_content, variables
        )

        return EmailSenderUtils.send_email(
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            from_addr=from_addr,
            password=password,
            to_addrs=to_addrs,
            subject=subject,
            content=rendered_content,
            content_type=content_type,
            cc_addrs=cc_addrs,
            bcc_addrs=bcc_addrs,
            attachments=attachments,
            use_ssl=use_ssl
        )

    @staticmethod
    def send_html_email(
        smtp_server: str,
        smtp_port: int,
        from_addr: str,
        password: str,
        to_addrs: List[str],
        subject: str,
        html_content: str,
        cc_addrs: Optional[List[str]] = None,
        bcc_addrs: Optional[List[str]] = None,
        attachments: Optional[List[str]] = None,
        use_ssl: bool = True
    ) -> bool:
        """
        发送HTML邮件
        
        Args:
            smtp_server: SMTP服务器
            smtp_port: SMTP端口
            from_addr: 发件人地址
            password: 发件人密码或授权码
            to_addrs: 收件人地址列表
            subject: 邮件主题
            html_content: HTML内容
            cc_addrs: 抄送地址列表
            bcc_addrs: 密送地址列表
            attachments: 附件路径列表
            use_ssl: 是否使用SSL
            
        Returns:
            bool: 如果发送成功则返回True，否则返回False
        """
        return EmailSenderUtils.send_email(
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            from_addr=from_addr,
            password=password,
            to_addrs=to_addrs,
            subject=subject,
            content=html_content,
            content_type='html',
            cc_addrs=cc_addrs,
            bcc_addrs=bcc_addrs,
            attachments=attachments,
            use_ssl=use_ssl
        )

    @staticmethod
    def send_email_with_attachment(
        smtp_server: str,
        smtp_port: int,
        from_addr: str,
        password: str,
        to_addrs: List[str],
        subject: str,
        content: str,
        attachment_paths: List[str],
        use_ssl: bool = True
    ) -> bool:
        """
        发送带附件的邮件
        
        Args:
            smtp_server: SMTP服务器
            smtp_port: SMTP端口
            from_addr: 发件人地址
            password: 发件人密码或授权码
            to_addrs: 收件人地址列表
            subject: 邮件主题
            content: 邮件内容
            attachment_paths: 附件路径列表
            use_ssl: 是否使用SSL
            
        Returns:
            bool: 如果发送成功则返回True，否则返回False
        """
        return EmailSenderUtils.send_email(
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            from_addr=from_addr,
            password=password,
            to_addrs=to_addrs,
            subject=subject,
            content=content,
            attachments=attachment_paths,
            use_ssl=use_ssl
        )

    @staticmethod
    def get_smtp_server(domain: str) -> Optional[str]:
        """
        根据域名获取SMTP服务器
        
        Args:
            domain: 域名
            
        Returns:
            Optional[str]: SMTP服务器地址
        """
        smtp_servers = {
            'qq.com': 'smtp.qq.com',
            '163.com': 'smtp.163.com',
            '126.com': 'smtp.126.com',
            'gmail.com': 'smtp.gmail.com',
            'outlook.com': 'smtp.office365.com',
            'hotmail.com': 'smtp.office365.com',
            'sina.com': 'smtp.sina.com',
            'sohu.com': 'smtp.sohu.com'
        }
        return smtp_servers.get(domain.lower())

    @staticmethod
    def validate_email_config(
        smtp_server: str,
        smtp_port: int,
        from_addr: str,
        password: str,
        use_ssl: bool = True
    ) -> bool:
        """
        验证邮件配置
        
        Args:
            smtp_server: SMTP服务器
            smtp_port: SMTP端口
            from_addr: 发件人地址
            password: 发件人密码或授权码
            use_ssl: 是否使用SSL
            
        Returns:
            bool: 配置是否有效
        """
        try:
            if use_ssl:
                server = smtplib.SMTP_SSL(smtp_server, smtp_port)
            else:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()

            server.login(from_addr, password)
            server.quit()
            return True
        except Exception:
            return False

    @staticmethod
    def send_test_email(
        smtp_server: str,
        smtp_port: int,
        from_addr: str,
        password: str,
        test_to_addr: str,
        use_ssl: bool = True
    ) -> bool:
        """
        发送测试邮件
        
        Args:
            smtp_server: SMTP服务器
            smtp_port: SMTP端口
            from_addr: 发件人地址
            password: 发件人密码或授权码
            test_to_addr: 测试收件人地址
            use_ssl: 是否使用SSL
            
        Returns:
            bool: 测试是否成功
        """
        subject = "邮件配置测试"
        content = "这是一封测试邮件，用于验证邮件配置是否正确。"

        return EmailSenderUtils.send_email(
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            from_addr=from_addr,
            password=password,
            to_addrs=[test_to_addr],
            subject=subject,
            content=content,
            use_ssl=use_ssl
        )
