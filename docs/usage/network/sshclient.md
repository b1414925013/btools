# SSHClient 使用指南

`SSHClient` 类是基于paramiko库实现的SSH客户端，支持直接连接和通过跳板机连接到目标Linux服务器。

## 基本使用

### 直接连接

```python
from btools import SSHClient

# 创建SSH客户端实例
ssh = SSHClient()

# 直接连接到服务器
ssh.connect(
    hostname="192.168.1.100",
    port=22,
    username="root",
    password="your_password"  # 或使用key_filename参数指定密钥文件
)

# 执行命令
result = ssh.execute("ls -la")
print("STDOUT:", result['stdout'])
print("STDERR:", result['stderr'])
print("Return Code:", result['returncode'])

# 使用sudo执行命令
result = ssh.execute("apt update", sudo=True, sudo_password="your_password")
print("STDOUT:", result['stdout'])

# 上传文件
ssh.upload("local_file.txt", "/remote/path/local_file.txt")

# 下载文件
ssh.download("/remote/path/remote_file.txt", "local_download.txt")

# 文件操作
ssh.file_operation('mkdir', '/remote/path/new_dir')  # 创建目录
ssh.file_operation('mv', '/remote/path/file1.txt', '/remote/path/file2.txt')  # 移动文件
ssh.file_operation('cp', '/remote/path/file.txt', '/remote/path/file_copy.txt')  # 复制文件
ssh.file_operation('rm', '/remote/path/unwanted.txt')  # 删除文件
ssh.file_operation('rmdir', '/remote/path/empty_dir')  # 删除空目录

# 关闭连接
ssh.close()
```

### 通过跳板机连接

```python
from btools import SSHClient

# 创建SSH客户端实例
ssh = SSHClient()

# 通过跳板机连接到目标服务器
ssh.connect_via_jump(
    # 跳板机信息
    jump_host="jump.example.com",
    # 目标服务器信息
    target_host="192.168.1.100",
    # 其他参数
    jump_port=22,
    jump_username="jump_user",
    jump_password="jump_password",  # 或使用jump_key_filename
    target_port=22,
    target_username="target_user",
    target_password="target_password"  # 或使用target_key_filename
)

# 执行命令
result = ssh.execute("ls -la")
print("STDOUT:", result['stdout'])

# 关闭连接
ssh.close()
```

## 代理支持

`SSHClient` 支持五种代理类型：
- `none`: 无代理（默认）
- `http`: HTTP代理
- `https`: HTTPS代理
- `socks4`: SOCKS4代理
- `socks5`: SOCKS5代理

### 使用SOCKS5代理连接

```python
from btools import SSHClient

# 创建SSH客户端实例
ssh = SSHClient()

# 通过SOCKS5代理连接
ssh.connect(
    hostname="192.168.1.100",
    username="root",
    password="your_password",
    # 代理设置
    proxy_type="socks5",
    proxy_host="proxy.example.com",
    proxy_port=1080,
    proxy_username="proxy_user",
    proxy_password="proxy_pass"
)

# 执行命令
result = ssh.execute("uname -a")
print("STDOUT:", result['stdout'])

# 关闭连接
ssh.close()
```

### 使用HTTP代理连接

```python
from btools import SSHClient

# 创建SSH客户端实例
ssh = SSHClient()

# 通过HTTP代理连接
ssh.connect(
    hostname="192.168.1.100",
    username="root",
    password="your_password",
    # 代理设置
    proxy_type="http",
    proxy_host="proxy.example.com",
    proxy_port=8080,
    proxy_username="proxy_user",
    proxy_password="proxy_pass"
)

# 执行命令
result = ssh.execute("uname -a")
print("STDOUT:", result['stdout'])

# 关闭连接
ssh.close()
```

## 交互式Shell

```python
from btools import SSHClient
import time

# 创建SSH客户端实例
ssh = SSHClient()

# 连接服务器
ssh.connect(
    hostname="192.168.1.100",
    username="root",
    password="your_password"
)

# 打开交互式shell
channel = ssh.open_shell()

# 发送命令
channel.send("ls -la\n")
time.sleep(0.5)  # 等待命令执行

# 读取输出
output = channel.recv(1024).decode('utf-8')
print(output)

# 发送另一个命令
channel.send("uname -a\n")
time.sleep(0.5)
output = channel.recv(1024).decode('utf-8')
print(output)

# 关闭channel
channel.close()

# 关闭连接
ssh.close()
```

## 使用上下文管理器

```python
from btools import SSHClient

# 使用上下文管理器，自动关闭连接
with SSHClient() as ssh:
    # 连接服务器
    ssh.connect(
        hostname="192.168.1.100",
        username="root",
        password="your_password"
    )
    
    # 执行命令
    result = ssh.execute("uname -a")
    print("STDOUT:", result['stdout'])

# 连接会在这里自动关闭
```

## 文件操作

### 上传文件

```python
# 上传单个文件
ssh.upload("local_file.txt", "/remote/path/local_file.txt")

# 上传目录
ssh.upload("local_dir", "/remote/path/local_dir")
```

### 下载文件

```python
# 下载单个文件
ssh.download("/remote/path/remote_file.txt", "local_download.txt")

# 下载目录
ssh.download("/remote/path/remote_dir", "local_dir")
```

### 服务器端文件操作

```python
# 创建目录
ssh.file_operation('mkdir', '/remote/path/new_dir')

# 移动文件
ssh.file_operation('mv', '/remote/path/file1.txt', '/remote/path/file2.txt')

# 复制文件
ssh.file_operation('cp', '/remote/path/file.txt', '/remote/path/file_copy.txt')

# 删除文件
ssh.file_operation('rm', '/remote/path/unwanted.txt')

# 删除空目录
ssh.file_operation('rmdir', '/remote/path/empty_dir')

# 删除非空目录
ssh.file_operation('rm', '/remote/path/non_empty_dir', recursive=True)
```