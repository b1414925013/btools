"""系统工具类"""
import os
import sys
import platform
import socket
import subprocess
import time
import psutil
from typing import Any, Dict, List, Optional, Union


class SystemUtils:
    """系统工具类"""

    @staticmethod
    def get_os_name() -> str:
        """
        获取操作系统名称
        
        Returns:
            str: 操作系统名称
        """
        return platform.system()

    @staticmethod
    def get_os_version() -> str:
        """
        获取操作系统版本
        
        Returns:
            str: 操作系统版本
        """
        return platform.version()

    @staticmethod
    def get_os_release() -> str:
        """
        获取操作系统发行版
        
        Returns:
            str: 操作系统发行版
        """
        return platform.release()

    @staticmethod
    def get_python_version() -> str:
        """
        获取Python版本
        
        Returns:
            str: Python版本
        """
        return platform.python_version()

    @staticmethod
    def get_python_version_tuple() -> tuple:
        """
        获取Python版本元组
        
        Returns:
            tuple: Python版本元组
        """
        return sys.version_info

    @staticmethod
    def get_system_architecture() -> str:
        """
        获取系统架构
        
        Returns:
            str: 系统架构
        """
        return platform.architecture()[0]

    @staticmethod
    def get_machine() -> str:
        """
        获取机器类型
        
        Returns:
            str: 机器类型
        """
        return platform.machine()

    @staticmethod
    def get_hostname() -> str:
        """
        获取主机名
        
        Returns:
            str: 主机名
        """
        return socket.gethostname()

    @staticmethod
    def get_ip_address() -> str:
        """
        获取IP地址
        
        Returns:
            str: IP地址
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return '127.0.0.1'

    @staticmethod
    def get_all_ip_addresses() -> List[str]:
        """
        获取所有IP地址
        
        Returns:
            List[str]: IP地址列表
        """
        ips = []
        try:
            for interface, addrs in psutil.net_if_addrs().items():
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        ips.append(addr.address)
        except Exception:
            pass
        return ips

    @staticmethod
    def get_env(key: str, default: Optional[str] = None) -> str:
        """
        获取环境变量
        
        Args:
            key: 环境变量名
            default: 默认值
            
        Returns:
            str: 环境变量值
        """
        return os.environ.get(key, default)

    @staticmethod
    def set_env(key: str, value: str) -> None:
        """
        设置环境变量
        
        Args:
            key: 环境变量名
            value: 环境变量值
        """
        os.environ[key] = value

    @staticmethod
    def has_env(key: str) -> bool:
        """
        检查环境变量是否存在
        
        Args:
            key: 环境变量名
            
        Returns:
            bool: 如果存在则返回True，否则返回False
        """
        return key in os.environ

    @staticmethod
    def get_all_env() -> Dict[str, str]:
        """
        获取所有环境变量
        
        Returns:
            Dict[str, str]: 环境变量字典
        """
        return dict(os.environ)

    @staticmethod
    def get_cwd() -> str:
        """
        获取当前工作目录
        
        Returns:
            str: 当前工作目录
        """
        return os.getcwd()

    @staticmethod
    def chdir(path: str) -> None:
        """
        更改工作目录
        
        Args:
            path: 新的工作目录
        """
        os.chdir(path)

    @staticmethod
    def get_temp_dir() -> str:
        """
        获取临时目录
        
        Returns:
            str: 临时目录
        """
        return os.getenv('TEMP') or os.getenv('TMP') or '/tmp'

    @staticmethod
    def get_home_dir() -> str:
        """
        获取用户主目录
        
        Returns:
            str: 用户主目录
        """
        return os.path.expanduser('~')

    @staticmethod
    def get_current_process_id() -> int:
        """
        获取当前进程ID
        
        Returns:
            int: 当前进程ID
        """
        return os.getpid()

    @staticmethod
    def get_current_process_name() -> str:
        """
        获取当前进程名称
        
        Returns:
            str: 当前进程名称
        """
        return psutil.Process().name()

    @staticmethod
    def get_cpu_count() -> int:
        """
        获取CPU核心数
        
        Returns:
            int: CPU核心数
        """
        return os.cpu_count() or 1

    @staticmethod
    def get_cpu_percent() -> float:
        """
        获取CPU使用率
        
        Returns:
            float: CPU使用率
        """
        return psutil.cpu_percent(interval=1)

    @staticmethod
    def get_memory_info() -> Dict[str, Union[int, float]]:
        """
        获取内存信息
        
        Returns:
            Dict[str, Union[int, float]]: 内存信息
        """
        memory = psutil.virtual_memory()
        return {
            'total': memory.total,
            'available': memory.available,
            'used': memory.used,
            'percent': memory.percent
        }

    @staticmethod
    def get_disk_info(path: str = '/') -> Dict[str, Union[int, float]]:
        """
        获取磁盘信息
        
        Args:
            path: 磁盘路径
            
        Returns:
            Dict[str, Union[int, float]]: 磁盘信息
        """
        disk = psutil.disk_usage(path)
        return {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percent': disk.percent
        }

    @staticmethod
    def get_disk_partitions() -> List[Dict[str, str]]:
        """
        获取磁盘分区信息
        
        Returns:
            List[Dict[str, str]]: 磁盘分区信息
        """
        partitions = []
        for partition in psutil.disk_partitions():
            partitions.append({
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'fstype': partition.fstype,
                'opts': partition.opts
            })
        return partitions

    @staticmethod
    def execute_command(cmd: str, shell: bool = True) -> tuple:
        """
        执行系统命令
        
        Args:
            cmd: 命令
            shell: 是否使用shell
            
        Returns:
            tuple: (返回码, 标准输出, 标准错误)
        """
        try:
            result = subprocess.run(
                cmd, 
                shell=shell, 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return 1, '', str(e)

    @staticmethod
    def get_system_time() -> float:
        """
        获取系统时间
        
        Returns:
            float: 系统时间戳
        """
        return time.time()

    @staticmethod
    def get_system_boot_time() -> float:
        """
        获取系统启动时间
        
        Returns:
            float: 系统启动时间戳
        """
        return psutil.boot_time()

    @staticmethod
    def get_uptime() -> float:
        """
        获取系统运行时间
        
        Returns:
            float: 系统运行时间（秒）
        """
        return time.time() - psutil.boot_time()

    @staticmethod
    def is_windows() -> bool:
        """
        检查是否为Windows系统
        
        Returns:
            bool: 如果是Windows系统则返回True，否则返回False
        """
        return platform.system() == 'Windows'

    @staticmethod
    def is_linux() -> bool:
        """
        检查是否为Linux系统
        
        Returns:
            bool: 如果是Linux系统则返回True，否则返回False
        """
        return platform.system() == 'Linux'

    @staticmethod
    def is_macos() -> bool:
        """
        检查是否为MacOS系统
        
        Returns:
            bool: 如果是MacOS系统则返回True，否则返回False
        """
        return platform.system() == 'Darwin'

    @staticmethod
    def get_platform() -> str:
        """
        获取平台信息
        
        Returns:
            str: 平台信息
        """
        return platform.platform()

    @staticmethod
    def get_processor() -> str:
        """
        获取处理器信息
        
        Returns:
            str: 处理器信息
        """
        return platform.processor()

    @staticmethod
    def get_network_io_counters() -> Dict[str, int]:
        """
        获取网络IO计数器
        
        Returns:
            Dict[str, int]: 网络IO计数器
        """
        io = psutil.net_io_counters()
        return {
            'bytes_sent': io.bytes_sent,
            'bytes_recv': io.bytes_recv,
            'packets_sent': io.packets_sent,
            'packets_recv': io.packets_recv,
            'errin': io.errin,
            'errout': io.errout,
            'dropin': io.dropin,
            'dropout': io.dropout
        }

    @staticmethod
    def get_process_list() -> List[Dict[str, Union[int, str, float]]]:
        """
        获取进程列表
        
        Returns:
            List[Dict[str, Union[int, str, float]]]: 进程列表
        """
        processes = []
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu_percent': proc.info['cpu_percent'],
                    'memory_percent': proc.info['memory_percent']
                })
        except Exception:
            pass
        return processes

    @staticmethod
    def kill_process(pid: int) -> bool:
        """
        终止进程
        
        Args:
            pid: 进程ID
            
        Returns:
            bool: 如果成功终止则返回True，否则返回False
        """
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait(timeout=5)
            return True
        except Exception:
            return False

    @staticmethod
    def get_load_average() -> tuple:
        """
        获取系统负载平均值
        
        Returns:
            tuple: 系统负载平均值
        """
        try:
            return os.getloadavg()
        except AttributeError:
            # Windows系统不支持
            return (0.0, 0.0, 0.0)

    @staticmethod
    def get_file_system_encoding() -> str:
        """
        获取文件系统编码
        
        Returns:
            str: 文件系统编码
        """
        return sys.getfilesystemencoding()

    @staticmethod
    def get_python_executable() -> str:
        """
        获取Python可执行文件路径
        
        Returns:
            str: Python可执行文件路径
        """
        return sys.executable

    @staticmethod
    def get_python_path() -> List[str]:
        """
        获取Python路径
        
        Returns:
            List[str]: Python路径列表
        """
        return sys.path
