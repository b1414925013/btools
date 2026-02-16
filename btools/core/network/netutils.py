"""网络工具类"""
import socket
import urllib.parse
import urllib.request
import urllib.error
import ipaddress
import subprocess
import platform
from typing import Optional, List, Dict, Any


class NetUtils:
    """网络工具类"""

    @staticmethod
    def get_hostname() -> str:
        """
        获取主机名
        
        Returns:
            str: 主机名
        """
        return socket.gethostname()

    @staticmethod
    def get_ip_address(hostname: Optional[str] = None) -> str:
        """
        获取IP地址
        
        Args:
            hostname: 主机名，默认为None（获取本地IP）
            
        Returns:
            str: IP地址
        """
        if hostname is None:
            hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

    @staticmethod
    def get_all_ip_addresses() -> List[str]:
        """
        获取所有IP地址
        
        Returns:
            List[str]: IP地址列表
        """
        ips = []
        hostname = socket.gethostname()
        try:
            addrinfo = socket.getaddrinfo(hostname, None, socket.AF_INET)
            for info in addrinfo:
                ip = info[4][0]
                if ip not in ips:
                    ips.append(ip)
        except Exception:
            pass
        return ips

    @staticmethod
    def is_ipv4(ip: str) -> bool:
        """
        检查是否为IPv4地址
        
        Args:
            ip: IP地址
            
        Returns:
            bool: 如果是IPv4地址则返回True，否则返回False
        """
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_ipv6(ip: str) -> bool:
        """
        检查是否为IPv6地址
        
        Args:
            ip: IP地址
            
        Returns:
            bool: 如果是IPv6地址则返回True，否则返回False
        """
        try:
            ipaddress.IPv6Address(ip)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_private_ip(ip: str) -> bool:
        """
        检查是否为私有IP地址
        
        Args:
            ip: IP地址
            
        Returns:
            bool: 如果是私有IP地址则返回True，否则返回False
        """
        try:
            addr = ipaddress.ip_address(ip)
            return addr.is_private
        except ValueError:
            return False

    @staticmethod
    def is_loopback_ip(ip: str) -> bool:
        """
        检查是否为回环IP地址
        
        Args:
            ip: IP地址
            
        Returns:
            bool: 如果是回环IP地址则返回True，否则返回False
        """
        try:
            addr = ipaddress.ip_address(ip)
            return addr.is_loopback
        except ValueError:
            return False

    @staticmethod
    def is_reserved_ip(ip: str) -> bool:
        """
        检查是否为保留IP地址
        
        Args:
            ip: IP地址
            
        Returns:
            bool: 如果是保留IP地址则返回True，否则返回False
        """
        try:
            addr = ipaddress.ip_address(ip)
            return addr.is_reserved
        except ValueError:
            return False

    @staticmethod
    def ping(host: str, count: int = 4, timeout: int = 2) -> bool:
        """
         ping主机
        
        Args:
            host: 主机名或IP地址
            count: 发送的数据包数量
            timeout: 超时时间（秒）
            
        Returns:
            bool: 如果ping成功则返回True，否则返回False
        """
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, str(count), '-w' if platform.system().lower() == 'windows' else '-W', str(timeout), host]
        
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def get_http_status(url: str) -> int:
        """
        获取HTTP状态码
        
        Args:
            url: URL
            
        Returns:
            int: HTTP状态码
        """
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                return response.getcode()
        except urllib.error.HTTPError as e:
            return e.code
        except Exception:
            return 0

    @staticmethod
    def download_file(url: str, save_path: str) -> bool:
        """
        下载文件
        
        Args:
            url: 文件URL
            save_path: 保存路径
            
        Returns:
            bool: 如果下载成功则返回True，否则返回False
        """
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                with open(save_path, 'wb') as f:
                    f.write(response.read())
            return True
        except Exception:
            return False

    @staticmethod
    def url_encode(url: str) -> str:
        """
        URL编码
        
        Args:
            url: 原始URL
            
        Returns:
            str: 编码后的URL
        """
        return urllib.parse.quote(url)

    @staticmethod
    def url_decode(url: str) -> str:
        """
        URL解码
        
        Args:
            url: 编码后的URL
            
        Returns:
            str: 解码后的URL
        """
        return urllib.parse.unquote(url)

    @staticmethod
    def parse_url(url: str) -> Dict[str, Any]:
        """
        解析URL
        
        Args:
            url: URL
            
        Returns:
            Dict[str, Any]: URL各部分组成
        """
        parsed = urllib.parse.urlparse(url)
        return {
            'scheme': parsed.scheme,
            'netloc': parsed.netloc,
            'path': parsed.path,
            'params': parsed.params,
            'query': parsed.query,
            'fragment': parsed.fragment,
            'username': parsed.username,
            'password': parsed.password,
            'hostname': parsed.hostname,
            'port': parsed.port
        }

    @staticmethod
    def build_url(base_url: str, params: Dict[str, Any]) -> str:
        """
        构建带参数的URL
        
        Args:
            base_url: 基础URL
            params: 查询参数
            
        Returns:
            str: 带参数的URL
        """
        url_parts = list(urllib.parse.urlparse(base_url))
        query = dict(urllib.parse.parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urllib.parse.urlencode(query)
        return urllib.parse.urlunparse(url_parts)

    @staticmethod
    def get_free_port() -> int:
        """
        获取空闲端口
        
        Returns:
            int: 空闲端口
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', 0))
            return s.getsockname()[1]

    @staticmethod
    def is_port_open(host: str, port: int, timeout: int = 2) -> bool:
        """
        检查端口是否开放
        
        Args:
            host: 主机名或IP地址
            port: 端口号
            timeout: 超时时间（秒）
            
        Returns:
            bool: 如果端口开放则返回True，否则返回False
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((host, port))
                return True
        except Exception:
            return False

    @staticmethod
    def get_service_by_port(port: int, protocol: str = 'tcp') -> Optional[str]:
        """
        根据端口获取服务名
        
        Args:
            port: 端口号
            protocol: 协议（tcp或udp）
            
        Returns:
            Optional[str]: 服务名，如果未找到则返回None
        """
        try:
            return socket.getservbyport(port, protocol)
        except Exception:
            return None

    @staticmethod
    def get_port_by_service(service: str, protocol: str = 'tcp') -> Optional[int]:
        """
        根据服务名获取端口
        
        Args:
            service: 服务名
            protocol: 协议（tcp或udp）
            
        Returns:
            Optional[int]: 端口号，如果未找到则返回None
        """
        try:
            return socket.getservbyname(service, protocol)
        except Exception:
            return None

    @staticmethod
    def resolve_hostname(hostname: str) -> List[str]:
        """
        解析主机名到IP地址列表
        
        Args:
            hostname: 主机名
            
        Returns:
            List[str]: IP地址列表
        """
        ips = []
        try:
            addrinfo = socket.getaddrinfo(hostname, None, socket.AF_INET)
            for info in addrinfo:
                ip = info[4][0]
                if ip not in ips:
                    ips.append(ip)
        except Exception:
            pass
        return ips

    @staticmethod
    def get_subnet_mask(ip: str, cidr: int) -> str:
        """
        获取子网掩码
        
        Args:
            ip: IP地址
            cidr: CIDR前缀长度
            
        Returns:
            str: 子网掩码
        """
        try:
            network = ipaddress.IPv4Network(f"{ip}/{cidr}", strict=False)
            return str(network.netmask)
        except Exception:
            return ''

    @staticmethod
    def get_network_address(ip: str, subnet_mask: str) -> str:
        """
        获取网络地址
        
        Args:
            ip: IP地址
            subnet_mask: 子网掩码
            
        Returns:
            str: 网络地址
        """
        try:
            ip_obj = ipaddress.IPv4Address(ip)
            mask_obj = ipaddress.IPv4Address(subnet_mask)
            network_obj = ip_obj & mask_obj
            return str(network_obj)
        except Exception:
            return ''

    @staticmethod
    def get_broadcast_address(ip: str, subnet_mask: str) -> str:
        """
        获取广播地址
        
        Args:
            ip: IP地址
            subnet_mask: 子网掩码
            
        Returns:
            str: 广播地址
        """
        try:
            ip_obj = ipaddress.IPv4Address(ip)
            mask_obj = ipaddress.IPv4Address(subnet_mask)
            network_obj = ip_obj & mask_obj
            broadcast_obj = network_obj | ipaddress.IPv4Address(int(mask_obj) ^ 0xFFFFFFFF)
            return str(broadcast_obj)
        except Exception:
            return ''

    @staticmethod
    def is_in_subnet(ip: str, network: str) -> bool:
        """
        检查IP是否在子网内
        
        Args:
            ip: IP地址
            network: 网络地址（如 192.168.1.0/24）
            
        Returns:
            bool: 如果IP在子网内则返回True，否则返回False
        """
        try:
            ip_obj = ipaddress.ip_address(ip)
            network_obj = ipaddress.ip_network(network, strict=False)
            return ip_obj in network_obj
        except Exception:
            return False

    @staticmethod
    def get_public_ip() -> Optional[str]:
        """
        获取公网IP
        
        Returns:
            Optional[str]: 公网IP，如果获取失败则返回None
        """
        try:
            with urllib.request.urlopen('https://api.ipify.org', timeout=5) as response:
                return response.read().decode('utf-8')
        except Exception:
            try:
                with urllib.request.urlopen('https://ipinfo.io/ip', timeout=5) as response:
                    return response.read().decode('utf-8').strip()
            except Exception:
                return None

    @staticmethod
    def trace_route(host: str, max_hops: int = 30) -> List[str]:
        """
        跟踪路由
        
        Args:
            host: 主机名或IP地址
            max_hops: 最大跳数
            
        Returns:
            List[str]: 路由节点列表
        """
        nodes = []
        param = '-n' if platform.system().lower() == 'windows' else '-n'
        command = ['tracert' if platform.system().lower() == 'windows' else 'traceroute', param, '-h' if platform.system().lower() == 'windows' else '-m', str(max_hops), host]
        
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            lines = output.split('\n')
            for line in lines:
                if platform.system().lower() == 'windows':
                    if 'ms' in line:
                        parts = line.split()
                        for part in parts:
                            if NetUtils.is_ipv4(part):
                                nodes.append(part)
                                break
                else:
                    if '(' in line and ')' in line:
                        start = line.find('(') + 1
                        end = line.find(')')
                        ip = line[start:end]
                        if NetUtils.is_ipv4(ip):
                            nodes.append(ip)
        except Exception:
            pass
        
        return nodes

    @staticmethod
    def get_dns_servers() -> List[str]:
        """
        获取DNS服务器
        
        Returns:
            List[str]: DNS服务器列表
        """
        servers = []
        if platform.system().lower() == 'windows':
            try:
                output = subprocess.check_output(['ipconfig', '/all'], stderr=subprocess.STDOUT, universal_newlines=True)
                lines = output.split('\n')
                for line in lines:
                    if 'DNS Servers' in line or 'Preferred DNS server' in line:
                        parts = line.split(':')
                        if len(parts) > 1:
                            ip = parts[1].strip()
                            if NetUtils.is_ipv4(ip):
                                servers.append(ip)
            except Exception:
                pass
        else:
            try:
                with open('/etc/resolv.conf', 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith('nameserver'):
                            parts = line.split()
                            if len(parts) > 1:
                                ip = parts[1].strip()
                                if NetUtils.is_ipv4(ip):
                                    servers.append(ip)
            except Exception:
                pass
        return servers