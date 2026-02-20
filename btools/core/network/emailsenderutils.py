"""邮件发送工具类"""
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
        # 渲染模板
        rendered_content = template_content
        for key, value in variables.items():
            rendered_content = rendered_content.replace(f'{{{{{key}}}}}', str(value))

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
