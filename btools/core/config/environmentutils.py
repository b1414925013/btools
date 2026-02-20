#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
环境变量管理工具类

提供环境变量管理，不同环境配置切换等功能
"""
import os
import dotenv
from typing import Dict, Optional, Any, List


class EnvironmentUtils:
    """
    环境变量管理工具类
    """

    @staticmethod
    def load_env(file_path: str = '.env') -> bool:
        """
        加载环境变量文件

        Args:
            file_path: 环境变量文件路径

        Returns:
            是否成功
        """
        try:
            dotenv.load_dotenv(file_path)
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_env(key: str, default: Optional[Any] = None) -> Optional[str]:
        """
        获取环境变量

        Args:
            key: 环境变量键
            default: 默认值

        Returns:
            环境变量值或默认值
        """
        return os.getenv(key, default)

    @staticmethod
    def get_env_int(key: str, default: int = 0) -> int:
        """
        获取整型环境变量

        Args:
            key: 环境变量键
            default: 默认值

        Returns:
            整型环境变量值或默认值
        """
        value = os.getenv(key)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            return default

    @staticmethod
    def get_env_bool(key: str, default: bool = False) -> bool:
        """
        获取布尔型环境变量

        Args:
            key: 环境变量键
            default: 默认值

        Returns:
            布尔型环境变量值或默认值
        """
        value = os.getenv(key)
        if value is None:
            return default
        return value.lower() in ('true', '1', 'yes', 'y', 't')

    @staticmethod
    def get_env_float(key: str, default: float = 0.0) -> float:
        """
        获取浮点型环境变量

        Args:
            key: 环境变量键
            default: 默认值

        Returns:
            浮点型环境变量值或默认值
        """
        value = os.getenv(key)
        if value is None:
            return default
        try:
            return float(value)
        except ValueError:
            return default

    @staticmethod
    def set_env(key: str, value: str) -> None:
        """
        设置环境变量

        Args:
            key: 环境变量键
            value: 环境变量值
        """
        os.environ[key] = value

    @staticmethod
    def unset_env(key: str) -> None:
        """
        取消设置环境变量

        Args:
            key: 环境变量键
        """
        if key in os.environ:
            del os.environ[key]

    @staticmethod
    def has_env(key: str) -> bool:
        """
        检查环境变量是否存在

        Args:
            key: 环境变量键

        Returns:
            是否存在
        """
        return key in os.environ

    @staticmethod
    def get_all_env() -> Dict[str, str]:
        """
        获取所有环境变量

        Returns:
            环境变量字典
        """
        return dict(os.environ)

    @staticmethod
    def get_env_prefix(prefix: str) -> Dict[str, str]:
        """
        获取指定前缀的环境变量

        Args:
            prefix: 环境变量前缀

        Returns:
            环境变量字典
        """
        result = {}
        for key, value in os.environ.items():
            if key.startswith(prefix):
                result[key] = value
        return result

    @staticmethod
    def load_environment(environment: str = 'development') -> bool:
        """
        加载指定环境的配置

        Args:
            environment: 环境名称

        Returns:
            是否成功
        """
        # 尝试加载对应环境的配置文件
        env_files = [
            f'.env.{environment}',
            f'.env.{environment}.local',
            '.env'
        ]

        success = False
        for env_file in env_files:
            if os.path.exists(env_file):
                if EnvironmentUtils.load_env(env_file):
                    success = True

        # 设置当前环境
        EnvironmentUtils.set_env('ENVIRONMENT', environment)

        return success

    @staticmethod
    def get_current_environment() -> str:
        """
        获取当前环境

        Returns:
            当前环境名称
        """
        return EnvironmentUtils.get_env('ENVIRONMENT', 'development')

    @staticmethod
    def is_development() -> bool:
        """
        是否为开发环境

        Returns:
            是否为开发环境
        """
        return EnvironmentUtils.get_current_environment() == 'development'

    @staticmethod
    def is_production() -> bool:
        """
        是否为生产环境

        Returns:
            是否为生产环境
        """
        return EnvironmentUtils.get_current_environment() == 'production'

    @staticmethod
    def is_test() -> bool:
        """
        是否为测试环境

        Returns:
            是否为测试环境
        """
        return EnvironmentUtils.get_current_environment() == 'test'

    @staticmethod
    def export_env(file_path: str = '.env') -> bool:
        """
        导出环境变量到文件

        Args:
            file_path: 导出文件路径

        Returns:
            是否成功
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                for key, value in os.environ.items():
                    f.write(f"{key}={value}\n")
            return True
        except Exception as e:
            return False

    @staticmethod
    def validate_environment(required_vars: List[str]) -> List[str]:
        """
        验证环境变量

        Args:
            required_vars: 必需的环境变量列表

        Returns:
            缺失的环境变量列表
        """
        missing_vars = []
        for var in required_vars:
            if not EnvironmentUtils.has_env(var):
                missing_vars.append(var)
        return missing_vars

    @staticmethod
    def override_env(vars: Dict[str, str]) -> None:
        """
        覆盖环境变量

        Args:
            vars: 要覆盖的环境变量字典
        """
        for key, value in vars.items():
            EnvironmentUtils.set_env(key, value)

    @staticmethod
    def get_env_list(key: str, separator: str = ',', default: List[str] = None) -> List[str]:
        """
        获取列表型环境变量

        Args:
            key: 环境变量键
            separator: 分隔符
            default: 默认值

        Returns:
            列表型环境变量值或默认值
        """
        value = os.getenv(key)
        if value is None:
            return default or []
        return [item.strip() for item in value.split(separator) if item.strip()]

    @staticmethod
    def get_env_dict(key: str, pair_separator: str = ',', kv_separator: str = '=', default: Dict[str, str] = None) -> Dict[str, str]:
        """
        获取字典型环境变量

        Args:
            key: 环境变量键
            pair_separator: 键值对分隔符
            kv_separator: 键值分隔符
            default: 默认值

        Returns:
            字典型环境变量值或默认值
        """
        value = os.getenv(key)
        if value is None:
            return default or {}

        result = {}
        for pair in value.split(pair_separator):
            if kv_separator in pair:
                k, v = pair.split(kv_separator, 1)
                result[k.strip()] = v.strip()

        return result

    @staticmethod
    def reload_env() -> bool:
        """
        重新加载环境变量

        Returns:
            是否成功
        """
        # 清除当前环境变量
        for key in list(os.environ.keys()):
            if not key.startswith('PYTHON'):
                del os.environ[key]

        # 重新加载
        return EnvironmentUtils.load_environment()

    @staticmethod
    def get_env_file_path(environment: str = 'development') -> str:
        """
        获取环境变量文件路径

        Args:
            environment: 环境名称

        Returns:
            环境变量文件路径
        """
        # 优先返回存在的文件
        env_files = [
            f'.env.{environment}.local',
            f'.env.{environment}',
            '.env.local',
            '.env'
        ]

        for env_file in env_files:
            if os.path.exists(env_file):
                return env_file

        return '.env'

    @staticmethod
    def create_env_file(file_path: str, vars: Dict[str, str]) -> bool:
        """
        创建环境变量文件

        Args:
            file_path: 文件路径
            vars: 环境变量字典

        Returns:
            是否成功
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                for key, value in vars.items():
                    f.write(f"{key}={value}\n")
            return True
        except Exception as e:
            return False

    @staticmethod
    def merge_env_files(file_paths: List[str], output_path: str) -> bool:
        """
        合并环境变量文件

        Args:
            file_paths: 要合并的文件路径列表
            output_path: 输出文件路径

        Returns:
            是否成功
        """
        try:
            merged_vars = {}

            # 按顺序加载文件，后面的文件会覆盖前面的
            for file_path in file_paths:
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            line = line.strip()
                            if line and not line.startswith('#'):
                                if '=' in line:
                                    key, value = line.split('=', 1)
                                    merged_vars[key.strip()] = value.strip()

            # 写入合并后的文件
            with open(output_path, 'w', encoding='utf-8') as f:
                for key, value in merged_vars.items():
                    f.write(f"{key}={value}\n")

            return True
        except Exception as e:
            return False

    @staticmethod
    def get_sensitive_env(key: str, default: Optional[Any] = None) -> Optional[str]:
        """
        获取敏感环境变量

        Args:
            key: 环境变量键
            default: 默认值

        Returns:
            环境变量值或默认值
        """
        # 这里可以添加敏感信息的处理逻辑
        # 例如从密钥管理服务获取
        return EnvironmentUtils.get_env(key, default)

    @staticmethod
    def is_env_file_uptodate(file_path: str) -> bool:
        """
        检查环境变量文件是否最新

        Args:
            file_path: 环境变量文件路径

        Returns:
            是否最新
        """
        # 这里可以添加文件更新检查逻辑
        # 例如检查文件修改时间
        return os.path.exists(file_path)