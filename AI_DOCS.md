# BTools 项目文档

## 项目概览

BTools 是一个全面的 Python 工具库，提供了丰富的工具类和函数，涵盖了从基础工具到高级功能的各个方面。该库设计的目标是为开发者提供一套统一、便捷、高效的工具集合，减少重复代码编写，提高开发效率。

## 目录结构

BTools 项目采用模块化设计，按照功能领域将工具类组织到不同的目录中。整体结构如下：

```
BTools/
├── btools/                  # 主源码目录
│   ├── core/                # 核心功能模块
│   │   ├── ai/              # AI 相关工具
│   │   ├── api/             # API 工具
│   │   ├── automation/      # 自动化工具
│   │   ├── basic/           # 基础工具
│   │   ├── cache/           # 缓存工具
│   │   ├── config/          # 配置工具
│   │   ├── container/       # 容器工具
│   │   ├── data/            # 数据处理工具
│   │   ├── log/             # 日志工具
│   │   ├── media/           # 媒体处理工具
│   │   ├── network/         # 网络工具
│   │   ├── project/         # 项目管理工具
│   │   ├── release/         # 发布工具
│   │   ├── scheduler/       # 调度工具
│   │   ├── system/          # 系统工具
│   │   ├── template/        # 模板工具
│   │   └── test/            # 测试工具
│   └── __init__.py          # 包初始化文件
├── docs/                    # 文档目录
│   ├── guides/              # 指南文档
│   └── usage/               # 使用文档
├── test/                    # 测试目录
├── .gitignore               # Git 忽略文件
├── README.md                # 项目说明文件
├── requirements.txt         # 依赖文件
└── setup.py                 # 安装配置文件
```

## 核心功能模块

### 1. 基础工具 (basic)

基础工具模块提供了一系列常用的基础功能，包括：

- **arrayutils.py**: 数组操作工具，提供数组的各种操作方法
- **dictutils.py**: 字典操作工具，提供字典的各种操作方法
- **stringutils.py**: 字符串操作工具，提供字符串的各种处理方法
- **typeutils.py**: 类型操作工具，提供类型检查和转换方法
- **classutils.py**: 类操作工具，提供类的各种操作方法
- **annotationutils.py**: 注解操作工具，提供注解的解析和处理方法
- **htmlutils.py**: HTML 操作工具，提供 HTML 转义和处理方法
- **runtimeutils.py**: 运行时操作工具，提供运行时的各种操作方法
- **decoratorutils.py**: 装饰器工具，提供各种实用的装饰器

### 2. 自动化工具 (automation)

自动化工具模块提供了自动化测试和操作的功能：

- **fakerutils.py**: 测试数据生成工具，用于生成各种类型的测试数据
- **seleniumutils.py**: Selenium 自动化测试工具，用于 Web 自动化测试
- **appiumutils.py**: Appium 自动化测试工具，用于移动应用自动化测试
- **playwrightutils.py**: Playwright 自动化测试工具，用于现代 Web 应用自动化测试

### 3. 网络工具 (network)

网络工具模块提供了网络相关的功能：

- **httputils.py**: HTTP 工具，提供 HTTP 请求和响应处理
- **emailutils.py**: 邮件工具，提供邮件发送和接收功能
- **netutils.py**: 网络工具，提供网络相关的操作方法
- **sshutils.py**: SSH 工具，提供 SSH 连接和操作功能

### 4. 数据工具 (data)

数据工具模块提供了数据处理和存储的功能：

- **fileutils.py**: 文件操作工具，提供文件的各种操作方法
- **jsonutils.py**: JSON 操作工具，提供 JSON 数据的处理方法
- **xmlutils.py**: XML 操作工具，提供 XML 数据的处理方法
- **csvutils.py**: CSV 操作工具，提供 CSV 数据的处理方法
- **excelutils.py**: Excel 操作工具，提供 Excel 文件的处理方法
- **datetimeutils.py**: 日期时间工具，提供日期时间的处理方法
- **cryptoutils.py**: 加密工具，提供数据加密和解密功能

### 5. 系统工具 (system)

系统工具模块提供了系统相关的功能：

- **processutils.py**: 进程操作工具，提供进程的管理和监控功能
- **pathutils.py**: 路径操作工具，提供路径的处理方法
- **platformutils.py**: 平台工具，提供平台相关的信息和操作
- **systemutils.py**: 系统工具，提供系统相关的操作方法
- **threadutils.py**: 线程操作工具，提供线程的管理和操作功能

### 6. 测试工具 (test)

测试工具模块提供了测试相关的功能：

- **loadtestutils.py**: 负载测试工具，用于模拟并发请求和测试系统性能
- **performancetestutils.py**: 性能测试工具，用于测试代码性能
- **contracttestutils.py**: 契约测试工具，用于测试服务之间的契约
- **mockutils.py**: 模拟工具，用于模拟对象和行为

### 7. 其他模块

- **ai/**: AI 相关工具，提供 AI 模型的使用和管理功能
- **api/**: API 工具，提供 API 开发和测试功能
- **cache/**: 缓存工具，提供缓存的管理和操作功能
- **config/**: 配置工具，提供配置的管理和读取功能
- **container/**: 容器工具，提供 Docker 和 Kubernetes 的操作功能
- **log/**: 日志工具，提供日志的记录和管理功能
- **media/**: 媒体处理工具，提供图片、二维码等媒体的处理功能
- **project/**: 项目管理工具，提供项目的管理和操作功能
- **release/**: 发布工具，提供项目的发布和分发功能
- **scheduler/**: 调度工具，提供任务的调度和执行功能
- **template/**: 模板工具，提供模板的处理和渲染功能

## 安装和使用

### 安装

```bash
# 从源码安装
pip install -e .

# 或从 PyPI 安装（如果已发布）
pip install btools
```

### 基本使用

```python
# 导入所有工具
from btools import *

# 或导入特定模块
from btools.core.basic import StringUtils, ArrayUtils, DictUtil
from btools.core.automation import FakerUtils
from btools.core.network import HTTPClient
from btools.core.data import FileUtils
from btools.core.system import ProcessUtils
```

## 模块使用示例

### 基础工具示例

#### StringUtils

```python
# 字符串空值判断
StringUtils.is_empty("")  # True
StringUtils.is_not_empty("hello")  # True

# 字符串修剪
StringUtils.trim("  hello  ")  # "hello"

# 字符串分割
StringUtils.split("a,b,c", ",")  # ["a", "b", "c"]

# 字符串连接
StringUtils.join(["a", "b", "c"], ",")  # "a,b,c"

# 字符串替换
StringUtils.replace("hello world", "world", "BTools")  # "hello BTools"
```

#### ArrayUtils

```python
# 数组空值判断
ArrayUtils.is_empty([])  # True
ArrayUtils.is_not_empty([1, 2, 3])  # True

# 数组大小
ArrayUtils.size([1, 2, 3])  # 3

# 添加元素
ArrayUtils.add([1, 2, 3], 4)  # [1, 2, 3, 4]

# 添加多个元素
ArrayUtils.add_all([1, 2, 3], [4, 5, 6])  # [1, 2, 3, 4, 5, 6]

# 获取元素
ArrayUtils.get([1, 2, 3], 0)  # 1
```

#### DictUtil

```python
# 字典空值判断
DictUtil.is_empty({})  # True
DictUtil.is_not_empty({"a": 1})  # True

# 获取值
DictUtil.get({"a": 1, "b": 2}, "a")  # 1
DictUtil.get({"a": 1, "b": 2}, "c", "default")  # "default"

# 合并字典
DictUtil.merge({"a": 1}, {"b": 2})  # {"a": 1, "b": 2}

# 反转字典
DictUtil.reverse({"a": 1, "b": 2})  # {1: "a", 2: "b"}
```

### 自动化工具示例

#### FakerUtils

```python
# 生成随机姓名
FakerUtils.name()  # "John Doe"

# 生成随机邮箱
FakerUtils.email()  # "john.doe@example.com"

# 生成随机电话号码
FakerUtils.phone_number()  # "13812345678"

# 生成随机地址
FakerUtils.address()  # "北京市朝阳区某某街道123号"

# 生成随机日期
FakerUtils.date()  # "2023-01-01"

# 生成随机数字
FakerUtils.random_number(digits=6)  # 123456

# 生成随机字符串
FakerUtils.random_string(length=10)  # "abcdefghij"

# 生成随机布尔值
FakerUtils.boolean()  # True

# 生成随机UUID
FakerUtils.uuid()  # "550e8400-e29b-41d4-a716-446655440000"

# 生成随机IP地址
FakerUtils.ip_address()  # "192.168.1.1"

# 生成随机URL
FakerUtils.url()  # "https://www.example.com"

# 生成随机公司名称
FakerUtils.company()  # "某某科技有限公司"

# 生成随机职位
FakerUtils.job()  # "软件工程师"

# 生成随机银行卡号
FakerUtils.credit_card_number()  # "4111111111111111"

# 生成随机身份证号
FakerUtils.id_card()  # "110101199001011234"
```

### 网络工具示例

#### HTTPClient

```python
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
    json={"name": "John Doe", "email": "john@example.com"}
)
print(response.status_code)
print(response.json())

# 发送PUT请求
response = client.put(
    "/users/1",
    json={"name": "John Smith"}
)
print(response.status_code)

# 发送DELETE请求
response = client.delete("/users/1")
print(response.status_code)

# 关闭会话
client.close()
```

### 数据工具示例

#### FileUtils

```python
# 写入文件
FileUtils.write_file("test.txt", "Hello, World!")

# 读取文件
content = FileUtils.read_file("test.txt")
print(content)  # "Hello, World!"

# 追加内容到文件
FileUtils.append_file("test.txt", "\nAppend this line")

# 读取文件的所有行
lines = FileUtils.read_lines("test.txt")
print(lines)  # ["Hello, World!", "Append this line"]

# 检查文件是否存在
FileUtils.exists("test.txt")  # True

# 复制文件
FileUtils.copy("test.txt", "test_copy.txt")

# 移动文件
FileUtils.move("test_copy.txt", "copy/test_copy.txt")

# 删除文件
FileUtils.delete("test.txt")

# 创建目录
FileUtils.create_directory("new_dir")

# 列出目录中的文件和子目录
items = FileUtils.list_directory(".")
print(items)

# 递归遍历目录
for root, dirs, files in FileUtils.walk("."):
    print(f"Root: {root}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")
```

### 系统工具示例

#### ProcessUtils

```python
# 启动进程
process = ProcessUtils.start_process(
    command=["python", "script.py"],
    cwd="/working/dir",
    env={"VAR": "value"}
)

# 获取进程 ID
pid = process.pid
print(f"进程 ID: {pid}")

# 运行并等待进程完成
result = ProcessUtils.run_process(
    command=["python", "script.py"],
    capture_output=True,
    timeout=30
)

print(f"返回码: {result.returncode}")
print(f"标准输出: {result.stdout}")
print(f"标准错误: {result.stderr}")

# 检查进程是否正在运行
is_running = ProcessUtils.is_process_running(pid)
print(f"进程是否运行: {is_running}")

# 终止进程
success = ProcessUtils.terminate_process(pid)
print(f"终止进程成功: {success}")

# 强制终止进程
success = ProcessUtils.kill_process(pid)
print(f"强制终止进程成功: {success}")
```

### 测试工具示例

#### LoadTestUtils

```python
# 定义测试函数
def test_request():
    import requests
    response = requests.get("https://example.com")
    return response.status_code == 200

# 运行负载测试
results = LoadTestUtils.run_load_test(
    func=test_request,
    concurrent_users=10,  # 并发用户数
    duration=30,  # 持续时间（秒）
    ramp_up=5  # 预热时间（秒）
)

print(f"总请求数: {results['total_requests']}")
print(f"成功率: {results['success_rate']}%")
print(f"平均响应时间: {results['average_response_time']}s")

# 定义性能阈值
thresholds = {
    "max_response_time": 2.0,  # 最大响应时间 2秒
    "min_success_rate": 95.0,   # 最小成功率 95%
    "max_error_rate": 5.0        # 最大错误率 5%
}

# 检查阈值
check_result = LoadTestUtils.check_thresholds(results, thresholds)
print(f"是否通过: {check_result['passed']}")
print(f"成功率: {check_result['success_rate']:.2f}%")
print(f"平均响应时间: {check_result['avg_response_time']:.2f}s")
print(f"问题: {check_result['issues']}")
```

## 项目特点

1. **模块化设计**: 按照功能领域组织代码，便于维护和扩展
2. **全面的工具集**: 涵盖了从基础工具到高级功能的各个方面
3. **跨平台兼容**: 支持 Windows、Linux、macOS 等多种操作系统
4. **易于使用**: 提供了简洁明了的 API，便于开发者使用
5. **丰富的文档**: 每个模块都有详细的文档和使用示例
6. **高质量的代码**: 遵循 Python 最佳实践，代码质量高
7. **完善的测试**: 每个模块都有对应的测试用例，确保功能的正确性

## 如何贡献

1. Fork 项目仓库
2. 创建特性分支
3. 提交更改
4. 推送分支
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。

## 联系方式

- 项目地址: https://github.com/b1414925013/btools
- 问题反馈: https://github.com/b1414925013/btools/issues

## 总结

BTools 是一个功能全面、设计合理的 Python 工具库，为开发者提供了丰富的工具类和函数，涵盖了从基础工具到高级功能的各个方面。通过使用 BTools，开发者可以减少重复代码编写，提高开发效率，专注于业务逻辑的实现。

该库的模块化设计使得它易于维护和扩展，而丰富的文档和示例则使得它易于使用。无论是在小型项目还是大型项目中，BTools 都能为开发者提供有力的支持。