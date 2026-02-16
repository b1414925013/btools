# NetUtils 使用指南

`NetUtils` 是一个网络工具类，提供了丰富的网络操作方法，包括获取主机名、获取IP地址、检查IP类型、检查是否为私有IP、检查是否为回环IP、ping操作、URL编解码等功能。

## 功能特性

- 获取主机名
- 获取IP地址
- 检查是否为IPv4
- 检查是否为IPv6
- 检查是否为私有IP
- 检查是否为回环IP
- ping操作
- URL编解码

## 基本用法

### 导入

```python
from btools import NetUtils
```

### 示例

#### 获取主机名和IP地址

```python
# 获取主机名
print(NetUtils.get_hostname())  # 输出: 主机名

# 获取IP地址
print(NetUtils.get_ip_address())  # 输出: IP地址
```

#### IP类型检查

```python
# 检查是否为IPv4
print(NetUtils.is_ipv4("192.168.1.1"))  # 输出: True
print(NetUtils.is_ipv4("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # 输出: False

# 检查是否为IPv6
print(NetUtils.is_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # 输出: True
print(NetUtils.is_ipv6("192.168.1.1"))  # 输出: False

# 检查是否为私有IP
print(NetUtils.is_private_ip("192.168.1.1"))  # 输出: True
print(NetUtils.is_private_ip("8.8.8.8"))  # 输出: False

# 检查是否为回环IP
print(NetUtils.is_loopback_ip("127.0.0.1"))  # 输出: True
print(NetUtils.is_loopback_ip("192.168.1.1"))  # 输出: False
```

#### ping操作

```python
# ping本地主机
result = NetUtils.ping("127.0.0.1", count=1, timeout=1)
print(result)  # 输出: True

# ping外部主机
result = NetUtils.ping("8.8.8.8", count=1, timeout=1)
print(result)  # 输出: True 或 False
```

#### URL编解码

```python
# URL编码
data = "Hello World!"
encoded = NetUtils.url_encode(data)
print(encoded)  # 输出: Hello%20World%21

# URL解码
decoded = NetUtils.url_decode(encoded)
print(decoded)  # 输出: Hello World!
```

## 高级用法

### 批量检查IP地址

```python
# 批量检查IP地址
ips = ["192.168.1.1", "8.8.8.8", "127.0.0.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]
for ip in ips:
    print(f"IP: {ip}")
    print(f"  是IPv4: {NetUtils.is_ipv4(ip)}")
    print(f"  是IPv6: {NetUtils.is_ipv6(ip)}")
    print(f"  是私有IP: {NetUtils.is_private_ip(ip)}")
    print(f"  是回环IP: {NetUtils.is_loopback_ip(ip)}")
    print(f"  可ping通: {NetUtils.ping(ip, count=1, timeout=1)}")
```

### 构建URL

```python
# 构建URL
base_url = "https://api.example.com"
endpoint = "/users"
params = {
    "name": "John Doe",
    "age": 30
}

# 编码参数
encoded_params = "&".join([f"{NetUtils.url_encode(k)}={NetUtils.url_encode(v)}" for k, v in params.items()])

# 构建完整URL
url = f"{base_url}{endpoint}?{encoded_params}"
print(url)  # 输出: https://api.example.com/users?name=John%20Doe&age=30
```

## 注意事项

1. `ping()` 方法可能会因为网络环境或防火墙设置而返回 False，即使主机实际上是可达的。
2. 获取IP地址可能会返回多个IP地址，具体取决于系统配置。

## 总结

`NetUtils` 提供了全面的网络操作功能，简化了网络操作的复杂度，使代码更加简洁易读。无论是基本的网络信息获取还是高级的网络操作，`NetUtils` 都能满足你的需求。