# -*- coding: utf-8 -*-
"""
IO工具类模块
提供IO流的读写、复制、转换等功能
"""
import io
import sys
from typing import Union, Optional, IO, BinaryIO, TextIO, Any
import shutil
import os


class IOUtils:
    """
    IO工具类
    提供IO流的读写、复制、转换等功能
    """

    @staticmethod
    def read_bytes(input_stream: Union[BinaryIO, str, bytes]) -> bytes:
        """
        读取字节流

        Args:
            input_stream: 输入流，可以是二进制IO对象、文件路径或字节数据

        Returns:
            bytes: 读取的字节数据
        """
        if isinstance(input_stream, bytes):
            return input_stream
        elif isinstance(input_stream, str):
            with open(input_stream, 'rb') as f:
                return f.read()
        else:
            # 保存当前位置
            pos = input_stream.tell() if hasattr(input_stream, 'tell') else None
            try:
                # 尝试读取全部内容
                return input_stream.read()
            finally:
                # 恢复位置
                if pos is not None and hasattr(input_stream, 'seek'):
                    input_stream.seek(pos)

    @staticmethod
    def read_text(input_stream: Union[TextIO, str, bytes], encoding: str = 'utf-8') -> str:
        """
        读取文本流

        Args:
            input_stream: 输入流，可以是文本IO对象、文件路径或字节数据
            encoding: 编码方式

        Returns:
            str: 读取的文本内容
        """
        if isinstance(input_stream, str):
            if os.path.exists(input_stream):
                with open(input_stream, 'r', encoding=encoding) as f:
                    return f.read()
            else:
                return input_stream
        elif isinstance(input_stream, bytes):
            return input_stream.decode(encoding)
        else:
            # 保存当前位置
            pos = input_stream.tell() if hasattr(input_stream, 'tell') else None
            try:
                # 尝试读取全部内容
                return input_stream.read()
            finally:
                # 恢复位置
                if pos is not None and hasattr(input_stream, 'seek'):
                    input_stream.seek(pos)

    @staticmethod
    def write_bytes(output_stream: Union[BinaryIO, str], data: bytes) -> None:
        """
        写入字节流

        Args:
            output_stream: 输出流，可以是二进制IO对象或文件路径
            data: 要写入的字节数据
        """
        if isinstance(output_stream, str):
            with open(output_stream, 'wb') as f:
                f.write(data)
        else:
            output_stream.write(data)

    @staticmethod
    def write_text(output_stream: Union[TextIO, str], data: str, encoding: str = 'utf-8') -> None:
        """
        写入文本流

        Args:
            output_stream: 输出流，可以是文本IO对象或文件路径
            data: 要写入的文本内容
            encoding: 编码方式
        """
        if isinstance(output_stream, str):
            with open(output_stream, 'w', encoding=encoding) as f:
                f.write(data)
        else:
            output_stream.write(data)

    @staticmethod
    def copy(input_stream: Union[IO, str], output_stream: Union[IO, str], buffer_size: int = 8192) -> int:
        """
        复制流

        Args:
            input_stream: 输入流，可以是IO对象或文件路径
            output_stream: 输出流，可以是IO对象或文件路径
            buffer_size: 缓冲区大小

        Returns:
            int: 复制的字节数
        """
        # 处理文件路径
        if isinstance(input_stream, str):
            with open(input_stream, 'rb') as f:
                return IOUtils.copy(f, output_stream, buffer_size)
        elif isinstance(output_stream, str):
            with open(output_stream, 'wb') as f:
                return IOUtils.copy(input_stream, f, buffer_size)
        
        # 复制流
        count = 0
        while True:
            buf = input_stream.read(buffer_size)
            if not buf:
                break
            output_stream.write(buf)
            count += len(buf)
        return count

    @staticmethod
    def to_bytes_io(data: Union[str, bytes]) -> io.BytesIO:
        """
        转换为BytesIO对象

        Args:
            data: 数据，可以是字符串或字节

        Returns:
            io.BytesIO: BytesIO对象
        """
        if isinstance(data, str):
            return io.BytesIO(data.encode('utf-8'))
        else:
            return io.BytesIO(data)

    @staticmethod
    def to_string_io(data: Union[str, bytes], encoding: str = 'utf-8') -> io.StringIO:
        """
        转换为StringIO对象

        Args:
            data: 数据，可以是字符串或字节
            encoding: 编码方式

        Returns:
            io.StringIO: StringIO对象
        """
        if isinstance(data, bytes):
            return io.StringIO(data.decode(encoding))
        else:
            return io.StringIO(data)

    @staticmethod
    def close(io_obj: Optional[IO]) -> None:
        """
        关闭IO对象

        Args:
            io_obj: IO对象
        """
        if io_obj and hasattr(io_obj, 'close'):
            try:
                io_obj.close()
            except Exception:
                pass

    @staticmethod
    def get_available_bytes(input_stream: BinaryIO) -> int:
        """
        获取可用字节数

        Args:
            input_stream: 输入流

        Returns:
            int: 可用字节数
        """
        if hasattr(input_stream, 'size'):
            return input_stream.size
        elif hasattr(input_stream, 'getbuffer'):
            return len(input_stream.getbuffer())
        else:
            # 对于其他流，尝试读取并重置位置
            pos = input_stream.tell() if hasattr(input_stream, 'tell') else None
            try:
                # 读取所有内容
                data = input_stream.read()
                return len(data)
            finally:
                # 恢复位置
                if pos is not None and hasattr(input_stream, 'seek'):
                    input_stream.seek(pos)

    @staticmethod
    def skip(input_stream: IO, n: int) -> int:
        """
        跳过指定字节数

        Args:
            input_stream: 输入流
            n: 要跳过的字节数

        Returns:
            int: 实际跳过的字节数
        """
        if hasattr(input_stream, 'seek'):
            try:
                pos = input_stream.tell()
                input_stream.seek(pos + n)
                return n
            except Exception:
                pass
        
        # 如果无法seek，则读取并丢弃
        count = 0
        while count < n:
            buf = input_stream.read(min(8192, n - count))
            if not buf:
                break
            count += len(buf)
        return count

    @staticmethod
    def read_lines(input_stream: Union[TextIO, str], encoding: str = 'utf-8') -> list:
        """
        读取所有行

        Args:
            input_stream: 输入流，可以是文本IO对象或文件路径
            encoding: 编码方式

        Returns:
            list: 行列表
        """
        if isinstance(input_stream, str):
            with open(input_stream, 'r', encoding=encoding) as f:
                return f.readlines()
        else:
            return input_stream.readlines()

    @staticmethod
    def write_lines(output_stream: Union[TextIO, str], lines: list, encoding: str = 'utf-8') -> None:
        """
        写入多行

        Args:
            output_stream: 输出流，可以是文本IO对象或文件路径
            lines: 行列表
            encoding: 编码方式
        """
        if isinstance(output_stream, str):
            with open(output_stream, 'w', encoding=encoding) as f:
                f.writelines(lines)
        else:
            output_stream.writelines(lines)

    @staticmethod
    def is_closed(io_obj: IO) -> bool:
        """
        检查IO对象是否已关闭

        Args:
            io_obj: IO对象

        Returns:
            bool: 是否已关闭
        """
        if hasattr(io_obj, 'closed'):
            return io_obj.closed
        return False


# 便捷函数

def read_bytes(input_stream: Union[BinaryIO, str, bytes]) -> bytes:
    """
    读取字节流

    Args:
        input_stream: 输入流，可以是二进制IO对象、文件路径或字节数据

    Returns:
        bytes: 读取的字节数据
    """
    return IOUtils.read_bytes(input_stream)


def read_text(input_stream: Union[TextIO, str, bytes], encoding: str = 'utf-8') -> str:
    """
    读取文本流

    Args:
        input_stream: 输入流，可以是文本IO对象、文件路径或字节数据
        encoding: 编码方式

    Returns:
        str: 读取的文本内容
    """
    return IOUtils.read_text(input_stream, encoding)


def write_bytes(output_stream: Union[BinaryIO, str], data: bytes) -> None:
    """
    写入字节流

    Args:
        output_stream: 输出流，可以是二进制IO对象或文件路径
        data: 要写入的字节数据
    """
    IOUtils.write_bytes(output_stream, data)


def write_text(output_stream: Union[TextIO, str], data: str, encoding: str = 'utf-8') -> None:
    """
    写入文本流

    Args:
        output_stream: 输出流，可以是文本IO对象或文件路径
        data: 要写入的文本内容
        encoding: 编码方式
    """
    IOUtils.write_text(output_stream, data, encoding)


def copy(input_stream: Union[IO, str], output_stream: Union[IO, str], buffer_size: int = 8192) -> int:
    """
    复制流

    Args:
        input_stream: 输入流，可以是IO对象或文件路径
        output_stream: 输出流，可以是IO对象或文件路径
        buffer_size: 缓冲区大小

    Returns:
        int: 复制的字节数
    """
    return IOUtils.copy(input_stream, output_stream, buffer_size)


def to_bytes_io(data: Union[str, bytes]) -> io.BytesIO:
    """
    转换为BytesIO对象

    Args:
        data: 数据，可以是字符串或字节

    Returns:
        io.BytesIO: BytesIO对象
    """
    return IOUtils.to_bytes_io(data)


def to_string_io(data: Union[str, bytes], encoding: str = 'utf-8') -> io.StringIO:
    """
    转换为StringIO对象

    Args:
        data: 数据，可以是字符串或字节
        encoding: 编码方式

    Returns:
        io.StringIO: StringIO对象
    """
    return IOUtils.to_string_io(data, encoding)


def close(io_obj: Optional[IO]) -> None:
    """
    关闭IO对象

    Args:
        io_obj: IO对象
    """
    IOUtils.close(io_obj)


def get_available_bytes(input_stream: BinaryIO) -> int:
    """
    获取可用字节数

    Args:
        input_stream: 输入流

    Returns:
        int: 可用字节数
    """
    return IOUtils.get_available_bytes(input_stream)


def skip(input_stream: IO, n: int) -> int:
    """
    跳过指定字节数

    Args:
        input_stream: 输入流
        n: 要跳过的字节数

    Returns:
        int: 实际跳过的字节数
    """
    return IOUtils.skip(input_stream, n)


def read_lines(input_stream: Union[TextIO, str], encoding: str = 'utf-8') -> list:
    """
    读取所有行

    Args:
        input_stream: 输入流，可以是文本IO对象或文件路径
        encoding: 编码方式

    Returns:
        list: 行列表
    """
    return IOUtils.read_lines(input_stream, encoding)


def write_lines(output_stream: Union[TextIO, str], lines: list, encoding: str = 'utf-8') -> None:
    """
    写入多行

    Args:
        output_stream: 输出流，可以是文本IO对象或文件路径
        lines: 行列表
        encoding: 编码方式
    """
    IOUtils.write_lines(output_stream, lines, encoding)


def is_closed(io_obj: IO) -> bool:
    """
    检查IO对象是否已关闭

    Args:
        io_obj: IO对象

    Returns:
        bool: 是否已关闭
    """
    return IOUtils.is_closed(io_obj)
