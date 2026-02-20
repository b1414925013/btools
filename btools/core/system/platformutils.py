#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨平台兼容工具类

提供跨平台兼容工具，处理不同 OS 的差异等功能
"""
import os
import platform
import sys
from typing import Dict, Any, Optional


class PlatformUtils:
    """
    跨平台兼容工具类
    """

    @staticmethod
    def get_os() -> str:
        """
        获取操作系统名称

        Returns:
            操作系统名称
        """
        return platform.system()

    @staticmethod
    def get_os_version() -> str:
        """
        获取操作系统版本

        Returns:
            操作系统版本
        """
        return platform.version()

    @staticmethod
    def get_platform() -> str:
        """
        获取平台信息

        Returns:
            平台信息
        """
        return platform.platform()

    @staticmethod
    def get_architecture() -> tuple:
        """
        获取系统架构

        Returns:
            系统架构元组
        """
        return platform.architecture()

    @staticmethod
    def get_machine() -> str:
        """
        获取机器类型

        Returns:
            机器类型
        """
        return platform.machine()

    @staticmethod
    def get_processor() -> str:
        """
        获取处理器信息

        Returns:
            处理器信息
        """
        return platform.processor()

    @staticmethod
    def is_windows() -> bool:
        """
        是否为 Windows 系统

        Returns:
            是否为 Windows 系统
        """
        return PlatformUtils.get_os() == 'Windows'

    @staticmethod
    def is_linux() -> bool:
        """
        是否为 Linux 系统

        Returns:
            是否为 Linux 系统
        """
        return PlatformUtils.get_os() == 'Linux'

    @staticmethod
    def is_macos() -> bool:
        """
        是否为 macOS 系统

        Returns:
            是否为 macOS 系统
        """
        return PlatformUtils.get_os() == 'Darwin'

    @staticmethod
    def is_unix() -> bool:
        """
        是否为 Unix 系统

        Returns:
            是否为 Unix 系统
        """
        os_name = PlatformUtils.get_os()
        return os_name in ['Linux', 'Darwin', 'Unix']

    @staticmethod
    def get_python_version() -> str:
        """
        获取 Python 版本

        Returns:
            Python 版本
        """
        return platform.python_version()

    @staticmethod
    def get_python_version_tuple() -> tuple:
        """
        获取 Python 版本元组

        Returns:
            Python 版本元组
        """
        return sys.version_info

    @staticmethod
    def get_python_implementation() -> str:
        """
        获取 Python 实现

        Returns:
            Python 实现
        """
        return platform.python_implementation()

    @staticmethod
    def get_system_info() -> Dict[str, Any]:
        """
        获取系统信息

        Returns:
            系统信息字典
        """
        return {
            'os': PlatformUtils.get_os(),
            'os_version': PlatformUtils.get_os_version(),
            'platform': PlatformUtils.get_platform(),
            'architecture': PlatformUtils.get_architecture(),
            'machine': PlatformUtils.get_machine(),
            'processor': PlatformUtils.get_processor(),
            'python_version': PlatformUtils.get_python_version(),
            'python_implementation': PlatformUtils.get_python_implementation(),
            'python_version_tuple': PlatformUtils.get_python_version_tuple()
        }

    @staticmethod
    def get_line_ending() -> str:
        """
        获取行结束符

        Returns:
            行结束符
        """
        if PlatformUtils.is_windows():
            return '\r\n'
        else:
            return '\n'

    @staticmethod
    def get_path_separator() -> str:
        """
        获取路径分隔符

        Returns:
            路径分隔符
        """
        return os.path.sep

    @staticmethod
    def get_environment_variable_separator() -> str:
        """
        获取环境变量分隔符

        Returns:
            环境变量分隔符
        """
        if PlatformUtils.is_windows():
            return ';'
        else:
            return ':'

    @staticmethod
    def get_user_home() -> str:
        """
        获取用户主目录

        Returns:
            用户主目录
        """
        return os.path.expanduser('~')

    @staticmethod
    def get_temp_dir() -> str:
        """
        获取临时目录

        Returns:
            临时目录
        """
        return os.path.abspath(os.environ.get('TEMP', os.environ.get('TMP', '/tmp')))

    @staticmethod
    def get_current_working_dir() -> str:
        """
        获取当前工作目录

        Returns:
            当前工作目录
        """
        return os.getcwd()

    @staticmethod
    def get_executable_path() -> str:
        """
        获取可执行文件路径

        Returns:
            可执行文件路径
        """
        return sys.executable

    @staticmethod
    def get_module_search_paths() -> list:
        """
        获取模块搜索路径

        Returns:
            模块搜索路径列表
        """
        return sys.path

    @staticmethod
    def get_system_encoding() -> str:
        """
        获取系统编码

        Returns:
            系统编码
        """
        return sys.getdefaultencoding()

    @staticmethod
    def get_file_system_encoding() -> str:
        """
        获取文件系统编码

        Returns:
            文件系统编码
        """
        return sys.getfilesystemencoding()

    @staticmethod
    def is_64bit() -> bool:
        """
        是否为 64 位系统

        Returns:
            是否为 64 位系统
        """
        arch = PlatformUtils.get_architecture()
        return '64bit' in arch[0]

    @staticmethod
    def is_32bit() -> bool:
        """
        是否为 32 位系统

        Returns:
            是否为 32 位系统
        """
        arch = PlatformUtils.get_architecture()
        return '32bit' in arch[0]

    @staticmethod
    def get_cpu_count() -> int:
        """
        获取 CPU 核心数

        Returns:
            CPU 核心数
        """
        return os.cpu_count() or 1

    @staticmethod
    def get_memory_info() -> Dict[str, Any]:
        """
        获取内存信息

        Returns:
            内存信息字典
        """
        try:
            if PlatformUtils.is_windows():
                import psutil
                mem = psutil.virtual_memory()
                return {
                    'total': mem.total,
                    'available': mem.available,
                    'used': mem.used,
                    'percent': mem.percent
                }
            elif PlatformUtils.is_linux():
                with open('/proc/meminfo', 'r') as f:
                    meminfo = {}
                    for line in f:
                        key, value = line.strip().split(':', 1)
                        meminfo[key] = value.strip()
                    return meminfo
            elif PlatformUtils.is_macos():
                import subprocess
                result = subprocess.run(['sysctl', 'hw.memsize'], capture_output=True, text=True)
                total_memory = int(result.stdout.split(':')[1].strip())
                return {'total': total_memory}
            else:
                return {}
        except Exception as e:
            return {}

    @staticmethod
    def get_disk_info(path: str = '.') -> Dict[str, Any]:
        """
        获取磁盘信息

        Args:
            path: 路径

        Returns:
            磁盘信息字典
        """
        try:
            stat = os.statvfs(path)
            return {
                'total': stat.f_frsize * stat.f_blocks,
                'free': stat.f_frsize * stat.f_bavail,
                'used': stat.f_frsize * (stat.f_blocks - stat.f_bavail),
                'percent': (stat.f_blocks - stat.f_bavail) / stat.f_blocks * 100
            }
        except Exception as e:
            return {}

    @staticmethod
    def get_network_info() -> Dict[str, Any]:
        """
        获取网络信息

        Returns:
            网络信息字典
        """
        try:
            import socket
            hostname = socket.gethostname()
            ip_addresses = []
            
            for addrinfo in socket.getaddrinfo(hostname, None):
                ip_addresses.append(addrinfo[4][0])
            
            return {
                'hostname': hostname,
                'ip_addresses': ip_addresses
            }
        except Exception as e:
            return {}

    @staticmethod
    def get_battery_info() -> Dict[str, Any]:
        """
        获取电池信息

        Returns:
            电池信息字典
        """
        try:
            if PlatformUtils.is_windows():
                import psutil
                battery = psutil.sensors_battery()
                if battery:
                    return {
                        'percent': battery.percent,
                        'secsleft': battery.secsleft,
                        'power_plugged': battery.power_plugged
                    }
                else:
                    return {}
            elif PlatformUtils.is_linux():
                try:
                    with open('/sys/class/power_supply/BAT0/capacity', 'r') as f:
                        capacity = int(f.read().strip())
                    with open('/sys/class/power_supply/BAT0/status', 'r') as f:
                        status = f.read().strip()
                    return {
                        'percent': capacity,
                        'status': status
                    }
                except:
                    return {}
            elif PlatformUtils.is_macos():
                import subprocess
                result = subprocess.run(['pmset', '-g', 'batt'], capture_output=True, text=True)
                return {'output': result.stdout}
            else:
                return {}
        except Exception as e:
            return {}

    @staticmethod
    def get_platform_specific_command(command: str) -> str:
        """
        获取平台特定的命令

        Args:
            command: 命令

        Returns:
            平台特定的命令
        """
        if PlatformUtils.is_windows():
            # Windows 平台命令映射
            command_map = {
                'ls': 'dir',
                'cat': 'type',
                'grep': 'findstr',
                'cp': 'copy',
                'mv': 'move',
                'rm': 'del',
                'mkdir': 'mkdir',
                'rmdir': 'rmdir',
                'pwd': 'cd',
                'clear': 'cls'
            }
            return command_map.get(command, command)
        else:
            return command

    @staticmethod
    def run_platform_specific_command(command: str, *args) -> tuple:
        """
        运行平台特定的命令

        Args:
            command: 命令
            *args: 命令参数

        Returns:
            (返回码, 标准输出, 标准错误)
        """
        import subprocess
        
        if PlatformUtils.is_windows():
            # Windows 平台使用 shell=True
            cmd = [PlatformUtils.get_platform_specific_command(command)] + list(args)
            result = subprocess.run(
                ' '.join(cmd),
                shell=True,
                capture_output=True,
                text=True
            )
        else:
            # Unix 平台直接运行
            cmd = [PlatformUtils.get_platform_specific_command(command)] + list(args)
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True
            )
        
        return result.returncode, result.stdout, result.stderr

    @staticmethod
    def get_environment() -> Dict[str, str]:
        """
        获取环境变量

        Returns:
            环境变量字典
        """
        return dict(os.environ)

    @staticmethod
    def set_environment_variable(name: str, value: str) -> None:
        """
        设置环境变量

        Args:
            name: 环境变量名
            value: 环境变量值
        """
        os.environ[name] = value

    @staticmethod
    def get_environment_variable(name: str, default: Optional[str] = None) -> Optional[str]:
        """
        获取环境变量

        Args:
            name: 环境变量名
            default: 默认值

        Returns:
            环境变量值或默认值
        """
        return os.environ.get(name, default)

    @staticmethod
    def unset_environment_variable(name: str) -> None:
        """
        取消设置环境变量

        Args:
            name: 环境变量名
        """
        if name in os.environ:
            del os.environ[name]

    @staticmethod
    def get_system_locale() -> Dict[str, str]:
        """
        获取系统区域设置

        Returns:
            系统区域设置字典
        """
        try:
            if PlatformUtils.is_windows():
                import locale
                return {
                    'language': locale.getlocale()[0],
                    'encoding': locale.getpreferredencoding()
                }
            else:
                import subprocess
                result = subprocess.run(['locale'], capture_output=True, text=True)
                locale_info = {}
                for line in result.stdout.split('\n'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        locale_info[key.strip()] = value.strip()
                return locale_info
        except Exception as e:
            return {}

    @staticmethod
    def get_platform_features() -> Dict[str, bool]:
        """
        获取平台特性

        Returns:
            平台特性字典
        """
        return {
            'windows': PlatformUtils.is_windows(),
            'linux': PlatformUtils.is_linux(),
            'macos': PlatformUtils.is_macos(),
            'unix': PlatformUtils.is_unix(),
            '64bit': PlatformUtils.is_64bit(),
            '32bit': PlatformUtils.is_32bit(),
            'has_psutil': False,
            'has_subprocess': True,
            'has_socket': True
        }

    @staticmethod
    def detect_platform_issues() -> list:
        """
        检测平台问题

        Returns:
            平台问题列表
        """
        issues = []

        # 检查 Python 版本
        major, minor, _ = PlatformUtils.get_python_version_tuple()
        if major < 3:
            issues.append('Python 2 已不再受支持')
        elif major == 3 and minor < 6:
            issues.append('Python 3.6 以下版本可能存在兼容性问题')

        # 检查系统内存
        mem_info = PlatformUtils.get_memory_info()
        if mem_info and 'total' in mem_info:
            total_memory_gb = mem_info['total'] / (1024 ** 3)
            if total_memory_gb < 1:
                issues.append('系统内存不足 1GB，可能会影响性能')

        # 检查磁盘空间
        disk_info = PlatformUtils.get_disk_info()
        if disk_info and 'free' in disk_info:
            free_space_gb = disk_info['free'] / (1024 ** 3)
            if free_space_gb < 1:
                issues.append('磁盘空间不足 1GB，可能会影响操作')

        return issues