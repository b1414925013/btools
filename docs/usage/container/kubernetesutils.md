# KubernetesUtils 使用指南

`KubernetesUtils` 类提供了 Kubernetes 资源管理，包括部署、扩缩容操作等功能。

## 基本使用

### Pod 操作

```python
from btools import KubernetesUtils

# 获取 Pod 列表
pods = KubernetesUtils.get_pods(namespace="default")
for pod in pods:
    print(f"{pod['metadata']['name']} - {pod['status']['phase']}")

# 获取特定 Pod 的详细信息
pod_info = KubernetesUtils.get_pod("my-pod", namespace="default")
print(pod_info)

# 删除 Pod
success = KubernetesUtils.delete_pod("my-pod", namespace="default")
```

### Deployment 操作

```python
from btools import KubernetesUtils

# 获取 Deployment 列表
deployments = KubernetesUtils.get_deployments(namespace="default")
for dep in deployments:
    print(f"{dep['metadata']['name']}")

# 扩缩容 Deployment
success = KubernetesUtils.scale_deployment(
    name="my-deployment",
    replicas=5,
    namespace="default"
)

# 更新 Deployment 镜像
success = KubernetesUtils.update_deployment_image(
    name="my-deployment",
    container="my-container",
    image="myapp:v2.0.0",
    namespace="default"
)

# 删除 Deployment
success = KubernetesUtils.delete_deployment("my-deployment", namespace="default")
```

### Service 操作

```python
from btools import KubernetesUtils

# 获取 Service 列表
services = KubernetesUtils.get_services(namespace="default")
for svc in services:
    print(f"{svc['metadata']['name']} - {svc['spec']['type']}")

# 获取特定 Service 的详细信息
service_info = KubernetesUtils.get_service("my-service", namespace="default")
print(service_info)

# 删除 Service
success = KubernetesUtils.delete_service("my-service", namespace="default")
```

### 命名空间操作

```python
from btools import KubernetesUtils

# 获取所有命名空间
namespaces = KubernetesUtils.get_namespaces()
print(namespaces)

# 创建命名空间
success = KubernetesUtils.create_namespace("my-namespace")

# 删除命名空间
success = KubernetesUtils.delete_namespace("my-namespace")
```

## 高级功能

### 应用和删除资源

```python
from btools import KubernetesUtils

# 从 YAML 文件应用资源
success = KubernetesUtils.apply("deployment.yaml")

# 从 YAML 文件删除资源
success = KubernetesUtils.delete("deployment.yaml")

# 从字符串应用资源
yaml_content = """
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx:latest
"""
success = KubernetesUtils.apply_from_string(yaml_content)
```

### 查看日志

```python
from btools import KubernetesUtils

# 获取 Pod 日志
logs = KubernetesUtils.get_pod_logs(
    pod_name="my-pod",
    namespace="default",
    container="my-container",
    tail=100
)
print(logs)

# 实时跟踪日志
logs = KubernetesUtils.get_pod_logs(
    pod_name="my-pod",
    namespace="default",
    follow=True
)
```

### 端口转发

```python
from btools import KubernetesUtils

# 端口转发
success = KubernetesUtils.port_forward(
    pod_name="my-pod",
    local_port=8080,
    pod_port=80,
    namespace="default"
)
```

### 执行命令

```python
from btools import KubernetesUtils

# 在 Pod 中执行命令
result = KubernetesUtils.exec_in_pod(
    pod_name="my-pod",
    command=["ls", "-la"],
    namespace="default",
    container="my-container"
)
print(result)
```

### 配置管理

```python
from btools import KubernetesUtils

# 获取 ConfigMap
configmap = KubernetesUtils.get_configmap("my-configmap", namespace="default")

# 创建 ConfigMap
success = KubernetesUtils.create_configmap(
    name="my-configmap",
    data={"key": "value"},
    namespace="default"
)

# 获取 Secret
secret = KubernetesUtils.get_secret("my-secret", namespace="default")

# 创建 Secret
success = KubernetesUtils.create_secret(
    name="my-secret",
    data={"password": "secret"},
    namespace="default"
)
```

## 系统信息

```python
from btools import KubernetesUtils

# 检查 kubectl 是否可用
is_available = KubernetesUtils.is_available()

# 获取 Kubernetes 版本
version = KubernetesUtils.get_version()
print(version)

# 获取集群信息
info = KubernetesUtils.get_cluster_info()
print(info)

# 获取当前上下文
context = KubernetesUtils.get_current_context()
print(context)

# 切换上下文
success = KubernetesUtils.use_context("my-context")
```
