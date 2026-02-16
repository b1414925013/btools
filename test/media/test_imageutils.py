#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ImageUtils 测试文件
"""
import unittest
import os
import tempfile
from PIL import Image
from btools.core.media.imageutils import ImageUtils


class TestImageUtils(unittest.TestCase):
    """
    ImageUtils 测试类
    """

    def setUp(self):
        """
        测试前的准备工作
        """
        # 创建临时目录用于测试
        self.temp_dir = tempfile.mkdtemp()
        # 创建测试图片
        self.test_image_path = os.path.join(self.temp_dir, "test_image.jpg")
        # 创建一个简单的测试图片
        img = Image.new('RGB', (200, 200), color='red')
        img.save(self.test_image_path)

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

    def test_resize(self):
        """
        测试调整图片大小
        """
        # 打开测试图片
        img = ImageUtils.open(self.test_image_path)
        # 调整图片大小
        resized_img = ImageUtils.resize(img, 100, 100)
        # 验证结果
        self.assertEqual(resized_img.size, (100, 100))

    def test_crop(self):
        """
        测试裁剪图片
        """
        # 打开测试图片
        img = ImageUtils.open(self.test_image_path)
        # 裁剪图片
        cropped_img = ImageUtils.crop(img, 50, 50, 150, 150)
        # 验证结果
        self.assertEqual(cropped_img.size, (100, 100))

    def test_thumbnail(self):
        """
        测试创建缩略图
        """
        # 打开测试图片
        img = ImageUtils.open(self.test_image_path)
        # 创建缩略图
        thumbnail_img = ImageUtils.thumbnail(img, (50, 50))
        # 验证结果
        self.assertTrue(thumbnail_img.size[0] <= 50)
        self.assertTrue(thumbnail_img.size[1] <= 50)

    def test_get_image_size(self):
        """
        测试获取图片大小
        """
        # 打开测试图片
        img = ImageUtils.open(self.test_image_path)
        # 获取图片大小
        size = ImageUtils.get_image_size(img)
        # 验证结果
        self.assertEqual(size, (200, 200))


if __name__ == '__main__':
    unittest.main()
