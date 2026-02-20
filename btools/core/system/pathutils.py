#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨平台路径处理工具类

提供跨平台路径处理，统一路径格式等功能
"""
import os
import sys
from typing import Optional, List, Tuple


class PathUtils:
    """
    跨平台路径处理工具类
    """

    @staticmethod
    def join(*paths) -> str:
        """
        连接路径

        Args:
            *paths: 路径片段

        Returns:
            连接后的路径
        """
        return os.path.join(*paths)

    @staticmethod
    def split(path: str) -> Tuple[str, str]:
        """
        分割路径

        Args:
            path: 路径

        Returns:
            (目录, 文件名) 元组
        """
        return os.path.split(path)

    @staticmethod
    def splitext(path: str) -> Tuple[str, str]:
        """
        分割路径扩展名

        Args:
            path: 路径

        Returns:
            (路径, 扩展名) 元组
        """
        return os.path.splitext(path)

    @staticmethod
    def basename(path: str) -> str:
        """
        获取路径的基本名称

        Args:
            path: 路径

        Returns:
            基本名称
        """
        return os.path.basename(path)

    @staticmethod
    def dirname(path: str) -> str:
        """
        获取路径的目录名称

        Args:
            path: 路径

        Returns:
            目录名称
        """
        return os.path.dirname(path)

    @staticmethod
    def exists(path: str) -> bool:
        """
        检查路径是否存在

        Args:
            path: 路径

        Returns:
            是否存在
        """
        return os.path.exists(path)

    @staticmethod
    def isfile(path: str) -> bool:
        """
        检查路径是否为文件

        Args:
            path: 路径

        Returns:
            是否为文件
        """
        return os.path.isfile(path)

    @staticmethod
    def isdir(path: str) -> bool:
        """
        检查路径是否为目录

        Args:
            path: 路径

        Returns:
            是否为目录
        """
        return os.path.isdir(path)

    @staticmethod
    def isabs(path: str) -> bool:
        """
        检查路径是否为绝对路径

        Args:
            path: 路径

        Returns:
            是否为绝对路径
        """
        return os.path.isabs(path)

    @staticmethod
    def abspath(path: str) -> str:
        """
        获取绝对路径

        Args:
            path: 路径

        Returns:
            绝对路径
        """
        return os.path.abspath(path)

    @staticmethod
    def normpath(path: str) -> str:
        """
        规范化路径

        Args:
            path: 路径

        Returns:
            规范化后的路径
        """
        return os.path.normpath(path)

    @staticmethod
    def realpath(path: str) -> str:
        """
        获取真实路径

        Args:
            path: 路径

        Returns:
            真实路径
        """
        return os.path.realpath(path)

    @staticmethod
    def relpath(path: str, start: str = os.curdir) -> str:
        """
        获取相对路径

        Args:
            path: 路径
            start: 起始路径

        Returns:
            相对路径
        """
        return os.path.relpath(path, start)

    @staticmethod
    def commonpath(paths: List[str]) -> str:
        """
        获取共同路径

        Args:
            paths: 路径列表

        Returns:
            共同路径
        """
        return os.path.commonpath(paths)

    @staticmethod
    def commonprefix(paths: List[str]) -> str:
        """
        获取共同前缀

        Args:
            paths: 路径列表

        Returns:
            共同前缀
        """
        return os.path.commonprefix(paths)

    @staticmethod
    def expanduser(path: str) -> str:
        """
        展开用户主目录

        Args:
            path: 路径

        Returns:
            展开后的路径
        """
        return os.path.expanduser(path)

    @staticmethod
    def expandvars(path: str) -> str:
        """
        展开环境变量

        Args:
            path: 路径

        Returns:
            展开后的路径
        """
        return os.path.expandvars(path)

    @staticmethod
    def get_extension(path: str) -> str:
        """
        获取文件扩展名

        Args:
            path: 路径

        Returns:
            文件扩展名
        """
        return os.path.splitext(path)[1]

    @staticmethod
    def get_filename_without_extension(path: str) -> str:
        """
        获取不含扩展名的文件名

        Args:
            path: 路径

        Returns:
            不含扩展名的文件名
        """
        return os.path.splitext(os.path.basename(path))[0]

    @staticmethod
    def change_extension(path: str, new_extension: str) -> str:
        """
        更改文件扩展名

        Args:
            path: 路径
            new_extension: 新扩展名

        Returns:
            更改扩展名后的路径
        """
        if not new_extension.startswith('.'):
            new_extension = '.' + new_extension
        return os.path.splitext(path)[0] + new_extension

    @staticmethod
    def ensure_directory(path: str) -> bool:
        """
        确保目录存在

        Args:
            path: 目录路径

        Returns:
            是否成功
        """
        try:
            os.makedirs(path, exist_ok=True)
            return True
        except Exception as e:
            return False

    @staticmethod
    def remove(path: str) -> bool:
        """
        删除文件或目录

        Args:
            path: 路径

        Returns:
            是否成功
        """
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                import shutil
                shutil.rmtree(path)
            return True
        except Exception as e:
            return False

    @staticmethod
    def copy(src: str, dst: str) -> bool:
        """
        复制文件或目录

        Args:
            src: 源路径
            dst: 目标路径

        Returns:
            是否成功
        """
        try:
            import shutil
            if os.path.isfile(src):
                shutil.copy2(src, dst)
            elif os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
            return True
        except Exception as e:
            return False

    @staticmethod
    def move(src: str, dst: str) -> bool:
        """
        移动文件或目录

        Args:
            src: 源路径
            dst: 目标路径

        Returns:
            是否成功
        """
        try:
            import shutil
            shutil.move(src, dst)
            return True
        except Exception as e:
            return False

    @staticmethod
    def rename(src: str, dst: str) -> bool:
        """
        重命名文件或目录

        Args:
            src: 源路径
            dst: 目标路径

        Returns:
            是否成功
        """
        try:
            os.rename(src, dst)
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_size(path: str) -> int:
        """
        获取文件或目录大小

        Args:
            path: 路径

        Returns:
            大小（字节）
        """
        try:
            if os.path.isfile(path):
                return os.path.getsize(path)
            elif os.path.isdir(path):
                total = 0
                for root, _, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        total += os.path.getsize(file_path)
                return total
            return 0
        except Exception as e:
            return 0

    @staticmethod
    def get_modification_time(path: str) -> float:
        """
        获取修改时间

        Args:
            path: 路径

        Returns:
            修改时间（时间戳）
        """
        return os.path.getmtime(path)

    @staticmethod
    def get_access_time(path: str) -> float:
        """
        获取访问时间

        Args:
            path: 路径

        Returns:
            访问时间（时间戳）
        """
        return os.path.getatime(path)

    @staticmethod
    def get_creation_time(path: str) -> float:
        """
        获取创建时间

        Args:
            path: 路径

        Returns:
            创建时间（时间戳）
        """
        if sys.platform == 'win32':
            return os.path.getctime(path)
        else:
            # 在 Unix 系统上，getctime 返回的是元数据更改时间
            stat = os.stat(path)
            try:
                return stat.st_birthtime
            except AttributeError:
                # 如果系统不支持 st_birthtime，返回修改时间
                return os.path.getmtime(path)

    @staticmethod
    def walk(path: str) -> List[str]:
        """
        遍历目录

        Args:
            path: 目录路径

        Returns:
            文件路径列表
        """
        files = []
        for root, _, filenames in os.walk(path):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        return files

    @staticmethod
    def find_files(directory: str, pattern: str = '*') -> List[str]:
        """
        查找文件

        Args:
            directory: 目录路径
            pattern: 文件名模式

        Returns:
            文件路径列表
        """
        import glob
        search_path = os.path.join(directory, pattern)
        return glob.glob(search_path, recursive=True)

    @staticmethod
    def find_files_by_extension(directory: str, extension: str) -> List[str]:
        """
        按扩展名查找文件

        Args:
            directory: 目录路径
            extension: 文件扩展名

        Returns:
            文件路径列表
        """
        if not extension.startswith('.'):
            extension = '.' + extension
        return PathUtils.find_files(directory, f'**/*{extension}')

    @staticmethod
    def get_temp_file(suffix: str = '', prefix: str = 'tmp', dir: Optional[str] = None) -> str:
        """
        获取临时文件路径

        Args:
            suffix: 后缀
            prefix: 前缀
            dir: 目录

        Returns:
            临时文件路径
        """
        import tempfile
        fd, path = tempfile.mkstemp(suffix=suffix, prefix=prefix, dir=dir)
        os.close(fd)
        return path

    @staticmethod
    def get_temp_directory(suffix: str = '', prefix: str = 'tmp', dir: Optional[str] = None) -> str:
        """
        获取临时目录路径

        Args:
            suffix: 后缀
            prefix: 前缀
            dir: 目录

        Returns:
            临时目录路径
        """
        import tempfile
        return tempfile.mkdtemp(suffix=suffix, prefix=prefix, dir=dir)

    @staticmethod
    def get_user_home() -> str:
        """
        获取用户主目录

        Returns:
            用户主目录
        """
        return os.path.expanduser('~')

    @staticmethod
    def get_current_working_directory() -> str:
        """
        获取当前工作目录

        Returns:
            当前工作目录
        """
        return os.getcwd()

    @staticmethod
    def get_path_separator() -> str:
        """
        获取路径分隔符

        Returns:
            路径分隔符
        """
        return os.path.sep

    @staticmethod
    def get_alt_separator() -> Optional[str]:
        """
        获取备用路径分隔符

        Returns:
            备用路径分隔符
        """
        return os.path.altsep

    @staticmethod
    def get_extsep() -> str:
        """
        获取扩展名分隔符

        Returns:
            扩展名分隔符
        """
        return os.path.extsep

    @staticmethod
    def get_curdir() -> str:
        """
        获取当前目录符号

        Returns:
            当前目录符号
        """
        return os.curdir

    @staticmethod
    def get_pardir() -> str:
        """
        获取父目录符号

        Returns:
            父目录符号
        """
        return os.pardir

    @staticmethod
    def normalize_path(path: str) -> str:
        """
        规范化路径格式

        Args:
            path: 路径

        Returns:
            规范化后的路径
        """
        # 展开用户主目录和环境变量
        path = os.path.expanduser(path)
        path = os.path.expandvars(path)
        # 规范化路径
        path = os.path.normpath(path)
        # 转换为绝对路径
        path = os.path.abspath(path)
        return path

    @staticmethod
    def to_unix_path(path: str) -> str:
        """
        转换为 Unix 风格路径

        Args:
            path: 路径

        Returns:
            Unix 风格路径
        """
        return path.replace('\\', '/')

    @staticmethod
    def to_windows_path(path: str) -> str:
        """
        转换为 Windows 风格路径

        Args:
            path: 路径

        Returns:
            Windows 风格路径
        """
        return path.replace('/', '\\')

    @staticmethod
    def get_path_without_drive(path: str) -> str:
        """
        获取不含驱动器的路径

        Args:
            path: 路径

        Returns:
            不含驱动器的路径
        """
        if os.name == 'nt':  # Windows
            if len(path) > 2 and path[1] == ':':
                return path[2:]
        return path

    @staticmethod
    def get_drive(path: str) -> str:
        """
        获取驱动器

        Args:
            path: 路径

        Returns:
            驱动器
        """
        if os.name == 'nt':  # Windows
            if len(path) > 2 and path[1] == ':':
                return path[:2]
        return ''

    @staticmethod
    def is_path_safe(path: str) -> bool:
        """
        检查路径是否安全

        Args:
            path: 路径

        Returns:
            是否安全
        """
        try:
            # 规范化路径
            normalized = os.path.normpath(path)
            # 检查是否包含相对路径组件
            if '..' in normalized.split(os.path.sep):
                return False
            # 检查是否为绝对路径（可选）
            # if not os.path.isabs(normalized):
            #     return False
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_relative_path(from_path: str, to_path: str) -> str:
        """
        获取相对路径

        Args:
            from_path: 起始路径
            to_path: 目标路径

        Returns:
            相对路径
        """
        return os.path.relpath(to_path, from_path)

    @staticmethod
    def resolve_path(path: str, base_path: Optional[str] = None) -> str:
        """
        解析路径

        Args:
            path: 路径
            base_path: 基础路径

        Returns:
            解析后的路径
        """
        if base_path and not os.path.isabs(path):
            path = os.path.join(base_path, path)
        return PathUtils.normalize_path(path)

    @staticmethod
    def get_common_directory(paths: List[str]) -> str:
        """
        获取共同目录

        Args:
            paths: 路径列表

        Returns:
            共同目录
        """
        if not paths:
            return ''
        # 确保所有路径都是绝对路径
        absolute_paths = [os.path.abspath(path) for path in paths]
        # 获取共同路径
        return os.path.commonpath(absolute_paths)

    @staticmethod
    def split_path_into_components(path: str) -> List[str]:
        """
        将路径分割为组件

        Args:
            path: 路径

        Returns:
            路径组件列表
        """
        components = []
        while True:
            path, component = os.path.split(path)
            if component:
                components.append(component)
            else:
                if path:
                    components.append(path)
                break
        components.reverse()
        return components

    @staticmethod
    def join_path_components(components: List[str]) -> str:
        """
        连接路径组件

        Args:
            components: 路径组件列表

        Returns:
            连接后的路径
        """
        return os.path.join(*components)

    @staticmethod
    def get_path_depth(path: str) -> int:
        """
        获取路径深度

        Args:
            path: 路径

        Returns:
            路径深度
        """
        components = PathUtils.split_path_into_components(path)
        return len(components)

    @staticmethod
    def get_temp_path() -> str:
        """
        获取临时路径

        Returns:
            临时路径
        """
        return os.path.abspath(os.environ.get('TEMP', os.environ.get('TMP', '/tmp')))

    @staticmethod
    def get_home_path() -> str:
        """
        获取主目录路径

        Returns:
            主目录路径
        """
        return PathUtils.get_user_home()

    @staticmethod
    def get_desktop_path() -> str:
        """
        获取桌面路径

        Returns:
            桌面路径
        """
        home = PathUtils.get_user_home()
        if os.name == 'nt':  # Windows
            return os.path.join(home, 'Desktop')
        elif os.name == 'posix':  # Unix-like
            if os.environ.get('XDG_DESKTOP_DIR'):
                return os.environ['XDG_DESKTOP_DIR']
            elif os.name == 'darwin':  # macOS
                return os.path.join(home, 'Desktop')
            else:  # Linux
                return os.path.join(home, 'Desktop')
        return home

    @staticmethod
    def get_documents_path() -> str:
        """
        获取文档路径

        Returns:
            文档路径
        """
        home = PathUtils.get_user_home()
        if os.name == 'nt':  # Windows
            return os.path.join(home, 'Documents')
        elif os.name == 'posix':  # Unix-like
            if os.environ.get('XDG_DOCUMENTS_DIR'):
                return os.environ['XDG_DOCUMENTS_DIR']
            elif os.name == 'darwin':  # macOS
                return os.path.join(home, 'Documents')
            else:  # Linux
                return os.path.join(home, 'Documents')
        return home

    @staticmethod
    def get_downloads_path() -> str:
        """
        获取下载路径

        Returns:
            下载路径
        """
        home = PathUtils.get_user_home()
        if os.name == 'nt':  # Windows
            return os.path.join(home, 'Downloads')
        elif os.name == 'posix':  # Unix-like
            if os.environ.get('XDG_DOWNLOAD_DIR'):
                return os.environ['XDG_DOWNLOAD_DIR']
            elif os.name == 'darwin':  # macOS
                return os.path.join(home, 'Downloads')
            else:  # Linux
                return os.path.join(home, 'Downloads')
        return home