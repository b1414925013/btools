#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
打包工具类

提供打包工具，支持 wheel、egg、sdist 等格式
"""
import subprocess
import os
import shutil
from typing import List, Optional, Dict


class PackagingUtils:
    """
    打包工具类
    """

    @staticmethod
    def run_python_command(cmd: List[str]) -> tuple[int, str, str]:
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
    def build_sdist(path: str = '.', output_dir: str = 'dist') -> Optional[str]:
        """
        构建 sdist 包

        Args:
            path: 项目路径
            output_dir: 输出目录

        Returns:
            构建的包路径
        """
        cmd = ['setup.py', 'sdist', f'--dist-dir={output_dir}']
        code, stdout, stderr = PackagingUtils.run_python_command(cmd)
        if code == 0:
            # 查找构建的包
            dist_files = os.listdir(output_dir)
            sdist_files = [f for f in dist_files if f.endswith('.tar.gz')]
            if sdist_files:
                return os.path.join(output_dir, sdist_files[0])
        return None

    @staticmethod
    def build_wheel(path: str = '.', output_dir: str = 'dist', universal: bool = False) -> Optional[str]:
        """
        构建 wheel 包

        Args:
            path: 项目路径
            output_dir: 输出目录
            universal: 是否构建通用 wheel

        Returns:
            构建的包路径
        """
        cmd = ['setup.py', 'bdist_wheel', f'--dist-dir={output_dir}']
        if universal:
            cmd.append('--universal')
        code, stdout, stderr = PackagingUtils.run_python_command(cmd)
        if code == 0:
            # 查找构建的包
            dist_files = os.listdir(output_dir)
            wheel_files = [f for f in dist_files if f.endswith('.whl')]
            if wheel_files:
                return os.path.join(output_dir, wheel_files[0])
        return None

    @staticmethod
    def build_egg(path: str = '.', output_dir: str = 'dist') -> Optional[str]:
        """
        构建 egg 包

        Args:
            path: 项目路径
            output_dir: 输出目录

        Returns:
            构建的包路径
        """
        cmd = ['setup.py', 'bdist_egg', f'--dist-dir={output_dir}']
        code, stdout, stderr = PackagingUtils.run_python_command(cmd)
        if code == 0:
            # 查找构建的包
            dist_files = os.listdir(output_dir)
            egg_files = [f for f in dist_files if f.endswith('.egg')]
            if egg_files:
                return os.path.join(output_dir, egg_files[0])
        return None

    @staticmethod
    def build_all(path: str = '.', output_dir: str = 'dist') -> Dict[str, Optional[str]]:
        """
        构建所有格式的包

        Args:
            path: 项目路径
            output_dir: 输出目录

        Returns:
            各格式包的路径
        """
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)

        return {
            'sdist': PackagingUtils.build_sdist(path, output_dir),
            'wheel': PackagingUtils.build_wheel(path, output_dir),
            'egg': PackagingUtils.build_egg(path, output_dir)
        }

    @staticmethod
    def clean_build_artifacts(path: str = '.') -> bool:
        """
        清理构建产物

        Args:
            path: 项目路径

        Returns:
            是否成功
        """
        artifacts = [
            'build',
            'dist',
            '*.egg-info',
            '*.egg',
            '__pycache__'
        ]

        for artifact in artifacts:
            artifact_path = os.path.join(path, artifact)
            if os.path.exists(artifact_path):
                if os.path.isdir(artifact_path):
                    shutil.rmtree(artifact_path, ignore_errors=True)
                else:
                    os.remove(artifact_path)

        return True

    @staticmethod
    def check_package_structure(path: str = '.') -> List[str]:
        """
        检查包结构

        Args:
            path: 项目路径

        Returns:
            问题列表
        """
        issues = []

        required_files = ['setup.py', 'README.md', 'requirements.txt']
        for file in required_files:
            if not os.path.exists(os.path.join(path, file)):
                issues.append(f"缺少文件: {file}")

        # 检查 setup.py 是否有效
        if os.path.exists(os.path.join(path, 'setup.py')):
            code, _, stderr = PackagingUtils.run_python_command(['setup.py', '--version'])
            if code != 0:
                issues.append(f"setup.py 有问题: {stderr}")

        return issues

    @staticmethod
    def get_package_info(path: str = '.') -> Dict[str, Optional[str]]:
        """
        获取包信息

        Args:
            path: 项目路径

        Returns:
            包信息
        """
        info = {
            'name': None,
            'version': None,
            'description': None,
            'author': None
        }

        setup_file = os.path.join(path, 'setup.py')
        if os.path.exists(setup_file):
            # 尝试运行 setup.py --version 获取版本
            code, stdout, _ = PackagingUtils.run_python_command(['setup.py', '--version'])
            if code == 0:
                info['version'] = stdout.strip()

            # 简单解析 setup.py
            with open(setup_file, 'r', encoding='utf-8') as f:
                content = f.read()
                import re
                for key in info.keys():
                    if key != 'version':
                        match = re.search(rf'{key}\s*=\s*[\'"]([^\'"]+)[\'"]', content)
                        if match:
                            info[key] = match.group(1)

        return info

    @staticmethod
    def verify_package(package_path: str) -> bool:
        """
        验证包

        Args:
            package_path: 包路径

        Returns:
            是否有效
        """
        if not os.path.exists(package_path):
            return False

        # 对于 wheel 包，使用 wheel 工具验证
        if package_path.endswith('.whl'):
            try:
                code, _, _ = PackagingUtils.run_python_command(['-m', 'wheel', 'verify', package_path])
                return code == 0
            except:
                # 如果没有 wheel 模块，跳过验证
                pass

        return True
