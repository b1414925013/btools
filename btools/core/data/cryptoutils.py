# -*- coding: utf-8 -*-
"""
增强的加密工具模块
"""
import hashlib
import hmac
import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from typing import Any, Dict, Optional, Tuple, Union


class CryptoUtils:
    """
    加密工具类
    提供增强的加密和解密功能
    """

    @staticmethod
    def md5(text: Union[str, bytes]) -> str:
        """
        MD5加密

        Args:
            text: 要加密的文本

        Returns:
            MD5加密后的十六进制字符串
        """
        if isinstance(text, str):
            text = text.encode('utf-8')
        return hashlib.md5(text).hexdigest()

    @staticmethod
    def sha1(text: Union[str, bytes]) -> str:
        """
        SHA1加密

        Args:
            text: 要加密的文本

        Returns:
            SHA1加密后的十六进制字符串
        """
        if isinstance(text, str):
            text = text.encode('utf-8')
        return hashlib.sha1(text).hexdigest()

    @staticmethod
    def sha256(text: Union[str, bytes]) -> str:
        """
        SHA256加密

        Args:
            text: 要加密的文本

        Returns:
            SHA256加密后的十六进制字符串
        """
        if isinstance(text, str):
            text = text.encode('utf-8')
        return hashlib.sha256(text).hexdigest()

    @staticmethod
    def sha512(text: Union[str, bytes]) -> str:
        """
        SHA512加密

        Args:
            text: 要加密的文本

        Returns:
            SHA512加密后的十六进制字符串
        """
        if isinstance(text, str):
            text = text.encode('utf-8')
        return hashlib.sha512(text).hexdigest()

    @staticmethod
    def hmac_md5(key: Union[str, bytes], text: Union[str, bytes]) -> str:
        """
        HMAC-MD5加密

        Args:
            key: 密钥
            text: 要加密的文本

        Returns:
            HMAC-MD5加密后的十六进制字符串
        """
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(text, str):
            text = text.encode('utf-8')
        return hmac.new(key, text, hashlib.md5).hexdigest()

    @staticmethod
    def hmac_sha256(key: Union[str, bytes], text: Union[str, bytes]) -> str:
        """
        HMAC-SHA256加密

        Args:
            key: 密钥
            text: 要加密的文本

        Returns:
            HMAC-SHA256加密后的十六进制字符串
        """
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(text, str):
            text = text.encode('utf-8')
        return hmac.new(key, text, hashlib.sha256).hexdigest()

    @staticmethod
    def base64_encode(text: Union[str, bytes]) -> str:
        """
        Base64编码

        Args:
            text: 要编码的文本

        Returns:
            Base64编码后的字符串
        """
        if isinstance(text, str):
            text = text.encode('utf-8')
        return base64.b64encode(text).decode('utf-8')

    @staticmethod
    def base64_decode(text: str) -> bytes:
        """
        Base64解码

        Args:
            text: 要解码的Base64字符串

        Returns:
            解码后的字节
        """
        return base64.b64decode(text.encode('utf-8'))

    @staticmethod
    def generate_rsa_keys(bits: int = 2048) -> Tuple[str, str]:
        """
        生成RSA密钥对

        Args:
            bits: 密钥长度，默认2048

        Returns:
            (私钥, 公钥) 元组
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=bits,
            backend=default_backend()
        )
        
        # 生成私钥PEM
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
        
        # 生成公钥PEM
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        
        return private_pem, public_pem

    @staticmethod
    def rsa_encrypt(public_key_pem: str, text: Union[str, bytes]) -> str:
        """
        RSA加密

        Args:
            public_key_pem: 公钥PEM字符串
            text: 要加密的文本

        Returns:
            加密后的Base64字符串
        """
        if isinstance(text, str):
            text = text.encode('utf-8')
        
        # 加载公钥
        public_key = serialization.load_pem_public_key(
            public_key_pem.encode('utf-8'),
            backend=default_backend()
        )
        
        # 加密
        encrypted = public_key.encrypt(
            text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return CryptoUtils.base64_encode(encrypted)

    @staticmethod
    def rsa_decrypt(private_key_pem: str, encrypted_text: str) -> str:
        """
        RSA解密

        Args:
            private_key_pem: 私钥PEM字符串
            encrypted_text: 加密后的Base64字符串

        Returns:
            解密后的文本
        """
        # 加载私钥
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode('utf-8'),
            password=None,
            backend=default_backend()
        )
        
        # 解码并解密
        encrypted_data = CryptoUtils.base64_decode(encrypted_text)
        decrypted = private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return decrypted.decode('utf-8')

    @staticmethod
    def generate_aes_key(key_size: int = 256) -> str:
        """
        生成AES密钥

        Args:
            key_size: 密钥长度，默认256位

        Returns:
            Base64编码的AES密钥
        """
        import os
        key = os.urandom(key_size // 8)
        return CryptoUtils.base64_encode(key)

    @staticmethod
    def aes_encrypt(key: Union[str, bytes], text: Union[str, bytes], 
                   mode: str = 'CBC') -> Dict[str, str]:
        """
        AES加密

        Args:
            key: 密钥
            text: 要加密的文本
            mode: 加密模式，默认CBC

        Returns:
            包含密文和IV的字典
        """
        import os
        if isinstance(key, str):
            if len(key) % 4 == 0:
                # 假设是Base64编码的密钥
                key = CryptoUtils.base64_decode(key)
            else:
                # 直接使用字符串作为密钥
                key = key.encode('utf-8')
        
        if isinstance(text, str):
            text = text.encode('utf-8')
        
        # 生成IV
        iv = os.urandom(16)
        
        # 选择加密模式
        if mode == 'CBC':
            cipher = Cipher(
                algorithms.AES(key),
                modes.CBC(iv),
                backend=default_backend()
            )
        elif mode == 'ECB':
            cipher = Cipher(
                algorithms.AES(key),
                modes.ECB(),
                backend=default_backend()
            )
        else:
            raise ValueError(f"Unsupported mode: {mode}")
        
        # 加密
        encryptor = cipher.encryptor()
        
        # 填充
        padding_length = 16 - (len(text) % 16)
        text += bytes([padding_length]) * padding_length
        
        ciphertext = encryptor.update(text) + encryptor.finalize()
        
        return {
            'ciphertext': CryptoUtils.base64_encode(ciphertext),
            'iv': CryptoUtils.base64_encode(iv)
        }

    @staticmethod
    def aes_decrypt(key: Union[str, bytes], ciphertext: str, iv: str, 
                   mode: str = 'CBC', return_bytes: bool = False) -> Union[str, bytes]:
        """
        AES解密

        Args:
            key: 密钥
            ciphertext: 密文
            iv: 初始化向量
            mode: 加密模式，默认CBC
            return_bytes: 是否返回字节，默认False

        Returns:
            解密后的文本或字节
        """
        if isinstance(key, str):
            if len(key) % 4 == 0:
                # 假设是Base64编码的密钥
                key = CryptoUtils.base64_decode(key)
            else:
                # 直接使用字符串作为密钥
                key = key.encode('utf-8')
        
        # 解码
        ciphertext = CryptoUtils.base64_decode(ciphertext)
        iv = CryptoUtils.base64_decode(iv)
        
        # 选择加密模式
        if mode == 'CBC':
            cipher = Cipher(
                algorithms.AES(key),
                modes.CBC(iv),
                backend=default_backend()
            )
        elif mode == 'ECB':
            cipher = Cipher(
                algorithms.AES(key),
                modes.ECB(),
                backend=default_backend()
            )
        else:
            raise ValueError(f"Unsupported mode: {mode}")
        
        # 解密
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        
        # 去除填充
        padding_length = plaintext[-1]
        plaintext = plaintext[:-padding_length]
        
        if return_bytes:
            return plaintext
        try:
            return plaintext.decode('utf-8')
        except UnicodeDecodeError:
            return plaintext

    @staticmethod
    def password_hash(password: str, salt: Optional[str] = None) -> str:
        """
        密码哈希

        Args:
            password: 密码
            salt: 盐值，默认自动生成

        Returns:
            哈希后的密码
        """
        import os
        if salt is None:
            salt = os.urandom(16).hex()
        
        # 使用pbkdf2_hmac
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        )
        
        return f"{salt}${key.hex()}"

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """
        验证密码

        Args:
            password: 密码
            hashed_password: 哈希后的密码

        Returns:
            是否验证通过
        """
        try:
            salt, hashed = hashed_password.split('$')
            new_hash = CryptoUtils.password_hash(password, salt)
            return new_hash == hashed_password
        except:
            return False

    @staticmethod
    def generate_token(length: int = 32) -> str:
        """
        生成随机令牌

        Args:
            length: 令牌长度，默认32

        Returns:
            随机令牌
        """
        import os
        import binascii
        return binascii.hexlify(os.urandom(length // 2)).decode('utf-8')

    @staticmethod
    def encrypt_file(input_file: str, output_file: str, key: Union[str, bytes]):
        """
        加密文件

        Args:
            input_file: 输入文件路径
            output_file: 输出文件路径
            key: 密钥
        """
        import os
        
        if isinstance(key, str):
            if len(key) % 4 == 0:
                key = CryptoUtils.base64_decode(key)
            else:
                key = key.encode('utf-8')
        
        # 读取文件
        with open(input_file, 'rb') as f:
            data = f.read()
        
        # 加密
        result = CryptoUtils.aes_encrypt(key, data)
        
        # 写入文件
        with open(output_file, 'w', encoding='utf-8') as f:
            import json
            json.dump(result, f)

    @staticmethod
    def decrypt_file(input_file: str, output_file: str, key: Union[str, bytes]):
        """
        解密文件

        Args:
            input_file: 输入文件路径
            output_file: 输出文件路径
            key: 密钥
        """
        # 读取文件
        with open(input_file, 'r', encoding='utf-8') as f:
            import json
            data = json.load(f)
        
        # 解密，返回字节
        plaintext = CryptoUtils.aes_decrypt(key, data['ciphertext'], data['iv'], return_bytes=True)
        
        # 写入文件
        with open(output_file, 'wb') as f:
            f.write(plaintext)


# 便捷函数

def md5(text: Union[str, bytes]) -> str:
    """
    MD5加密

    Args:
        text: 要加密的文本

    Returns:
        MD5加密后的十六进制字符串
    """
    return CryptoUtils.md5(text)


def sha1(text: Union[str, bytes]) -> str:
    """
    SHA1加密

    Args:
        text: 要加密的文本

    Returns:
        SHA1加密后的十六进制字符串
    """
    return CryptoUtils.sha1(text)


def sha256(text: Union[str, bytes]) -> str:
    """
    SHA256加密

    Args:
        text: 要加密的文本

    Returns:
        SHA256加密后的十六进制字符串
    """
    return CryptoUtils.sha256(text)


def sha512(text: Union[str, bytes]) -> str:
    """
    SHA512加密

    Args:
        text: 要加密的文本

    Returns:
        SHA512加密后的十六进制字符串
    """
    return CryptoUtils.sha512(text)


def hmac_md5(key: Union[str, bytes], text: Union[str, bytes]) -> str:
    """
    HMAC-MD5加密

    Args:
        key: 密钥
        text: 要加密的文本

    Returns:
        HMAC-MD5加密后的十六进制字符串
    """
    return CryptoUtils.hmac_md5(key, text)


def hmac_sha256(key: Union[str, bytes], text: Union[str, bytes]) -> str:
    """
    HMAC-SHA256加密

    Args:
        key: 密钥
        text: 要加密的文本

    Returns:
        HMAC-SHA256加密后的十六进制字符串
    """
    return CryptoUtils.hmac_sha256(key, text)


def base64_encode(text: Union[str, bytes]) -> str:
    """
    Base64编码

    Args:
        text: 要编码的文本

    Returns:
        Base64编码后的字符串
    """
    return CryptoUtils.base64_encode(text)


def base64_decode(text: str) -> bytes:
    """
    Base64解码

    Args:
        text: 要解码的Base64字符串

    Returns:
        解码后的字节
    """
    return CryptoUtils.base64_decode(text)


def generate_rsa_keys(bits: int = 2048) -> Tuple[str, str]:
    """
    生成RSA密钥对

    Args:
        bits: 密钥长度，默认2048

    Returns:
        (私钥, 公钥) 元组
    """
    return CryptoUtils.generate_rsa_keys(bits)


def rsa_encrypt(public_key_pem: str, text: Union[str, bytes]) -> str:
    """
    RSA加密

    Args:
        public_key_pem: 公钥PEM字符串
        text: 要加密的文本

    Returns:
        加密后的Base64字符串
    """
    return CryptoUtils.rsa_encrypt(public_key_pem, text)


def rsa_decrypt(private_key_pem: str, encrypted_text: str) -> str:
    """
    RSA解密

    Args:
        private_key_pem: 私钥PEM字符串
        encrypted_text: 加密后的Base64字符串

    Returns:
        解密后的文本
    """
    return CryptoUtils.rsa_decrypt(private_key_pem, encrypted_text)


def generate_aes_key(key_size: int = 256) -> str:
    """
    生成AES密钥

    Args:
        key_size: 密钥长度，默认256位

    Returns:
        Base64编码的AES密钥
    """
    return CryptoUtils.generate_aes_key(key_size)


def aes_encrypt(key: Union[str, bytes], text: Union[str, bytes], 
               mode: str = 'CBC') -> Dict[str, str]:
    """
    AES加密

    Args:
        key: 密钥
        text: 要加密的文本
        mode: 加密模式，默认CBC

    Returns:
        包含密文和IV的字典
    """
    return CryptoUtils.aes_encrypt(key, text, mode)


def aes_decrypt(key: Union[str, bytes], ciphertext: str, iv: str, 
               mode: str = 'CBC') -> str:
    """
    AES解密

    Args:
        key: 密钥
        ciphertext: 密文
        iv: 初始化向量
        mode: 加密模式，默认CBC

    Returns:
        解密后的文本
    """
    return CryptoUtils.aes_decrypt(key, ciphertext, iv, mode)


def password_hash(password: str, salt: Optional[str] = None) -> str:
    """
    密码哈希

    Args:
        password: 密码
        salt: 盐值，默认自动生成

    Returns:
        哈希后的密码
    """
    return CryptoUtils.password_hash(password, salt)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    验证密码

    Args:
        password: 密码
        hashed_password: 哈希后的密码

    Returns:
        是否验证通过
    """
    return CryptoUtils.verify_password(password, hashed_password)


def generate_token(length: int = 32) -> str:
    """
    生成随机令牌

    Args:
        length: 令牌长度，默认32

    Returns:
        随机令牌
    """
    return CryptoUtils.generate_token(length)


def encrypt_file(input_file: str, output_file: str, key: Union[str, bytes]):
    """
    加密文件

    Args:
        input_file: 输入文件路径
        output_file: 输出文件路径
        key: 密钥
    """
    CryptoUtils.encrypt_file(input_file, output_file, key)


def decrypt_file(input_file: str, output_file: str, key: Union[str, bytes]):
    """
    解密文件

    Args:
        input_file: 输入文件路径
        output_file: 输出文件路径
        key: 密钥
    """
    CryptoUtils.decrypt_file(input_file, output_file, key)
