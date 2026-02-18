# -*- coding: utf-8 -*-
"""
测试数据生成工具测试
"""
import unittest
from btools.core.automation.fakerutils import (
    FakerUtils, random_string, random_integer, random_float, random_boolean, 
    random_date, random_datetime, random_email, random_phone, random_name, 
    random_address, random_company, random_position, random_id_card, 
    random_bank_card, random_ip, random_url, random_user_agent, 
    random_credit_card, random_user, random_product, random_order, 
    generate_test_data
)


class TestFakerUtils(unittest.TestCase):
    """
    测试数据生成工具测试类
    """

    def test_random_string(self):
        """
        测试生成随机字符串
        """
        # 测试默认长度
        result = FakerUtils.random_string()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 10)
        
        # 测试指定长度
        result = FakerUtils.random_string(20)
        self.assertEqual(len(result), 20)
        
        # 测试包含特殊字符
        result = FakerUtils.random_string(10, include_special=True)
        self.assertEqual(len(result), 10)

    def test_random_integer(self):
        """
        测试生成随机整数
        """
        result = FakerUtils.random_integer()
        self.assertIsInstance(result, int)
        
        # 测试指定范围
        result = FakerUtils.random_integer(1, 100)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 100)

    def test_random_float(self):
        """
        测试生成随机浮点数
        """
        result = FakerUtils.random_float()
        self.assertIsInstance(result, float)
        
        # 测试指定范围和小数位数
        result = FakerUtils.random_float(1.0, 10.0, 3)
        self.assertGreaterEqual(result, 1.0)
        self.assertLessEqual(result, 10.0)
        self.assertEqual(len(str(result).split('.')[1]), 3)

    def test_random_boolean(self):
        """
        测试生成随机布尔值
        """
        result = FakerUtils.random_boolean()
        self.assertIsInstance(result, bool)

    def test_random_email(self):
        """
        测试生成随机邮箱地址
        """
        result = FakerUtils.random_email()
        self.assertIsInstance(result, str)
        self.assertIn('@', result)
        
        # 测试指定域名
        result = FakerUtils.random_email('test.com')
        self.assertEndsWith(result, '@test.com')

    def test_random_phone(self):
        """
        测试生成随机手机号码
        """
        result = FakerUtils.random_phone()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 11)
        
        # 测试指定前缀
        result = FakerUtils.random_phone('138')
        self.assertStartsWith(result, '138')
        self.assertEqual(len(result), 11)

    def test_random_name(self):
        """
        测试生成随机中文姓名
        """
        result = FakerUtils.random_name()
        self.assertIsInstance(result, str)

    def test_random_address(self):
        """
        测试生成随机地址
        """
        result = FakerUtils.random_address()
        self.assertIsInstance(result, str)

    def test_random_company(self):
        """
        测试生成随机公司名称
        """
        result = FakerUtils.random_company()
        self.assertIsInstance(result, str)

    def test_random_position(self):
        """
        测试生成随机职位
        """
        result = FakerUtils.random_position()
        self.assertIsInstance(result, str)

    def test_random_id_card(self):
        """
        测试生成随机身份证号
        """
        result = FakerUtils.random_id_card()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 18)

    def test_random_bank_card(self):
        """
        测试生成随机银行卡号
        """
        result = FakerUtils.random_bank_card()
        self.assertIsInstance(result, str)
        self.assertGreaterEqual(len(result), 16)
        self.assertLessEqual(len(result), 19)

    def test_random_ip(self):
        """
        测试生成随机IP地址
        """
        result = FakerUtils.random_ip()
        self.assertIsInstance(result, str)
        parts = result.split('.')
        self.assertEqual(len(parts), 4)
        for part in parts:
            self.assertTrue(0 <= int(part) <= 255)

    def test_random_url(self):
        """
        测试生成随机URL
        """
        result = FakerUtils.random_url()
        self.assertIsInstance(result, str)
        self.assertIn('://', result)

    def test_random_user_agent(self):
        """
        测试生成随机User-Agent
        """
        result = FakerUtils.random_user_agent()
        self.assertIsInstance(result, str)

    def test_random_credit_card(self):
        """
        测试生成随机信用卡信息
        """
        result = FakerUtils.random_credit_card()
        self.assertIsInstance(result, dict)
        self.assertIn('number', result)
        self.assertIn('expiry', result)
        self.assertIn('cvv', result)

    def test_random_user(self):
        """
        测试生成随机用户信息
        """
        result = FakerUtils.random_user()
        self.assertIsInstance(result, dict)
        self.assertIn('name', result)
        self.assertIn('email', result)
        self.assertIn('phone', result)
        self.assertIn('address', result)
        self.assertIn('company', result)
        self.assertIn('position', result)
        self.assertIn('id_card', result)
        self.assertIn('bank_card', result)
        self.assertIn('ip', result)

    def test_random_product(self):
        """
        测试生成随机产品信息
        """
        result = FakerUtils.random_product()
        self.assertIsInstance(result, dict)
        self.assertIn('name', result)
        self.assertIn('price', result)
        self.assertIn('stock', result)
        self.assertIn('sku', result)
        self.assertIn('category', result)
        self.assertIn('description', result)

    def test_random_order(self):
        """
        测试生成随机订单信息
        """
        result = FakerUtils.random_order()
        self.assertIsInstance(result, dict)
        self.assertIn('order_id', result)
        self.assertIn('user_id', result)
        self.assertIn('total_amount', result)
        self.assertIn('order_time', result)
        self.assertIn('status', result)
        self.assertIn('payment_method', result)

    def test_generate_test_data(self):
        """
        测试根据模板生成测试数据
        """
        template = {
            "name": "name",
            "email": "email",
            "phone": "phone",
            "age": "integer",
            "salary": "float",
            "active": "boolean",
            "address": "address",
            "company": "company",
            "position": "position",
            "id_card": "id_card",
            "bank_card": "bank_card",
            "ip": "ip",
            "url": "url",
            "user_agent": "user_agent",
            "date": "date",
            "datetime": "datetime",
            "user": "user",
            "product": "product",
            "order": "order"
        }
        
        result = FakerUtils.generate_test_data(template)
        self.assertIsInstance(result, dict)
        for key in template.keys():
            self.assertIn(key, result)

    def test_convenience_functions(self):
        """
        测试便捷函数
        """
        # 测试random_string
        result = random_string()
        self.assertIsInstance(result, str)
        
        # 测试random_integer
        result = random_integer()
        self.assertIsInstance(result, int)
        
        # 测试random_float
        result = random_float()
        self.assertIsInstance(result, float)
        
        # 测试random_boolean
        result = random_boolean()
        self.assertIsInstance(result, bool)
        
        # 测试random_email
        result = random_email()
        self.assertIsInstance(result, str)
        
        # 测试random_phone
        result = random_phone()
        self.assertIsInstance(result, str)
        
        # 测试random_name
        result = random_name()
        self.assertIsInstance(result, str)
        
        # 测试random_address
        result = random_address()
        self.assertIsInstance(result, str)
        
        # 测试random_company
        result = random_company()
        self.assertIsInstance(result, str)
        
        # 测试random_position
        result = random_position()
        self.assertIsInstance(result, str)
        
        # 测试random_id_card
        result = random_id_card()
        self.assertIsInstance(result, str)
        
        # 测试random_bank_card
        result = random_bank_card()
        self.assertIsInstance(result, str)
        
        # 测试random_ip
        result = random_ip()
        self.assertIsInstance(result, str)
        
        # 测试random_url
        result = random_url()
        self.assertIsInstance(result, str)
        
        # 测试random_user_agent
        result = random_user_agent()
        self.assertIsInstance(result, str)
        
        # 测试random_credit_card
        result = random_credit_card()
        self.assertIsInstance(result, dict)
        
        # 测试random_user
        result = random_user()
        self.assertIsInstance(result, dict)
        
        # 测试random_product
        result = random_product()
        self.assertIsInstance(result, dict)
        
        # 测试random_order
        result = random_order()
        self.assertIsInstance(result, dict)
        
        # 测试generate_test_data
        template = {"name": "name", "age": "integer"}
        result = generate_test_data(template)
        self.assertIsInstance(result, dict)

    def assertStartsWith(self, string, prefix):
        """
        断言字符串以指定前缀开头
        """
        self.assertTrue(string.startswith(prefix))

    def assertEndsWith(self, string, suffix):
        """
        断言字符串以指定后缀结尾
        """
        self.assertTrue(string.endswith(suffix))


if __name__ == '__main__':
    unittest.main()