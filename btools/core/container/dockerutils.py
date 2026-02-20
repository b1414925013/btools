#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docker 操作工具类

提供 Docker 操作封装，镜像构建、容器管理等功能
"""
import subprocess
import json
from typing import List, Dict, Optional, Any, Tuple


class DockerUtils:
    """
    Docker 操作工具类
    """

    @staticmethod
    def run_docker_command(cmd: List[str]) -> Tuple[int, str, str]:
        """
        运行 Docker 命令

        Args:
            cmd: Docker 命令列表

        Returns:
            (返回码, 标准输出, 标准错误)
        """
        try:
            result = subprocess.run(
                ['docker'] + cmd,
                capture_output=True,
                text=True
            )
            return result.returncode, result.stdout.strip(), result.stderr.strip()
        except Exception as e:
            return 1, '', str(e)

    @staticmethod
    def build_image(path: str, tag: str, dockerfile: str = None) -> bool:
        """
        构建 Docker 镜像

        Args:
            path: 构建上下文路径
            tag: 镜像标签
            dockerfile: Dockerfile 路径

        Returns:
            是否成功
        """
        cmd = ['build', '-t', tag]
        if dockerfile:
            cmd.extend(['-f', dockerfile])
        cmd.append(path)
        code, _, _ = DockerUtils.run_docker_command(cmd)
        return code == 0

    @staticmethod
    def list_images() -> List[Dict[str, Any]]:
        """
        列出所有 Docker 镜像

        Returns:
            镜像列表
        """
        code, stdout, _ = DockerUtils.run_docker_command(['images', '--format', '{{json .}}'])
        if code == 0:
            images = []
            for line in stdout.split('\n'):
                if line:
                    images.append(json.loads(line))
            return images
        return []

    @staticmethod
    def pull_image(image: str) -> bool:
        """
        拉取 Docker 镜像

        Args:
            image: 镜像名称

        Returns:
            是否成功
        """
        code, _, _ = DockerUtils.run_docker_command(['pull', image])
        return code == 0

    @staticmethod
    def push_image(image: str) -> bool:
        """
        推送 Docker 镜像

        Args:
            image: 镜像名称

        Returns:
            是否成功
        """
        code, _, _ = DockerUtils.run_docker_command(['push', image])
        return code == 0

    @staticmethod
    def remove_image(image: str, force: bool = False) -> bool:
        """
        删除 Docker 镜像

        Args:
            image: 镜像名称
            force: 是否强制删除

        Returns:
            是否成功
        """
        cmd = ['rmi']
        if force:
            cmd.append('-f')
        cmd.append(image)
        code, _, _ = DockerUtils.run_docker_command(cmd)
        return code == 0

    @staticmethod
    def run_container(image: str, name: str = None, ports: List[str] = None, 
                     volumes: List[str] = None, environment: Dict[str, str] = None, 
                     detach: bool = True) -> Optional[str]:
        """
        运行 Docker 容器

        Args:
            image: 镜像名称
            name: 容器名称
            ports: 端口映射列表
            volumes: 卷映射列表
            environment: 环境变量字典
            detach: 是否后台运行

        Returns:
            容器 ID
        """
        cmd = ['run']
        if name:
            cmd.extend(['--name', name])
        if ports:
            for port in ports:
                cmd.extend(['-p', port])
        if volumes:
            for volume in volumes:
                cmd.extend(['-v', volume])
        if environment:
            for key, value in environment.items():
                cmd.extend(['-e', f'{key}={value}'])
        if detach:
            cmd.append('-d')
        cmd.append(image)
        
        code, stdout, _ = DockerUtils.run_docker_command(cmd)
        if code == 0:
            return stdout
        return None

    @staticmethod
    def list_containers(all: bool = False) -> List[Dict[str, Any]]:
        """
        列出所有 Docker 容器

        Args:
            all: 是否包括停止的容器

        Returns:
            容器列表
        """
        cmd = ['ps']
        if all:
            cmd.append('-a')
        cmd.extend(['--format', '{{json .}}'])
        code, stdout, _ = DockerUtils.run_docker_command(cmd)
        if code == 0:
            containers = []
            for line in stdout.split('\n'):
                if line:
                    containers.append(json.loads(line))
            return containers
        return []

    @staticmethod
    def start_container(container: str) -> bool:
        """
        启动 Docker 容器

        Args:
            container: 容器名称或 ID

        Returns:
            是否成功
        """
        code, _, _ = DockerUtils.run_docker_command(['start', container])
        return code == 0

    @staticmethod
    def stop_container(container: str) -> bool:
        """
        停止 Docker 容器

        Args:
            container: 容器名称或 ID

        Returns:
            是否成功
        """
        code, _, _ = DockerUtils.run_docker_command(['stop', container])
        return code == 0

    @staticmethod
    def restart_container(container: str) -> bool:
        """
        重启 Docker 容器

        Args:
            container: 容器名称或 ID

        Returns:
            是否成功
        """
        code, _, _ = DockerUtils.run_docker_command(['restart', container])
        return code == 0

    @staticmethod
    def remove_container(container: str, force: bool = False) -> bool:
        """
        删除 Docker 容器

        Args:
            container: 容器名称或 ID
            force: 是否强制删除

        Returns:
            是否成功
        """
        cmd = ['rm']
        if force:
            cmd.append('-f')
        cmd.append(container)
        code, _, _ = DockerUtils.run_docker_command(cmd)
        return code == 0

    @staticmethod
    def get_container_logs(container: str, tail: int = 100) -> str:
        """
        获取容器日志

        Args:
            container: 容器名称或 ID
            tail: 显示最后几行

        Returns:
            日志内容
        """
        code, stdout, _ = DockerUtils.run_docker_command(['logs', '--tail', str(tail), container])
        if code == 0:
            return stdout
        return ''

    @staticmethod
    def exec_command(container: str, command: List[str]) -> Optional[str]:
        """
        在容器中执行命令

        Args:
            container: 容器名称或 ID
            command: 要执行的命令

        Returns:
            命令输出
        """
        cmd = ['exec', container]
        cmd.extend(command)
        code, stdout, _ = DockerUtils.run_docker_command(cmd)
        if code == 0:
            return stdout
        return None

    @staticmethod
    def inspect_container(container: str) -> Optional[Dict[str, Any]]:
        """
        检查容器详细信息

        Args:
            container: 容器名称或 ID

        Returns:
            容器信息
        """
        code, stdout, _ = DockerUtils.run_docker_command(['inspect', container])
        if code == 0:
            return json.loads(stdout)[0]
        return None

    @staticmethod
    def inspect_image(image: str) -> Optional[Dict[str, Any]]:
        """
        检查镜像详细信息

        Args:
            image: 镜像名称

        Returns:
            镜像信息
        """
        code, stdout, _ = DockerUtils.run_docker_command(['inspect', image])
        if code == 0:
            return json.loads(stdout)[0]
        return None
