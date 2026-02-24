# ResourceUtils 使用指南

`ResourceUtils` 是一个资源工具类，提供了丰富的资源加载、读取等功能，支持从文件系统、包路径等多种来源获取资源。

## 功能特性

- **资源路径获取**：支持从文件系统、包路径等获取资源路径
- **资源流获取**：支持获取资源的输入流
- **资源内容读取**：支持读取资源的文本内容和字节内容
- **资源URL获取**：支持获取资源的URL
- **资源存在检查**：支持检查资源是否存在
- **URL资源加载**：支持从网络URL加载资源

## 基本用法

### 导入

```python
from btools import ResourceUtils
```

### 示例

#### 1. 获取资源路径

```python
# 从文件系统获取资源路径
path = ResourceUtils.get_resource_path('config.properties')
print(f"Resource path: {path}")

# 从类所在的包中获取资源路径
class MyClass:
    pass

path = ResourceUtils.get_resource_path('data.json', MyClass)
print(f"Resource path from class: {path}")
```

#### 2. 获取资源输入流

```python
# 从文件系统获取资源输入流
stream = ResourceUtils.get_resource_stream('config.properties')
if stream:
    content = stream.read().decode('utf-8')
    print(f"Resource content: {content}")
    stream.close()

# 使用别名方法
stream = ResourceUtils.get_resource_as_stream('config.properties')
if stream:
    content = stream.read().decode('utf-8')
    print(f"Resource content (alias): {content}")
    stream.close()
```

#### 3. 读取资源内容

```python
# 读取文本资源
content = ResourceUtils.read_resource('config.properties', encoding='utf-8')
print(f"Text content: {content}")

# 读取字节资源
bytes_content = ResourceUtils.read_resource_bytes('image.png')
print(f"Bytes content length: {len(bytes_content)}")

# 使用别名方法
text_content = ResourceUtils.get_resource_text('config.properties')
print(f"Text content (alias): {text_content}")

bytes_content = ResourceUtils.get_resource_bytes('image.png')
print(f"Bytes content length (alias): {len(bytes_content)}")
```

#### 4. 获取资源URL

```python
# 获取本地资源的URL
url = ResourceUtils.get_resource_url('config.properties')
print(f"Resource URL: {url}")

# 直接传递URL
web_url = 'https://example.com/api/data'
url = ResourceUtils.get_resource_url(web_url)
print(f"Web URL: {url}")
```

#### 5. 检查资源是否存在

```python
# 检查资源是否存在
exists = ResourceUtils.exists('config.properties')
print(f"Resource exists: {exists}")

# 检查不存在的资源
exists = ResourceUtils.exists('non_existent_file.txt')
print(f"Non-existent resource exists: {exists}")
```

#### 6. 从URL加载资源

```python
# 从网络URL加载文本资源
url = 'https://httpbin.org/get'
content = ResourceUtils.load_from_url(url, encoding='utf-8')
print(f"Content from URL: {content}")

# 从网络URL加载字节资源
image_url = 'https://example.com/image.png'
bytes_content = ResourceUtils.load_from_url(image_url, encoding=None)
print(f"Image bytes length: {len(bytes_content)}")
```

## 高级用法

### 从类所在包加载资源

当你需要从某个类所在的包中加载资源时，可以使用 `cls` 参数：

```python
class ConfigLoader:
    def load_config(self):
        # 从 ConfigLoader 所在的包中加载 config.json
        content = ResourceUtils.read_resource('config.json', cls=self.__class__)
        return content

loader = ConfigLoader()
config = loader.load_config()
print(f"Loaded config: {config}")
```

### 处理资源加载失败

`ResourceUtils` 的所有方法在资源不存在或加载失败时都会返回 `None`，你可以根据返回值进行错误处理：

```python
# 尝试加载资源
content = ResourceUtils.read_resource('config.properties')

if content is None:
    # 资源加载失败，使用默认配置
    print("Failed to load config.properties, using default configuration")
    content = "default.key=default.value"
else:
    # 资源加载成功
    print("Loaded config.properties successfully")

# 处理配置...
```

### 跨平台资源访问

`ResourceUtils` 会自动处理跨平台的路径差异，确保在不同操作系统上都能正确访问资源：

```python
# 在任何平台上都能正确获取资源路径
path = ResourceUtils.get_resource_path('resources/data/config.json')
print(f"Cross-platform resource path: {path}")
```

## 注意事项

1. **资源查找顺序**：`ResourceUtils` 会按照以下顺序查找资源：
   - 如果提供了 `cls` 参数，首先从该类所在的包中查找
   - 然后从当前工作目录查找
   - 最后从 Python 路径中查找

2. **异常处理**：所有方法都会捕获异常并返回 `None`，确保即使资源不存在也不会导致程序崩溃

3. **URL 支持**：当资源名称已经是一个完整的 URL 时，会直接返回该 URL

4. **编码处理**：读取文本资源时，默认使用 UTF-8 编码，你可以根据需要指定其他编码

5. **流资源管理**：获取资源流后，记得关闭流以避免资源泄漏

## 应用场景

`ResourceUtils` 适用于以下场景：

- **配置文件加载**：加载应用程序的配置文件
- **资源文件读取**：读取应用程序所需的资源文件，如模板、数据文件等
- **跨平台资源访问**：在不同操作系统上统一访问资源
- **网络资源加载**：从网络 URL 加载资源
- **包内资源访问**：访问打包在 Python 包中的资源文件

这些功能使得 `ResourceUtils` 成为处理各种资源的强大工具，可以大大简化资源加载和访问的代码。
