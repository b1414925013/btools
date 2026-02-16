# Logger 使用指南

`Logger` 类提供了一个简单的接口，用于记录不同严重级别的日志消息。

## 基本使用

```python
from btools import Logger

# 创建日志记录器实例
logger = Logger(name="myapp", level=Logger.INFO)

# 记录日志消息
logger.debug("这是一条调试消息")
logger.info("这是一条信息消息")
logger.warning("这是一条警告消息")
logger.error("这是一条错误消息")
logger.critical("这是一条严重错误消息")

# 记录到文件
file_logger = Logger(name="myapp", level=Logger.INFO, file_path="app.log")
file_logger.info("这条消息将同时记录到控制台和文件")
```

## 日志级别

`Logger` 支持以下日志级别（从低到高）：

- `Logger.DEBUG` (10)
- `Logger.INFO` (20)
- `Logger.WARNING` (30)
- `Logger.ERROR` (40)
- `Logger.CRITICAL` (50)

## 高级功能

### 自动获取调用方信息

`Logger` 会自动记录日志消息的调用方信息，包括：
- 调用文件路径
- 调用行号
- 调用函数名

### 默认应用名称

如果不指定 `name` 参数，`Logger` 会使用 `Default_AppName` 作为默认应用名称：

```python
# 使用默认应用名称
logger = Logger(level=Logger.INFO)
logger.info("使用默认应用名称的日志")
```

### 日志格式

日志消息的格式为：
```
YYYY-MM-DD HH:MM:SS,mmm - 应用名称 - 日志级别 - 调用文件:行号 - 日志消息
```

例如：
```
2023-12-25 14:30:00,123 - myapp - INFO - main.py:42 - 这是一条信息消息
```