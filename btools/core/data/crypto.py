"""加密解密工具类"""
import hashlib
import hmac
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asymmetric_padding
from cryptography.hazmat.primitives import serialization
import os


class CryptoUtils:
    """加密解密工具类"""

    @staticmethod
    def md5(data: str or bytes) -> str:
        """
        MD5哈希算法
        
        Args:
            data: 要哈希的数据，可以是字符串或字节
            
        Returns:
            str: MD5哈希值（十六进制字符串）
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        md5_obj = hashlib.md5()
        md5_obj.update(data)
        return md5_obj.hexdigest()

    @staticmethod
    def sha1(data: str or bytes) -> str:
        """
        SHA-1哈希算法
        
        Args:
            data: 要哈希的数据，可以是字符串或字节
            
        Returns:
            str: SHA-1哈希值（十六进制字符串）
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        sha1_obj = hashlib.sha1()
        sha1_obj.update(data)
        return sha1_obj.hexdigest()

    @staticmethod
    def sha256(data: str or bytes) -> str:
        """
        SHA-256哈希算法
        
        Args:
            data: 要哈希的数据，可以是字符串或字节
            
        Returns:
            str: SHA-256哈希值（十六进制字符串）
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        sha256_obj = hashlib.sha256()
        sha256_obj.update(data)
        return sha256_obj.hexdigest()

    @staticmethod
    def hmac_sha256(key: str or bytes, data: str or bytes) -> str:
        """
        HMAC-SHA256哈希算法
        
        Args:
            key: 密钥，可以是字符串或字节
            data: 要哈希的数据，可以是字符串或字节
            
        Returns:
            str: HMAC-SHA256哈希值（十六进制字符串）
        """
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(data, str):
            data = data.encode('utf-8')
        hmac_obj = hmac.new(key, data, hashlib.sha256)
        return hmac_obj.hexdigest()

    @staticmethod
    def aes_encrypt(data: str, key: str) -> str:
        """
        AES加密（ECB模式）
        
        Args:
            data: 要加密的字符串
            key: 密钥（16、24或32字节）
            
        Returns:
            str: 加密后的Base64编码字符串
        """
        # 确保密钥长度正确
        key = key.ljust(32)[:32].encode('utf-8')
        data = data.encode('utf-8')
        
        # 填充数据
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        
        # 创建加密器
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # 加密数据
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Base64编码
        return base64.b64encode(encrypted_data).decode('utf-8')

    @staticmethod
    def aes_decrypt(encrypted_data: str, key: str) -> str:
        """
        AES解密（ECB模式）
        
        Args:
            encrypted_data: 加密后的Base64编码字符串
            key: 密钥（16、24或32字节）
            
        Returns:
            str: 解密后的字符串
        """
        # 确保密钥长度正确
        key = key.ljust(32)[:32].encode('utf-8')
        
        # Base64解码
        encrypted_data = base64.b64decode(encrypted_data)
        
        # 创建解密器
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # 解密数据
        decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        
        # 移除填充
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
        
        return decrypted_data.decode('utf-8')

    @staticmethod
    def generate_rsa_keys(private_key_path: str = None, public_key_path: str = None, key_size: int = 2048):
        """
        生成RSA密钥对
        
        Args:
            private_key_path: 私钥保存路径
            public_key_path: 公钥保存路径
            key_size: 密钥大小（默认2048）
            
        Returns:
            tuple: (私钥PEM, 公钥PEM)
        """
        # 生成私钥
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        
        # 获取私钥PEM
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        # 获取公钥
        public_key = private_key.public_key()
        
        # 获取公钥PEM
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        # 保存密钥到文件
        if private_key_path:
            with open(private_key_path, 'wb') as f:
                f.write(private_pem)
        
        if public_key_path:
            with open(public_key_path, 'wb') as f:
                f.write(public_pem)
        
        return private_pem.decode('utf-8'), public_pem.decode('utf-8')

    @staticmethod
    def rsa_encrypt(data: str, public_key_pem: str) -> str:
        """
        RSA加密
        
        Args:
            data: 要加密的字符串
            public_key_pem: 公钥PEM字符串
            
        Returns:
            str: 加密后的Base64编码字符串
        """
        # 加载公钥
        public_key = serialization.load_pem_public_key(
            public_key_pem.encode('utf-8'),
            backend=default_backend()
        )
        
        # 加密数据
        encrypted_data = public_key.encrypt(
            data.encode('utf-8'),
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashlib.sha256()),
                algorithm=hashlib.sha256(),
                label=None
            )
        )
        
        # Base64编码
        return base64.b64encode(encrypted_data).decode('utf-8')

    @staticmethod
    def rsa_decrypt(encrypted_data: str, private_key_pem: str) -> str:
        """
        RSA解密
        
        Args:
            encrypted_data: 加密后的Base64编码字符串
            private_key_pem: 私钥PEM字符串
            
        Returns:
            str: 解密后的字符串
        """
        # 加载私钥
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode('utf-8'),
            password=None,
            backend=default_backend()
        )
        
        # Base64解码
        encrypted_data = base64.b64decode(encrypted_data)
        
        # 解密数据
        decrypted_data = private_key.decrypt(
            encrypted_data,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashlib.sha256()),
                algorithm=hashlib.sha256(),
                label=None
            )
        )
        
        return decrypted_data.decode('utf-8')

    @staticmethod
    def base64_encode(data: str or bytes) -> str:
        """
        Base64编码
        
        Args:
            data: 要编码的数据，可以是字符串或字节
            
        Returns:
            str: Base64编码后的字符串
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        return base64.b64encode(data).decode('utf-8')

    @staticmethod
    def base64_decode(encoded_data: str) -> str:
        """
        Base64解码
        
        Args:
            encoded_data: Base64编码后的字符串
            
        Returns:
            str: 解码后的字符串
        """
        return base64.b64decode(encoded_data).decode('utf-8')

    @staticmethod
    def generate_random_string(length: int) -> str:
        """
        生成随机字符串
        
        Args:
            length: 字符串长度
            
        Returns:
            str: 随机字符串
        """
        return base64.b64encode(os.urandom(length * 3 // 4)).decode('utf-8')[:length]
