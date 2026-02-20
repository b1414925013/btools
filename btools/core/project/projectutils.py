#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目管理工具类

提供项目结构管理、依赖分析、版本管理等功能
"""
import os
import json
import yaml
import subprocess
from typing import Dict, List, Optional, Any


class ProjectUtils:
    """
    项目管理工具类
    """

    @staticmethod
    def get_project_structure(project_path: str = ".") -> Dict[str, Any]:
        """
        获取项目结构

        Args:
            project_path: 项目路径

        Returns:
            项目结构字典
        """
        structure = {}
        for root, dirs, files in os.walk(project_path):
            # 跳过隐藏目录
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'venv', '.venv']]
            
            rel_path = os.path.relpath(root, project_path)
            if rel_path == '.':
                rel_path = ''
            
            current = structure
            if rel_path:
                for part in rel_path.split(os.sep):
                    if part not in current:
                        current[part] = {}
                    current = current[part]
            
            current['__files__'] = files
        
        return structure

    @staticmethod
    def analyze_dependencies(project_path: str = ".") -> Dict[str, List[str]]:
        """
        分析项目依赖

        Args:
            project_path: 项目路径

        Returns:
            依赖字典
        """
        dependencies = {
            'pip': [],
            'requirements': [],
            'setup': []
        }
        
        # 检查 requirements.txt
        req_file = os.path.join(project_path, 'requirements.txt')
        if os.path.exists(req_file):
            with open(req_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        dependencies['requirements'].append(line)
        
        # 检查 setup.py
        setup_file = os.path.join(project_path, 'setup.py')
        if os.path.exists(setup_file):
            # 简单解析 setup.py 中的 install_requires
            with open(setup_file, 'r', encoding='utf-8') as f:
                content = f.read()
                import re
                match = re.search(r'install_requires\s*=\s*\[(.*?)\]', content, re.DOTALL)
                if match:
                    reqs = match.group(1)
                    for req in re.findall(r'[\'"]([^\'"]+)[\'"]', reqs):
                        dependencies['setup'].append(req)
        
        # 检查当前安装的包
        try:
            result = subprocess.run(
                ['pip', 'list', '--format=json'],
                capture_output=True,
                text=True,
                check=True
            )
            packages = json.loads(result.stdout)
            dependencies['pip'] = [f"{p['name']}=={p['version']}" for p in packages]
        except:
            pass
        
        return dependencies

    @staticmethod
    def get_project_info(project_path: str = ".") -> Dict[str, Optional[str]]:
        """
        获取项目信息

        Args:
            project_path: 项目路径

        Returns:
            项目信息字典
        """
        info = {
            'name': None,
            'version': None,
            'description': None,
            'author': None
        }
        
        # 检查 setup.py
        setup_file = os.path.join(project_path, 'setup.py')
        if os.path.exists(setup_file):
            with open(setup_file, 'r', encoding='utf-8') as f:
                content = f.read()
                import re
                for key in info.keys():
                    match = re.search(rf'{key}\s*=\s*[\'"]([^\'"]+)[\'"]', content)
                    if match:
                        info[key] = match.group(1)
        
        # 检查 pyproject.toml
        pyproject_file = os.path.join(project_path, 'pyproject.toml')
        if os.path.exists(pyproject_file):
            try:
                import tomli
                with open(pyproject_file, 'rb') as f:
                    data = tomli.load(f)
                    if 'project' in data:
                        for key in info.keys():
                            if key in data['project']:
                                info[key] = str(data['project'][key])
            except:
                pass
        
        return info

    @staticmethod
    def validate_project_structure(project_path: str = ".") -> List[str]:
        """
        验证项目结构

        Args:
            project_path: 项目路径

        Returns:
            问题列表
        """
        issues = []
        
        required_files = ['setup.py', 'requirements.txt', 'README.md']
        for file in required_files:
            if not os.path.exists(os.path.join(project_path, file)):
                issues.append(f"缺少必要文件: {file}")
        
        # 检查目录结构
        if not os.path.exists(os.path.join(project_path, 'tests')):
            issues.append("缺少 tests 目录")
        
        if not os.path.exists(os.path.join(project_path, 'docs')):
            issues.append("缺少 docs 目录")
        
        return issues
