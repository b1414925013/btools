# -*- coding: utf-8 -*-
"""
IO工具类测试
"""
import unittest
import tempfile
import os
import io

from btools.core.data.ioutils import (
    IOUtils, read_bytes, read_text, write_bytes, write_text,
    copy, to_bytes_io, to_string_io, close, get_available_bytes,
    skip, read_lines, write_lines, is_closed
)


class TestIOUtils(unittest.TestCase):
    """
    IO工具类测试
    """

    def setUp(self):
        """
        测试前的准备工作
        """
        # 创建测试文件
        self.test_txt_file = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False)
        self.test_txt_file.write('Hello, World!\nThis is a test file.')
        self.test_txt_file.close()
        
        self.test_bin_file = tempfile.NamedTemporaryFile(mode='wb', suffix='.bin', delete=False)
        self.test_bin_file.write(b'Hello, World!')
        self.test_bin_file.close()

    def tearDown(self):
        """
        测试后的清理工作
        """
        if os.path.exists(self.test_txt_file.name):
            os.unlink(self.test_txt_file.name)
        if os.path.exists(self.test_bin_file.name):
            os.unlink(self.test_bin_file.name)

    def test_read_bytes(self):
        """
        测试读取字节流
        """
        # 从文件路径读取
        bytes_data = IOUtils.read_bytes(self.test_bin_file.name)
        self.assertEqual(bytes_data, b'Hello, World!')
        
        # 从BytesIO对象读取
        buffer = io.BytesIO(b'Hello, World!')
        bytes_data = IOUtils.read_bytes(buffer)
        self.assertEqual(bytes_data, b'Hello, World!')
        
        # 直接传递字节数据
        bytes_data = IOUtils.read_bytes(b'Hello, World!')
        self.assertEqual(bytes_data, b'Hello, World!')

    def test_read_text(self):
        """
        测试读取文本流
        """
        # 从文件路径读取
        text = IOUtils.read_text(self.test_txt_file.name)
        self.assertIn('Hello, World!', text)
        self.assertIn('This is a test file.', text)
        
        # 从StringIO对象读取
        buffer = io.StringIO('Hello, World!')
        text = IOUtils.read_text(buffer)
        self.assertEqual(text, 'Hello, World!')
        
        # 从字节数据读取
        text = IOUtils.read_text(b'Hello, World!', encoding='utf-8')
        self.assertEqual(text, 'Hello, World!')
        
        # 直接传递字符串
        text = IOUtils.read_text('Hello, World!')
        self.assertEqual(text, 'Hello, World!')

    def test_write_bytes(self):
        """
        测试写入字节流
        """
        # 写入到临时文件
        temp_out = tempfile.NamedTemporaryFile(mode='wb', suffix='.bin', delete=False)
        temp_out.close()
        
        IOUtils.write_bytes(temp_out.name, b'Hello, World!')
        
        # 验证写入成功
        with open(temp_out.name, 'rb') as f:
            content = f.read()
            self.assertEqual(content, b'Hello, World!')
        
        os.unlink(temp_out.name)
        
        # 写入到BytesIO对象
        buffer = io.BytesIO()
        IOUtils.write_bytes(buffer, b'Hello, World!')
        buffer.seek(0)
        self.assertEqual(buffer.read(), b'Hello, World!')

    def test_write_text(self):
        """
        测试写入文本流
        """
        # 写入到临时文件
        temp_out = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False)
        temp_out.close()
        
        IOUtils.write_text(temp_out.name, 'Hello, World!')
        
        # 验证写入成功
        with open(temp_out.name, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertEqual(content, 'Hello, World!')
        
        os.unlink(temp_out.name)
        
        # 写入到StringIO对象
        buffer = io.StringIO()
        IOUtils.write_text(buffer, 'Hello, World!')
        buffer.seek(0)
        self.assertEqual(buffer.read(), 'Hello, World!')

    def test_copy(self):
        """
        测试复制流
        """
        # 复制文件
        temp_out = tempfile.NamedTemporaryFile(mode='wb', suffix='.txt', delete=False)
        temp_out.close()
        
        bytes_copied = IOUtils.copy(self.test_txt_file.name, temp_out.name)
        self.assertGreater(bytes_copied, 0)
        
        # 验证复制成功
        with open(temp_out.name, 'rb') as f:
            content = f.read()
            self.assertIn(b'Hello, World!', content)
        
        os.unlink(temp_out.name)
        
        # 复制IO对象
        source = io.BytesIO(b'Hello, World!')
        destination = io.BytesIO()
        bytes_copied = IOUtils.copy(source, destination)
        self.assertEqual(bytes_copied, 13)
        destination.seek(0)
        self.assertEqual(destination.read(), b'Hello, World!')

    def test_to_bytes_io(self):
        """
        测试转换为BytesIO对象
        """
        # 从字符串转换
        bytes_io = IOUtils.to_bytes_io('Hello, World!')
        self.assertEqual(bytes_io.getvalue(), b'Hello, World!')
        
        # 从字节转换
        bytes_io = IOUtils.to_bytes_io(b'Hello, World!')
        self.assertEqual(bytes_io.getvalue(), b'Hello, World!')

    def test_to_string_io(self):
        """
        测试转换为StringIO对象
        """
        # 从字符串转换
        string_io = IOUtils.to_string_io('Hello, World!')
        self.assertEqual(string_io.getvalue(), 'Hello, World!')
        
        # 从字节转换
        string_io = IOUtils.to_string_io(b'Hello, World!', encoding='utf-8')
        self.assertEqual(string_io.getvalue(), 'Hello, World!')

    def test_close(self):
        """
        测试关闭IO对象
        """
        buffer = io.BytesIO(b'Hello, World!')
        self.assertFalse(is_closed(buffer))
        
        IOUtils.close(buffer)
        self.assertTrue(is_closed(buffer))

    def test_get_available_bytes(self):
        """
        测试获取可用字节数
        """
        buffer = io.BytesIO(b'Hello, World!')
        available = IOUtils.get_available_bytes(buffer)
        self.assertEqual(available, 13)

    def test_skip(self):
        """
        测试跳过指定字节数
        """
        buffer = io.BytesIO(b'Hello, World!')
        skipped = IOUtils.skip(buffer, 5)
        self.assertEqual(skipped, 5)
        self.assertEqual(buffer.read(), b', World!')

    def test_read_lines(self):
        """
        测试读取所有行
        """
        # 从文件读取
        lines = IOUtils.read_lines(self.test_txt_file.name)
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0].strip(), 'Hello, World!')
        self.assertEqual(lines[1].strip(), 'This is a test file.')
        
        # 从StringIO对象读取
        buffer = io.StringIO('Line 1\nLine 2\nLine 3')
        lines = IOUtils.read_lines(buffer)
        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0].strip(), 'Line 1')
        self.assertEqual(lines[1].strip(), 'Line 2')
        self.assertEqual(lines[2].strip(), 'Line 3')

    def test_write_lines(self):
        """
        测试写入多行
        """
        # 写入到临时文件
        temp_out = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False)
        temp_out.close()
        
        lines = ['Line 1', 'Line 2', 'Line 3']
        IOUtils.write_lines(temp_out.name, lines)
        
        # 验证写入成功
        with open(temp_out.name, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('Line 1', content)
            self.assertIn('Line 2', content)
            self.assertIn('Line 3', content)
        
        os.unlink(temp_out.name)
        
        # 写入到StringIO对象
        buffer = io.StringIO()
        IOUtils.write_lines(buffer, lines)
        buffer.seek(0)
        content = buffer.read()
        self.assertIn('Line 1', content)
        self.assertIn('Line 2', content)
        self.assertIn('Line 3', content)

    def test_is_closed(self):
        """
        测试检查IO对象是否已关闭
        """
        buffer = io.BytesIO(b'Hello, World!')
        self.assertFalse(IOUtils.is_closed(buffer))
        
        buffer.close()
        self.assertTrue(IOUtils.is_closed(buffer))

    def test_convenience_functions(self):
        """
        测试便捷函数
        """
        # 测试read_bytes
        bytes_data = read_bytes(b'Hello, World!')
        self.assertEqual(bytes_data, b'Hello, World!')
        
        # 测试read_text
        text = read_text('Hello, World!')
        self.assertEqual(text, 'Hello, World!')
        
        # 测试to_bytes_io
        bytes_io = to_bytes_io('Hello, World!')
        self.assertEqual(bytes_io.getvalue(), b'Hello, World!')
        
        # 测试to_string_io
        string_io = to_string_io('Hello, World!')
        self.assertEqual(string_io.getvalue(), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
