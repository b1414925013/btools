"""邮件工具类"""
import smtplib
import poplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr, formataddr
from typing import Any, Optional, List, Dict


class MailUtils:
    """邮件工具类"""

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
            msg['From'] = MailUtils._format_addr(from_addr)
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
                        attachment.add_header('Content-Disposition', 'attachment', filename=Header(attachment_path.split('/')[-1], 'utf-8').encode())
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
        except Exception:
            return False

    @staticmethod
    def receive_email_pop3(
        pop_server: str,
        pop_port: int,
        username: str,
        password: str,
        mail_count: int = 10,
        use_ssl: bool = True
    ) -> List[Dict[str, Any]]:
        """
        使用POP3接收邮件
        
        Args:
            pop_server: POP3服务器
            pop_port: POP3端口
            username: 用户名
            password: 密码
            mail_count: 邮件数量
            use_ssl: 是否使用SSL
            
        Returns:
            List[Dict[str, Any]]: 邮件列表
        """
        emails = []
        try:
            # 连接POP3服务器
            if use_ssl:
                server = poplib.POP3_SSL(pop_server, pop_port)
            else:
                server = poplib.POP3(pop_server, pop_port)

            # 登录
            server.user(username)
            server.pass_(password)

            # 获取邮件数量
            resp, mails, octets = server.list()
            mail_total = len(mails)
            start_index = max(1, mail_total - mail_count + 1)

            # 读取邮件
            for i in range(start_index, mail_total + 1):
                resp, lines, octets = server.retr(i)
                msg_content = b'\r\n'.join(lines).decode('utf-8', errors='ignore')
                # 解析邮件内容
                # 这里简化处理，实际应该使用email模块解析
                emails.append({
                    'index': i,
                    'content': msg_content
                })

            server.quit()
        except Exception:
            pass
        return emails

    @staticmethod
    def receive_email_imap(
        imap_server: str,
        imap_port: int,
        username: str,
        password: str,
        folder: str = 'INBOX',
        mail_count: int = 10,
        use_ssl: bool = True
    ) -> List[Dict[str, Any]]:
        """
        使用IMAP接收邮件
        
        Args:
            imap_server: IMAP服务器
            imap_port: IMAP端口
            username: 用户名
            password: 密码
            folder: 邮箱文件夹
            mail_count: 邮件数量
            use_ssl: 是否使用SSL
            
        Returns:
            List[Dict[str, Any]]: 邮件列表
        """
        emails = []
        try:
            # 连接IMAP服务器
            if use_ssl:
                server = imaplib.IMAP4_SSL(imap_server, imap_port)
            else:
                server = imaplib.IMAP4(imap_server, imap_port)

            # 登录
            server.login(username, password)

            # 选择文件夹
            server.select(folder)

            # 搜索邮件
            typ, data = server.search(None, 'ALL')
            mail_ids = data[0].split()
            start_index = max(0, len(mail_ids) - mail_count)
            recent_mail_ids = mail_ids[start_index:]

            # 读取邮件
            for mail_id in recent_mail_ids:
                typ, data = server.fetch(mail_id, '(RFC822)')
                msg_content = data[0][1].decode('utf-8', errors='ignore')
                # 解析邮件内容
                # 这里简化处理，实际应该使用email模块解析
                emails.append({
                    'id': mail_id.decode(),
                    'content': msg_content
                })

            server.logout()
        except Exception:
            pass
        return emails

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

        return MailUtils.send_email(
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
    def create_html_email(
        template: str,
        variables: Dict[str, Any]
    ) -> str:
        """
        创建HTML邮件
        
        Args:
            template: HTML模板
            variables: 变量字典
            
        Returns:
            str: HTML邮件内容
        """
        html_content = template
        for key, value in variables.items():
            html_content = html_content.replace(f'{{{{{key}}}}}', str(value))
        return html_content

    @staticmethod
    def validate_email_format(email: str) -> bool:
        """
        验证邮箱格式
        
        Args:
            email: 邮箱地址
            
        Returns:
            bool: 如果邮箱格式正确则返回True，否则返回False
        """
        from btools.core.data.regexutils import RegexUtils
        return RegexUtils.validate_email(email)

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
    def get_pop_server(domain: str) -> Optional[str]:
        """
        根据域名获取POP服务器
        
        Args:
            domain: 域名
            
        Returns:
            Optional[str]: POP服务器地址
        """
        pop_servers = {
            'qq.com': 'pop.qq.com',
            '163.com': 'pop.163.com',
            '126.com': 'pop.126.com',
            'gmail.com': 'pop.gmail.com',
            'outlook.com': 'pop.outlook.com',
            'hotmail.com': 'pop.hotmail.com',
            'sina.com': 'pop.sina.com',
            'sohu.com': 'pop.sohu.com'
        }
        return pop_servers.get(domain.lower())

    @staticmethod
    def get_imap_server(domain: str) -> Optional[str]:
        """
        根据域名获取IMAP服务器
        
        Args:
            domain: 域名
            
        Returns:
            Optional[str]: IMAP服务器地址
        """
        imap_servers = {
            'qq.com': 'imap.qq.com',
            '163.com': 'imap.163.com',
            '126.com': 'imap.126.com',
            'gmail.com': 'imap.gmail.com',
            'outlook.com': 'imap.outlook.com',
            'hotmail.com': 'imap.hotmail.com',
            'sina.com': 'imap.sina.com',
            'sohu.com': 'imap.sohu.com'
        }
        return imap_servers.get(domain.lower())