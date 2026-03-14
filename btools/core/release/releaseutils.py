#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
发布工具类

提供发布工具，自动化版本号管理、CHANGELOG 生成等功能
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class ReleaseUtils:
    """
    发布工具类
    """

    @staticmethod
    def get_current_version(setup_py_path: str = "setup.py") -> Optional[str]:
        """
        获取当前版本号

        Args:
            setup_py_path: setup.py 文件路径

        Returns:
            当前版本号
        """
        if not os.path.exists(setup_py_path):
            return None

        with open(setup_py_path, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r"version\s*=\s*['\"]([^'\"]+)['\"]", content)
            if match:
                return match.group(1)
        return None

    @staticmethod
    def bump_version(current_version: str, bump_type: str = "patch") -> str:
        """
        升级版本号

        Args:
            current_version: 当前版本号
            bump_type: 升级类型 (major, minor, patch)

        Returns:
            新版本号
        """
        parts = current_version.split(".")
        while len(parts) < 3:
            parts.append("0")

        major, minor, patch = map(int, parts[:3])

        if bump_type == "major":
            major += 1
            minor = 0
            patch = 0
        elif bump_type == "minor":
            minor += 1
            patch = 0
        elif bump_type == "patch":
            patch += 1

        return f"{major}.{minor}.{patch}"

    @staticmethod
    def update_version(
        setup_py_path: str = "setup.py",
        new_version: str = None,
        bump_type: str = "patch",
    ) -> bool:
        """
        更新版本号

        Args:
            setup_py_path: setup.py 文件路径
            new_version: 新版本号，None 则自动升级
            bump_type: 升级类型 (major, minor, patch)

        Returns:
            是否成功
        """
        if not os.path.exists(setup_py_path):
            return False

        with open(setup_py_path, "r", encoding="utf-8") as f:
            content = f.read()

        current_version = ReleaseUtils.get_current_version(setup_py_path)
        if not current_version:
            return False

        if not new_version:
            new_version = ReleaseUtils.bump_version(current_version, bump_type)

        # 更新 setup.py 中的版本号
        new_content = re.sub(
            r"version\s*=\s*['\"]([^'\"]+)['\"]", f'version="{new_version}"', content
        )

        with open(setup_py_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        return True

    @staticmethod
    def generate_changelog(
        git_repo_path: str = ".", output_file: str = "CHANGELOG.md"
    ) -> bool:
        """
        生成 CHANGELOG

        Args:
            git_repo_path: Git 仓库路径
            output_file: 输出文件路径

        Returns:
            是否成功
        """
        try:
            import subprocess

            # 获取所有标签
            tags_cmd = ["git", "tag", "--sort=-v:refname"]
            tags_result = subprocess.run(
                tags_cmd, cwd=git_repo_path, capture_output=True, text=True
            )

            if tags_result.returncode != 0:
                return False

            tags = tags_result.stdout.strip().split("\n")
            if not tags:
                return False

            changelog = "# CHANGELOG\n\n"

            # 为每个标签生成变更记录
            for i, tag in enumerate(tags):
                if not tag:
                    continue

                # 获取标签日期
                date_cmd = ["git", "log", "-1", "--format=%ai", tag]
                date_result = subprocess.run(
                    date_cmd, cwd=git_repo_path, capture_output=True, text=True
                )

                if date_result.returncode == 0:
                    date_str = date_result.stdout.strip().split(" ")[0]
                else:
                    date_str = datetime.now().strftime("%Y-%m-%d")

                changelog += f"## {tag} ({date_str})\n\n"

                # 获取该标签与前一个标签之间的提交
                if i < len(tags) - 1:
                    prev_tag = tags[i + 1]
                    log_cmd = [
                        "git",
                        "log",
                        f"{prev_tag}..{tag}",
                        "--pretty=format:  * %s",
                    ]
                else:
                    # 第一个标签，获取所有提交
                    log_cmd = ["git", "log", tag, "--pretty=format:  * %s"]

                log_result = subprocess.run(
                    log_cmd, cwd=git_repo_path, capture_output=True, text=True
                )

                if log_result.returncode == 0:
                    commits = log_result.stdout.strip()
                    if commits:
                        changelog += commits + "\n\n"
                    else:
                        changelog += "  * No changes\n\n"

            # 写入 CHANGELOG 文件
            with open(
                os.path.join(git_repo_path, output_file), "w", encoding="utf-8"
            ) as f:
                f.write(changelog)

            return True
        except:
            return False

    @staticmethod
    def validate_version(version: str) -> bool:
        """
        验证版本号格式是否符合语义化版本规范

        Args:
            version: 版本号字符串

        Returns:
            是否符合语义化版本规范
        """
        if not version:
            return False

        # 语义化版本正则表达式
        pattern = r'^(\d+)\.(\d+)\.(\d+)(?:-([a-zA-Z0-9.]+))?$'
        match = re.match(pattern, version)

        if not match:
            return False

        return True

    @staticmethod
    def compare_versions(version1: str, version2: str) -> int:
        """
        比较两个版本号

        Args:
            version1: 第一个版本号
            version2: 第二个版本号

        Returns:
            1: version1 > version2
            0: version1 == version2
            -1: version1 < version2
        """
        def parse_version(v):
            # 分离主版本和预发布版本
            parts = v.split('-')
            main_version = parts[0]
            pre_release = parts[1] if len(parts) > 1 else None

            # 解析主版本号
            main_parts = list(map(int, main_version.split('.')))

            return (main_parts, pre_release)

        v1_parts, v1_pre = parse_version(version1)
        v2_parts, v2_pre = parse_version(version2)

        # 比较主版本号
        for i in range(max(len(v1_parts), len(v2_parts))):
            p1 = v1_parts[i] if i < len(v1_parts) else 0
            p2 = v2_parts[i] if i < len(v2_parts) else 0

            if p1 > p2:
                return 1
            elif p1 < p2:
                return -1

        # 主版本号相同，比较预发布版本
        if v1_pre is None and v2_pre is None:
            return 0
        elif v1_pre is None:
            return 1  # 正式版本 > 预发布版本
        elif v2_pre is None:
            return -1
        else:
            # 比较预发布版本字符串
            if v1_pre < v2_pre:
                return -1
            elif v1_pre > v2_pre:
                return 1
            else:
                return 0

    @staticmethod
    def is_prerelease(version: str) -> bool:
        """
        检查版本号是否为预发布版本

        Args:
            version: 版本号字符串

        Returns:
            是否为预发布版本
        """
        if not version:
            return False

        # 检查是否包含预发布标识
        return '-' in version

    @staticmethod
    def check_release_ready(path: str = ".") -> List[str]:
        """
        检查是否准备好发布

        Args:
            path: 项目路径

        Returns:
            问题列表
        """
        issues = []

        # 检查必要文件
        required_files = ["setup.py", "README.md", "CHANGELOG.md"]
        for file in required_files:
            if not os.path.exists(os.path.join(path, file)):
                issues.append(f"缺少文件: {file}")

        # 检查版本号
        version = ReleaseUtils.get_current_version(os.path.join(path, "setup.py"))
        if not version:
            issues.append("无法获取版本号")

        # 检查 Git 状态
        try:
            import subprocess

            status_cmd = ["git", "status", "--porcelain"]
            status_result = subprocess.run(
                status_cmd, cwd=path, capture_output=True, text=True
            )

            if status_result.returncode == 0:
                if status_result.stdout.strip():
                    issues.append("Git 仓库有未提交的更改")
        except:
            pass

        return issues

    @staticmethod
    def create_release_tag(
        version: str, message: str = None, git_repo_path: str = "."
    ) -> bool:
        """
        创建发布标签

        Args:
            version: 版本号
            message: 标签消息
            git_repo_path: Git 仓库路径

        Returns:
            是否成功
        """
        try:
            import subprocess

            tag_name = f"v{version}"
            tag_cmd = ["git", "tag", "-a", tag_name]

            if message:
                tag_cmd.extend(["-m", message])

            result = subprocess.run(
                tag_cmd, cwd=git_repo_path, capture_output=True, text=True
            )

            return result.returncode == 0
        except:
            return False

    @staticmethod
    def push_release_tag(
        tag_name: str, remote: str = "origin", git_repo_path: str = "."
    ) -> bool:
        """
        推送发布标签

        Args:
            tag_name: 标签名称
            remote: 远程仓库
            git_repo_path: Git 仓库路径

        Returns:
            是否成功
        """
        try:
            import subprocess

            push_cmd = ["git", "push", remote, tag_name]
            result = subprocess.run(
                push_cmd, cwd=git_repo_path, capture_output=True, text=True
            )

            return result.returncode == 0
        except:
            return False
