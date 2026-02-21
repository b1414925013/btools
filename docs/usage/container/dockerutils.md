# DockerUtils 使用指南

`DockerUtils` 类提供了 Docker 操作封装，包括镜像构建、容器管理等功能。

## 基本使用

### 镜像操作

```python
from btools import DockerUtils

# 构建镜像
success = DockerUtils.build_image(
    path=".",
    tag="myapp:latest",
    dockerfile="Dockerfile"
)

# 列出所有镜像
images = DockerUtils.list_images()
for image in images:
    print(f"{image['Repository']}:{image['Tag']}")

# 拉取镜像
success = DockerUtils.pull_image("nginx:latest")

# 推送镜像
success = DockerUtils.push_image("myapp:latest")

# 删除镜像
success = DockerUtils.remove_image("myapp:latest")
```

### 容器操作

```python
from btools import DockerUtils

# 运行容器
success = DockerUtils.run_container(
    image="nginx:latest",
    name="my-nginx",
    ports={"8080": "80"},
    volumes={"/host/path": "/container/path"},
    environment={"ENV": "production"}
)

# 列出所有容器
containers = DockerUtils.list_containers(all=True)
for container in containers:
    print(f"{container['Names']} - {container['Status']}")

# 启动容器
success = DockerUtils.start_container("my-nginx")

# 停止容器
success = DockerUtils.stop_container("my-nginx")

# 重启容器
success = DockerUtils.restart_container("my-nginx")

# 删除容器
success = DockerUtils.remove_container("my-nginx")
```

### 容器信息

```python
from btools import DockerUtils

# 获取容器日志
logs = DockerUtils.get_container_logs("my-nginx", tail=100)
print(logs)

# 检查容器是否运行
is_running = DockerUtils.is_container_running("my-nginx")

# 执行容器内命令
result = DockerUtils.exec_container(
    "my-nginx",
    ["ls", "-la"]
)
print(result)
```

## 高级功能

### 网络操作

```python
from btools import DockerUtils

# 创建网络
success = DockerUtils.create_network("my-network")

# 列出网络
networks = DockerUtils.list_networks()
print(networks)

# 连接容器到网络
success = DockerUtils.connect_container_to_network("my-nginx", "my-network")

# 断开容器从网络
success = DockerUtils.disconnect_container_from_network("my-nginx", "my-network")
```

### 卷操作

```python
from btools import DockerUtils

# 创建卷
success = DockerUtils.create_volume("my-volume")

# 列出卷
volumes = DockerUtils.list_volumes()
print(volumes)

# 删除卷
success = DockerUtils.remove_volume("my-volume")
```

### 系统信息

```python
from btools import DockerUtils

# 检查Docker是否可用
is_available = DockerUtils.is_available()

# 获取Docker版本
version = DockerUtils.get_version()
print(version)

# 获取Docker系统信息
info = DockerUtils.get_info()
print(info)
```

## Docker Compose 支持

```python
from btools import DockerUtils

# 使用Docker Compose启动服务
success = DockerUtils.compose_up("docker-compose.yml")

# 使用Docker Compose停止服务
success = DockerUtils.compose_down("docker-compose.yml")

# 查看Docker Compose服务状态
status = DockerUtils.compose_ps("docker-compose.yml")
print(status)
```
