# btools

一个用于Python项目的实用工具类和函数集合。

## 目录

- [概述](#概述)
- [安装](#安装)
- [使用方法](#使用方法)
  - [Logger](#logger)
  - [Config](#config)
  - [HTTPClient](#httpclient)
  - [SSHClient](#sshclient)
  - [CSVHandler](#csvhandler)
  - [ExcelHandler](#excelhandler)
  - [TestUtils](#testutils)
  - [AssertEnhancer](#assertenhancer)
  - [SeleniumUtils](#seleniumutils)
  - [PlaywrightUtils](#playwrightutils)
  - [AppiumUtils](#appiumutils)
  - [Validator](#validator)
  - [Converter](#converter)
- [如何打包](#如何打包)
- [如何添加本地依赖库](#如何添加本地依赖库)
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

### 从PyPI安装（发布后）

```bash
pip install btools
```

### 从wheel文件安装

1. 首先，按照[如何打包](#如何打包)部分的说明打包项目
2. 然后安装生成的wheel文件：

```bash
pip install btools-1.0.0-py3-none-any.whl
```

## 使用方法

### Logger

`Logger` 类提供了一个简单的接口，用于记录不同严重级别的日志消息。

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

### Config

`Config` 类提供了从JSON或YAML文件加载、保存和操作配置数据的方法。

#### 使用JSON文件

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

#### 使用YAML文件

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

生成的YAML文件内容示例：

```yaml
database:
  host: localhost
  port: 5432
  credentials:
    username: admin
```

### HTTPClient

`HTTPClient` 类是基于requests库实现的HTTP客户端，提供了发送GET、POST、PUT、PATCH、DELETE等HTTP请求的方法，支持Header管理、RESTful URL参数、文件上传下载等功能。

```python
from btools import HTTPClient

# 创建HTTP客户端实例
client = HTTPClient(
    base_url="https://api.example.com",
    headers={"Content-Type": "application/json"},
    timeout=30
)

# ==================== 使用缓存 ====================
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

# ==================== 使用重试机制 ====================
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

# ==================== 同时使用缓存和重试 ====================
# 创建同时使用缓存和重试的HTTP客户端
full_client = HTTPClient(
    base_url="https://api.example.com",
    use_cache=True,
    cache_name="api_cache",
    retry_enabled=True,
    retry_total=3
)

# ==================== Header管理 ====================
# 添加Header（保留原有Header）
client.add_headers({"Authorization": "Bearer token123", "X-Custom-Header": "value"})

# 设置Header（替换所有Header）
client.set_headers({"Content-Type": "application/xml"})

# 清空所有Header
client.clear_headers()

# 链式调用
client.add_headers({"Content-Type": "application/json"}) \
      .add_headers({"Authorization": "Bearer token123"})

# ==================== 发送HTTP请求 ====================
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

# ==================== RESTful URL路径参数 ====================
# 替换URL路径中的参数，如 /users/{user_id}
response = client.get("/users/{user_id}", params={"user_id": 123, "include": "profile"})
# 实际请求URL: https://api.example.com/users/123?include=profile

response = client.put("/users/{user_id}/posts/{post_id}", 
                     params={"user_id": 123, "post_id": 456},
                     json={"title": "New Title"})
# 实际请求URL: https://api.example.com/users/123/posts/456

# ==================== 文件上传 ====================
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

# ==================== 文件下载 ====================
# 下载文件
save_path = client.download_file(
    url="/files/document.pdf",
    save_path="downloads/document.pdf",
    params={"version": "latest"},
    chunk_size=8192  # 下载块大小
)
print(f"文件已保存到: {save_path}")

# ==================== 使用上下文管理器 ====================
with HTTPClient(base_url="https://api.example.com") as client:
    response = client.get("/users")
    print(response.json())
# 上下文管理器会自动关闭会话

# ==================== 使用绝对URL ====================
response = client.get("https://google.com")
print(response.status_code)

# 关闭会话
client.close()
```

### SSHClient

`SSHClient` 类是基于paramiko库实现的SSH客户端，支持直接连接和通过跳板机连接到目标Linux服务器。

#### 直接连接

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

#### 通过跳板机连接

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

#### 使用代理连接

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

#### 交互式Shell

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

#### 使用上下文管理器

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

### Validator

`Validator` 类提供了验证各种类型数据的静态方法。

```python
from btools import Validator

# 验证邮箱
print(Validator.is_email("user@example.com"))  # True
print(Validator.is_email("invalid-email"))      # False

# 验证手机号（中国大陆）
print(Validator.is_phone("13812345678"))  # True
print(Validator.is_phone("1234567890"))   # False

# 验证URL
print(Validator.is_url("https://example.com"))  # True
print(Validator.is_url("invalid-url"))          # False

# 验证IPv4地址
print(Validator.is_ipv4("192.168.1.1"))   # True
print(Validator.is_ipv4("999.999.999.999"))  # False

# 验证日期
print(Validator.is_date("2023-12-25"))  # True
print(Validator.is_date("2023/12/25"))  # False（默认格式为YYYY-MM-DD）
print(Validator.is_date("2023/12/25", "%Y/%m/%d"))  # True

# 验证数字
print(Validator.is_number("123"))      # True
print(Validator.is_integer("123.45"))  # False
print(Validator.is_positive("-10"))     # False

# 验证空值
print(Validator.is_empty(None))        # True
print(Validator.is_empty(""))          # True
print(Validator.is_empty("   "))        # True
print(Validator.is_empty([]))           # True
print(Validator.is_empty({}))           # True
print(Validator.is_empty("hello"))      # False

# 验证字符串长度
print(Validator.is_length_between("hello", 3, 10))  # True
print(Validator.is_length_between("hi", 3, 10))      # False
```

### Converter

`Converter` 类提供了在不同数据类型之间转换的静态方法。

```python
from btools import Converter
from datetime import datetime

# 转换为基本类型
print(Converter.to_int("123"))       # 123
print(Converter.to_float("123.45"))  # 123.45
print(Converter.to_bool("true"))      # True
print(Converter.to_bool("0"))         # False
print(Converter.to_str(123))          # "123"

# 转换为集合
print(Converter.to_list("hello"))     # ["hello"]
print(Converter.to_list((1, 2, 3)))   # [1, 2, 3]
print(Converter.to_dict({"a": 1}))    # {"a": 1}

# 转换为datetime
print(Converter.to_datetime("2023-12-25"))  # datetime对象
print(Converter.to_datetime("2023/12/25", "%Y/%m/%d"))  # datetime对象

# 从datetime转换
now = datetime.now()
print(Converter.datetime_to_str(now))  # "2023-12-25 14:30:00"
print(Converter.datetime_to_str(now, "%Y-%m-%d"))  # "2023-12-25"

# 转换命名规范
print(Converter.camel_to_snake("camelCase"))  # "camel_case"
print(Converter.snake_to_camel("snake_case"))  # "snakeCase"
print(Converter.snake_to_camel("snake_case", capitalize_first=True))  # "SnakeCase"
```

### TestUtils

`TestUtils` 类提供了自动化测试中常用的工具方法，包括测试数据生成、测试报告生成等功能。

```python
from btools import TestUtils

# ==================== 生成测试数据 ====================
# 生成随机字符串
random_str = TestUtils.generate_random_string()
print(f"随机字符串: {random_str}")

# 生成随机邮箱
random_email = TestUtils.generate_random_email()
print(f"随机邮箱: {random_email}")

# 生成随机手机号
random_phone = TestUtils.generate_random_phone()
print(f"随机手机号: {random_phone}")

# 生成随机日期
random_date = TestUtils.generate_random_date()
print(f"随机日期: {random_date}")

# 根据模板生成测试数据
test_data_template = {
    "username": "${random_string}",
    "email": "${random_email}",
    "phone": "${random_phone}",
    "register_date": "${random_date}",
    "profile": {
        "first_name": "${random_string:5}",
        "last_name": "${random_string:5}"
    }
}

generated_data = TestUtils.generate_test_data(test_data_template)
print(f"生成的测试数据: {generated_data}")

# ==================== 配置文件操作 ====================
# 加载测试配置
config = TestUtils.load_test_config("test_config.yaml")
print(f"加载的配置: {config}")

# ==================== 测试结果操作 ====================
# 保存测试结果
test_results = {
    "test_name": "登录测试",
    "status": "PASS",
    "duration": 2.5,
    "timestamp": "2023-12-25 10:00:00"
}

# 保存为JSON
TestUtils.save_test_results(test_results, "test_results.json")
print("测试结果已保存为JSON")

# 保存为YAML
TestUtils.save_test_results(test_results, "test_results.yaml", format="yaml")
print("测试结果已保存为YAML")

# ==================== 生成测试报告 ====================
# 准备测试用例数据
test_cases = [
    {
        "name": "登录成功测试",
        "description": "测试正常登录流程",
        "status": "PASS",
        "start_time": "2023-12-25 10:00:00",
        "end_time": "2023-12-25 10:00:02",
        "duration": 2.1
    },
    {
        "name": "登录失败测试",
        "description": "测试密码错误时的登录失败场景",
        "status": "PASS",
        "start_time": "2023-12-25 10:00:03",
        "end_time": "2023-12-25 10:00:05",
        "duration": 1.8
    },
    {
        "name": "注册测试",
        "description": "测试用户注册功能",
        "status": "FAIL",
        "start_time": "2023-12-25 10:00:06",
        "end_time": "2023-12-25 10:00:09",
        "duration": 3.2,
        "error": "邮箱格式不正确"
    }
]

# 生成HTML测试报告
report_path = TestUtils.generate_test_report(test_cases, "test_report.html")
print(f"测试报告已生成: {report_path}")

# ==================== 等待元素装饰器 ====================
# 使用等待元素装饰器
@TestUtils.wait_for_element(timeout=10)
def find_element_by_id(driver, element_id):
    return driver.find_element("id", element_id)

# 调用带等待的函数
try:
    element = find_element_by_id(driver, "login-button")
    print("找到登录按钮")
except TimeoutError as e:
    print(f"找不到元素: {e}")
```

### AssertEnhancer

`AssertEnhancer` 类提供了增强的断言方法，适用于API测试和UI测试中的各种断言场景。

```python
from btools import AssertEnhancer

# ==================== 字符串断言 ====================
# 断言字符串包含
AssertEnhancer.assert_contains("Hello World", "World")
print("字符串包含断言通过")

# ==================== JSON断言 ====================
# 断言JSON相等
expected_json = {"name": "John", "age": 30}
actual_json = {"name": "John", "age": 30}
AssertEnhancer.assert_json_equals(actual_json, expected_json)
print("JSON相等断言通过")

# ==================== HTTP响应断言 ====================
# 断言响应状态码
import requests
response = requests.get("https://api.example.com/users")
AssertEnhancer.assert_response_status(response, 200)
print("响应状态码断言通过")

# 断言响应JSON
expected_response_json = {"status": "success", "data": []}
AssertEnhancer.assert_response_json(response, expected_response_json)
print("响应JSON断言通过")
```

### SeleniumUtils

`SeleniumUtils` 类提供了基于Selenium的Web自动化测试操作，支持各种浏览器和常用的Web元素操作。

```python
from btools import SeleniumUtils

# ==================== 初始化浏览器 ====================
# 获取Chrome浏览器实例
driver = SeleniumUtils.get_driver(
    browser="chrome",
    headless=False,
    implicit_wait=10
)

# 打开网页
driver.get("https://www.example.com")

# ==================== 元素操作 ====================
# 查找元素
username_input = SeleniumUtils.find_element(driver, "id", "username")

# 点击元素
SeleniumUtils.click_element(driver, "id", "login-button")

# 输入文本
SeleniumUtils.send_keys(driver, "id", "username", "testuser")
SeleniumUtils.send_keys(driver, "id", "password", "password123")

# 获取元素文本
title = SeleniumUtils.get_element_text(driver, "css_selector", "h1")
print(f"页面标题: {title}")

# 获取元素属性
value = SeleniumUtils.get_element_attribute(driver, "id", "username", "value")
print(f"输入框值: {value}")

# ==================== 元素检查 ====================
# 检查元素是否存在
if SeleniumUtils.is_element_present(driver, "id", "submit-button"):
    print("提交按钮存在")

# 检查元素是否可见
if SeleniumUtils.is_element_visible(driver, "id", "success-message"):
    print("成功消息可见")

# ==================== 滚动操作 ====================
# 滚动到元素位置
SeleniumUtils.scroll_to_element(driver, "id", "footer")

# 滚动到页面顶部
SeleniumUtils.scroll_to_top(driver)

# 滚动到页面底部
SeleniumUtils.scroll_to_bottom(driver)

# ==================== 窗口操作 ====================
# 切换到新窗口
SeleniumUtils.switch_to_window(driver, 1)

# 关闭其他窗口
SeleniumUtils.close_other_windows(driver)

# ==================== iframe操作 ====================
# 切换到iframe
SeleniumUtils.switch_to_frame(driver, "id", "content-frame")

# 切换回默认内容
SeleniumUtils.switch_to_default_content(driver)

# ==================== 截图 ====================
# 截取屏幕
 screenshot_path = SeleniumUtils.take_screenshot(driver, filename="test_screenshot.png")
print(f"截图保存到: {screenshot_path}")

# ==================== 其他操作 ====================
# 等待页面加载完成
SeleniumUtils.wait_for_page_load(driver)

# 执行JavaScript
result = SeleniumUtils.execute_javascript(driver, "return document.title;")
print(f"页面标题: {result}")

# 刷新页面
SeleniumUtils.refresh_page(driver)

# 浏览器后退
SeleniumUtils.navigate_back(driver)

# 浏览器前进
SeleniumUtils.navigate_forward(driver)

# ==================== 关闭浏览器 ====================
SeleniumUtils.close_driver(driver)

# ==================== 使用SeleniumElement ====================
from btools import SeleniumElement

# 创建元素实例
login_button = SeleniumElement(driver, "id", "login-button")

# 点击元素
login_button.click()

# 检查元素是否可见
if login_button.is_visible():
    print("登录按钮可见")
```

### PlaywrightUtils

`PlaywrightUtils` 类提供了基于Playwright的Web自动化测试操作，支持现代浏览器和更高级的自动化功能。

```python
from btools import PlaywrightUtils

# ==================== 初始化浏览器 ====================
# 获取浏览器实例
playwright, browser, context, page = PlaywrightUtils.get_browser(
    browser="chromium",
    headless=False,
    slow_mo=100
)

# 打开网页
page.goto("https://www.example.com")

# ==================== 元素操作 ====================
# 点击元素
PlaywrightUtils.click_element(page, "#login-button")

# 输入文本
PlaywrightUtils.send_keys(page, "#username", "testuser")
PlaywrightUtils.send_keys(page, "#password", "password123")

# 获取元素文本
title = PlaywrightUtils.get_element_text(page, "h1")
print(f"页面标题: {title}")

# 获取元素属性
value = PlaywrightUtils.get_element_attribute(page, "#username", "value")
print(f"输入框值: {value}")

# ==================== 元素检查 ====================
# 检查元素是否可见
if PlaywrightUtils.is_element_visible(page, ".success-message"):
    print("成功消息可见")

# 检查元素是否隐藏
if PlaywrightUtils.is_element_hidden(page, ".loading-spinner"):
    print("加载 spinner 已隐藏")

# ==================== 滚动操作 ====================
# 滚动到元素位置
PlaywrightUtils.scroll_to_element(page, "#footer")

# 滚动到页面顶部
PlaywrightUtils.scroll_to_top(page)

# 滚动到页面底部
PlaywrightUtils.scroll_to_bottom(page)

# ==================== 窗口操作 ====================
# 切换到新窗口
new_page = PlaywrightUtils.switch_to_window(page, 1)

# 关闭其他窗口
PlaywrightUtils.close_other_windows(page)

# ==================== iframe操作 ====================
# 切换到iframe
frame = PlaywrightUtils.switch_to_frame(page, "#content-frame")

# ==================== 截图 ====================
# 截取屏幕
 screenshot_path = PlaywrightUtils.take_screenshot(page, filename="test_screenshot.png", full_page=True)
print(f"截图保存到: {screenshot_path}")

# ==================== 其他操作 ====================
# 等待页面加载状态
PlaywrightUtils.wait_for_load_state(page, state="networkidle")

# 执行JavaScript
result = PlaywrightUtils.execute_javascript(page, "return document.title;")
print(f"页面标题: {result}")

# 刷新页面
PlaywrightUtils.refresh_page(page)

# 浏览器后退
PlaywrightUtils.navigate_back(page)

# 浏览器前进
PlaywrightUtils.navigate_forward(page)

# 填充表单
 form_data = {
    "#name": "John Doe",
    "#email": "john@example.com",
    "#message": "Hello, World!"
}
PlaywrightUtils.fill_form(page, form_data)

# ==================== 关闭浏览器 ====================
PlaywrightUtils.close_browser(playwright, browser, context)

# ==================== 使用PlaywrightElement ====================
from btools import PlaywrightElement

# 创建元素实例
login_button = PlaywrightElement(page, "#login-button")

# 点击元素
login_button.click()

# 检查元素是否可见
if login_button.is_visible():
    print("登录按钮可见")
```

### AppiumUtils

`AppiumUtils` 类提供了基于Appium的移动应用自动化测试操作，支持Android和iOS平台。

```python
from btools import AppiumUtils

# ==================== 初始化driver ====================
# 获取Android driver实例
driver = AppiumUtils.get_driver(
    platform_name="Android",
    platform_version="13",
    device_name="Android Emulator",
    app_package="com.example.app",
    app_activity=".MainActivity",
    automation_name="UiAutomator2",
    no_reset=True
)

# ==================== 元素操作 ====================
# 点击元素
AppiumUtils.click_element(driver, "id", "com.example.app:id/login_button")

# 输入文本
AppiumUtils.send_keys(driver, "id", "com.example.app:id/username_input", "testuser")
AppiumUtils.send_keys(driver, "id", "com.example.app:id/password_input", "password123")

# 获取元素文本
title = AppiumUtils.get_element_text(driver, "id", "com.example.app:id/title_text")
print(f"标题: {title}")

# 获取元素属性
value = AppiumUtils.get_element_attribute(driver, "id", "com.example.app:id/username_input", "text")
print(f"输入框值: {value}")

# ==================== 元素检查 ====================
# 检查元素是否存在
if AppiumUtils.is_element_present(driver, "id", "com.example.app:id/submit_button"):
    print("提交按钮存在")

# 检查元素是否可见
if AppiumUtils.is_element_visible(driver, "id", "com.example.app:id/success_message"):
    print("成功消息可见")

# ==================== 滚动操作 ====================
# 滚动到元素位置
AppiumUtils.scroll_to_element(driver, "id", "com.example.app:id/footer")

# 向上滑动
AppiumUtils.swipe_up(driver, duration=1000)

# 向下滑动
AppiumUtils.swipe_down(driver, duration=1000)

# 向左滑动
AppiumUtils.swipe_left(driver, duration=1000)

# 向右滑动
AppiumUtils.swipe_right(driver, duration=1000)

# ==================== 触摸操作 ====================
# 点击指定坐标
AppiumUtils.tap(driver, 500, 1000)

# 长按元素
AppiumUtils.long_press(driver, "id", "com.example.app:id/item")

# ==================== 应用操作 ====================
# 获取设备尺寸
size = AppiumUtils.get_device_size(driver)
print(f"设备尺寸: {size}")

# 获取当前Activity（Android）
activity = AppiumUtils.get_current_activity(driver)
print(f"当前Activity: {activity}")

# 获取当前包名（Android）
package = AppiumUtils.get_current_package(driver)
print(f"当前包名: {package}")

# 启动应用
AppiumUtils.launch_app(driver)

# 关闭应用
AppiumUtils.close_app(driver)

# 重置应用
AppiumUtils.reset_app(driver)

# 将应用切换到后台
AppiumUtils.background_app(driver, seconds=5)

# ==================== 网络操作 ====================
# 设置网络连接（仅WiFi）
AppiumUtils.set_network_connection(driver, 2)

# 获取网络连接状态
network_status = AppiumUtils.get_network_connection(driver)
print(f"网络状态: {network_status}")

# ==================== GSM操作（Android） ====================
# 模拟电话呼叫
AppiumUtils.make_gsm_call(driver, "10086", "call")

# 设置GSM信号强度
AppiumUtils.set_gsm_signal(driver, "good")

# 设置GSM语音状态
AppiumUtils.set_gsm_voice(driver, "home")

# ==================== 截图 ====================
# 截取屏幕
 screenshot_path = AppiumUtils.take_screenshot(driver, filename="app_screenshot.png")
print(f"截图保存到: {screenshot_path}")

# ==================== 关闭driver ====================
AppiumUtils.close_driver(driver)

# ==================== 使用AppiumElement ====================
from btools import AppiumElement

# 创建元素实例
login_button = AppiumElement(driver, "id", "com.example.app:id/login_button")

# 点击元素
login_button.click()

# 检查元素是否可见
if login_button.is_visible():
    print("登录按钮可见")
```

### CSVHandler

`CSVHandler` 类提供了CSV文件的读写操作功能。

```python
from btools import CSVHandler

# ==================== 读取CSV文件 ====================
# 基本读取
csv_data = CSVHandler.read_csv("data.csv")
print("CSV数据:", csv_data)

# 读取时跳过表头
csv_data_no_header = CSVHandler.read_csv("data.csv", skip_header=True)
print("CSV数据（无表头）:", csv_data_no_header)

# 自定义分隔符
csv_data_tab = CSVHandler.read_csv("data.tsv", delimiter="\t")
print("TSV数据:", csv_data_tab)

# 以字典形式读取（使用表头作为键）
csv_dict_data = CSVHandler.read_csv_dict("data.csv")
print("CSV字典数据:", csv_dict_data)

# ==================== 写入CSV文件 ====================
# 基本写入
data = [
    ["姓名", "年龄", "城市"],
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]
CSVHandler.write_csv("output.csv", data)
print("CSV文件写入完成")

# 写入时指定表头
data_no_header = [
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]
header = ["姓名", "年龄", "城市"]
CSVHandler.write_csv("output_with_header.csv", data_no_header, header=header)
print("带表头的CSV文件写入完成")

# 以字典形式写入
dict_data = [
    {"姓名": "张三", "年龄": 25, "城市": "北京"},
    {"姓名": "李四", "年龄": 30, "城市": "上海"},
    {"姓名": "王五", "年龄": 28, "城市": "广州"}
]
CSVHandler.write_csv_dict("output_dict.csv", dict_data)
print("字典形式CSV文件写入完成")
```

### ExcelHandler

`ExcelHandler` 类提供了Excel文件的读写和单元格更新操作功能。

**注意：使用ExcelHandler需要安装openpyxl库**

```bash
pip install openpyxl
```

```python
from btools import ExcelHandler

# ==================== 读取Excel文件 ====================
# 基本读取
excel_data = ExcelHandler.read_excel("data.xlsx")
print("Excel数据:", excel_data)

# 读取指定工作表
excel_data_sheet = ExcelHandler.read_excel("data.xlsx", sheet_name="Sheet2")
print("指定工作表数据:", excel_data_sheet)

# 读取时跳过表头
excel_data_no_header = ExcelHandler.read_excel("data.xlsx", skip_header=True)
print("Excel数据（无表头）:", excel_data_no_header)

# 以字典形式读取（使用表头作为键）
excel_dict_data = ExcelHandler.read_excel_dict("data.xlsx")
print("Excel字典数据:", excel_dict_data)

# ==================== 写入Excel文件 ====================
# 基本写入
data = [
    ["姓名", "年龄", "城市"],
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]
ExcelHandler.write_excel("output.xlsx", data)
print("Excel文件写入完成")

# 写入到指定工作表
data_no_header = [
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]
header = ["姓名", "年龄", "城市"]
ExcelHandler.write_excel("output_with_header.xlsx", data_no_header, 
                        sheet_name="员工信息", header=header)
print("带表头的Excel文件写入完成")

# 以字典形式写入
dict_data = [
    {"姓名": "张三", "年龄": 25, "城市": "北京"},
    {"姓名": "李四", "年龄": 30, "城市": "上海"},
    {"姓名": "王五", "年龄": 28, "城市": "广州"}
]
ExcelHandler.write_excel_dict("output_dict.xlsx", dict_data, sheet_name="员工数据")
print("字典形式Excel文件写入完成")

# ==================== 更新Excel单元格 ====================
# 更新单个单元格
ExcelHandler.update_excel_cell("output.xlsx", cell="A1", value="员工姓名")
print("Excel单元格更新完成")

# 更新指定工作表的单元格
ExcelHandler.update_excel_cell("output.xlsx", sheet_name="Sheet1", 
                             cell="B1", value="员工年龄")
print("指定工作表的Excel单元格更新完成")
```

## 如何打包

要将`btools`项目打包为wheel文件，请按照以下步骤操作：

### 1. 安装所需工具

```bash
pip install --upgrade setuptools wheel build
```

### 2. 打包项目

在项目根目录运行以下命令：

```bash
python setup.py bdist_wheel
```

这将创建一个`dist`目录，包含wheel文件，例如：`btools-1.0.0-py3-none-any.whl`。

### 3. 验证包

您可以通过解压wheel文件来验证其内容：

```bash
# 在Windows上
rename btools-1.0.0-py3-none-any.whl btools-1.0.0-py3-none-any.zip
# 然后使用压缩工具解压

# 在Linux/Mac上
unzip btools-1.0.0-py3-none-any.whl -d whl_contents
```

## 如何添加本地依赖库

要添加本地的库文件作为`btools`项目的依赖，请按照以下步骤操作：

### 1. 准备本地库文件

确保您的本地库已经打包为wheel文件。如果尚未打包，请按照以下步骤操作：

```bash
# 进入本地库项目目录
cd /path/to/your/local/library

# 安装打包工具
pip install --upgrade setuptools wheel

# 打包为wheel文件
python setup.py bdist_wheel
```

这将在本地库项目的`dist`目录中生成wheel文件，例如：`local_library-1.0.0-py3-none-any.whl`。

### 2. 在setup.py中添加本地依赖

有两种方法可以添加本地依赖：

#### 方法一：使用相对路径引用wheel文件

```python
# setup.py
from setuptools import setup, find_packages

setup(
    # 其他配置...
    install_requires=[
        'pyyaml',
        'requests',
        # 添加本地依赖
        'local_library @ file:///path/to/your/local/library/dist/local_library-1.0.0-py3-none-any.whl'
    ],
)
```

#### 方法二：使用本地目录路径

```python
# setup.py
from setuptools import setup, find_packages

setup(
    # 其他配置...
    install_requires=[
        'pyyaml',
        'requests',
        # 添加本地依赖
        'local_library @ file:///path/to/your/local/library'
    ],
)
```

### 3. 安装本地依赖

在`btools`项目目录中运行以下命令来安装依赖：

```bash
pip install -e .
```

或者，当您打包`btools`项目时，本地依赖也会被包含在安装过程中：

```bash
# 打包btools项目
python setup.py bdist_wheel

# 安装btools包（会自动安装所有依赖，包括本地依赖）
pip install dist/btools-1.0.0-py3-none-any.whl
```

### 4. 验证依赖安装

运行以下命令来验证本地依赖是否已正确安装：

```bash
pip list | grep local_library
```

如果输出显示了本地库的版本信息，则说明依赖安装成功。

## 如何添加新类

要向`btools`包添加新类，请按照以下步骤操作：

### 1. 创建类文件

在`btools/`下的适当目录中创建一个新的Python文件：

- 核心功能：`btools/core/`
- 工具函数：`btools/utils/`

例如，要创建一个新的`Database`类：

```python
# btools/core/database.py

class Database:
    """
    数据库连接和查询工具类
    """
    
    def __init__(self, host, port, username, password, database):
        """
        初始化数据库连接
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        """
        连接到数据库
        """
        # 实现代码
        pass
    
    def query(self, sql, params=None):
        """
        执行SQL查询
        """
        # 实现代码
        pass
    
    def disconnect(self):
        """
        断开数据库连接
        """
        # 实现代码
        pass
```

### 2. 更新__init__.py

将新类添加到`btools`目录下的`__init__.py`文件中：

```python
# btools/__init__.py

__version__ = "1.0.0"

# 导出核心模块
from .core.logger import Logger
from .core.config import Config
from .core.database import Database  # 添加这一行

# 导出工具模块
from .utils.validator import Validator
from .utils.converter import Converter

__all__ = [
    "Logger",
    "Config",
    "Database",  # 添加这一行
    "Validator",
    "Converter"
]
```

### 3. 更新文档

在README.md文件中添加新类的文档，包括使用示例。

### 4. 测试新类

创建一个测试脚本来验证新类是否正常工作：

```python
# test_database.py

from btools import Database

# 测试Database类
db = Database(
    host="localhost",
    port=5432,
    username="admin",
    password="password123",
    database="mydb"
)

# 测试连接
db.connect()

# 测试查询
# result = db.query("SELECT * FROM users")

# 测试断开连接
db.disconnect()

print("Database类测试完成！")
```

### 5. 重新打包项目

添加新类后，重新打包项目以包含更改：

```bash
python setup.py bdist_wheel
```

## 许可证

本项目采用MIT许可证。有关详细信息，请参阅[LICENSE](LICENSE)文件。
