#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Git 操作工具类

提供 Git 操作封装，分支管理、提交规范检查等功能
"""
import subprocess
import os
from typing import List, Dict, Optional, Tuple


class GitUtils:
    """
    Git 操作工具类
    """

    @staticmethod
    def run_git_command(cmd: List[str], cwd: str = ".") -> Tuple[int, str, str]:
        """
        运行 Git 命令

        Args:
            cmd: Git 命令列表
            cwd: 工作目录

        Returns:
            (返回码, 标准输出, 标准错误)
        """
        try:
            result = subprocess.run(
                ['git'] + cmd,
                cwd=cwd,
                capture_output=True,
                text=True
            )
            return result.returncode, result.stdout.strip(), result.stderr.strip()
        except Exception as e:
            return 1, '', str(e)

    @staticmethod
    def get_current_branch(cwd: str = ".") -> Optional[str]:
        """
        获取当前分支

        Args:
            cwd: 工作目录

        Returns:
            当前分支名
        """
        code, stdout, _ = GitUtils.run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'], cwd)
        if code == 0:
            return stdout
        return None

    @staticmethod
    def get_branches(cwd: str = ".") -> List[str]:
        """
        获取所有分支

        Args:
            cwd: 工作目录

        Returns:
            分支列表
        """
        code, stdout, _ = GitUtils.run_git_command(['branch', '--list'], cwd)
        if code == 0:
            branches = []
            for line in stdout.split('\n'):
                line = line.strip()
                if line:
                    # 移除分支前的 * 标记
                    branches.append(line.replace('* ', ''))
            return branches
        return []

    @staticmethod
    def create_branch(branch_name: str, cwd: str = ".") -> bool:
        """
        创建分支

        Args:
            branch_name: 分支名
            cwd: 工作目录

        Returns:
            是否成功
        """
        code, _, _ = GitUtils.run_git_command(['checkout', '-b', branch_name], cwd)
        return code == 0

    @staticmethod
    def checkout_branch(branch_name: str, cwd: str = ".") -> bool:
        """
        切换分支

        Args:
            branch_name: 分支名
            cwd: 工作目录

        Returns:
            是否成功
        """
        code, _, _ = GitUtils.run_git_command(['checkout', branch_name], cwd)
        return code == 0

    @staticmethod
    def merge_branch(branch_name: str, cwd: str = ".") -> bool:
        """
        合并分支

        Args:
            branch_name: 要合并的分支名
            cwd: 工作目录

        Returns:
            是否成功
        """
        code, _, _ = GitUtils.run_git_command(['merge', branch_name], cwd)
        return code == 0

    @staticmethod
    def delete_branch(branch_name: str, force: bool = False, cwd: str = ".") -> bool:
        """
        删除分支

        Args:
            branch_name: 分支名
            force: 是否强制删除
            cwd: 工作目录

        Returns:
            是否成功
        """
        cmd = ['branch', '-d']
        if force:
            cmd = ['branch', '-D']
        cmd.append(branch_name)
        code, _, _ = GitUtils.run_git_command(cmd, cwd)
        return code == 0

    @staticmethod
    def get_status(cwd: str = ".") -> str:
        """
        获取 Git 状态

        Args:
            cwd: 工作目录

        Returns:
            状态信息
        """
        code, stdout, _ = GitUtils.run_git_command(['status', '--porcelain'], cwd)
        if code == 0:
            return stdout
        return ''

    @staticmethod
    def add_files(files: List[str] = [], cwd: str = ".") -> bool:
        """
        添加文件到暂存区

        Args:
            files: 文件列表，空列表表示添加所有
            cwd: 工作目录

        Returns:
            是否成功
        """
        cmd = ['add']
        if not files:
            cmd.append('.')
        else:
            cmd.extend(files)
        code, _, _ = GitUtils.run_git_command(cmd, cwd)
        return code == 0

    @staticmethod
    def commit(message: str, cwd: str = ".") -> bool:
        """
        提交更改

        Args:
            message: 提交信息
            cwd: 工作目录

        Returns:
            是否成功
        """
        code, _, _ = GitUtils.run_git_command(['commit', '-m', message], cwd)
        return code == 0

    @staticmethod
    def push(remote: str = 'origin', branch: Optional[str] = None, cwd: str = ".") -> bool:
        """
        推送更改

        Args:
            remote: 远程仓库
            branch: 分支名，None 表示当前分支
            cwd: 工作目录

        Returns:
            是否成功
        """
        cmd = ['push', remote]
        if branch:
            cmd.append(branch)
        else:
            cmd.append('--set-upstream')
            cmd.append(f'{remote}')
            current_branch = GitUtils.get_current_branch(cwd)
            if current_branch:
                cmd.append(current_branch)
            else:
                return False
        code, _, _ = GitUtils.run_git_command(cmd, cwd)
        return code == 0

    @staticmethod
    def pull(remote: str = 'origin', branch: Optional[str] = None, cwd: str = ".") -> bool:
        """
        拉取更改

        Args:
            remote: 远程仓库
            branch: 分支名，None 表示当前分支
            cwd: 工作目录

        Returns:
            是否成功
        """
        cmd = ['pull', remote]
        if branch:
            cmd.append(branch)
        code, _, _ = GitUtils.run_git_command(cmd, cwd)
        return code == 0

    @staticmethod
    def check_commit_message(message: str) -> List[str]:
        """
        检查提交信息是否符合规范

        Args:
            message: 提交信息

        Returns:
            问题列表
        """
        issues = []
        
        # 检查长度
        if len(message) > 50:
            issues.append("提交信息第一行不应超过50个字符")
        
        if len(message) < 10:
            issues.append("提交信息过于简短")
        
        # 检查格式
        import re
        if not re.match(r'^(feat|fix|docs|style|refactor|test|chore):\s.*', message):
            issues.append("提交信息应符合 Conventional Commits 规范，格式为: type: subject")
        
        return issues

    @staticmethod
    def get_commit_history(limit: int = 10, cwd: str = ".") -> List[Dict[str, str]]:
        """
        获取提交历史

        Args:
            limit: 限制数量
            cwd: 工作目录

        Returns:
            提交历史列表
        """
        cmd = ['log', f'--max-count={limit}', '--pretty=format:%H|%an|%ad|%s']
        code, stdout, _ = GitUtils.run_git_command(cmd, cwd)
        if code == 0:
            commits = []
            for line in stdout.split('\n'):
                if line:
                    parts = line.split('|', 3)
                    if len(parts) == 4:
                        commits.append({
                            'hash': parts[0],
                            'author': parts[1],
                            'date': parts[2],
                            'message': parts[3]
                        })
            return commits
        return []

    @staticmethod
    def is_git_repository(cwd: str = ".") -> bool:
        """
        检查是否为 Git 仓库

        Args:
            cwd: 工作目录

        Returns:
            是否为 Git 仓库
        """
        code, _, _ = GitUtils.run_git_command(['rev-parse', '--is-inside-work-tree'], cwd)
        return code == 0
