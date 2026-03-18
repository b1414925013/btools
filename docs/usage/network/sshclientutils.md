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

# 执行命令并清洗输出（去除ANSI转义码等）
result = ssh.execute("ls --color=always", clean_output=True)
print("清洗后的输出:", result['stdout'])

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

## 输出清洗和命令过滤

SSHClient 提供了灵活的输出控制选项，可以根据需要清洗输出内容或移除命令本身和提示符。

### clean_output 参数

**作用：** 清洗输出内容，去除ANSI转义码、控制字符等终端控制序列

**适用场景：**
- 命令输出包含颜色代码（如 `ls --color=always`）
- 输出包含终端控制序列（如光标移动、清除屏幕等）
- 需要纯净的文本输出用于进一步处理
- 输出需要显示在非终端环境中（如Web界面）

**默认值：**
- `execute` 方法：`False`（保持向后兼容）
- `execute_as_root` 方法：`False`（保持向后兼容）
- `su_to_root` 方法：`True`（交互式shell通常需要清洗）
- `start_root_shell` 方法：`True`（交互式shell通常需要清洗）
- `execute_in_root_shell` 方法：`True`（交互式shell通常需要清洗）

**使用示例：**

```python
# 基本命令执行，不清洗输出（默认）
result = ssh.execute("ls --color=always")
print("原始输出:", result['stdout'])  # 包含ANSI颜色代码

# 清洗输出
result = ssh.execute("ls --color=always", clean_output=True)
print("清洗后输出:", result['stdout'])  # 不包含ANSI颜色代码

# root命令执行，不清洗输出（默认）
result = ssh.execute_as_root('ls --color=always /root', root_password='root_password')
print("原始输出:", result['stdout'])

# root命令执行，清洗输出
result = ssh.execute_as_root('ls --color=always /root', root_password='root_password', clean_output=True)
print("清洗后输出:", result['stdout'])

# 在root shell中执行命令，默认清洗输出
result = ssh.execute_in_root_shell('ls --color=always')
print("清洗后输出:", result['stdout'])

# 在root shell中执行命令，不清洗输出
result = ssh.execute_in_root_shell('ls --color=always', clean_output=False)
print("原始输出:", result['stdout'])
```

**清洗的内容：**
- ANSI颜色转义码（如 `\x1b[31m` 红色）
- CSI序列（光标移动、清除屏幕等）
- OSC序列（设置窗口标题等）
- 字符集切换序列
- 私有序列
- 控制字符（除了换行符）
- 多余的回车符

### remove_command 参数

**作用：** 移除命令本身和提示符，只保留命令的实际输出

**适用场景：**
- 只需要命令的输出结果，不需要命令回显
- 需要解析输出内容，命令和提示符会干扰解析
- 输出需要用于自动化处理或日志记录
- 希望输出更简洁清晰

**默认值：** `False`（保持原有行为）

**使用示例：**

```python
# 启动 root shell 会话
result = ssh.start_root_shell('root_password')
if result['success']:
    # 执行命令，不移除命令和提示符（默认）
    result1 = ssh.execute_in_root_shell('whoami')
    print("完整输出:", result1['stdout'])
    # 输出示例：
    # whoami
    # root
    # [root@server ~]#
    
    # 执行命令，移除命令和提示符
    result2 = ssh.execute_in_root_shell('whoami', remove_command=True)
    print("仅命令输出:", result2['stdout'])
    # 输出：root
    
    # 执行多条命令，移除命令和提示符
    result3 = ssh.execute_in_root_shell('ls -la', remove_command=True)
    print("文件列表:", result3['stdout'])
    # 只包含文件列表，不包含命令和提示符
    
    # 执行命令，同时清洗输出和移除命令
    result4 = ssh.execute_in_root_shell('ls --color=always', clean_output=True, remove_command=True)
    print("纯净输出:", result4['stdout'])
    # 既没有ANSI代码，也没有命令和提示符
    
    ssh.close_root_shell()
```

**移除的内容：**
- 命令本身（如 `whoami`、`ls -la`）
- 命令提示符（如 `[root@server ~]#`、`$`、`>`）
- 空行
- 以 `#`、`$`、`->` 或 `>` 结尾的行

### 参数组合使用

`clean_output` 和 `remove_command` 可以组合使用，根据需要灵活控制输出：

```python
# 组合1：不清洗，不移除（最原始的输出）
result = ssh.execute_in_root_shell('ls --color=always', clean_output=False, remove_command=False)
# 包含：ANSI代码 + 命令 + 提示符 + 实际输出

# 组合2：清洗，不移除（去除控制序列，保留命令和提示符）
result = ssh.execute_in_root_shell('ls --color=always', clean_output=True, remove_command=False)
# 包含：命令 + 提示符 + 实际输出（无ANSI代码）

# 组合3：不清洗，移除（保留ANSI代码，去除命令和提示符）
result = ssh.execute_in_root_shell('ls --color=always', clean_output=False, remove_command=True)
# 包含：ANSI代码 + 实际输出

# 组合4：清洗，移除（最纯净的输出）
result = ssh.execute_in_root_shell('ls --color=always', clean_output=True, remove_command=True)
# 包含：仅实际输出（无ANSI代码，无命令，无提示符）
```

### 使用建议

1. **选择 clean_output=True 的情况：**
   - 输出需要显示在非终端环境（如Web界面、日志文件）
   - 输出需要进一步处理或解析
   - 输出包含大量终端控制序列
   - 希望输出更易读

2. **选择 clean_output=False 的情况：**
   - 需要保留原始输出格式
   - 输出需要在终端中显示（保留颜色和格式）
   - 调试或查看完整输出内容
   - 保持向后兼容性

3. **选择 remove_command=True 的情况：**
   - 只需要命令的实际输出结果
   - 输出需要用于自动化处理
   - 命令和提示符会干扰输出解析
   - 希望输出更简洁

4. **选择 remove_command=False 的情况：**
   - 需要查看完整的交互过程
   - 调试或排查问题
   - 需要确认命令是否正确执行
   - 保持向后兼容性

## 切换到 root 用户执行命令

SSHClient 提供两种方式执行 root 权限命令，各有不同的适用场景：

### 方法一：execute_as_root - 直接执行 root 命令

**适用场景：**
- 偶尔执行 root 命令（命令数量少、频率低）
- 不需要保持 shell 会话状态
- 希望每次执行都是独立的会话
- 对性能要求不高的场景

**特点：**
- 每次执行都使用 `su -c` 方式，独立会话
- 每次都需要提供 root 密码
- 不占用服务器资源
- 执行速度相对较慢（每次都要切换用户）

```python
from btools import SSHClient

# 创建SSH客户端实例
ssh = SSHClient()

# 连接到服务器（使用普通用户）
ssh.connect(
    hostname="192.168.1.100",
    username="user",
    password="user_password"
)

# 执行 root 权限命令
result = ssh.execute_as_root('cat /etc/shadow', root_password='root_password')
print("/etc/shadow 内容:", result['stdout'])
print("错误信息:", result['stderr'])
print("返回码:", result['returncode'])

# 执行 root 权限命令并清洗输出
result = ssh.execute_as_root('ls --color=always /root', root_password='root_password', clean_output=True)
print("清洗后的输出:", result['stdout'])

# 执行多条 root 命令
result1 = ssh.execute_as_root('systemctl status sshd', root_password='root_password')
print("SSH服务状态:", result1['stdout'])

result2 = ssh.execute_as_root('fdisk -l', root_password='root_password')
print("磁盘信息:", result2['stdout'])

# 重启服务
result3 = ssh.execute_as_root('systemctl restart nginx', root_password='root_password')
if result3['returncode'] == 0:
    print("Nginx 重启成功")
else:
    print(f"Nginx 重启失败: {result3['stderr']}")

# 关闭连接
ssh.close()
```

### 方法二：保持 root shell 会话

**适用场景：**
- 需要连续执行多条 root 命令
- 命令执行频率较高
- 需要共享 root 会话状态（如工作目录、环境变量等）
- 对执行速度有要求的场景

**特点：**
- 启动一次 root shell，保持会话打开
- 只需在启动时输入一次密码
- 保持 shell 会话状态（工作目录、环境变量等）
- 执行速度更快
- 会占用服务器资源，使用完毕后需要关闭

```python
from btools import SSHClient

# 创建SSH客户端实例
ssh = SSHClient()

# 连接到服务器（使用普通用户）
ssh.connect(
    hostname="192.168.1.100",
    username="user",
    password="user_password"
)

# 启动 root shell 会话
result = ssh.start_root_shell('root_password')
if result['success']:
    print("成功切换到 root 用户")
    
    # 在保持的 root shell 中执行多条命令
    result1 = ssh.execute_in_root_shell('whoami')
    print("当前用户:", result1['stdout'])  # 输出: root
    
    result2 = ssh.execute_in_root_shell('cd /root && pwd')
    print("当前目录:", result2['stdout'])  # 输出: /root
    
    # 继续执行命令，工作目录保持在 /root
    result3 = ssh.execute_in_root_shell('ls -la')
    print("root 目录内容:", result3['stdout'])
    
    # 执行系统管理命令
    result4 = ssh.execute_in_root_shell('systemctl status nginx')
    print("Nginx 状态:", result4['stdout'])
    
    # 检查执行结果
    if result4['success']:
        print("命令执行成功")
    else:
        print(f"命令执行失败: {result4['stderr']}")
    
    # 使用完毕后关闭 root shell
    ssh.close_root_shell()
    print("root shell 已关闭")
else:
    print(f"切换到 root 失败: {result['stderr']}")

# 关闭SSH连接
ssh.close()
```

### 高级用法：指定提示符

当需要在 root shell 中执行交互式命令或切换到其他用户时，可以使用 `expected_prompt` 参数指定期望的提示符。

**适用场景：**
- 切换到其他用户（如 dbuser）
- 进入 Docker 容器
- 进入数据库命令行（如 MySQL、PostgreSQL）
- 执行需要交互的命令

```python
from btools import SSHClient

# 创建SSH客户端实例
ssh = SSHClient()

# 连接到服务器
ssh.connect(
    hostname="192.168.1.100",
    username="user",
    password="user_password"
)

# 启动 root shell 会话
result = ssh.start_root_shell('root_password')
if result['success']:
    print("成功切换到 root 用户")
    
    # 1. 切换到 dbuser（提示符变为 $）
    result1 = ssh.execute_in_root_shell('su - dbuser', expected_prompt='$')
    print("成功切换到 dbuser")
    
    # 2. 使用 docker 进入容器（提示符变为 #）
    result2 = ssh.execute_in_root_shell(
        'docker exec -it my_container bash', 
        expected_prompt='#'
    )
    print("成功进入容器")
    
    # 3. 进入 MySQL 命令行
    # 首先输入 mysql 命令，等待密码提示
    result3 = ssh.execute_in_root_shell(
        'mysql -u root -p', 
        expected_prompt='Enter password:'
    )
    
    # 输入密码，等待 mysql> 提示符
    result4 = ssh.execute_in_root_shell(
        'mysql_password', 
        expected_prompt='mysql>'
    )
    
    # 执行 SQL 查询
    result5 = ssh.execute_in_root_shell(
        'SELECT * FROM users LIMIT 5;', 
        expected_prompt='mysql>'
    )
    print("查询结果:", result5['stdout'])
    
    # 退出 MySQL
    result6 = ssh.execute_in_root_shell(
        'exit', 
        expected_prompt='#'
    )
    
    # 退出容器
    result7 = ssh.execute_in_root_shell(
        'exit', 
        expected_prompt='$'
    )
    
    # 退出 dbuser，回到 root
    result8 = ssh.execute_in_root_shell(
        'exit', 
        expected_prompt='#'
    )
    
    # 关闭 root shell
    ssh.close_root_shell()
    print("root shell 已关闭")

# 关闭SSH连接
ssh.close()
```

**提示符匹配规则：**

- `#` - root 用户提示符
- `$` - 普通用户提示符
- `mysql>` - MySQL 命令行提示符
- `postgres=#` - PostgreSQL 命令行提示符
- `->` - 数据库命令行提示符（如某些 NoSQL 数据库）
- `>` - Windows CMD 或其他命令行提示符
- 任何自定义字符串 - 根据实际需求指定

**注意事项：**

1. 如果不指定 `expected_prompt`，系统会自动检测常见的提示符（#、$、->、>）
2. 指定 `expected_prompt` 可以提高匹配的准确性，特别是在复杂的交互场景中
3. 提示符匹配是包含关系，只要输出中包含指定的字符串即可匹配成功

### 两种方法对比

| 特性 | execute_as_root | 保持 root shell 会话 |
|------|-----------------|---------------------|
| **密码输入** | 每次执行都需要输入 | 只需启动时输入一次 |
| **会话状态** | 每次都是新会话 | 保持会话状态 |
| **执行速度** | 较慢（每次切换用户） | 较快（保持会话） |
| **资源占用** | 不占用服务器资源 | 占用服务器资源 |
| **适用场景** | 偶尔执行、命令少 | 频繁执行、命令多 |
| **使用复杂度** | 简单 | 需要管理会话生命周期 |

### 使用建议

1. **选择 execute_as_root 的情况：**
   - 只需要执行 1-2 条 root 命令
   - 命令之间没有依赖关系
   - 不需要保持工作目录或环境变量
   - 对执行速度要求不高

2. **选择保持 root shell 会话的情况：**
   - 需要执行 3 条以上的 root 命令
   - 命令之间有依赖关系（如 cd 后执行其他命令）
   - 需要保持工作目录或环境变量
   - 对执行速度有要求
   - 需要频繁执行 root 命令

### 在跳板机场景中使用

两种方法都支持跳板机场景，您可以根据需要选择：

**使用 execute_as_root：**

```python
from btools import SSHClient

# 创建SSH客户端实例
ssh = SSHClient()

# 通过跳板机连接到目标服务器
ssh.connect_via_jump(
    jump_host="jump.example.com",
    jump_username="jump_user",
    jump_password="jump_password",
    target_host="192.168.1.100",
    target_username="user",
    target_password="user_password"
)

# 执行 root 权限命令
result = ssh.execute_as_root('cat /etc/passwd', root_password='root_password')
print(result['stdout'])

# 执行更多 root 命令
result = ssh.execute_as_root('ls -la /root', root_password='root_password')
print(result['stdout'])

# 关闭连接
ssh.close()
```

**使用保持 root shell 会话：**

```python
from btools import SSHClient

# 创建SSH客户端实例
ssh = SSHClient()

# 通过跳板机连接到目标服务器
ssh.connect_via_jump(
    jump_host="jump.example.com",
    jump_username="jump_user",
    jump_password="jump_password",
    target_host="192.168.1.100",
    target_username="user",
    target_password="user_password"
)

# 启动 root shell 会话
result = ssh.start_root_shell('root_password')
if result['success']:
    # 执行多条 root 命令
    result1 = ssh.execute_in_root_shell('whoami')
    print(result1['stdout'])
    
    result2 = ssh.execute_in_root_shell('cd /root && ls -la')
    print(result2['stdout'])
    
    result3 = ssh.execute_in_root_shell('systemctl status nginx')
    print(result3['stdout'])
    
    # 关闭 root shell
    ssh.close_root_shell()

# 关闭连接
ssh.close()
```

### 注意事项

1. **密码安全**：避免在代码中硬编码密码，建议使用环境变量或配置文件
   ```python
   import os
   root_password = os.environ.get('ROOT_PASSWORD')
   result = ssh.execute_as_root('whoami', root_password=root_password)
   ```

2. **超时设置**：`start_root_shell` 方法默认超时时间为 10 秒，可根据网络情况调整
   ```python
   result = ssh.start_root_shell("root_password", timeout=20)
   ```

3. **错误处理**：建议始终检查执行是否成功
   ```python
   # execute_as_root
   result = ssh.execute_as_root('whoami', root_password='root_password')
   if result['returncode'] != 0:
       print(f"执行失败: {result['stderr']}")
   
   # 保持 root shell 会话
   result = ssh.start_root_shell("root_password")
   if not result['success']:
       print(f"启动失败: {result['stderr']}")
   ```

4. **资源管理**：使用保持 root shell 会话时，务必在完成后关闭
   ```python
   try:
       ssh.start_root_shell('root_password')
       # 执行命令...
   finally:
       ssh.close_root_shell()
   ```

5. **会话状态**：保持 root shell 会话时，命令之间会共享工作目录和环境变量
   ```python
   ssh.start_root_shell('root_password')
   ssh.execute_in_root_shell('cd /tmp')  # 切换到 /tmp
   ssh.execute_in_root_shell('pwd')      # 输出 /tmp（保持了工作目录）
   ```

6. **兼容性**：两种方法都适用于大多数 Linux 发行版（CentOS、Ubuntu、Debian 等），
   支持中英文密码提示

7. **性能考虑**：
   - 偶尔执行少量命令：使用 `execute_as_root`
   - 频繁执行多条命令：使用保持 root shell 会话
   - 长时间不使用时，记得关闭 root shell 会话释放资源