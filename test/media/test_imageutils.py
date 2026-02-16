#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ImageUtils 测试文件
"""
import unittest
import os
import tempfile
from btools.core.media.imageutils import ImageUtils


class TestImageUtils(unittest.TestCase):
    """
    ImageUtils 测试类
    """

    def setUp(self):
        """
        测试前的准备工作
        """
        self.image_utils = ImageUtils()
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

    def test_resize_image(self):
        """
        测试调整图片大小
        """
        # 创建测试图片路径
        test_image = os.path.join(self.temp_dir, "test_image.jpg")
        # 创建一个简单的测试图片
        self.image_utils.create_thumbnail(test_image, width=100, height=100)
        
        # 调整图片大小
        output_image = os.path.join(self.temp_dir, "resized_image.jpg")
        result = self.image_utils.resize_image(test_image, 200, 200, output_image)
        
        # 验证结果
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_image))

    def test_crop_image(self):
        """
        测试裁剪图片
        """
        # 创建测试图片路径
        test_image = os.path.join(self.temp_dir, "test_image.jpg")
        # 创建一个简单的测试图片
        self.image_utils.create_thumbnail(test_image, width=200, height=200)
        
        # 裁剪图片
        output_image = os.path.join(self.temp_dir, "cropped_image.jpg")
        result = self.image_utils.crop_image(test_image, 50, 50, 100, 100, output_image)
        
        # 验证结果
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_image))

    def test_convert_image_format(self):
        """
        测试转换图片格式
        """
        # 创建测试图片路径
        test_image = os.path.join(self.temp_dir, "test_image.jpg")
        # 创建一个简单的测试图片
        self.image_utils.create_thumbnail(test_image, width=100, height=100)
        
        # 转换图片格式
        output_image = os.path.join(self.temp_dir, "converted_image.png")
        result = self.image_utils.convert_image_format(test_image, output_image)
        
        # 验证结果
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_image))

    def test_create_thumbnail(self):
        """
        测试创建缩略图
        """
        # 创建缩略图
        thumbnail_path = os.path.join(self.temp_dir, "thumbnail.jpg")
        result = self.image_utils.create_thumbnail(thumbnail_path, width=100, height=100)
        
        # 验证结果
        self.assertTrue(result)
        self.assertTrue(os.path.exists(thumbnail_path))

    def test_get_image_info(self):
        """
        测试获取图片信息
        """
        # 创建测试图片路径
        test_image = os.path.join(self.temp_dir, "test_image.jpg")
        # 创建一个简单的测试图片
        self.image_utils.create_thumbnail(test_image, width=100, height=100)
        
        # 获取图片信息
        info = self.image_utils.get_image_info(test_image)
        
        # 验证结果
        self.assertIsInstance(info, dict)
        self.assertIn('width', info)
        self.assertIn('height', info)
        self.assertIn('format', info)


if __name__ == '__main__':
    unittest.main()
