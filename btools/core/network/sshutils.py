import paramiko
import socket
import os
from typing import Optional, Dict, Any, Tuple

class SSHClient:
    """
    SSH客户端类，支持直接连接和通过跳板机连接
    
    Attributes:
        client (paramiko.SSHClient): SSH客户端实例
        jump_client (paramiko.SSHClient): 跳板机SSH客户端实例
        is_connected (bool): 是否已连接
        transport (paramiko.Transport): SSH传输实例
    """
    
    def __init__(self):
        """
        初始化SSHClient实例
        """
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.jump_client = None
        self.is_connected = False
        self.transport = None
    
    def connect(self, hostname: str, port: int = 22, username: str = None, password: str = None, 
                key_filename: str = None, timeout: int = 30, proxy_type: str = None, 
                proxy_host: str = None, proxy_port: int = None, proxy_username: str = None, 
                proxy_password: str = None):
        """
        直接连接到SSH服务器
        
        Args:
            hostname (str): 主机名或IP地址
            port (int): SSH端口，默认为22
            username (str): 用户名
            password (str): 密码
            key_filename (str): SSH密钥文件路径
            timeout (int): 超时时间（秒）
            proxy_type (str): 代理类型，可选值："socks4", "socks5", "http", "telnet", None（默认无代理）
            proxy_host (str): 代理主机名或IP地址
            proxy_port (int): 代理端口
            proxy_username (str): 代理用户名
            proxy_password (str): 代理密码
            
        Raises:
            paramiko.SSHException: SSH连接失败
            socket.timeout: 连接超时
        """
        try:
            # 处理代理设置
            sock = None
            if proxy_type:
                proxy_type = proxy_type.lower()
                if proxy_type == "socks4":
                    import socks
                    sock = socks.socksocket()
                    sock.set_proxy(socks.SOCKS4, proxy_host, proxy_port, username=proxy_username)
                    sock.settimeout(timeout)
                    sock.connect((hostname, port))
                elif proxy_type == "socks5":
                    import socks
                    sock = socks.socksocket()
                    sock.set_proxy(socks.SOCKS5, proxy_host, proxy_port, username=proxy_username, password=proxy_password)
                    sock.settimeout(timeout)
                    sock.connect((hostname, port))
                elif proxy_type == "http":
                    import httplib2
                    from urllib.parse import urlparse
                    proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}" if proxy_username else f"http://{proxy_host}:{proxy_port}"
                    http = httplib2.Http(proxy_info=urlparse(proxy_url))
                    # 这里简化处理，实际实现可能需要更复杂的HTTP代理隧道
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    sock.connect((hostname, port))
                elif proxy_type == "telnet":
                    # Telnet代理实现较为复杂，这里仅做示例
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    sock.connect((hostname, port))
            
            self.client.connect(
                hostname=hostname,
                port=port,
                username=username,
                password=password,
                key_filename=key_filename,
                timeout=timeout,
                sock=sock
            )
            
            # 获取传输实例，用于交互式shell
            self.transport = self.client.get_transport()
            self.is_connected = True
        except ImportError as e:
            if "socks" in str(e):
                raise ImportError("Please install PySocks for SOCKS proxy support: pip install PySocks")
            elif "httplib2" in str(e):
                raise ImportError("Please install httplib2 for HTTP proxy support: pip install httplib2")
            raise
        except Exception as e:
            raise
    
    def connect_via_jump(self, jump_host: str, target_host: str, jump_port: int = 22, jump_username: str = None, 
                        jump_password: str = None, jump_key_filename: str = None,
                        target_port: int = 22, target_username: str = None,
                        target_password: str = None, target_key_filename: str = None, timeout: int = 30,
                        proxy_type: str = None, proxy_host: str = None, proxy_port: int = None,
                        proxy_username: str = None, proxy_password: str = None):
        """
        通过跳板机连接到目标SSH服务器
        
        Args:
            jump_host (str): 跳板机主机名或IP地址
            target_host (str): 目标服务器主机名或IP地址
            jump_port (int): 跳板机SSH端口，默认为22
            jump_username (str): 跳板机用户名
            jump_password (str): 跳板机密码
            jump_key_filename (str): 跳板机SSH密钥文件路径
            target_port (int): 目标服务器SSH端口，默认为22
            target_username (str): 目标服务器用户名
            target_password (str): 目标服务器密码
            target_key_filename (str): 目标服务器SSH密钥文件路径
            timeout (int): 超时时间（秒）
            proxy_type (str): 代理类型，可选值："socks4", "socks5", "http", "telnet", None（默认无代理）
            proxy_host (str): 代理主机名或IP地址
            proxy_port (int): 代理端口
            proxy_username (str): 代理用户名
            proxy_password (str): 代理密码
            
        Raises:
            paramiko.SSHException: SSH连接失败
            socket.timeout: 连接超时
        """
        try:
            # 处理代理设置
            jump_sock = None
            if proxy_type:
                proxy_type = proxy_type.lower()
                if proxy_type == "socks4":
                    import socks
                    jump_sock = socks.socksocket()
                    jump_sock.set_proxy(socks.SOCKS4, proxy_host, proxy_port, username=proxy_username)
                    jump_sock.settimeout(timeout)
                    jump_sock.connect((jump_host, jump_port))
                elif proxy_type == "socks5":
                    import socks
                    jump_sock = socks.socksocket()
                    jump_sock.set_proxy(socks.SOCKS5, proxy_host, proxy_port, username=proxy_username, password=proxy_password)
                    jump_sock.settimeout(timeout)
                    jump_sock.connect((jump_host, jump_port))
                elif proxy_type == "http":
                    import httplib2
                    from urllib.parse import urlparse
                    proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}" if proxy_username else f"http://{proxy_host}:{proxy_port}"
                    http = httplib2.Http(proxy_info=urlparse(proxy_url))
                    # 这里简化处理，实际实现可能需要更复杂的HTTP代理隧道
                    jump_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    jump_sock.settimeout(timeout)
                    jump_sock.connect((jump_host, jump_port))
                elif proxy_type == "telnet":
                    # Telnet代理实现较为复杂，这里仅做示例
                    jump_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    jump_sock.settimeout(timeout)
                    jump_sock.connect((jump_host, jump_port))
            
            # 连接跳板机
            self.jump_client = paramiko.SSHClient()
            self.jump_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.jump_client.connect(
                hostname=jump_host,
                port=jump_port,
                username=jump_username,
                password=jump_password,
                key_filename=jump_key_filename,
                timeout=timeout,
                sock=jump_sock
            )
            
            # 创建到目标服务器的SSH隧道
            transport = self.jump_client.get_transport()
            if not transport:
                raise paramiko.SSHException("Failed to get transport from jump server")
            
            dest_addr = (target_host, target_port)
            local_addr = ('127.0.0.1', 0)  # 随机本地端口
            channel = transport.open_channel('direct-tcpip', dest_addr, local_addr, timeout=timeout)
            
            # 通过隧道连接到目标服务器
            self.client.connect(
                hostname=target_host,
                port=target_port,
                username=target_username,
                password=target_password,
                key_filename=target_key_filename,
                sock=channel,
                timeout=timeout
            )
            
            # 获取传输实例，用于交互式shell
            self.transport = self.client.get_transport()
            self.is_connected = True
        except Exception as e:
            # 清理连接
            if self.jump_client:
                try:
                    self.jump_client.close()
                except:
                    pass
                self.jump_client = None
            raise
    
    def execute(self, command: str, sudo: bool = False, sudo_password: str = None) -> Dict[str, Any]:
        """
        执行SSH命令
        
        Args:
            command (str): 要执行的命令
            sudo (bool): 是否使用sudo执行
            sudo_password (str): sudo密码
            
        Returns:
            dict: 包含执行结果的字典，格式为 {'stdout': str, 'stderr': str, 'returncode': int}
            
        Raises:
            Exception: 未连接到服务器
        """
        if not self.is_connected:
            raise Exception("Not connected to SSH server")
        
        if sudo:
            if sudo_password:
                command = f"echo '{sudo_password}' | sudo -S {command}"
            else:
                command = f"sudo {command}"
        
        stdin, stdout, stderr = self.client.exec_command(command)
        stdout_content = stdout.read().decode('utf-8')
        stderr_content = stderr.read().decode('utf-8')
        returncode = stdout.channel.recv_exit_status()
        
        return {
            'stdout': stdout_content,
            'stderr': stderr_content,
            'returncode': returncode
        }
    
    def upload(self, local_path: str, remote_path: str):
        """
        上传文件到SSH服务器
        
        Args:
            local_path (str): 本地文件路径
            remote_path (str): 远程文件路径
            
        Raises:
            Exception: 未连接到服务器
        """
        if not self.is_connected:
            raise Exception("Not connected to SSH server")
        
        sftp = self.client.open_sftp()
        try:
            sftp.put(local_path, remote_path)
        finally:
            sftp.close()
    
    def download(self, remote_path: str, local_path: str):
        """
        从SSH服务器下载文件
        
        Args:
            remote_path (str): 远程文件路径
            local_path (str): 本地文件路径
            
        Raises:
            Exception: 未连接到服务器
        """
        if not self.is_connected:
            raise Exception("Not connected to SSH server")
        
        sftp = self.client.open_sftp()
        try:
            sftp.get(remote_path, local_path)
        finally:
            sftp.close()
    
    def open_shell(self, term: str = 'xterm', width: int = 80, height: int = 24) -> paramiko.Channel:
        """
        打开交互式shell
        
        Args:
            term (str): 终端类型，默认为'xterm'
            width (int): 终端宽度，默认为80
            height (int): 终端高度，默认为24
            
        Returns:
            paramiko.Channel: shell通道实例
            
        Raises:
            Exception: 未连接到服务器
        """
        if not self.is_connected:
            raise Exception("Not connected to SSH server")
        
        if not self.transport:
            self.transport = self.client.get_transport()
        
        channel = self.transport.open_session()
        channel.get_pty(term=term, width=width, height=height)
        channel.invoke_shell()
        return channel
    
    def file_operation(self, operation: str, source: str, destination: str = None) -> bool:
        """
        执行文件操作（移动、复制、删除）
        
        Args:
            operation (str): 操作类型，可选值：'mv', 'cp', 'rm', 'mkdir', 'rmdir'
            source (str): 源文件路径
            destination (str): 目标文件路径（对于mv和cp操作）
            
        Returns:
            bool: 操作是否成功
            
        Raises:
            Exception: 未连接到服务器或操作不支持
        """
        if not self.is_connected:
            raise Exception("Not connected to SSH server")
        
        operation = operation.lower()
        
        if operation == 'mv':
            if not destination:
                raise Exception("Destination is required for mv operation")
            command = f"mv '{source}' '{destination}'"
        elif operation == 'cp':
            if not destination:
                raise Exception("Destination is required for cp operation")
            command = f"cp '{source}' '{destination}'"
        elif operation == 'rm':
            command = f"rm '{source}'"
        elif operation == 'mkdir':
            command = f"mkdir -p '{source}'"
        elif operation == 'rmdir':
            command = f"rmdir '{source}'"
        else:
            raise Exception(f"Unsupported operation: {operation}")
        
        result = self.execute(command)
        return result['returncode'] == 0
    
    def close(self):
        """
        关闭SSH连接
        """
        try:
            if self.client:
                self.client.close()
        except:
            pass
        
        try:
            if self.jump_client:
                self.jump_client.close()
        except:
            pass
        
        self.is_connected = False
        self.transport = None
    
    def __enter__(self):
        """
        支持上下文管理器
        """
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出上下文管理器时关闭连接
        """
        self.close()
