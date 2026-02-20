#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kubernetes 操作工具类

提供 K8s 资源管理，部署、扩缩容操作等功能
"""
import subprocess
import json
from typing import List, Dict, Optional, Any, Tuple


class KubernetesUtils:
    """
    Kubernetes 操作工具类
    """

    @staticmethod
    def run_kubectl_command(cmd: List[str]) -> Tuple[int, str, str]:
        """
        运行 kubectl 命令

        Args:
            cmd: kubectl 命令列表

        Returns:
            (返回码, 标准输出, 标准错误)
        """
        try:
            result = subprocess.run(
                ['kubectl'] + cmd,
                capture_output=True,
                text=True
            )
            return result.returncode, result.stdout.strip(), result.stderr.strip()
        except Exception as e:
            return 1, '', str(e)

    @staticmethod
    def get_pods(namespace: str = 'default') -> List[Dict[str, Any]]:
        """
        获取 Pod 列表

        Args:
            namespace: 命名空间

        Returns:
            Pod 列表
        """
        code, stdout, _ = KubernetesUtils.run_kubectl_command([
            'get', 'pods',
            '--namespace', namespace,
            '--output', 'json'
        ])
        if code == 0:
            data = json.loads(stdout)
            return data.get('items', [])
        return []

    @staticmethod
    def get_deployments(namespace: str = 'default') -> List[Dict[str, Any]]:
        """
        获取 Deployment 列表

        Args:
            namespace: 命名空间

        Returns:
            Deployment 列表
        """
        code, stdout, _ = KubernetesUtils.run_kubectl_command([
            'get', 'deployments',
            '--namespace', namespace,
            '--output', 'json'
        ])
        if code == 0:
            data = json.loads(stdout)
            return data.get('items', [])
        return []

    @staticmethod
    def get_services(namespace: str = 'default') -> List[Dict[str, Any]]:
        """
        获取 Service 列表

        Args:
            namespace: 命名空间

        Returns:
            Service 列表
        """
        code, stdout, _ = KubernetesUtils.run_kubectl_command([
            'get', 'services',
            '--namespace', namespace,
            '--output', 'json'
        ])
        if code == 0:
            data = json.loads(stdout)
            return data.get('items', [])
        return []

    @staticmethod
    def get_namespaces() -> List[Dict[str, Any]]:
        """
        获取命名空间列表

        Returns:
            命名空间列表
        """
        code, stdout, _ = KubernetesUtils.run_kubectl_command([
            'get', 'namespaces',
            '--output', 'json'
        ])
        if code == 0:
            data = json.loads(stdout)
            return data.get('items', [])
        return []

    @staticmethod
    def create_namespace(name: str) -> bool:
        """
        创建命名空间

        Args:
            name: 命名空间名称

        Returns:
            是否成功
        """
        code, _, _ = KubernetesUtils.run_kubectl_command([
            'create', 'namespace', name
        ])
        return code == 0

    @staticmethod
    def delete_namespace(name: str) -> bool:
        """
        删除命名空间

        Args:
            name: 命名空间名称

        Returns:
            是否成功
        """
        code, _, _ = KubernetesUtils.run_kubectl_command([
            'delete', 'namespace', name
        ])
        return code == 0

    @staticmethod
    def apply_manifest(manifest_path: str, namespace: str = 'default') -> bool:
        """
        应用 Kubernetes 清单

        Args:
            manifest_path: 清单文件路径
            namespace: 命名空间

        Returns:
            是否成功
        """
        code, _, _ = KubernetesUtils.run_kubectl_command([
            'apply', '-f', manifest_path,
            '--namespace', namespace
        ])
        return code == 0

    @staticmethod
    def delete_manifest(manifest_path: str, namespace: str = 'default') -> bool:
        """
        删除 Kubernetes 清单

        Args:
            manifest_path: 清单文件路径
            namespace: 命名空间

        Returns:
            是否成功
        """
        code, _, _ = KubernetesUtils.run_kubectl_command([
            'delete', '-f', manifest_path,
            '--namespace', namespace
        ])
        return code == 0

    @staticmethod
    def scale_deployment(name: str, replicas: int, namespace: str = 'default') -> bool:
        """
        扩缩容 Deployment

        Args:
            name: Deployment 名称
            replicas: 副本数
            namespace: 命名空间

        Returns:
            是否成功
        """
        code, _, _ = KubernetesUtils.run_kubectl_command([
            'scale', 'deployment', name,
            '--replicas', str(replicas),
            '--namespace', namespace
        ])
        return code == 0

    @staticmethod
    def rollout_restart_deployment(name: str, namespace: str = 'default') -> bool:
        """
        重启 Deployment

        Args:
            name: Deployment 名称
            namespace: 命名空间

        Returns:
            是否成功
        """
        code, _, _ = KubernetesUtils.run_kubectl_command([
            'rollout', 'restart', 'deployment', name,
            '--namespace', namespace
        ])
        return code == 0

    @staticmethod
    def get_pod_logs(pod_name: str, namespace: str = 'default', tail: int = 100) -> str:
        """
        获取 Pod 日志

        Args:
            pod_name: Pod 名称
            namespace: 命名空间
            tail: 显示最后几行

        Returns:
            日志内容
        """
        code, stdout, _ = KubernetesUtils.run_kubectl_command([
            'logs', pod_name,
            '--namespace', namespace,
            '--tail', str(tail)
        ])
        if code == 0:
            return stdout
        return ''

    @staticmethod
    def exec_in_pod(pod_name: str, command: List[str], namespace: str = 'default') -> Optional[str]:
        """
        在 Pod 中执行命令

        Args:
            pod_name: Pod 名称
            command: 要执行的命令
            namespace: 命名空间

        Returns:
            命令输出
        """
        cmd = [
            'exec', pod_name,
            '--namespace', namespace,
            '--'
        ]
        cmd.extend(command)
        code, stdout, _ = KubernetesUtils.run_kubectl_command(cmd)
        if code == 0:
            return stdout
        return None

    @staticmethod
    def port_forward(pod_name: str, local_port: int, remote_port: int, namespace: str = 'default') -> bool:
        """
        端口转发

        Args:
            pod_name: Pod 名称
            local_port: 本地端口
            remote_port: 远程端口
            namespace: 命名空间

        Returns:
            是否成功
        """
        # 注意：这是一个阻塞命令，实际使用中需要在后台运行
        code, _, _ = KubernetesUtils.run_kubectl_command([
            'port-forward', pod_name,
            f'{local_port}:{remote_port}',
            '--namespace', namespace
        ])
        return code == 0

    @staticmethod
    def describe_resource(resource_type: str, resource_name: str, namespace: str = 'default') -> str:
        """
        查看资源详细信息

        Args:
            resource_type: 资源类型
            resource_name: 资源名称
            namespace: 命名空间

        Returns:
            资源详细信息
        """
        code, stdout, _ = KubernetesUtils.run_kubectl_command([
            'describe', resource_type, resource_name,
            '--namespace', namespace
        ])
        if code == 0:
            return stdout
        return ''

    @staticmethod
    def get_resource(resource_type: str, resource_name: str, namespace: str = 'default') -> Optional[Dict[str, Any]]:
        """
        获取资源详细信息（JSON 格式）

        Args:
            resource_type: 资源类型
            resource_name: 资源名称
            namespace: 命名空间

        Returns:
            资源详细信息
        """
        code, stdout, _ = KubernetesUtils.run_kubectl_command([
            'get', resource_type, resource_name,
            '--namespace', namespace,
            '--output', 'json'
        ])
        if code == 0:
            return json.loads(stdout)
        return None

    @staticmethod
    def get_contexts() -> List[Dict[str, Any]]:
        """
        获取上下文列表

        Returns:
            上下文列表
        """
        code, stdout, _ = KubernetesUtils.run_kubectl_command([
            'config', 'get-contexts',
            '--output', 'json'
        ])
        if code == 0:
            data = json.loads(stdout)
            return data.get('contexts', [])
        return []

    @staticmethod
    def use_context(context_name: str) -> bool:
        """
        切换上下文

        Args:
            context_name: 上下文名称

        Returns:
            是否成功
        """
        code, _, _ = KubernetesUtils.run_kubectl_command([
            'config', 'use-context', context_name
        ])
        return code == 0
