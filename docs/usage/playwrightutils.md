# PlaywrightUtils 使用指南

`PlaywrightUtils` 类提供了基于Playwright的Web自动化测试操作，支持现代浏览器和更高级的自动化功能。

## 依赖

使用 `PlaywrightUtils` 需要安装以下依赖：

```bash
pip install playwright
playwright install
```

## 基本使用

### 初始化浏览器

```python
from btools import PlaywrightUtils

# 获取浏览器实例
playwright, browser, context, page = PlaywrightUtils.get_browser(
    browser="chromium",
    headless=False,
    slow_mo=100
)

# 打开网页
page.goto("https://www.example.com")
```

### 元素操作

```python
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
```

### 元素检查

```python
# 检查元素是否可见
if PlaywrightUtils.is_element_visible(page, ".success-message"):
    print("成功消息可见")

# 检查元素是否隐藏
if PlaywrightUtils.is_element_hidden(page, ".loading-spinner"):
    print("加载 spinner 已隐藏")
```

### 滚动操作

```python
# 滚动到元素位置
PlaywrightUtils.scroll_to_element(page, "#footer")

# 滚动到页面顶部
PlaywrightUtils.scroll_to_top(page)

# 滚动到页面底部
PlaywrightUtils.scroll_to_bottom(page)
```

### 窗口操作

```python
# 切换到新窗口
new_page = PlaywrightUtils.switch_to_window(page, 1)

# 关闭其他窗口
PlaywrightUtils.close_other_windows(page)
```

### iframe操作

```python
# 切换到iframe
frame = PlaywrightUtils.switch_to_frame(page, "#content-frame")
```

### 截图

```python
# 截取屏幕
screenshot_path = PlaywrightUtils.take_screenshot(page, filename="test_screenshot.png", full_page=True)
print(f"截图保存到: {screenshot_path}")
```

### 其他操作

```python
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
```

### 关闭浏览器

```python
PlaywrightUtils.close_browser(playwright, browser, context)
```

## 使用 PlaywrightElement

```python
from btools import PlaywrightElement

# 创建元素实例
login_button = PlaywrightElement(page, "#login-button")

# 点击元素
login_button.click()

# 检查元素是否可见
if login_button.is_visible():
    print("登录按钮可见")

# 获取元素文本
text = login_button.get_text()
print(f"按钮文本: {text}")

# 输入文本（如果是输入框）
username_input = PlaywrightElement(page, "#username")
username_input.send_keys("testuser")
```

## 高级功能

### 浏览器选项配置

```python
# 配置浏览器上下文
context_options = {
    "viewport": {"width": 1920, "height": 1080},
    "ignore_https_errors": True
}

# 使用自定义选项创建浏览器实例
playwright, browser, context, page = PlaywrightUtils.get_browser(
    browser="chromium",
    headless=False,
    context_options=context_options
)
```

### 网络请求拦截

```python
# 拦截网络请求
def handle_request(request):
    if request.url.endswith(".png") or request.url.endswith(".jpg"):
        request.abort()
    else:
        request.continue_()

# 设置请求拦截
page.on("request", handle_request)

# 打开网页
page.goto("https://example.com")
```

### 等待条件

```python
# 等待元素出现
PlaywrightUtils.wait_for_element(page, "#login-button", timeout=10000)
print("登录按钮已出现")

# 等待元素可点击
PlaywrightUtils.wait_for_element_clickable(page, "#submit-button", timeout=10000)
print("提交按钮可点击")

# 等待元素文本
PlaywrightUtils.wait_for_element_text(page, ".status", "Success", timeout=10000)
print("状态文本已更新为 Success")

# 等待URL变化
PlaywrightUtils.wait_for_url(page, "**/dashboard**", timeout=10000)
print("已导航到仪表板页面")
```

### 多浏览器支持

```python
# 使用Firefox
playwright, browser, context, page = PlaywrightUtils.get_browser(
    browser="firefox",
    headless=False
)

# 使用WebKit
playwright, browser, context, page = PlaywrightUtils.get_browser(
    browser="webkit",
    headless=False
)
```

### 测试场景示例

#### 登录测试

```python
def test_login():
    # 初始化浏览器
    playwright, browser, context, page = PlaywrightUtils.get_browser(
        browser="chromium",
        headless=False
    )
    
    try:
        # 打开登录页面
        page.goto("https://example.com/login")
        
        # 输入用户名和密码
        PlaywrightUtils.send_keys(page, "#username", "testuser")
        PlaywrightUtils.send_keys(page, "#password", "password123")
        
        # 点击登录按钮
        PlaywrightUtils.click_element(page, "#login-button")
        
        # 等待登录成功
        PlaywrightUtils.wait_for_element(page, ".welcome-message", timeout=10000)
        
        # 验证登录成功
        welcome_text = PlaywrightUtils.get_element_text(page, ".welcome-message")
        assert "Welcome" in welcome_text
        print("登录测试通过")
        
    finally:
        # 关闭浏览器
        PlaywrightUtils.close_browser(playwright, browser, context)

# 运行测试
test_login()
```

#### 数据驱动测试

```python
def test_search(keyword):
    # 初始化浏览器
    playwright, browser, context, page = PlaywrightUtils.get_browser(
        browser="chromium",
        headless=False
    )
    
    try:
        # 打开搜索页面
        page.goto("https://example.com/search")
        
        # 输入搜索关键词
        PlaywrightUtils.send_keys(page, "#search-input", keyword)
        PlaywrightUtils.click_element(page, "#search-button")
        
        # 等待搜索结果
        PlaywrightUtils.wait_for_element(page, ".search-results", timeout=10000)
        
        # 验证搜索结果
        results_count = PlaywrightUtils.get_element_count(page, ".result-item")
        print(f"搜索 '{keyword}' 找到 {results_count} 个结果")
        assert results_count > 0
        
    finally:
        # 关闭浏览器
        PlaywrightUtils.close_browser(playwright, browser, context)

# 运行多个搜索测试
keywords = ["python", "automation", "testing"]
for keyword in keywords:
    test_search(keyword)
```

## 常见问题

### 浏览器安装问题

首次使用Playwright时，需要安装浏览器：

```bash
playwright install
```

### 元素定位问题

如果遇到元素定位失败，请检查：

1. 选择器是否正确（Playwright支持CSS选择器和XPath）
2. 元素是否在iframe中
3. 元素是否需要滚动才能可见
4. 元素是否有动态加载的延迟（使用 `wait_for_element`）

### 超时问题

如果遇到超时错误，请：

1. 增加超时时间
2. 使用更具体的等待条件
3. 检查网络连接是否稳定
4. 检查页面加载速度是否正常

### 无头模式

在CI/CD环境中，可以使用无头模式运行测试：

```python
playwright, browser, context, page = PlaywrightUtils.get_browser(
    browser="chromium",
    headless=True  # 无头模式
)
```

### 浏览器兼容性

`PlaywrightUtils` 支持以下浏览器：
- Chromium (Chrome/Edge)
- Firefox
- WebKit (Safari)

Playwright提供了更现代的自动化API，相比Selenium有更好的性能和可靠性。