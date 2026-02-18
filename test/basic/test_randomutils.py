#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RandomUtil 测试文件
"""
import string
import unittest
from btools.core.basic import RandomUtil


class TestRandomUtil(unittest.TestCase):
    """
    RandomUtil 测试类
    """

    def test_randomInt(self):
        """
        测试生成随机整数
        """
        # 测试默认范围
        for _ in range(100):
            value = RandomUtil.randomInt()
            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 999999999)

        # 测试指定范围
        for _ in range(100):
            value = RandomUtil.randomInt(1, 10)
            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 10)

    def test_randomFloat(self):
        """
        测试生成随机浮点数
        """
        # 测试默认范围
        for _ in range(100):
            value = RandomUtil.randomFloat()
            self.assertIsInstance(value, float)
            self.assertGreaterEqual(value, 0.0)
            self.assertLess(value, 1.0)

        # 测试指定范围
        for _ in range(100):
            value = RandomUtil.randomFloat(1.0, 2.0)
            self.assertIsInstance(value, float)
            self.assertGreaterEqual(value, 1.0)
            self.assertLess(value, 2.0)

    def test_randomBool(self):
        """
        测试生成随机布尔值
        """
        for _ in range(100):
            value = RandomUtil.randomBool()
            self.assertIsInstance(value, bool)

    def test_randomStr(self):
        """
        测试生成随机字符串
        """
        # 测试默认长度和字符集
        for _ in range(100):
            value = RandomUtil.randomStr()
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 8)
            for char in value:
                self.assertIn(char, string.ascii_letters + string.digits)

        # 测试指定长度和字符集
        for _ in range(100):
            value = RandomUtil.randomStr(10, string.ascii_lowercase)
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 10)
            for char in value:
                self.assertIn(char, string.ascii_lowercase)

    def test_randomLowerStr(self):
        """
        测试生成随机小写字符串
        """
        for _ in range(100):
            value = RandomUtil.randomLowerStr(10)
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 10)
            self.assertTrue(value.islower())
            for char in value:
                self.assertIn(char, string.ascii_lowercase)

    def test_randomUpperStr(self):
        """
        测试生成随机大写字符串
        """
        for _ in range(100):
            value = RandomUtil.randomUpperStr(10)
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 10)
            self.assertTrue(value.isupper())
            for char in value:
                self.assertIn(char, string.ascii_uppercase)

    def test_randomNumberStr(self):
        """
        测试生成随机数字字符串
        """
        for _ in range(100):
            value = RandomUtil.randomNumberStr(10)
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 10)
            self.assertTrue(value.isdigit())

    def test_randomHexStr(self):
        """
        测试生成随机十六进制字符串
        """
        for _ in range(100):
            value = RandomUtil.randomHexStr(10)
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 10)
            for char in value:
                self.assertIn(char, string.hexdigits)

    def test_randomChar(self):
        """
        测试生成随机字符
        """
        # 测试默认字符集
        for _ in range(100):
            value = RandomUtil.randomChar()
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 1)
            self.assertIn(value, string.ascii_letters + string.digits)

        # 测试指定字符集
        for _ in range(100):
            value = RandomUtil.randomChar(string.ascii_lowercase)
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 1)
            self.assertIn(value, string.ascii_lowercase)

    def test_randomChoice(self):
        """
        测试从序列中随机选择一个元素
        """
        sequence = [1, 2, 3, 4, 5]
        for _ in range(100):
            value = RandomUtil.randomChoice(sequence)
            self.assertIn(value, sequence)

    def test_randomChoices(self):
        """
        测试从序列中随机选择多个元素（可重复）
        """
        sequence = [1, 2, 3, 4, 5]
        for _ in range(100):
            values = RandomUtil.randomChoices(sequence, k=3)
            self.assertIsInstance(values, list)
            self.assertEqual(len(values), 3)
            for value in values:
                self.assertIn(value, sequence)

    def test_randomSample(self):
        """
        测试从序列中随机选择多个元素（不可重复）
        """
        sequence = [1, 2, 3, 4, 5]
        for _ in range(100):
            values = RandomUtil.randomSample(sequence, k=3)
            self.assertIsInstance(values, list)
            self.assertEqual(len(values), 3)
            # 检查元素是否唯一
            self.assertEqual(len(set(values)), 3)
            for value in values:
                self.assertIn(value, sequence)

    def test_shuffle(self):
        """
        测试打乱序列
        """
        sequence = [1, 2, 3, 4, 5]
        original = sequence.copy()
        RandomUtil.shuffle(sequence)
        # 检查序列长度是否相同
        self.assertEqual(len(sequence), len(original))
        # 检查元素是否相同
        self.assertEqual(set(sequence), set(original))

    def test_randomBytes(self):
        """
        测试生成随机字节串
        """
        for _ in range(100):
            value = RandomUtil.randomBytes(8)
            self.assertIsInstance(value, bytes)
            self.assertEqual(len(value), 8)

    def test_randomUUID(self):
        """
        测试生成随机UUID
        """
        import re
        uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        
        for _ in range(100):
            value = RandomUtil.randomUUID()
            self.assertIsInstance(value, str)
            self.assertTrue(re.match(uuid_pattern, value))

    def test_randomColor(self):
        """
        测试生成随机颜色
        """
        import re
        
        # 测试不包含透明度
        color_pattern = r'^#[0-9a-f]{6}$'
        for _ in range(100):
            value = RandomUtil.randomColor()
            self.assertIsInstance(value, str)
            self.assertTrue(re.match(color_pattern, value))

        # 测试包含透明度
        color_with_alpha_pattern = r'^#[0-9a-f]{8}$'
        for _ in range(100):
            value = RandomUtil.randomColor(alpha=True)
            self.assertIsInstance(value, str)
            self.assertTrue(re.match(color_with_alpha_pattern, value))

    def test_randomEmail(self):
        """
        测试生成随机邮箱地址
        """
        import re
        email_pattern = r'^[a-z0-9]+@example\.com$'
        
        for _ in range(100):
            value = RandomUtil.randomEmail()
            self.assertIsInstance(value, str)
            self.assertTrue(re.match(email_pattern, value))

    def test_randomPhone(self):
        """
        测试生成随机手机号
        """
        import re
        phone_pattern = r'^138\d{8}$'
        
        for _ in range(100):
            value = RandomUtil.randomPhone()
            self.assertIsInstance(value, str)
            self.assertTrue(re.match(phone_pattern, value))

    def test_randomPassword(self):
        """
        测试生成随机密码
        """
        import re
        
        for _ in range(100):
            value = RandomUtil.randomPassword(12)
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 12)
            # 检查是否包含大小写字母、数字和特殊字符
            self.assertTrue(any(c.isupper() for c in value))
            self.assertTrue(any(c.islower() for c in value))
            self.assertTrue(any(c.isdigit() for c in value))
            self.assertTrue(any(c in string.punctuation for c in value))

    def test_randomDate(self):
        """
        测试生成随机日期
        """
        for _ in range(100):
            year, month, day = RandomUtil.randomDate(2000, 2020)
            self.assertIsInstance(year, int)
            self.assertIsInstance(month, int)
            self.assertIsInstance(day, int)
            self.assertGreaterEqual(year, 2000)
            self.assertLessEqual(year, 2020)
            self.assertGreaterEqual(month, 1)
            self.assertLessEqual(month, 12)
            self.assertGreaterEqual(day, 1)
            self.assertLessEqual(day, 31)

    def test_randomTime(self):
        """
        测试生成随机时间
        """
        for _ in range(100):
            hour, minute, second = RandomUtil.randomTime()
            self.assertIsInstance(hour, int)
            self.assertIsInstance(minute, int)
            self.assertIsInstance(second, int)
            self.assertGreaterEqual(hour, 0)
            self.assertLessEqual(hour, 23)
            self.assertGreaterEqual(minute, 0)
            self.assertLessEqual(minute, 59)
            self.assertGreaterEqual(second, 0)
            self.assertLessEqual(second, 59)

    def test_setSeed(self):
        """
        测试设置随机种子
        """
        # 设置种子后，生成的随机数应该相同
        RandomUtil.setSeed(12345)
        value1 = RandomUtil.randomInt()
        
        RandomUtil.setSeed(12345)
        value2 = RandomUtil.randomInt()
        
        self.assertEqual(value1, value2)

    def test_getRandom(self):
        """
        测试获取随机数生成器实例
        """
        import random
        
        r = RandomUtil.getRandom()
        self.assertIsInstance(r, type(random))

    def test_randomGaussian(self):
        """
        测试生成高斯分布的随机数
        """
        for _ in range(100):
            value = RandomUtil.randomGaussian()
            self.assertIsInstance(value, float)

    def test_randomTriangular(self):
        """
        测试生成三角形分布的随机数
        """
        for _ in range(100):
            value = RandomUtil.randomTriangular(1.0, 3.0, 2.0)
            self.assertIsInstance(value, float)
            self.assertGreaterEqual(value, 1.0)
            self.assertLessEqual(value, 3.0)

    def test_randomExpovariate(self):
        """
        测试生成指数分布的随机数
        """
        for _ in range(100):
            value = RandomUtil.randomExpovariate(1.0)
            self.assertIsInstance(value, float)
            self.assertGreater(value, 0.0)


if __name__ == '__main__':
    unittest.main()