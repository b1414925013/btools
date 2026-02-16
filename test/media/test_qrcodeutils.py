#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QrCodeUtils 测试文件
"""
import unittest
import os
import tempfile
from btools.core.media.qrcodeutils import QrCodeUtils


class TestQrCodeUtils(unittest.TestCase):
    """
    QrCodeUtils 测试类
    """

    def setUp(self):
        """
        测试前的准备工作
        """
        # 创建临时目录用于测试
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """
        测试后的清理工作
        """
        # 清理临时目录
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(self.temp_dir)

    def test_generate_qr_code(self):
        """
        测试生成二维码
        """
        # 生成二维码
        qr_code_path = os.path.join(self.temp_dir, "test_qr_code.png")
        data = "https://github.com/btools-dev/btools"
        result = QrCodeUtils.save_qr_code(data, qr_code_path)
        
        # 验证结果
        self.assertTrue(result)
        self.assertTrue(os.path.exists(qr_code_path))

    def test_generate_qr_code_with_options(self):
        """
        测试带选项生成二维码
        """
        # 生成带选项的二维码
        qr_code_path = os.path.join(self.temp_dir, "test_qr_code_with_options.png")
        data = "https://github.com/btools-dev/btools"
        result = QrCodeUtils.save_qr_code(
            data, 
            qr_code_path, 
            box_size=10, 
            border=4
        )
        
        # 验证结果
        self.assertTrue(result)
        self.assertTrue(os.path.exists(qr_code_path))

    def test_read_qr_code(self):
        """
        测试读取二维码
        """
        # 首先生成一个二维码
        qr_code_path = os.path.join(self.temp_dir, "test_qr_code.png")
        expected_data = "https://github.com/btools-dev/btools"
        QrCodeUtils.save_qr_code(expected_data, qr_code_path)
        
        # 读取二维码
        result = QrCodeUtils.decode_qr_code_from_file(qr_code_path)
        
        # 验证结果
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_data)

    def test_generate_qr_code_with_logo(self):
        """
        测试生成带 logo 的二维码
        """
        # 创建一个简单的测试 logo
        logo_path = os.path.join(self.temp_dir, "logo.png")
        # 生成一个小的二维码作为 logo
        QrCodeUtils.save_qr_code("logo", logo_path, box_size=2, border=1)
        
        # 生成带 logo 的二维码
        qr_code_path = os.path.join(self.temp_dir, "test_qr_code_with_logo.png")
        data = "https://github.com/btools-dev/btools"
        result = QrCodeUtils.save_qr_code_with_logo(data, logo_path, qr_code_path)
        
        # 验证结果
        self.assertTrue(result)
        self.assertTrue(os.path.exists(qr_code_path))


if __name__ == '__main__':
    unittest.main()
