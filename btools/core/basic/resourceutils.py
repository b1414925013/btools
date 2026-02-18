import os
import sys
import importlib
import importlib.resources
from typing import Optional, Union, IO, Any
import urllib.request
import urllib.error


class ResourceUtils:
    """
    资源工具类，提供资源加载、读取等功能
    """

    @staticmethod
    def get_resource_path(resource_name: str, cls: Optional[Any] = None) -> Optional[str]:
        """
        获取资源路径
        
        Args:
            resource_name: 资源名称
            cls: 类对象，用于确定资源所在的包路径
            
        Returns:
            资源路径，如果资源不存在则返回None
        """
        try:
            if cls:
                # 从类所在的包中获取资源
                package = cls.__module__.rpartition('.')[0]
                if package:
                    with importlib.resources.path(package, resource_name) as path:
                        return str(path)
            
            # 尝试直接使用绝对路径
            if os.path.isabs(resource_name) and os.path.exists(resource_name):
                return resource_name
            
            # 尝试从当前目录获取
            current_dir = os.getcwd()
            resource_path = os.path.join(current_dir, resource_name)
            if os.path.exists(resource_path):
                return resource_path
            
            # 尝试从工作目录获取
            if os.path.exists(resource_name):
                return os.path.abspath(resource_name)
            
            # 尝试从Python路径中获取
            for path in sys.path:
                resource_path = os.path.join(path, resource_name)
                if os.path.exists(resource_path):
                    return resource_path
            
            return None
        except Exception:
            return None

    @staticmethod
    def get_resource_stream(resource_name: str, cls: Optional[Any] = None) -> Optional[IO]:
        """
        获取资源输入流
        
        Args:
            resource_name: 资源名称
            cls: 类对象，用于确定资源所在的包路径
            
        Returns:
            资源输入流，如果资源不存在则返回None
        """
        try:
            if cls:
                # 从类所在的包中获取资源
                package = cls.__module__.rpartition('.')[0]
                if package:
                    return importlib.resources.open_binary(package, resource_name)
            
            # 尝试从文件系统获取
            resource_path = ResourceUtils.get_resource_path(resource_name, cls)
            if resource_path:
                return open(resource_path, 'rb')
            
            return None
        except Exception:
            return None

    @staticmethod
    def read_resource(resource_name: str, encoding: str = 'utf-8', cls: Optional[Any] = None) -> Optional[str]:
        """
        读取资源内容
        
        Args:
            resource_name: 资源名称
            encoding: 编码，默认为utf-8
            cls: 类对象，用于确定资源所在的包路径
            
        Returns:
            资源内容，如果资源不存在则返回None
        """
        try:
            if cls:
                # 从类所在的包中获取资源
                package = cls.__module__.rpartition('.')[0]
                if package:
                    return importlib.resources.read_text(package, resource_name, encoding=encoding)
            
            # 尝试从文件系统获取
            resource_path = ResourceUtils.get_resource_path(resource_name, cls)
            if resource_path:
                with open(resource_path, 'r', encoding=encoding) as f:
                    return f.read()
            
            return None
        except Exception:
            return None

    @staticmethod
    def read_resource_bytes(resource_name: str, cls: Optional[Any] = None) -> Optional[bytes]:
        """
        读取资源字节内容
        
        Args:
            resource_name: 资源名称
            cls: 类对象，用于确定资源所在的包路径
            
        Returns:
            资源字节内容，如果资源不存在则返回None
        """
        try:
            if cls:
                # 从类所在的包中获取资源
                package = cls.__module__.rpartition('.')[0]
                if package:
                    return importlib.resources.read_binary(package, resource_name)
            
            # 尝试从文件系统获取
            resource_path = ResourceUtils.get_resource_path(resource_name, cls)
            if resource_path:
                with open(resource_path, 'rb') as f:
                    return f.read()
            
            return None
        except Exception:
            return None

    @staticmethod
    def get_resource_url(resource_name: str, cls: Optional[Any] = None) -> Optional[str]:
        """
        获取资源URL
        
        Args:
            resource_name: 资源名称
            cls: 类对象，用于确定资源所在的包路径
            
        Returns:
            资源URL，如果资源不存在则返回None
        """
        try:
            # 检查是否为绝对URL
            if resource_name.startswith(('http://', 'https://', 'file://')):
                return resource_name
            
            # 尝试获取本地文件路径并转换为file:// URL
            resource_path = ResourceUtils.get_resource_path(resource_name, cls)
            if resource_path:
                return f'file://{os.path.abspath(resource_path)}'
            
            return None
        except Exception:
            return None

    @staticmethod
    def exists(resource_name: str, cls: Optional[Any] = None) -> bool:
        """
        检查资源是否存在
        
        Args:
            resource_name: 资源名称
            cls: 类对象，用于确定资源所在的包路径
            
        Returns:
            如果资源存在则返回True，否则返回False
        """
        try:
            if cls:
                # 检查类所在包中的资源
                package = cls.__module__.rpartition('.')[0]
                if package:
                    return importlib.resources.is_resource(package, resource_name)
            
            # 检查文件系统中的资源
            resource_path = ResourceUtils.get_resource_path(resource_name, cls)
            return resource_path is not None
        except Exception:
            return False

    @staticmethod
    def load_from_url(url: str, encoding: Optional[str] = 'utf-8') -> Optional[Union[str, bytes]]:
        """
        从URL加载资源
        
        Args:
            url: 资源URL
            encoding: 编码，如果为None则返回字节内容
            
        Returns:
            资源内容，如果加载失败则返回None
        """
        try:
            with urllib.request.urlopen(url) as response:
                if encoding:
                    return response.read().decode(encoding)
                else:
                    return response.read()
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError):
            return None

    @staticmethod
    def get_resource_as_stream(resource_name: str, cls: Optional[Any] = None) -> Optional[IO]:
        """
        获取资源作为输入流（别名方法）
        
        Args:
            resource_name: 资源名称
            cls: 类对象，用于确定资源所在的包路径
            
        Returns:
            资源输入流，如果资源不存在则返回None
        """
        return ResourceUtils.get_resource_stream(resource_name, cls)

    @staticmethod
    def get_resource_bytes(resource_name: str, cls: Optional[Any] = None) -> Optional[bytes]:
        """
        获取资源字节内容（别名方法）
        
        Args:
            resource_name: 资源名称
            cls: 类对象，用于确定资源所在的包路径
            
        Returns:
            资源字节内容，如果资源不存在则返回None
        """
        return ResourceUtils.read_resource_bytes(resource_name, cls)

    @staticmethod
    def get_resource_text(resource_name: str, encoding: str = 'utf-8', cls: Optional[Any] = None) -> Optional[str]:
        """
        获取资源文本内容（别名方法）
        
        Args:
            resource_name: 资源名称
            encoding: 编码，默认为utf-8
            cls: 类对象，用于确定资源所在的包路径
            
        Returns:
            资源文本内容，如果资源不存在则返回None
        """
        return ResourceUtils.read_resource(resource_name, encoding, cls)
