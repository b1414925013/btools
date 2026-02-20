"""邮件模板工具类"""
from typing import Dict, Optional, List
import os
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
