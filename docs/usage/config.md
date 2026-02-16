# Config 使用指南

`Config` 类提供了从JSON或YAML文件加载、保存和操作配置数据的方法。

## 支持的文件格式

- **JSON**：`.json` 文件
- **YAML**：`.yaml` 或 `.yml` 文件

## 基本使用

### 使用JSON文件

```python
from btools import Config

# 创建配置实例（如果文件存在则加载）
config = Config("config.json")

# 设置配置值
config.set("database.host", "localhost")
config.set("database.port", 5432)
config.set("database.credentials.username", "admin")
config.set("database.credentials.password", "password123")

# 获取配置值
host = config.get("database.host")
port = config.get("database.port")
username = config.get("database.credentials.username")
password = config.get("database.credentials.password")
api_key = config.get("api.key", "default_key")  # 带默认值

# 保存配置到文件
config.save()

# 删除配置值
config.remove("database.credentials.password")
config.save()
```

### 使用YAML文件

```python
from btools import Config

# 创建配置实例（如果文件存在则加载）
config = Config("config.yaml")  # 或使用 config.yml 扩展名

# 设置配置值
config.set("database.host", "localhost")
config.set("database.port", 5432)
config.set("database.credentials.username", "admin")
config.set("database.credentials.password", "password123")

# 获取配置值
host = config.get("database.host")
port = config.get("database.port")
username = config.get("database.credentials.username")
password = config.get("database.credentials.password")
api_key = config.get("api.key", "default_key")  # 带默认值

# 保存配置到文件
config.save()

# 删除配置值
config.remove("database.credentials.password")
config.save()
```

## 生成的YAML文件示例

```yaml
database:
  host: localhost
  port: 5432
  credentials:
    username: admin
```

## 高级功能

### 嵌套配置

`Config` 支持通过点号分隔的路径访问嵌套配置：

```python
# 设置嵌套配置
config.set("app.settings.theme", "dark")
config.set("app.settings.language", "zh-CN")

# 获取嵌套配置
theme = config.get("app.settings.theme")
language = config.get("app.settings.language")
```

### 配置验证

可以通过默认值确保配置项存在：

```python
# 如果配置项不存在，返回默认值
timeout = config.get("app.timeout", 30)
retries = config.get("app.retries", 3)
```

### 配置合并

可以通过多次调用 `set` 方法合并配置：

```python
# 加载基础配置
config = Config("base_config.yaml")

# 合并额外配置
config.set("app.name", "My Application")
config.set("app.version", "1.0.0")

# 保存合并后的配置
config.save()
```