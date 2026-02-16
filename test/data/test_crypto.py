# -*- coding: utf-8 -*-
"""
加密工具测试
"""
import unittest
import tempfile
import os
from btools.core.data.crypto import (
    CryptoUtils, md5, sha1, sha256, sha512, hmac_md5, hmac_sha256,
    base64_encode, base64_decode, generate_rsa_keys, rsa_encrypt, rsa_decrypt,
    generate_aes_key, aes_encrypt, aes_decrypt, password_hash, verify_password,
    generate_token, encrypt_file, decrypt_file
)


class TestCryptoUtils(unittest.TestCase):
    """
    加密工具测试类
    """

    def setUp(self):
        """
        测试前设置
        """
        self.test_text = "测试文本"
        self.test_key = "测试密钥"

    def test_md5(self):
        """
        测试MD5加密
        """
        result = CryptoUtils.md5(self.test_text)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 32)  # MD5结果长度为32

        # 测试字节输入
        result_bytes = CryptoUtils.md5(self.test_text.encode('utf-8'))
        self.assertEqual(result, result_bytes)

    def test_sha1(self):
        """
        测试SHA1加密
        """
        result = CryptoUtils.sha1(self.test_text)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 40)  # SHA1结果长度为40

    def test_sha256(self):
        """
        测试SHA256加密
        """
        result = CryptoUtils.sha256(self.test_text)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 64)  # SHA256结果长度为64

    def test_sha512(self):
        """
        测试SHA512加密
        """
        result = CryptoUtils.sha512(self.test_text)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 128)  # SHA512结果长度为128

    def test_hmac_functions(self):
        """
        测试HMAC函数
        """
        # 测试HMAC-MD5
        hmac_md5_result = CryptoUtils.hmac_md5(self.test_key, self.test_text)
        self.assertIsInstance(hmac_md5_result, str)
        self.assertEqual(len(hmac_md5_result), 32)

        # 测试HMAC-SHA256
        hmac_sha256_result = CryptoUtils.hmac_sha256(self.test_key, self.test_text)
        self.assertIsInstance(hmac_sha256_result, str)
        self.assertEqual(len(hmac_sha256_result), 64)

    def test_base64_functions(self):
        """
        测试Base64编码解码
        """
        # 测试编码
        encoded = CryptoUtils.base64_encode(self.test_text)
        self.assertIsInstance(encoded, str)

        # 测试解码
        decoded = CryptoUtils.base64_decode(encoded)
        self.assertIsInstance(decoded, bytes)
        self.assertEqual(decoded.decode('utf-8'), self.test_text)

    def test_rsa_functions(self):
        """
        测试RSA加密解密
        """
        # 生成密钥对
        private_key, public_key = CryptoUtils.generate_rsa_keys(bits=1024)  # 使用1024位密钥以加快测试速度
        self.assertIsInstance(private_key, str)
        self.assertIsInstance(public_key, str)

        # 测试加密
        encrypted = CryptoUtils.rsa_encrypt(public_key, self.test_text)
        self.assertIsInstance(encrypted, str)

        # 测试解密
        decrypted = CryptoUtils.rsa_decrypt(private_key, encrypted)
        self.assertEqual(decrypted, self.test_text)

    def test_aes_functions(self):
        """
        测试AES加密解密
        """
        # 生成AES密钥
        aes_key = CryptoUtils.generate_aes_key()
        self.assertIsInstance(aes_key, str)

        # 测试CBC模式加密
        encrypted = CryptoUtils.aes_encrypt(aes_key, self.test_text, mode='CBC')
        self.assertIsInstance(encrypted, dict)
        self.assertIn('ciphertext', encrypted)
        self.assertIn('iv', encrypted)

        # 测试CBC模式解密
        decrypted = CryptoUtils.aes_decrypt(aes_key, encrypted['ciphertext'], encrypted['iv'], mode='CBC')
        self.assertEqual(decrypted, self.test_text)

    def test_password_hash_functions(self):
        """
        测试密码哈希和验证
        """
        # 测试密码哈希
        hashed = CryptoUtils.password_hash(self.test_text)
        self.assertIsInstance(hashed, str)
        self.assertIn('$', hashed)

        # 测试密码验证（正确密码）
        self.assertTrue(CryptoUtils.verify_password(self.test_text, hashed))

        # 测试密码验证（错误密码）
        self.assertFalse(CryptoUtils.verify_password('错误密码', hashed))

    def test_generate_token(self):
        """
        测试生成令牌
        """
        # 测试默认长度
        token = CryptoUtils.generate_token()
        self.assertIsInstance(token, str)
        self.assertEqual(len(token), 32)  # 默认长度32

        # 测试自定义长度
        token_64 = CryptoUtils.generate_token(length=64)
        self.assertEqual(len(token_64), 64)

    def test_file_encryption(self):
        """
        测试文件加密解密
        """
        # 创建临时文件，使用UTF-8编码
        with tempfile.NamedTemporaryFile(mode='wb', suffix='.txt', delete=False) as f:
            f.write(self.test_text.encode('utf-8'))
            input_file = f.name

        encrypted_file = input_file + '.encrypted'
        decrypted_file = input_file + '.decrypted'

        try:
            # 生成AES密钥
            aes_key = CryptoUtils.generate_aes_key()

            # 测试加密文件
            CryptoUtils.encrypt_file(input_file, encrypted_file, aes_key)
            self.assertTrue(os.path.exists(encrypted_file))

            # 测试解密文件
            CryptoUtils.decrypt_file(encrypted_file, decrypted_file, aes_key)
            self.assertTrue(os.path.exists(decrypted_file))

            # 验证解密后的内容
            with open(decrypted_file, 'rb') as f:
                content = f.read()
            self.assertEqual(content, self.test_text.encode('utf-8'))
        finally:
            # 清理临时文件
            for file in [input_file, encrypted_file, decrypted_file]:
                if os.path.exists(file):
                    os.unlink(file)

    def test_convenience_functions(self):
        """
        测试便捷函数
        """
        # 测试md5便捷函数
        self.assertIsInstance(md5(self.test_text), str)

        # 测试sha1便捷函数
        self.assertIsInstance(sha1(self.test_text), str)

        # 测试sha256便捷函数
        self.assertIsInstance(sha256(self.test_text), str)

        # 测试sha512便捷函数
        self.assertIsInstance(sha512(self.test_text), str)

        # 测试hmac_md5便捷函数
        self.assertIsInstance(hmac_md5(self.test_key, self.test_text), str)

        # 测试hmac_sha256便捷函数
        self.assertIsInstance(hmac_sha256(self.test_key, self.test_text), str)

        # 测试base64_encode便捷函数
        encoded = base64_encode(self.test_text)
        self.assertIsInstance(encoded, str)

        # 测试base64_decode便捷函数
        self.assertIsInstance(base64_decode(encoded), bytes)

        # 测试generate_token便捷函数
        self.assertIsInstance(generate_token(), str)

        # 测试password_hash便捷函数
        hashed = password_hash(self.test_text)
        self.assertIsInstance(hashed, str)

        # 测试verify_password便捷函数
        self.assertTrue(verify_password(self.test_text, hashed))


if __name__ == '__main__':
    unittest.main()
