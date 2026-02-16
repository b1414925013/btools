"""压缩工具类"""
import zipfile
import tarfile
import gzip
import bz2
import lzma
import os
import shutil
from typing import Any, List, Optional, Union


class CompressUtils:
    """压缩工具类"""

    @staticmethod
    def zip_directory(directory: str, output_path: str, include_root: bool = False) -> None:
        """
        压缩目录为ZIP文件
        
        Args:
            directory: 要压缩的目录
            output_path: 输出ZIP文件路径
            include_root: 是否包含根目录
        """
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            directory = os.path.abspath(directory)
            base_dir = os.path.dirname(directory) if include_root else directory
            
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, base_dir)
                    zipf.write(file_path, arcname)

    @staticmethod
    def zip_files(files: List[str], output_path: str) -> None:
        """
        压缩多个文件为ZIP文件
        
        Args:
            files: 要压缩的文件列表
            output_path: 输出ZIP文件路径
        """
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                if os.path.exists(file):
                    arcname = os.path.basename(file)
                    zipf.write(file, arcname)

    @staticmethod
    def unzip(zip_path: str, extract_dir: str) -> None:
        """
        解压ZIP文件
        
        Args:
            zip_path: ZIP文件路径
            extract_dir: 解压目录
        """
        os.makedirs(extract_dir, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_dir)

    @staticmethod
    def create_tar_gz(directory: str, output_path: str, include_root: bool = False) -> None:
        """
        创建tar.gz文件
        
        Args:
            directory: 要压缩的目录
            output_path: 输出tar.gz文件路径
            include_root: 是否包含根目录
        """
        with tarfile.open(output_path, 'w:gz') as tarf:
            directory = os.path.abspath(directory)
            base_dir = os.path.dirname(directory) if include_root else directory
            
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, base_dir)
                    tarf.add(file_path, arcname)

    @staticmethod
    def create_tar_bz2(directory: str, output_path: str, include_root: bool = False) -> None:
        """
        创建tar.bz2文件
        
        Args:
            directory: 要压缩的目录
            output_path: 输出tar.bz2文件路径
            include_root: 是否包含根目录
        """
        with tarfile.open(output_path, 'w:bz2') as tarf:
            directory = os.path.abspath(directory)
            base_dir = os.path.dirname(directory) if include_root else directory
            
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, base_dir)
                    tarf.add(file_path, arcname)

    @staticmethod
    def create_tar_xz(directory: str, output_path: str, include_root: bool = False) -> None:
        """
        创建tar.xz文件
        
        Args:
            directory: 要压缩的目录
            output_path: 输出tar.xz文件路径
            include_root: 是否包含根目录
        """
        with tarfile.open(output_path, 'w:xz') as tarf:
            directory = os.path.abspath(directory)
            base_dir = os.path.dirname(directory) if include_root else directory
            
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, base_dir)
                    tarf.add(file_path, arcname)

    @staticmethod
    def extract_tar(tar_path: str, extract_dir: str) -> None:
        """
        解压tar文件（支持tar.gz、tar.bz2、tar.xz）
        
        Args:
            tar_path: tar文件路径
            extract_dir: 解压目录
        """
        os.makedirs(extract_dir, exist_ok=True)
        with tarfile.open(tar_path, 'r') as tarf:
            tarf.extractall(extract_dir)

    @staticmethod
    def gzip_file(file_path: str, output_path: Optional[str] = None) -> None:
        """
        压缩文件为gzip格式
        
        Args:
            file_path: 要压缩的文件
            output_path: 输出gzip文件路径，默认为原文件路径加.gz后缀
        """
        if output_path is None:
            output_path = f"{file_path}.gz"
        
        with open(file_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    @staticmethod
    def gunzip_file(gzip_path: str, output_path: Optional[str] = None) -> None:
        """
        解压gzip文件
        
        Args:
            gzip_path: gzip文件路径
            output_path: 输出文件路径，默认为原文件路径去掉.gz后缀
        """
        if output_path is None:
            output_path = gzip_path.rstrip('.gz')
        
        with gzip.open(gzip_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    @staticmethod
    def bzip2_file(file_path: str, output_path: Optional[str] = None) -> None:
        """
        压缩文件为bzip2格式
        
        Args:
            file_path: 要压缩的文件
            output_path: 输出bzip2文件路径，默认为原文件路径加.bz2后缀
        """
        if output_path is None:
            output_path = f"{file_path}.bz2"
        
        with open(file_path, 'rb') as f_in:
            with bz2.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    @staticmethod
    def bunzip2_file(bzip2_path: str, output_path: Optional[str] = None) -> None:
        """
        解压bzip2文件
        
        Args:
            bzip2_path: bzip2文件路径
            output_path: 输出文件路径，默认为原文件路径去掉.bz2后缀
        """
        if output_path is None:
            output_path = bzip2_path.rstrip('.bz2')
        
        with bz2.open(bzip2_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    @staticmethod
    def lzma_file(file_path: str, output_path: Optional[str] = None) -> None:
        """
        压缩文件为lzma格式
        
        Args:
            file_path: 要压缩的文件
            output_path: 输出lzma文件路径，默认为原文件路径加.xz后缀
        """
        if output_path is None:
            output_path = f"{file_path}.xz"
        
        with open(file_path, 'rb') as f_in:
            with lzma.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    @staticmethod
    def unlzma_file(lzma_path: str, output_path: Optional[str] = None) -> None:
        """
        解压lzma文件
        
        Args:
            lzma_path: lzma文件路径
            output_path: 输出文件路径，默认为原文件路径去掉.xz后缀
        """
        if output_path is None:
            output_path = lzma_path.rstrip('.xz')
        
        with lzma.open(lzma_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    @staticmethod
    def is_zip_file(file_path: str) -> bool:
        """
        检查文件是否为ZIP文件
        
        Args:
            file_path: 文件路径
            
        Returns:
            bool: 如果是ZIP文件则返回True，否则返回False
        """
        return zipfile.is_zipfile(file_path)

    @staticmethod
    def is_tar_file(file_path: str) -> bool:
        """
        检查文件是否为tar文件
        
        Args:
            file_path: 文件路径
            
        Returns:
            bool: 如果是tar文件则返回True，否则返回False
        """
        try:
            with tarfile.open(file_path, 'r') as tarf:
                return True
        except Exception:
            return False

    @staticmethod
    def get_zip_info(zip_path: str) -> List[dict]:
        """
        获取ZIP文件信息
        
        Args:
            zip_path: ZIP文件路径
            
        Returns:
            List[dict]: ZIP文件内文件信息列表
        """
        info_list = []
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            for info in zipf.infolist():
                info_list.append({
                    'name': info.filename,
                    'size': info.file_size,
                    'compressed_size': info.compress_size,
                    'modified': info.date_time,
                    'is_dir': info.filename.endswith('/')
                })
        return info_list

    @staticmethod
    def get_tar_info(tar_path: str) -> List[dict]:
        """
        获取tar文件信息
        
        Args:
            tar_path: tar文件路径
            
        Returns:
            List[dict]: tar文件内文件信息列表
        """
        info_list = []
        with tarfile.open(tar_path, 'r') as tarf:
            for member in tarf.getmembers():
                info_list.append({
                    'name': member.name,
                    'size': member.size,
                    'mode': member.mode,
                    'type': member.type,
                    'modified': member.mtime,
                    'is_dir': member.isdir()
                })
        return info_list

    @staticmethod
    def compress_file(file_path: str, output_path: str, compression_type: str = 'zip') -> None:
        """
        压缩文件（根据指定类型）
        
        Args:
            file_path: 要压缩的文件
            output_path: 输出文件路径
            compression_type: 压缩类型，支持 'zip', 'gzip', 'bzip2', 'lzma'
        """
        if compression_type == 'zip':
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                arcname = os.path.basename(file_path)
                zipf.write(file_path, arcname)
        elif compression_type == 'gzip':
            CompressUtils.gzip_file(file_path, output_path)
        elif compression_type == 'bzip2':
            CompressUtils.bzip2_file(file_path, output_path)
        elif compression_type == 'lzma':
            CompressUtils.lzma_file(file_path, output_path)
        else:
            raise ValueError(f"Unsupported compression type: {compression_type}")

    @staticmethod
    def decompress_file(compressed_path: str, output_path: Optional[str] = None) -> None:
        """
        解压文件（自动检测类型）
        
        Args:
            compressed_path: 压缩文件路径
            output_path: 输出文件路径
        """
        if CompressUtils.is_zip_file(compressed_path):
            if output_path is None:
                output_path = os.path.splitext(compressed_path)[0]
            os.makedirs(output_path, exist_ok=True)
            CompressUtils.unzip(compressed_path, output_path)
        elif CompressUtils.is_tar_file(compressed_path):
            if output_path is None:
                output_path = os.path.splitext(os.path.splitext(compressed_path)[0])[0]
            os.makedirs(output_path, exist_ok=True)
            CompressUtils.extract_tar(compressed_path, output_path)
        elif compressed_path.endswith('.gz'):
            CompressUtils.gunzip_file(compressed_path, output_path)
        elif compressed_path.endswith('.bz2'):
            CompressUtils.bunzip2_file(compressed_path, output_path)
        elif compressed_path.endswith('.xz'):
            CompressUtils.unlzma_file(compressed_path, output_path)
        else:
            raise ValueError(f"Unsupported compression format: {compressed_path}")