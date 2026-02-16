# btools

一个用于Python项目的实用工具类和函数集合。

## 目录

- [概述](#概述)
- [安装](#安装)
- [快速开始](#快速开始)
- [文档](#文档)
- [如何打包](#如何打包)
- [如何添加新类](#如何添加新类)
- [许可证](#许可证)

## 概述

`btools` 是一个Python包，提供了一系列实用的工具类和函数，用于简化常见的开发任务。它包括：

- **Logger**: 一个简单而强大的日志记录类
- **Config**: 配置管理，支持JSON和YAML文件
- **HTTPClient**: HTTP客户端，基于requests库实现
- **SSHClient**: SSH客户端，支持直接连接和通过跳板机连接
- **CSVHandler**: CSV文件处理，支持CSV文件的读写
- **ExcelHandler**: Excel文件处理，支持Excel文件的读写和单元格更新
- **TestUtils**: 自动化测试工具，提供测试数据生成、测试报告生成等功能
- **AssertEnhancer**: 断言增强工具，提供更强大的断言方法
- **SeleniumUtils**: 基于Selenium的Web自动化测试工具
- **PlaywrightUtils**: 基于Playwright的Web自动化测试工具
- **AppiumUtils**: 基于Appium的移动应用自动化测试工具
- **Validator**: 常见类型和格式的数据验证工具
- **Converter**: 各种数据类型的转换工具

## 安装

### 从wheel文件安装

1. 首先，按照[如何打包](#如何打包)部分的说明打包项目
2. 然后安装生成的wheel文件：

```bash
pip install btools-1.0.0-py3-none-any.whl
```

### 从源码安装

```bash
pip install -e .
```

## 快速开始

```python
# 导入btools
from btools import Logger, Config, HTTPClient, SSHClient

# 使用Logger
logger = Logger(name="myapp", level=Logger.INFO)
logger.info("Hello, btools!")

# 使用Config
config = Config("config.yaml")
config.set("database.host", "localhost")

# 使用HTTPClient
client = HTTPClient(base_url="https://api.example.com")
response = client.get("/users")

# 使用SSHClient
ssh = SSHClient()
ssh.connect(hostname="192.168.1.100", username="root", password="your_password")
result = ssh.execute("ls -la")
print(result['stdout'])
ssh.close()
```

## 文档

详细的使用文档请参考：

- **使用指南**:
  - [Logger使用指南](docs/usage/logger.md)
  - [Config使用指南](docs/usage/config.md)
  - [HTTPClient使用指南](docs/usage/httpclient.md)
  - [SSHClient使用指南](docs/usage/sshclient.md)
  - [CSVHandler使用指南](docs/usage/csvhandler.md)
  - [ExcelHandler使用指南](docs/usage/excelhandler.md)
  - [TestUtils使用指南](docs/usage/testutils.md)
  - [AssertEnhancer使用指南](docs/usage/assertenhancer.md)
  - [SeleniumUtils使用指南](docs/usage/seleniumutils.md)
  - [PlaywrightUtils使用指南](docs/usage/playwrightutils.md)
  - [AppiumUtils使用指南](docs/usage/appiumutils.md)
  - [Validator使用指南](docs/usage/validator.md)
  - [Converter使用指南](docs/usage/converter.md)

- **开发指南**:
  - [如何打包](docs/guides/how-to-package.md)
  - [如何添加本地依赖库](docs/guides/how-to-add-local-dependency.md)
  - [如何添加新类](docs/guides/how-to-add-new-class.md)

## 如何打包

请参考[如何打包](docs/guides/how-to-package.md)指南。

## 如何添加新类

请参考[如何添加新类](docs/guides/how-to-add-new-class.md)指南。

## 许可证

本项目采用MIT许可证。有关详细信息，请参阅[LICENSE](LICENSE)文件。