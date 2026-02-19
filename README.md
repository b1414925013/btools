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
│   │   ├── validatorutils.py   # 数据验证工具
│   │   ├── beanutils.py        # Bean工具
│   │   ├── resourceutils.py    # 资源工具
│   │   ├── typeutils.py        # 泛型类型工具
│   │   ├── clipboardutils.py   # 剪贴板工具
│   │   ├── classutils.py       # 类工具
│   │   ├── enumutils.py        # 枚举工具
│   │   ├── runtimeutils.py     # 命令行工具
│   │   ├── randomutils.py      # 随机工具
│   │   ├── annotationutils.py  # 注解工具
│   │   ├── htmlutils.py        # HTML工具
│   │   ├── proxyutils.py       # 切面代理工具
│   │   ├── decoratorutils.py   # 装饰器工具
│   │   ├── dictutils.py        # 字典工具
│   │   └── assertutils.py      # 断言工具
│   ├── system/       # 系统工具类
│   │   ├── systemutils.py      # 系统工具
│   │   └── threadutils.py      # 线程工具
│   ├── scheduler/     # 定时任务工具类
│   │   └── scheduleutils.py    # 定时任务工具
│   ├── network/      # 网络工具类
│   │   ├── httputils.py         # HTTP客户端
│   │   ├── sshutils.py          # SSH客户端
│   │   ├── netutils.py         # 网络工具
│   │   └── mailutils.py        # 邮件工具
│   ├── data/         # 数据处理工具类
│   │   ├── fileutils.py        # 文件工具
│   │   ├── datetimeutils.py    # 日期时间工具
│   │   ├── cryptoutils.py      # 加密工具
│   │   ├── databaseutils.py    # 数据库工具
│   │   ├── csvutils.py         # CSV文件处理
│   │   ├── excelutils.py       # Excel文件处理
│   │   ├── encodeutils.py      # 编码工具
│   │   ├── regexutils.py       # 正则表达式工具
│   │   ├── jsonutils.py        # JSON工具
│   │   ├── jsonpathutils.py    # JSONPath工具
│   │   └── xmlutils.py         # XML工具
│   ├── media/        # 媒体工具类
│   │   ├── imageutils.py       # 图像处理
│   │   ├── qrcodeutils.py      # 二维码工具
│   │   ├── compressutils.py    # 压缩工具
│   │   ├── captchautils.py     # 验证码工具
│   │   └── wordutils.py        # Word文档工具
│   ├── template/     # 模板和国际化
│   │   ├── templateutils.py    # 模板工具
│   │   └── i18nutils.py        # 国际化工具
│   ├── cache/        # 缓存工具类
│   │   └── cacheutils.py       # 缓存工具
│   ├── config/       # 配置工具类
│   │   └── configutils.py      # 配置管理
│   ├── log/          # 日志工具类
│   │   └── logutils.py          # 日志记录
│   ├── automation/   # 自动化测试工具类
│   │   ├── testutils.py        # 测试工具
│   │   ├── seleniumutils.py    # Selenium自动化
│   │   ├── playwrightutils.py  # Playwright自动化
│   │   ├── appiumutils.py      # Appium自动化
│   │   └── fakerutils.py       # 测试数据生成工具
│   └── ai/           # AI工具类
│       └── aiutils.py          # AI工具
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
- **BeanUtils**: Bean工具，提供对象属性复制、深拷贝、浅拷贝、对象转字典等功能
- **ResourceUtils**: 资源工具，提供资源加载、读取等功能
- **TypeUtils**: 泛型类型工具，提供类型相关操作功能
- **ClipboardUtils**: 剪贴板工具，提供剪贴板操作功能
- **ClassUtils**: 类工具，提供类相关操作功能
- **EnumUtils**: 枚举工具，提供枚举相关操作功能
- **RuntimeUtils**: 命令行工具，提供命令行执行功能
- **RandomUtils**: 随机工具，提供随机数生成功能
- **AnnotationUtils**: 注解工具，提供注解相关操作功能
- **HtmlUtils**: HTML工具，提供HTML处理功能
- **ProxyUtil**: 切面代理工具，提供代理相关功能
- **DecoratorUtil**: 装饰器工具，提供装饰器创建和管理功能
- **DictUtil**: 字典工具，提供字典相关的便捷操作，类似Hutool的MapUtil
- **AssertUtil**: 断言工具，提供丰富的断言方法，包括字符串、JSON、HTTP响应等断言功能

#### 系统工具类 (system/)
- **SystemUtils**: 系统工具，提供系统信息获取、进程管理等功能
- **ThreadUtils**: 线程工具，提供线程创建、线程池、超时执行、线程本地存储等功能

#### 定时任务工具类 (scheduler/)
- **ScheduleUtils**: 定时任务工具，提供定时任务创建、管理、取消等功能

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
- **JSONUtils**: JSON工具，提供增强的JSON处理、序列化、反序列化、路径操作等功能
- **JSONPathUtils**: JSONPath工具，提供JSONPath解析、查询、更新、删除等功能
- **XmlUtils**: XML工具，提供XML解析、生成、转换、验证等功能，支持XML与字典/JSON的相互转换
- **IOUtils**: IO工具，提供IO流的读写、复制、转换等功能，支持字节流和文本流操作

#### 媒体工具类 (media/)
- **ImageUtils**: 图像处理工具，提供图像处理、转换等功能
- **QrCodeUtils**: 二维码工具，提供二维码生成、解析等功能
- **CompressUtils**: 压缩工具，提供文件压缩、解压等功能
- **CaptchaUtils**: 验证码工具，提供验证码生成、验证等功能
- **WordUtils**: Word文档工具，提供Word文档创建、编辑、格式化等功能

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
- **SeleniumUtils**: 基于Selenium的Web自动化测试工具
- **PlaywrightUtils**: 基于Playwright的Web自动化测试工具
- **AppiumUtils**: 基于Appium的移动应用自动化测试工具
- **FakerUtils**: 测试数据生成工具，提供类似Faker的测试数据生成功能，支持生成姓名、邮箱、手机号、地址、身份证号、银行卡号、IP地址、URL、User-Agent、用户信息、产品信息、订单信息等

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

#### 测试数据生成
```python
from btools import (
    random_name, random_email, random_phone, random_address,
    random_company, random_id_card, random_bank_card,
    random_ip, random_url, random_user, random_product,
    random_order, generate_test_data
)

# 生成随机姓名
name = random_name()
print(f"姓名: {name}")

# 生成随机邮箱
email = random_email()
print(f"邮箱: {email}")

# 生成随机手机号
phone = random_phone()
print(f"手机号: {phone}")

# 生成随机地址
address = random_address()
print(f"地址: {address}")

# 生成随机身份证号
id_card = random_id_card()
print(f"身份证号: {id_card}")

# 生成随机用户信息
user = random_user()
print(f"用户信息: {user}")

# 生成随机产品信息
product = random_product()
print(f"产品信息: {product}")

# 生成随机订单信息
order = random_order()
print(f"订单信息: {order}")

# 根据模板生成测试数据
template = {
    "name": "name",
    "email": "email",
    "phone": "phone",
    "age": "integer",
    "salary": "float",
    "address": "address",
    "company": "company"
}
data = generate_test_data(template)
print(f"模板生成数据: {data}")
```

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
from btools import SeleniumUtils, FakerUtils

# 使用FakerUtils - 测试数据生成
test_data = FakerUtils.random_string(10)
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
- [BeanUtils使用指南](docs/usage/basic/beanutils.md)
- [ResourceUtils使用指南](docs/usage/basic/resourceutils.md)
- [TypeUtils使用指南](docs/usage/basic/typeutils.md)
- [ClipboardUtils使用指南](docs/usage/basic/clipboardutils.md)
- [ClassUtils使用指南](docs/usage/basic/classutils.md)
- [EnumUtils使用指南](docs/usage/basic/enumutils.md)
- [RuntimeUtils使用指南](docs/usage/basic/runtimeutils.md)
- [RandomUtils使用指南](docs/usage/basic/randomutils.md)
- [AnnotationUtils使用指南](docs/usage/basic/annotationutils.md)
- [HtmlUtils使用指南](docs/usage/basic/htmlutils.md)
- [ProxyUtil使用指南](docs/usage/basic/proxyutils.md)
- [DecoratorUtil使用指南](docs/usage/basic/decoratorutils.md)
- [DictUtil使用指南](docs/usage/basic/dictutils.md)
- [AssertUtil使用指南](docs/usage/basic/assertutils.md)

#### 系统工具类
- [SystemUtils使用指南](docs/usage/system/systemutils.md)
- [ThreadUtils使用指南](docs/usage/system/threadutils.md)

#### 定时任务工具类
- [ScheduleUtils使用指南](docs/usage/scheduler/scheduleutils.md)

#### 网络工具类
- [HTTPClient使用指南](docs/usage/network/httpclientutils.md)
- [SSHClient使用指南](docs/usage/network/sshclientutils.md)
- [NetUtils使用指南](docs/usage/network/netutils.md)
- [MailUtils使用指南](docs/usage/network/mailutils.md)

#### 数据处理工具类
- [FileUtils使用指南](docs/usage/data/fileutils.md)
- [DateTimeUtils使用指南](docs/usage/data/datetimeutils.md)
- [CryptoUtils使用指南](docs/usage/data/cryptoutils.md)
- [DatabaseUtils使用指南](docs/usage/data/databaseutils.md)
- [CSVHandler使用指南](docs/usage/data/csvutils.md)
- [ExcelHandler使用指南](docs/usage/data/excelutils.md)
- [EncodeUtils使用指南](docs/usage/data/encodeutils.md)
- [RegexUtils使用指南](docs/usage/data/regexutils.md)
- [JSONUtils使用指南](docs/usage/data/jsonutils.md)
- [JSONPathUtils使用指南](docs/usage/data/jsonpathutils.md)
- [XmlUtils使用指南](docs/usage/data/xmlutils.md)

#### 媒体工具类
- [ImageUtils使用指南](docs/usage/media/imageutils.md)
- [QrCodeUtils使用指南](docs/usage/media/qrcodeutils.md)
- [CompressUtils使用指南](docs/usage/media/compressutils.md)
- [CaptchaUtils使用指南](docs/usage/media/captchautils.md)
- [WordUtils使用指南](docs/usage/media/wordutils.md)

#### 模板和国际化
- [TemplateUtils使用指南](docs/usage/template/templateutils.md)
- [I18nUtils使用指南](docs/usage/template/i18nutils.md)

#### 缓存工具类
- [CacheUtils使用指南](docs/usage/cache/cacheutils.md)

#### 配置工具类
- [Config使用指南](docs/usage/config/configutils.md)

#### 日志工具类
- [Logger使用指南](docs/usage/log/logutils.md)

#### 自动化测试工具类

- [SeleniumUtils使用指南](docs/usage/automation/seleniumutils.md)
- [PlaywrightUtils使用指南](docs/usage/automation/playwrightutils.md)
- [AppiumUtils使用指南](docs/usage/automation/appiumutils.md)
- [FakerUtils使用指南](docs/usage/automation/fakerutils.md)

#### AI工具类
- [AIUtils使用指南](docs/usage/ai/aiutils.md)

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