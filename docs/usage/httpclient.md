# HTTPClient 使用指南

`HTTPClient` 类是基于requests库实现的HTTP客户端，提供了发送GET、POST、PUT、PATCH、DELETE等HTTP请求的方法，支持Header管理、RESTful URL参数、文件上传下载等功能。

## 基本使用

```python
from btools import HTTPClient

# 创建HTTP客户端实例
client = HTTPClient(
    base_url="https://api.example.com",
    headers={"Content-Type": "application/json"},
    timeout=30
)

# 发送GET请求
response = client.get("/users", params={"page": 1, "limit": 10})
print(response.status_code)
print(response.json())

# 发送POST请求
response = client.post(
    "/users",
    json={"name": "John Doe", "email": "john@example.com"},
    params={"source": "web"}  # 查询参数
)
print(response.status_code)
print(response.json())

# 发送PUT请求
response = client.put(
    "/users/1",
    json={"name": "John Smith"}
)
print(response.status_code)

# 发送PATCH请求
response = client.patch(
    "/users/1",
    json={"email": "new@example.com"}
)
print(response.status_code)

# 发送DELETE请求
response = client.delete("/users/1", params={"force": "true"})
print(response.status_code)

# 关闭会话
client.close()
```

## Header 管理

### 添加 Header（保留原有 Header）

```python
# 添加Header（保留原有Header）
client.add_headers({"Authorization": "Bearer token123", "X-Custom-Header": "value"})
```

### 设置 Header（替换所有 Header）

```python
# 设置Header（替换所有Header）
client.set_headers({"Content-Type": "application/xml"})
```

### 清空所有 Header

```python
# 清空所有Header
client.clear_headers()
```

### 链式调用

```python
# 链式调用
client.add_headers({"Content-Type": "application/json"}) \
      .add_headers({"Authorization": "Bearer token123"})
```

## RESTful URL 路径参数

```python
# 替换URL路径中的参数，如 /users/{user_id}
response = client.get("/users/{user_id}", params={"user_id": 123, "include": "profile"})
# 实际请求URL: https://api.example.com/users/123?include=profile

response = client.put("/users/{user_id}/posts/{post_id}", 
                     params={"user_id": 123, "post_id": 456},
                     json={"title": "New Title"})
# 实际请求URL: https://api.example.com/users/123/posts/456
```

## 文件上传

使用 `requests-toolbelt` 库进行文件上传：

```python
# 上传单个文件
response = client.upload_file(
    url="/upload",
    file_path="local_file.txt",
    field_name="file",  # 表单字段名
    params={"category": "documents"}
)
print(response.status_code)

# 上传文件并附带其他表单数据
response = client.upload_file(
    url="/upload",
    file_path="document.pdf",
    field_name="file",
    form_data={
        "title": "测试文档",
        "description": "这是一个测试文件",
        "category": "pdf"
    },
    params={"user_id": 123}
)
print(response.status_code)
print(response.json())
```

## 文件下载

```python
# 下载文件
save_path = client.download_file(
    url="/files/document.pdf",
    save_path="downloads/document.pdf",
    params={"version": "latest"},
    chunk_size=8192  # 下载块大小
)
print(f"文件已保存到: {save_path}")
```

## 缓存支持

使用 `requests-cache` 库提供缓存功能：

```python
# 创建带缓存的HTTP客户端（使用内存缓存）
cache_client = HTTPClient(
    base_url="https://api.example.com",
    use_cache=True,
    cache_name="api_cache",
    cache_backend="memory"  # 可选：memory, sqlite, redis等
)

# 第一次请求会从服务器获取数据并缓存
response = cache_client.get("/users")
print("First request status:", response.status_code)

# 第二次相同的请求会从缓存中获取数据，不会发送实际的HTTP请求
response = cache_client.get("/users")
print("Second request status:", response.status_code)
print("From cache:", getattr(response, 'from_cache', False))
```

## 重试机制

```python
# 创建带重试机制的HTTP客户端
retry_client = HTTPClient(
    base_url="https://api.example.com",
    retry_enabled=True,
    retry_total=3,  # 最多重试3次
    retry_backoff_factor=0.5  # 重试间隔：0.5, 1, 2秒
)

# 当遇到网络错误或5xx错误时，会自动重试
response = retry_client.get("/users")
print("Response with retry:", response.status_code)
```

## 同时使用缓存和重试

```python
# 创建同时使用缓存和重试的HTTP客户端
full_client = HTTPClient(
    base_url="https://api.example.com",
    use_cache=True,
    cache_name="api_cache",
    retry_enabled=True,
    retry_total=3
)
```

## 使用上下文管理器

```python
with HTTPClient(base_url="https://api.example.com") as client:
    response = client.get("/users")
    print(response.json())
# 上下文管理器会自动关闭会话
```

## 使用绝对 URL

```python
response = client.get("https://google.com")
print(response.status_code)
```