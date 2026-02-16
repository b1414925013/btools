# SeleniumUtils 使用指南

`SeleniumUtils` 类提供了基于Selenium的Web自动化测试操作，支持各种浏览器和常用的Web元素操作。集成了 `webdriver-manager` 库，可以自动管理浏览器驱动的下载和更新。

## 依赖

使用 `SeleniumUtils` 需要安装以下依赖：

```bash
pip install selenium webdriver-manager
```

## 基本使用

### 初始化浏览器

```python
from btools import SeleniumUtils

# 获取Chrome浏览器实例
driver = SeleniumUtils.get_driver(
    browser="chrome",
    headless=False,
    implicit_wait=10
)

# 打开网页
driver.get("https://www.example.com")
```

### 元素操作

```python
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
```

### 元素检查

```python
# 检查元素是否存在
if SeleniumUtils.is_element_present(driver, "id", "submit-button"):
    print("提交按钮存在")

# 检查元素是否可见
if SeleniumUtils.is_element_visible(driver, "id", "success-message"):
    print("成功消息可见")
```

### 滚动操作

```python
# 滚动到元素位置
SeleniumUtils.scroll_to_element(driver, "id", "footer")

# 滚动到页面顶部
SeleniumUtils.scroll_to_top(driver)

# 滚动到页面底部
SeleniumUtils.scroll_to_bottom(driver)
```

### 窗口操作

```python
# 切换到新窗口
SeleniumUtils.switch_to_window(driver, 1)

# 关闭其他窗口
SeleniumUtils.close_other_windows(driver)
```

### iframe操作

```python
# 切换到iframe
SeleniumUtils.switch_to_frame(driver, "id", "content-frame")

# 切换回默认内容
SeleniumUtils.switch_to_default_content(driver)
```

### 截图

```python
# 截取屏幕
screenshot_path = SeleniumUtils.take_screenshot(driver, filename="test_screenshot.png")
print(f"截图保存到: {screenshot_path}")
```

### 其他操作

```python
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
```

### 关闭浏览器

```python
SeleniumUtils.close_driver(driver)
```

## 使用 SeleniumElement

```python
from btools import SeleniumElement

# 创建元素实例
login_button = SeleniumElement(driver, "id", "login-button")

# 点击元素
login_button.click()

# 检查元素是否可见
if login_button.is_visible():
    print("登录按钮可见")

# 获取元素文本
text = login_button.get_text()
print(f"按钮文本: {text}")

# 输入文本（如果是输入框）
username_input = SeleniumElement(driver, "id", "username")
username_input.send_keys("testuser")
```

## 高级功能

### 浏览器选项配置

```python
# 配置Chrome选项
chrome_options = SeleniumUtils.get_chrome_options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")

# 使用自定义选项创建driver
driver = SeleniumUtils.get_driver(
    browser="chrome",
    options=chrome_options,
    implicit_wait=10
)
```

### 显式等待

```python
# 显式等待元素出现
element = SeleniumUtils.wait_for_element(
    driver, 
    by="id", 
    value="login-button", 
    timeout=10
)
print("找到登录按钮")

# 显式等待元素可点击
SeleniumUtils.wait_for_element_clickable(
    driver, 
    by="id", 
    value="submit-button", 
    timeout=10
)
print("提交按钮可点击")

# 显式等待元素不可见
SeleniumUtils.wait_for_element_invisible(
    driver, 
    by="id", 
    value="loading-spinner", 
    timeout=10
)
print("加载 spinner 已隐藏")
```

### 多浏览器支持

```python
# 使用Firefox
driver = SeleniumUtils.get_driver(
    browser="firefox",
    headless=False,
    implicit_wait=10
)

# 使用Edge
driver = SeleniumUtils.get_driver(
    browser="edge",
    headless=False,
    implicit_wait=10
)
```

### 浏览器驱动自动管理

`SeleniumUtils` 集成了 `webdriver-manager` 库，可以自动下载和管理浏览器驱动：

```python
# 自动下载和使用Chrome驱动
driver = SeleniumUtils.get_driver(browser="chrome")
print("Chrome驱动自动管理成功")

# 自动下载和使用Firefox驱动
driver = SeleniumUtils.get_driver(browser="firefox")
print("Firefox驱动自动管理成功")

# 自动下载和使用Edge驱动
driver = SeleniumUtils.get_driver(browser="edge")
print("Edge驱动自动管理成功")
```

### 测试场景示例

#### 登录测试

```python
def test_login():
    # 初始化浏览器
    driver = SeleniumUtils.get_driver(browser="chrome")
    
    try:
        # 打开登录页面
        driver.get("https://example.com/login")
        
        # 输入用户名和密码
        SeleniumUtils.send_keys(driver, "id", "username", "testuser")
        SeleniumUtils.send_keys(driver, "id", "password", "password123")
        
        # 点击登录按钮
        SeleniumUtils.click_element(driver, "id", "login-button")
        
        # 等待登录成功
        SeleniumUtils.wait_for_element(
            driver, "css_selector", ".welcome-message", timeout=10
        )
        
        # 验证登录成功
        welcome_text = SeleniumUtils.get_element_text(
            driver, "css_selector", ".welcome-message"
        )
        assert "Welcome" in welcome_text
        print("登录测试通过")
        
    finally:
        # 关闭浏览器
        SeleniumUtils.close_driver(driver)

# 运行测试
test_login()
```

#### 表单提交测试

```python
def test_form_submission():
    # 初始化浏览器
    driver = SeleniumUtils.get_driver(browser="chrome")
    
    try:
        # 打开表单页面
        driver.get("https://example.com/form")
        
        # 填写表单
        SeleniumUtils.send_keys(driver, "id", "name", "John Doe")
        SeleniumUtils.send_keys(driver, "id", "email", "john@example.com")
        SeleniumUtils.send_keys(driver, "id", "message", "Hello, World!")
        
        # 提交表单
        SeleniumUtils.click_element(driver, "id", "submit-button")
        
        # 等待提交成功
        SeleniumUtils.wait_for_element(
            driver, "css_selector", ".success-message", timeout=10
        )
        
        # 验证提交成功
        success_text = SeleniumUtils.get_element_text(
            driver, "css_selector", ".success-message"
        )
        assert "Success" in success_text
        print("表单提交测试通过")
        
    finally:
        # 关闭浏览器
        SeleniumUtils.close_driver(driver)

# 运行测试
test_form_submission()
```

## 常见问题

### 浏览器驱动问题

`SeleniumUtils` 使用 `webdriver-manager` 自动管理浏览器驱动，解决了驱动版本不匹配的问题。如果遇到驱动相关错误，请确保：

1. 已安装 `webdriver-manager` 库
2. 浏览器已安装并更新到最新版本
3. 网络连接正常（驱动下载需要网络）

### 元素定位问题

如果遇到元素定位失败，请检查：

1. 元素选择器是否正确
2. 元素是否在iframe中（需要先切换到iframe）
3. 元素是否需要滚动才能可见
4. 页面是否完全加载（使用 `wait_for_page_load`）
5. 元素是否有动态加载的延迟（使用显式等待）

### 超时问题

如果遇到超时错误，请：

1. 增加隐式等待时间
2. 使用显式等待替代隐式等待
3. 检查网络连接是否稳定
4. 检查页面加载速度是否正常

### 无头模式

在CI/CD环境中，可以使用无头模式运行测试：

```python
driver = SeleniumUtils.get_driver(
    browser="chrome",
    headless=True,  # 无头模式
    implicit_wait=10
)
```

### 浏览器兼容性

`SeleniumUtils` 支持以下浏览器：
- Chrome
- Firefox
- Edge

不同浏览器的行为可能略有差异，请根据测试需求选择合适的浏览器。