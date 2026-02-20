#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
密钥管理工具类

提供密钥管理，安全存储和访问敏感信息等功能
"""
import os
import json
import base64
import hashlib
from typing import Dict, Optional, Any, List


class SecretsUtils:
    """
    密钥管理工具类
    """

    @staticmethod
    def encrypt_string(value: str, key: str) -> str:
        """
        加密字符串

        Args:
            value: 要加密的字符串
            key: 加密密钥

        Returns:
            加密后的字符串
        """
        try:
            from cryptography.fernet import Fernet
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
            import secrets

            # 生成密钥
            salt = secrets.token_bytes(16)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            derived_key = base64.urlsafe_b64encode(kdf.derive(key.encode()))
            fernet = Fernet(derived_key)

            # 加密
            encrypted = fernet.encrypt(value.encode())

            # 返回 salt + 加密数据
            return base64.urlsafe_b64encode(salt + encrypted).decode()
        except Exception as e:
            # 如果加密失败，返回原始值（不推荐在生产环境使用）
            return value

    @staticmethod
    def decrypt_string(encrypted_value: str, key: str) -> str:
        """
        解密字符串

        Args:
            encrypted_value: 加密的字符串
            key: 解密密钥

        Returns:
            解密后的字符串
        """
        try:
            from cryptography.fernet import Fernet
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

            # 解码
            data = base64.urlsafe_b64decode(encrypted_value.encode())
            salt = data[:16]
            encrypted = data[16:]

            # 生成密钥
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            derived_key = base64.urlsafe_b64encode(kdf.derive(key.encode()))
            fernet = Fernet(derived_key)

            # 解密
            decrypted = fernet.decrypt(encrypted)
            return decrypted.decode()
        except Exception as e:
            # 如果解密失败，返回原始值
            return encrypted_value

    @staticmethod
    def load_secrets(file_path: str, password: str = None) -> Dict[str, Any]:
        """
        加载密钥文件

        Args:
            file_path: 密钥文件路径
            password: 解密密码

        Returns:
            密钥字典
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 如果文件被加密
            if 'encrypted' in data and data['encrypted']:
                if not password:
                    raise ValueError("Password is required for encrypted secrets file")
                
                # 解密数据
                encrypted_data = data['data']
                decrypted_data = SecretsUtils.decrypt_string(encrypted_data, password)
                return json.loads(decrypted_data)
            else:
                return data.get('data', {})
        except Exception as e:
            return {}

    @staticmethod
    def save_secrets(file_path: str, secrets: Dict[str, Any], password: str = None) -> bool:
        """
        保存密钥文件

        Args:
            file_path: 密钥文件路径
            secrets: 密钥字典
            password: 加密密码

        Returns:
            是否成功
        """
        try:
            if password:
                # 加密数据
                data_str = json.dumps(secrets)
                encrypted_data = SecretsUtils.encrypt_string(data_str, password)
                output_data = {
                    'encrypted': True,
                    'data': encrypted_data
                }
            else:
                # 不加密
                output_data = {
                    'encrypted': False,
                    'data': secrets
                }

            # 确保目录存在
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # 写入文件
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)

            # 设置文件权限（仅当前用户可读写）
            if os.name == 'posix':  # Unix-like
                os.chmod(file_path, 0o600)

            return True
        except Exception as e:
            return False

    @staticmethod
    def get_secret(key: str, default: Optional[Any] = None, secrets_file: str = 'secrets.json', password: str = None) -> Optional[Any]:
        """
        获取密钥

        Args:
            key: 密钥键
            default: 默认值
            secrets_file: 密钥文件路径
            password: 解密密码

        Returns:
            密钥值或默认值
        """
        secrets = SecretsUtils.load_secrets(secrets_file, password)
        return secrets.get(key, default)

    @staticmethod
    def set_secret(key: str, value: Any, secrets_file: str = 'secrets.json', password: str = None) -> bool:
        """
        设置密钥

        Args:
            key: 密钥键
            value: 密钥值
            secrets_file: 密钥文件路径
            password: 加密密码

        Returns:
            是否成功
        """
        secrets = SecretsUtils.load_secrets(secrets_file, password)
        secrets[key] = value
        return SecretsUtils.save_secrets(secrets_file, secrets, password)

    @staticmethod
    def delete_secret(key: str, secrets_file: str = 'secrets.json', password: str = None) -> bool:
        """
        删除密钥

        Args:
            key: 密钥键
            secrets_file: 密钥文件路径
            password: 解密密码

        Returns:
            是否成功
        """
        secrets = SecretsUtils.load_secrets(secrets_file, password)
        if key in secrets:
            del secrets[key]
            return SecretsUtils.save_secrets(secrets_file, secrets, password)
        return True

    @staticmethod
    def generate_secret(length: int = 32) -> str:
        """
        生成随机密钥

        Args:
            length: 密钥长度

        Returns:
            随机密钥
        """
        import secrets
        import string

        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    @staticmethod
    def generate_api_key(prefix: str = 'sk', length: int = 32) -> str:
        """
        生成 API 密钥

        Args:
            prefix: 密钥前缀
            length: 密钥长度

        Returns:
            API 密钥
        """
        import secrets
        import string

        alphabet = string.ascii_letters + string.digits
        secret_part = ''.join(secrets.choice(alphabet) for _ in range(length))
        return f"{prefix}_{secret_part}"

    @staticmethod
    def hash_password(password: str) -> str:
        """
        哈希密码

        Args:
            password: 原始密码

        Returns:
            哈希后的密码
        """
        try:
            import bcrypt
            return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        except Exception as e:
            # 如果 bcrypt 不可用，使用简单的哈希（不推荐在生产环境使用）
            return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        """
        检查密码

        Args:
            password: 原始密码
            hashed_password: 哈希后的密码

        Returns:
            密码是否正确
        """
        try:
            import bcrypt
            return bcrypt.checkpw(password.encode(), hashed_password.encode())
        except Exception as e:
            # 如果 bcrypt 不可用，使用简单的哈希比较（不推荐在生产环境使用）
            return hashlib.sha256(password.encode()).hexdigest() == hashed_password

    @staticmethod
    def load_env_secrets(prefix: str = 'SECRET_', secrets_file: str = 'secrets.json', password: str = None) -> bool:
        """
        从密钥文件加载到环境变量

        Args:
            prefix: 环境变量前缀
            secrets_file: 密钥文件路径
            password: 解密密码

        Returns:
            是否成功
        """
        try:
            secrets = SecretsUtils.load_secrets(secrets_file, password)
            for key, value in secrets.items():
                env_key = f"{prefix}{key.upper()}"
                os.environ[env_key] = str(value)
            return True
        except Exception as e:
            return False

    @staticmethod
    def store_env_secrets(prefix: str = 'SECRET_', secrets_file: str = 'secrets.json', password: str = None) -> bool:
        """
        从环境变量存储到密钥文件

        Args:
            prefix: 环境变量前缀
            secrets_file: 密钥文件路径
            password: 加密密码

        Returns:
            是否成功
        """
        try:
            secrets = {}
            for key, value in os.environ.items():
                if key.startswith(prefix):
                    secret_key = key[len(prefix):].lower()
                    secrets[secret_key] = value
            return SecretsUtils.save_secrets(secrets_file, secrets, password)
        except Exception as e:
            return False

    @staticmethod
    def validate_secrets(required_secrets: List[str], secrets_file: str = 'secrets.json', password: str = None) -> List[str]:
        """
        验证必需的密钥

        Args:
            required_secrets: 必需的密钥列表
            secrets_file: 密钥文件路径
            password: 解密密码

        Returns:
            缺失的密钥列表
        """
        secrets = SecretsUtils.load_secrets(secrets_file, password)
        missing = []
        for secret in required_secrets:
            if secret not in secrets:
                missing.append(secret)
        return missing

    @staticmethod
    def rotate_secret(key: str, secrets_file: str = 'secrets.json', password: str = None) -> Optional[str]:
        """
        轮换密钥

        Args:
            key: 要轮换的密钥键
            secrets_file: 密钥文件路径
            password: 解密密码

        Returns:
            新的密钥值
        """
        new_secret = SecretsUtils.generate_secret()
        if SecretsUtils.set_secret(key, new_secret, secrets_file, password):
            return new_secret
        return None

    @staticmethod
    def backup_secrets(source_file: str = 'secrets.json', backup_file: str = 'secrets.backup.json', password: str = None) -> bool:
        """
        备份密钥文件

        Args:
            source_file: 源密钥文件路径
            backup_file: 备份文件路径
            password: 解密密码

        Returns:
            是否成功
        """
        try:
            secrets = SecretsUtils.load_secrets(source_file, password)
            return SecretsUtils.save_secrets(backup_file, secrets, password)
        except Exception as e:
            return False

    @staticmethod
    def restore_secrets(backup_file: str = 'secrets.backup.json', target_file: str = 'secrets.json', password: str = None) -> bool:
        """
        恢复密钥文件

        Args:
            backup_file: 备份文件路径
            target_file: 目标文件路径
            password: 解密密码

        Returns:
            是否成功
        """
        try:
            secrets = SecretsUtils.load_secrets(backup_file, password)
            return SecretsUtils.save_secrets(target_file, secrets, password)
        except Exception as e:
            return False

    @staticmethod
    def get_secrets_summary(secrets_file: str = 'secrets.json', password: str = None) -> Dict[str, Any]:
        """
        获取密钥摘要

        Args:
            secrets_file: 密钥文件路径
            password: 解密密码

        Returns:
            密钥摘要字典
        """
        try:
            secrets = SecretsUtils.load_secrets(secrets_file, password)
            summary = {
                'total_secrets': len(secrets),
                'secret_keys': list(secrets.keys()),
                'file_path': secrets_file
            }
            return summary
        except Exception as e:
            return {
                'total_secrets': 0,
                'secret_keys': [],
                'file_path': secrets_file,
                'error': str(e)
            }

    @staticmethod
    def clear_secrets(secrets_file: str = 'secrets.json') -> bool:
        """
        清除所有密钥

        Args:
            secrets_file: 密钥文件路径

        Returns:
            是否成功
        """
        try:
            if os.path.exists(secrets_file):
                os.remove(secrets_file)
            return True
        except Exception as e:
            return False

    @staticmethod
    def is_secret_file_secure(secrets_file: str = 'secrets.json') -> bool:
        """
        检查密钥文件是否安全

        Args:
            secrets_file: 密钥文件路径

        Returns:
            是否安全
        """
        try:
            if not os.path.exists(secrets_file):
                return False

            # 检查文件权限
            if os.name == 'posix':  # Unix-like
                import stat
                file_stat = os.stat(secrets_file)
                # 只允许所有者读写
                return file_stat.st_mode & (stat.S_IRWXG | stat.S_IRWXO) == 0
            else:  # Windows
                # Windows 权限检查比较复杂，这里简化处理
                return True
        except Exception as e:
            return False

    @staticmethod
    def get_aws_secrets(secret_name: str, region_name: str = 'us-east-1') -> Optional[Dict[str, Any]]:
        """
        从 AWS Secrets Manager 获取密钥

        Args:
            secret_name: 密钥名称
            region_name: AWS 区域

        Returns:
            密钥字典
        """
        try:
            import boto3
            from botocore.exceptions import ClientError

            session = boto3.session.Session()
            client = session.client(
                service_name='secretsmanager',
                region_name=region_name
            )

            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )

            if 'SecretString' in get_secret_value_response:
                return json.loads(get_secret_value_response['SecretString'])
            else:
                # 二进制密钥
                return {
                    'binary_secret': base64.b64encode(get_secret_value_response['SecretBinary']).decode()
                }
        except Exception as e:
            return None

    @staticmethod
    def get_gcp_secrets(secret_name: str, version_id: str = 'latest') -> Optional[Dict[str, Any]]:
        """
        从 GCP Secret Manager 获取密钥

        Args:
            secret_name: 密钥名称
            version_id: 版本 ID

        Returns:
            密钥字典
        """
        try:
            from google.cloud import secretmanager

            client = secretmanager.SecretManagerServiceClient()
            name = client.secret_version_path(
                os.environ.get('GOOGLE_CLOUD_PROJECT'),
                secret_name,
                version_id
            )

            response = client.access_secret_version(request={'name': name})
            secret_string = response.payload.data.decode('UTF-8')
            return json.loads(secret_string)
        except Exception as e:
            return None