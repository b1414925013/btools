#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分发工具类

提供分发工具，支持上传到 PyPI、私有仓库等功能
"""
import subprocess
import os
from typing import Optional, Dict, Tuple, List


class DistributionUtils:
    """
    分发工具类
    """

    @staticmethod
    def run_python_command(cmd: List) -> Tuple[int, str, str]:
        """
        运行 Python 命令

        Args:
            cmd: 命令列表

        Returns:
            (返回码, 标准输出, 标准错误)
        """
        try:
            result = subprocess.run(
                ['python'] + cmd,
                capture_output=True,
                text=True
            )
            return result.returncode, result.stdout.strip(), result.stderr.strip()
        except Exception as e:
            return 1, '', str(e)

    @staticmethod
    def upload_to_pypi(package_path: str, repository: str = None, username: str = None, password: str = None) -> bool:
        """
        上传包到 PyPI

        Args:
            package_path: 包路径
            repository: 仓库 URL，None 表示默认 PyPI
            username: 用户名
            password: 密码

        Returns:
            是否成功
        """
        try:
            # 检查 twine 是否已安装
            code, _, _ = DistributionUtils.run_python_command(['-m', 'twine', '--version'])
            if code != 0:
                # 尝试安装 twine
                install_code, _, _ = DistributionUtils.run_python_command(['-m', 'pip', 'install', 'twine'])
                if install_code != 0:
                    return False

            cmd = ['-m', 'twine', 'upload']
            
            if repository:
                cmd.extend(['--repository-url', repository])
            
            if username:
                cmd.extend(['--username', username])
            
            if password:
                cmd.extend(['--password', password])
            
            cmd.append(package_path)

            code, stdout, stderr = DistributionUtils.run_python_command(cmd)
            return code == 0
        except:
            return False

    @staticmethod
    def upload_to_testpypi(package_path: str, username: str = None, password: str = None) -> bool:
        """
        上传包到 TestPyPI

        Args:
            package_path: 包路径
            username: 用户名
            password: 密码

        Returns:
            是否成功
        """
        testpypi_url = 'https://test.pypi.org/legacy/'
        return DistributionUtils.upload_to_pypi(package_path, testpypi_url, username, password)

    @staticmethod
    def upload_all_to_pypi(dist_dir: str = 'dist', repository: str = None, username: str = None, password: str = None) -> Dict[str, bool]:
        """
        上传所有包到 PyPI

        Args:
            dist_dir: 分发目录
            repository: 仓库 URL
            username: 用户名
            password: 密码

        Returns:
            每个包的上传结果
        """
        results = {}

        if not os.path.exists(dist_dir):
            return results

        for file in os.listdir(dist_dir):
            if file.endswith(('.tar.gz', '.whl', '.egg')):
                file_path = os.path.join(dist_dir, file)
                success = DistributionUtils.upload_to_pypi(file_path, repository, username, password)
                results[file] = success

        return results

    @staticmethod
    def install_from_pypi(package_name: str, version: str = None, repository: str = None, upgrade: bool = False) -> bool:
        """
        从 PyPI 安装包

        Args:
            package_name: 包名
            version: 版本号
            repository: 仓库 URL
            upgrade: 是否升级

        Returns:
            是否成功
        """
        cmd = ['-m', 'pip', 'install']

        if upgrade:
            cmd.append('--upgrade')

        if repository:
            cmd.extend(['--index-url', repository])

        if version:
            package_spec = f'{package_name}=={version}'
        else:
            package_spec = package_name

        cmd.append(package_spec)

        code, _, _ = DistributionUtils.run_python_command(cmd)
        return code == 0

    @staticmethod
    def install_from_testpypi(package_name: str, version: str = None, upgrade: bool = False) -> bool:
        """
        从 TestPyPI 安装包

        Args:
            package_name: 包名
            version: 版本号
            upgrade: 是否升级

        Returns:
            是否成功
        """
        testpypi_url = 'https://test.pypi.org/simple/'
        return DistributionUtils.install_from_pypi(package_name, version, testpypi_url, upgrade)

    @staticmethod
    def check_pypi_version(package_name: str) -> Optional[str]:
        """
        检查 PyPI 上的最新版本

        Args:
            package_name: 包名

        Returns:
            最新版本号
        """
        try:
            # 检查 requests 是否已安装
            code, _, _ = DistributionUtils.run_python_command(['-c', 'import requests'])
            if code != 0:
                # 尝试安装 requests
                install_code, _, _ = DistributionUtils.run_python_command(['-m', 'pip', 'install', 'requests'])
                if install_code != 0:
                    return None

            # 使用 requests 查询 PyPI API
            import requests
            url = f'https://pypi.org/pypi/{package_name}/json'
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('info', {}).get('version')
            
            return None
        except:
            return None

    @staticmethod
    def configure_pypi_credentials(config_file: str = None) -> bool:
        """
        配置 PyPI 凭证

        Args:
            config_file: 配置文件路径，None 表示默认路径

        Returns:
            是否成功
        """
        try:
            import configparser
            import os

            if not config_file:
                # 使用默认配置文件路径
                if os.name == 'nt':  # Windows
                    config_dir = os.path.expanduser('~\\pypirc')
                else:  # Unix-like
                    config_dir = os.path.expanduser('~/.pypirc')
            else:
                config_dir = config_file

            # 创建配置文件
            config = configparser.ConfigParser()
            config['distutils'] = {
                'index-servers': 'pypi,testpypi'
            }
            config['pypi'] = {
                'repository': 'https://upload.pypi.org/legacy/',
                'username': ''
            }
            config['testpypi'] = {
                'repository': 'https://test.pypi.org/legacy/',
                'username': ''
            }

            # 写入配置文件
            with open(config_dir, 'w') as f:
                config.write(f)

            return True
        except:
            return False

    @staticmethod
    def get_distribution_info(package_name: str) -> Optional[Dict]:
        """
        获取包的分发信息

        Args:
            package_name: 包名

        Returns:
            分发信息
        """
        try:
            # 检查 requests 是否已安装
            code, _, _ = DistributionUtils.run_python_command(['-c', 'import requests'])
            if code != 0:
                return None

            import requests
            url = f'https://pypi.org/pypi/{package_name}/json'
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'name': data.get('info', {}).get('name'),
                    'version': data.get('info', {}).get('version'),
                    'summary': data.get('info', {}).get('summary'),
                    'home_page': data.get('info', {}).get('home_page'),
                    'author': data.get('info', {}).get('author'),
                    'license': data.get('info', {}).get('license'),
                    'classifiers': data.get('info', {}).get('classifiers', []),
                    'requires_dist': data.get('info', {}).get('requires_dist', []),
                    'package_urls': data.get('urls', [])
                }
            
            return None
        except:
            return None

    @staticmethod
    def mirror_package(package_name: str, source_repo: str, target_repo: str, version: str = None) -> bool:
        """
        镜像包从一个仓库到另一个仓库

        Args:
            package_name: 包名
            source_repo: 源仓库 URL
            target_repo: 目标仓库 URL
            version: 版本号

        Returns:
            是否成功
        """
        try:
            import tempfile

            # 创建临时目录
            with tempfile.TemporaryDirectory() as temp_dir:
                # 从源仓库下载包
                download_cmd = ['-m', 'pip', 'download', '--dest', temp_dir]
                if source_repo:
                    download_cmd.extend(['--index-url', source_repo])
                if version:
                    download_cmd.append(f'{package_name}=={version}')
                else:
                    download_cmd.append(package_name)

                code, _, _ = DistributionUtils.run_python_command(download_cmd)
                if code != 0:
                    return False

                # 上传到目标仓库
                for file in os.listdir(temp_dir):
                    if file.endswith(('.tar.gz', '.whl', '.egg')):
                        file_path = os.path.join(temp_dir, file)
                        upload_success = DistributionUtils.upload_to_pypi(file_path, target_repo)
                        if not upload_success:
                            return False

                return True
        except:
            return False