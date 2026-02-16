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

`btools` 是一个Python包，提供了一系列实用的工具类和函数，用于简化常见的开发任务。它采用模块化设计，按照功能分类组织，便于使用和维护。

### 项目结构

```
btools/
├── core/             # 核心工具类
│   ├── basic/        # 基础工具类
│   │   ├── stringutils.py      # 字符串工具
│   │   ├── collectionutils.py  # 集合工具
│   │   ├── arrayutils.py       # 数组工具
│   │   ├── mathutils.py        # 数学工具
│   │   ├── reflectutils.py     # 反射工具
│   │   ├── exceptionutils.py   # 异常工具
│   │   ├── convertutils.py     # 数据转换工具
│   │   └── validatorutils.py   # 数据验证工具
│   ├── system/       # 系统工具类
│   │   └── systemutils.py      # 系统工具
│   ├── network/      # 网络工具类
│   │   ├── http.py             # HTTP客户端
│   │   ├── ssh.py              # SSH客户端
│   │   ├── netutils.py         # 网络工具
│   │   └── mailutils.py        # 邮件工具
│   ├── data/         # 数据处理工具类
│   │   ├── fileutils.py        # 文件工具
│   │   ├── datetimeutils.py    # 日期时间工具
│   │   ├── crypto.py           # 加密工具
│   │   ├── database.py         # 数据库工具
│   │   ├── csvhandler.py       # CSV文件处理
│   │   ├── excelhandler.py     # Excel文件处理
│   │   ├── encodeutils.py      # 编码工具
│   │   └── regexutils.py       # 正则表达式工具
│   ├── media/        # 媒体工具类
│   │   ├── imageutils.py       # 图像处理
│   │   ├── qrcodeutils.py      # 二维码工具
│   │   └── compressutils.py    # 压缩工具
│   ├── template/     # 模板和国际化
│   │   ├── templateutils.py    # 模板工具
│   │   └── i18nutils.py        # 国际化工具
│   ├── cache/        # 缓存工具类
│   │   └── cache.py            # 缓存工具
│   ├── config/       # 配置工具类
│   │   └── config.py           # 配置管理
│   ├── log/          # 日志工具类
│   │   └── logger.py           # 日志记录
│   ├── automation/   # 自动化测试工具类
│   │   ├── testutils.py        # 测试工具
│   │   ├── seleniumutils.py    # Selenium自动化
│   │   ├── playwrightutils.py  # Playwright自动化
│   │   └── appiumutils.py      # Appium自动化
│   └── ai/           # AI工具类
│       └── ai.py               # AI工具
│   └── api/          # API工具类
│       └── fastapiutils.py     # FastAPI工具
└── __init__.py       # 包初始化文件
```

### 工具类分类

#### 基础工具类 (basic/)
- **StringUtils**: 字符串处理工具，提供字符串操作、格式化等功能
- **CollectionUtils**: 集合处理工具，提供字典、列表等集合操作功能
- **ArrayUtils**: 数组处理工具，提供数组操作、排序等功能
- **MathUtils**: 数学工具，提供数学计算、随机数生成等功能
- **ReflectUtils**: 反射工具，提供类、方法的动态获取和调用功能
- **ExceptionUtils**: 异常工具，提供异常处理、转换等功能
- **Converter**: 数据转换工具，提供各种数据类型的转换功能
- **Validator**: 数据验证工具，提供常见类型和格式的数据验证功能

#### 系统工具类 (system/)
- **SystemUtils**: 系统工具，提供系统信息获取、进程管理等功能

#### 网络工具类 (network/)
- **HTTPClient**: HTTP客户端，基于requests库实现，支持GET、POST等请求
- **SSHClient**: SSH客户端，支持直接连接和通过跳板机连接
- **NetUtils**: 网络工具，提供网络相关操作功能
- **MailUtils**: 邮件工具，提供邮件发送功能

#### 数据处理工具类 (data/)
- **FileUtils**: 文件工具，提供文件读写、目录操作等功能
- **DateTimeUtils**: 日期时间工具，提供日期时间处理、格式化等功能
- **CryptoUtils**: 加密工具，提供加密解密、哈希计算等功能
- **DatabaseUtils**: 数据库工具，提供数据库连接、操作等功能
- **CSVHandler**: CSV文件处理，支持CSV文件的读写
- **ExcelHandler**: Excel文件处理，支持Excel文件的读写和单元格更新
- **EncodeUtils**: 编码工具，提供编码转换、Base64等功能
- **RegexUtils**: 正则表达式工具，提供正则匹配、替换等功能

#### 媒体工具类 (media/)
- **ImageUtils**: 图像处理工具，提供图像处理、转换等功能
- **QrCodeUtils**: 二维码工具，提供二维码生成、解析等功能
- **CompressUtils**: 压缩工具，提供文件压缩、解压等功能

#### 模板和国际化 (template/)
- **TemplateUtils**: 模板工具，提供模板渲染、替换等功能
- **I18nUtils**: 国际化工具，提供多语言支持功能

#### 缓存工具类 (cache/)
- **CacheUtils**: 缓存工具，提供内存缓存、文件缓存等功能

#### 配置工具类 (config/)
- **Config**: 配置管理，支持JSON和YAML文件，提供配置读写、监听等功能

#### 日志工具类 (log/)
- **Logger**: 日志记录工具，提供多级别日志、文件输出等功能

#### 自动化测试工具类 (automation/)
- **TestUtils**: 自动化测试工具，提供测试数据生成、测试报告生成等功能
- **AssertEnhancer**: 断言增强工具，提供更强大的断言方法
- **SeleniumUtils**: 基于Selenium的Web自动化测试工具
- **PlaywrightUtils**: 基于Playwright的Web自动化测试工具
- **AppiumUtils**: 基于Appium的移动应用自动化测试工具

#### AI工具类 (ai/)
- **AIUtils**: AI工具，提供AI模型调用、文本处理等功能

#### API工具类 (api/)
- **FastAPIUtils**: FastAPI工具，提供应用创建、路由器管理、CORS配置、异常处理、响应格式化等功能

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

### 基础用法示例

```python
# 导入btools
from btools import (
    Logger, Config, HTTPClient, SSHClient, 
    FileUtils, DateTimeUtils, Converter, Validator,
    StringUtils, CollectionUtils, MathUtils
)

# 1. 使用Logger - 日志记录
logger = Logger(name="myapp", level=Logger.INFO)
logger.info("Hello, btools!")
logger.error("An error occurred")

# 2. 使用Config - 配置管理
config = Config("config.yaml")
config.set("database.host", "localhost")
host = config.get("database.host")

# 3. 使用HTTPClient - HTTP请求
client = HTTPClient(base_url="https://api.example.com")
response = client.get("/users")
print(response.json())

# 4. 使用SSHClient - SSH连接
ssh = SSHClient()
ssh.connect(hostname="192.168.1.100", username="root", password="your_password")
result = ssh.execute("ls -la")
print(result['stdout'])
ssh.close()

# 5. 使用FileUtils - 文件操作
FileUtils.write_file("test.txt", "Hello, World!")
content = FileUtils.read_file("test.txt")
print(content)

# 6. 使用DateTimeUtils - 日期时间处理
now = DateTimeUtils.now()
formatted_date = DateTimeUtils.format(now, "%Y-%m-%d %H:%M:%S")
print(f"Current time: {formatted_date}")

# 7. 使用Converter - 数据转换
num_str = "123"
num = Converter.to_int(num_str)
print(f"Converted number: {num}")

# 8. 使用Validator - 数据验证
email = "test@example.com"
is_valid = Validator.is_email(email)
print(f"Is valid email: {is_valid}")

# 9. 使用StringUtils - 字符串处理
text = "  Hello World  "
trimmed = StringUtils.trim(text)
print(f"Trimmed text: '{trimmed}'")

# 10. 使用CollectionUtils - 集合处理
data = {"name": "John", "age": 30}
keys = CollectionUtils.get_keys(data)
print(f"Dictionary keys: {keys}")

# 11. 使用MathUtils - 数学计算
random_num = MathUtils.random_int(1, 100)
print(f"Random number: {random_num}")
```

### 高级用法示例

#### 文件处理
```python
from btools import CSVHandler, ExcelHandler

# 使用CSVHandler - CSV文件处理
csv_handler = CSVHandler()
data = [
    ["Name", "Age", "City"],
    ["John", "30", "New York"],
    ["Alice", "25", "London"]
]
csv_handler.write("data.csv", data)

# 读取CSV文件
csv_data = csv_handler.read("data.csv")
print(csv_data)

# 使用ExcelHandler - Excel文件处理
excel_handler = ExcelHandler()
excel_handler.write("data.xlsx", {"Sheet1": data})

# 读取Excel文件
excel_data = excel_handler.read("data.xlsx", "Sheet1")
print(excel_data)
```

#### 自动化测试
```python
from btools import TestUtils, SeleniumUtils

# 使用TestUtils - 测试数据生成
test_data = TestUtils.generate_random_string(10)
print(f"Generated test data: {test_data}")

# 使用SeleniumUtils - Web自动化测试
selenium = SeleniumUtils()
driver = selenium.get_driver()
driver.get("https://www.google.com")
print(f"Page title: {driver.title}")
driver.quit()
```

## 文档

详细的使用文档请参考：

### 使用指南

#### 基础工具类
- [StringUtils使用指南](docs/usage/basic/stringutils.md)
- [CollectionUtils使用指南](docs/usage/basic/collectionutils.md)
- [ArrayUtils使用指南](docs/usage/basic/arrayutils.md)
- [MathUtils使用指南](docs/usage/basic/mathutils.md)
- [ReflectUtils使用指南](docs/usage/basic/reflectutils.md)
- [ExceptionUtils使用指南](docs/usage/basic/exceptionutils.md)
- [Converter使用指南](docs/usage/basic/converter.md)
- [Validator使用指南](docs/usage/basic/validator.md)

#### 系统工具类
- [SystemUtils使用指南](docs/usage/system/systemutils.md)

#### 网络工具类
- [HTTPClient使用指南](docs/usage/network/httpclient.md)
- [SSHClient使用指南](docs/usage/network/sshclient.md)
- [NetUtils使用指南](docs/usage/network/netutils.md)
- [MailUtils使用指南](docs/usage/network/mailutils.md)

#### 数据处理工具类
- [FileUtils使用指南](docs/usage/data/fileutils.md)
- [DateTimeUtils使用指南](docs/usage/data/datetimeutils.md)
- [CryptoUtils使用指南](docs/usage/data/crypto.md)
- [DatabaseUtils使用指南](docs/usage/data/database.md)
- [CSVHandler使用指南](docs/usage/data/csvhandler.md)
- [ExcelHandler使用指南](docs/usage/data/excelhandler.md)
- [EncodeUtils使用指南](docs/usage/data/encodeutils.md)
- [RegexUtils使用指南](docs/usage/data/regexutils.md)

#### 媒体工具类
- [ImageUtils使用指南](docs/usage/media/imageutils.md)
- [QrCodeUtils使用指南](docs/usage/media/qrcodeutils.md)
- [CompressUtils使用指南](docs/usage/media/compressutils.md)

#### 模板和国际化
- [TemplateUtils使用指南](docs/usage/template/templateutils.md)
- [I18nUtils使用指南](docs/usage/template/i18nutils.md)

#### 缓存工具类
- [CacheUtils使用指南](docs/usage/cache/cache.md)

#### 配置工具类
- [Config使用指南](docs/usage/config/config.md)

#### 日志工具类
- [Logger使用指南](docs/usage/log/logger.md)

#### 自动化测试工具类
- [TestUtils使用指南](docs/usage/automation/testutils.md)
- [AssertEnhancer使用指南](docs/usage/automation/assertenhancer.md)
- [SeleniumUtils使用指南](docs/usage/automation/seleniumutils.md)
- [PlaywrightUtils使用指南](docs/usage/automation/playwrightutils.md)
- [AppiumUtils使用指南](docs/usage/automation/appiumutils.md)

#### AI工具类
- [AIUtils使用指南](docs/usage/ai/ai.md)

#### API工具类
- [FastAPIUtils使用指南](docs/usage/api/fastapiutils.md)

### 开发指南
- [如何打包](docs/guides/how-to-package.md)
- [如何添加本地依赖库](docs/guides/how-to-add-local-dependency.md)
- [如何添加新类](docs/guides/how-to-add-new-class.md)

## 如何打包

请参考[如何打包](docs/guides/how-to-package.md)指南。

## 如何添加新类

请参考[如何添加新类](docs/guides/how-to-add-new-class.md)指南。

## 许可证

本项目采用MIT许可证。有关详细信息，请参阅[LICENSE](LICENSE)文件。