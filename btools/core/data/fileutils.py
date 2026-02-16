import os
import shutil
import glob
import hashlib
import zipfile
import tarfile
from pathlib import Path
from typing import List, Dict, Optional, Union, Callable
import time
import threading


class FileUtils:
    """
    文件操作工具类，提供通用的文件和目录操作功能
    """

    @staticmethod
    def read_file(file_path: str, encoding: str = 'utf-8') -> str:
        """
        读取文件内容
        
        Args:
            file_path: 文件路径
            encoding: 文件编码，默认为utf-8
            
        Returns:
            文件内容
        """
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()

    @staticmethod
    def write_file(file_path: str, content: str, encoding: str = 'utf-8', mode: str = 'w') -> None:
        """
        写入文件内容
        
        Args:
            file_path: 文件路径
            content: 要写入的内容
            encoding: 文件编码，默认为utf-8
            mode: 写入模式，默认为'w'（覆盖写入）
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, mode, encoding=encoding) as f:
            f.write(content)

    @staticmethod
    def append_file(file_path: str, content: str, encoding: str = 'utf-8') -> None:
        """
        追加写入文件内容
        
        Args:
            file_path: 文件路径
            content: 要追加的内容
            encoding: 文件编码，默认为utf-8
        """
        FileUtils.write_file(file_path, content, encoding, 'a')

    @staticmethod
    def exists(file_path: str) -> bool:
        """
        检查文件或目录是否存在
        
        Args:
            file_path: 文件或目录路径
            
        Returns:
            存在返回True，否则返回False
        """
        return os.path.exists(file_path)

    @staticmethod
    def is_file(file_path: str) -> bool:
        """
        检查是否为文件
        
        Args:
            file_path: 路径
            
        Returns:
            是文件返回True，否则返回False
        """
        return os.path.isfile(file_path)

    @staticmethod
    def is_dir(dir_path: str) -> bool:
        """
        检查是否为目录
        
        Args:
            dir_path: 路径
            
        Returns:
            是目录返回True，否则返回False
        """
        return os.path.isdir(dir_path)

    @staticmethod
    def create_dir(dir_path: str, recursive: bool = True) -> None:
        """
        创建目录
        
        Args:
            dir_path: 目录路径
            recursive: 是否递归创建父目录，默认为True
        """
        if recursive:
            os.makedirs(dir_path, exist_ok=True)
        else:
            os.mkdir(dir_path)

    @staticmethod
    def list_files(dir_path: str, pattern: str = '*', recursive: bool = False) -> List[str]:
        """
        列出目录中的文件
        
        Args:
            dir_path: 目录路径
            pattern: 文件匹配模式，默认为'*'（所有文件）
            recursive: 是否递归搜索子目录，默认为False
            
        Returns:
            文件路径列表
        """
        if not os.path.exists(dir_path):
            return []
        
        if recursive:
            files = []
            for root, _, filenames in os.walk(dir_path):
                for filename in filenames:
                    if glob.fnmatch.fnmatch(filename, pattern):
                        files.append(os.path.join(root, filename))
            return files
        else:
            return [os.path.join(dir_path, f) for f in os.listdir(dir_path) 
                   if os.path.isfile(os.path.join(dir_path, f)) 
                   and glob.fnmatch.fnmatch(f, pattern)]

    @staticmethod
    def list_dirs(dir_path: str) -> List[str]:
        """
        列出目录中的子目录
        
        Args:
            dir_path: 目录路径
            
        Returns:
            子目录路径列表
        """
        if not os.path.exists(dir_path):
            return []
        
        return [os.path.join(dir_path, d) for d in os.listdir(dir_path) 
               if os.path.isdir(os.path.join(dir_path, d))]

    @staticmethod
    def copy_file(src_path: str, dst_path: str, overwrite: bool = True) -> None:
        """
        复制文件
        
        Args:
            src_path: 源文件路径
            dst_path: 目标文件路径
            overwrite: 是否覆盖已存在的文件，默认为True
        """
        if not os.path.exists(src_path):
            raise FileNotFoundError(f"源文件不存在: {src_path}")
        
        if os.path.exists(dst_path) and not overwrite:
            raise FileExistsError(f"目标文件已存在: {dst_path}")
        
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.copy2(src_path, dst_path)

    @staticmethod
    def copy_dir(src_dir: str, dst_dir: str, overwrite: bool = True) -> None:
        """
        复制目录
        
        Args:
            src_dir: 源目录路径
            dst_dir: 目标目录路径
            overwrite: 是否覆盖已存在的文件，默认为True
        """
        if not os.path.exists(src_dir):
            raise FileNotFoundError(f"源目录不存在: {src_dir}")
        
        if os.path.exists(dst_dir):
            if overwrite:
                shutil.rmtree(dst_dir)
            else:
                raise FileExistsError(f"目标目录已存在: {dst_dir}")
        
        shutil.copytree(src_dir, dst_dir)

    @staticmethod
    def move_file(src_path: str, dst_path: str, overwrite: bool = True) -> None:
        """
        移动文件
        
        Args:
            src_path: 源文件路径
            dst_path: 目标文件路径
            overwrite: 是否覆盖已存在的文件，默认为True
        """
        if not os.path.exists(src_path):
            raise FileNotFoundError(f"源文件不存在: {src_path}")
        
        if os.path.exists(dst_path):
            if overwrite:
                os.remove(dst_path)
            else:
                raise FileExistsError(f"目标文件已存在: {dst_path}")
        
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.move(src_path, dst_path)

    @staticmethod
    def delete_file(file_path: str) -> None:
        """
        删除文件
        
        Args:
            file_path: 文件路径
        """
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.remove(file_path)

    @staticmethod
    def delete_dir(dir_path: str, recursive: bool = True) -> None:
        """
        删除目录
        
        Args:
            dir_path: 目录路径
            recursive: 是否递归删除子目录和文件，默认为True
        """
        if os.path.exists(dir_path):
            if recursive:
                shutil.rmtree(dir_path)
            else:
                os.rmdir(dir_path)

    @staticmethod
    def get_file_size(file_path: str) -> int:
        """
        获取文件大小（字节）
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件大小，单位为字节
        """
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            return 0
        return os.path.getsize(file_path)

    @staticmethod
    def get_file_hash(file_path: str, algorithm: str = 'md5') -> str:
        """
        获取文件哈希值
        
        Args:
            file_path: 文件路径
            algorithm: 哈希算法，可选值：md5, sha1, sha256, sha512
            
        Returns:
            文件哈希值
        """
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            return ''
        
        hash_obj = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()

    @staticmethod
    def compress_file(file_path: str, output_path: str, format: str = 'zip') -> None:
        """
        压缩文件
        
        Args:
            file_path: 要压缩的文件路径
            output_path: 压缩文件输出路径
            format: 压缩格式，可选值：zip, tar, tar.gz, tar.bz2
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if format == 'zip':
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(file_path, os.path.basename(file_path))
        elif format in ['tar', 'tar.gz', 'tar.bz2']:
            mode = 'w'
            if format == 'tar.gz':
                mode = 'w:gz'
            elif format == 'tar.bz2':
                mode = 'w:bz2'
            
            with tarfile.open(output_path, mode) as tarf:
                tarf.add(file_path, arcname=os.path.basename(file_path))

    @staticmethod
    def compress_dir(dir_path: str, output_path: str, format: str = 'zip') -> None:
        """
        压缩目录
        
        Args:
            dir_path: 要压缩的目录路径
            output_path: 压缩文件输出路径
            format: 压缩格式，可选值：zip, tar, tar.gz, tar.bz2
        """
        if not os.path.exists(dir_path):
            raise FileNotFoundError(f"目录不存在: {dir_path}")
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if format == 'zip':
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, dir_path)
                        zipf.write(file_path, arcname)
        elif format in ['tar', 'tar.gz', 'tar.bz2']:
            mode = 'w'
            if format == 'tar.gz':
                mode = 'w:gz'
            elif format == 'tar.bz2':
                mode = 'w:bz2'
            
            with tarfile.open(output_path, mode) as tarf:
                tarf.add(dir_path, arcname=os.path.basename(dir_path))

    @staticmethod
    def decompress_file(archive_path: str, output_dir: str) -> None:
        """
        解压文件
        
        Args:
            archive_path: 压缩文件路径
            output_dir: 解压输出目录
        """
        if not os.path.exists(archive_path):
            raise FileNotFoundError(f"压缩文件不存在: {archive_path}")
        
        os.makedirs(output_dir, exist_ok=True)
        
        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path, 'r') as zipf:
                zipf.extractall(output_dir)
        elif archive_path.endswith(('.tar', '.tar.gz', '.tar.bz2')):
            with tarfile.open(archive_path, 'r') as tarf:
                tarf.extractall(output_dir)

    @staticmethod
    def get_file_info(file_path: str) -> Dict[str, any]:
        """
        获取文件信息
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件信息字典
        """
        if not os.path.exists(file_path):
            return {}
        
        stat = os.stat(file_path)
        return {
            'path': file_path,
            'size': stat.st_size,
            'mode': stat.st_mode,
            'uid': stat.st_uid,
            'gid': stat.st_gid,
            'atime': stat.st_atime,
            'mtime': stat.st_mtime,
            'ctime': stat.st_ctime
        }

    @staticmethod
    def get_relative_path(path: str, base: str) -> str:
        """
        获取相对路径
        
        Args:
            path: 目标路径
            base: 基础路径
            
        Returns:
            相对路径
        """
        return os.path.relpath(path, base)

    @staticmethod
    def get_absolute_path(path: str) -> str:
        """
        获取绝对路径
        
        Args:
            path: 路径
            
        Returns:
            绝对路径
        """
        return os.path.abspath(path)

    @staticmethod
    def normalize_path(path: str) -> str:
        """
        规范化路径
        
        Args:
            path: 路径
            
        Returns:
            规范化后的路径
        """
        return os.path.normpath(path)

    @staticmethod
    def find_files(pattern: str, root_dir: str = '.') -> List[str]:
        """
        查找文件
        
        Args:
            pattern: 文件匹配模式
            root_dir: 搜索根目录，默认为当前目录
            
        Returns:
            匹配的文件路径列表
        """
        return glob.glob(os.path.join(root_dir, pattern), recursive=True)

    @staticmethod
    def touch(file_path: str) -> None:
        """
        创建空文件或更新文件时间戳
        
        Args:
            file_path: 文件路径
        """
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'a') as f:
                pass
        else:
            os.utime(file_path, None)


class FileMonitor:
    """
    文件监控类，实时监控文件变化
    """

    def __init__(self, paths: List[str], callback: Callable[[str, str], None]):
        """
        初始化文件监控器
        
        Args:
            paths: 要监控的文件或目录路径列表
            callback: 文件变化时的回调函数，参数为(文件路径, 变化类型)
                      变化类型: created, modified, deleted
        """
        self.paths = paths
        self.callback = callback
        self.file_times = {}
        self.running = False
        self.thread = None

    def start(self, interval: float = 1.0):
        """
        开始监控
        
        Args:
            interval: 监控间隔，默认为1秒
        """
        self.running = True
        self.thread = threading.Thread(target=self._monitor, args=(interval,))
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        """
        停止监控
        """
        self.running = False
        if self.thread:
            self.thread.join()

    def _monitor(self, interval: float):
        """
        监控线程函数
        
        Args:
            interval: 监控间隔
        """
        # 初始化文件时间戳
        for path in self.paths:
            if os.path.exists(path):
                if os.path.isfile(path):
                    self.file_times[path] = os.path.getmtime(path)
                elif os.path.isdir(path):
                    for root, _, files in os.walk(path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            self.file_times[file_path] = os.path.getmtime(file_path)

        while self.running:
            time.sleep(interval)
            
            # 检查文件变化
            current_files = {}
            
            # 收集当前所有文件
            for path in self.paths:
                if os.path.exists(path):
                    if os.path.isfile(path):
                        current_files[path] = os.path.getmtime(path)
                    elif os.path.isdir(path):
                        for root, _, files in os.walk(path):
                            for file in files:
                                file_path = os.path.join(root, file)
                                current_files[file_path] = os.path.getmtime(file_path)
            
            # 检测变化
            # 检查新增和修改的文件
            for file_path, mtime in current_files.items():
                if file_path not in self.file_times:
                    self.callback(file_path, 'created')
                elif mtime != self.file_times[file_path]:
                    self.callback(file_path, 'modified')
                self.file_times[file_path] = mtime
            
            # 检查删除的文件
            for file_path in list(self.file_times.keys()):
                if file_path not in current_files:
                    self.callback(file_path, 'deleted')
                    del self.file_times[file_path]