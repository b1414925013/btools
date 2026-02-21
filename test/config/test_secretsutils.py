"""测试SecretsUtils类"""
import unittest
import os
import tempfile
import json
from btools.core.config.secretsutils import SecretsUtils


class TestSecretsUtils(unittest.TestCase):
    """测试SecretsUtils类"""

    def setUp(self):
        """设置测试环境"""
        self.temp_file = tempfile.mktemp(suffix=".json")
        self.test_secrets = {
            'database_password': 'test_password',
            'api_key': 'sk_test_123',
            'private_key': 'test_private_key'
        }

    def tearDown(self):
        """清理测试环境"""
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_save_and_load_secrets(self):
        """测试保存和加载密钥"""
        # 保存密钥
        success = SecretsUtils.save_secrets(self.temp_file, self.test_secrets)
        self.assertTrue(success)

        # 加载密钥
        loaded = SecretsUtils.load_secrets(self.temp_file)
        self.assertEqual(loaded['database_password'], 'test_password')

    def test_get_and_set_secret(self):
        """测试获取和设置密钥"""
        # 保存初始密钥
        SecretsUtils.save_secrets(self.temp_file, self.test_secrets)

        # 获取密钥
        value = SecretsUtils.get_secret('api_key', secrets_file=self.temp_file)
        self.assertEqual(value, 'sk_test_123')

        # 设置新密钥
        success = SecretsUtils.set_secret('new_secret', 'new_value', secrets_file=self.temp_file)
        self.assertTrue(success)

        # 验证新密钥
        new_value = SecretsUtils.get_secret('new_secret', secrets_file=self.temp_file)
        self.assertEqual(new_value, 'new_value')

    def test_delete_secret(self):
        """测试删除密钥"""
        SecretsUtils.save_secrets(self.temp_file, self.test_secrets)
        success = SecretsUtils.delete_secret('private_key', secrets_file=self.temp_file)
        self.assertTrue(success)

        loaded = SecretsUtils.load_secrets(self.temp_file)
        self.assertNotIn('private_key', loaded)

    def test_generate_secret(self):
        """测试生成随机密钥"""
        secret = SecretsUtils.generate_secret()
        self.assertIsNotNone(secret)
        self.assertEqual(len(secret), 32)

        long_secret = SecretsUtils.generate_secret(length=64)
        self.assertEqual(len(long_secret), 64)

    def test_generate_api_key(self):
        """测试生成API密钥"""
        api_key = SecretsUtils.generate_api_key(prefix='sk', length=32)
        self.assertTrue(api_key.startswith('sk_'))
        self.assertGreater(len(api_key), len('sk_'))

    def test_hash_and_check_password(self):
        """测试密码哈希和验证"""
        hashed = SecretsUtils.hash_password('my_password')
        self.assertIsNotNone(hashed)

        is_valid = SecretsUtils.check_password('my_password', hashed)
        self.assertTrue(is_valid)

        is_invalid = SecretsUtils.check_password('wrong_password', hashed)
        self.assertFalse(is_invalid)

    def test_validate_secrets(self):
        """测试验证必需的密钥"""
        SecretsUtils.save_secrets(self.temp_file, self.test_secrets)
        missing = SecretsUtils.validate_secrets(
            ['database_password', 'api_key', 'non_existent'],
            secrets_file=self.temp_file
        )
        self.assertEqual(missing, ['non_existent'])

    def test_get_secrets_summary(self):
        """测试获取密钥摘要"""
        SecretsUtils.save_secrets(self.temp_file, self.test_secrets)
        summary = SecretsUtils.get_secrets_summary(self.temp_file)
        self.assertEqual(summary['total_secrets'], 3)
        self.assertIn('database_password', summary['secret_keys'])

    def test_clear_secrets(self):
        """测试清除所有密钥"""
        SecretsUtils.save_secrets(self.temp_file, self.test_secrets)
        self.assertTrue(os.path.exists(self.temp_file))

        success = SecretsUtils.clear_secrets(self.temp_file)
        self.assertTrue(success)
        self.assertFalse(os.path.exists(self.temp_file))


if __name__ == "__main__":
    unittest.main()
