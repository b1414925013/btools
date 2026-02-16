# AppiumUtils 使用指南

`AppiumUtils` 类提供了基于Appium的移动应用自动化测试操作，支持Android和iOS平台。

## 依赖

使用 `AppiumUtils` 需要安装以下依赖：

```bash
pip install Appium-Python-Client
```

同时需要：
- 安装Appium服务器
- 配置Android SDK（Android测试）
- 配置Xcode（iOS测试）
- 准备测试设备或模拟器

## 基本使用

### 初始化driver

#### Android测试

```python
from btools import AppiumUtils

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
```

#### iOS测试

```python
# 获取iOS driver实例
driver = AppiumUtils.get_driver(
    platform_name="iOS",
    platform_version="16.0",
    device_name="iPhone Simulator",
    app="/path/to/your/app.app",
    automation_name="XCUITest",
    no_reset=True
)
```

### 元素操作

```python
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
```

### 元素检查

```python
# 检查元素是否存在
if AppiumUtils.is_element_present(driver, "id", "com.example.app:id/submit_button"):
    print("提交按钮存在")

# 检查元素是否可见
if AppiumUtils.is_element_visible(driver, "id", "com.example.app:id/success_message"):
    print("成功消息可见")
```

### 滚动操作

```python
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
```

### 触摸操作

```python
# 点击指定坐标
AppiumUtils.tap(driver, 500, 1000)

# 长按元素
AppiumUtils.long_press(driver, "id", "com.example.app:id/item")
```

### 应用操作

```python
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
```

### 网络操作

```python
# 设置网络连接（仅WiFi）
AppiumUtils.set_network_connection(driver, 2)

# 获取网络连接状态
network_status = AppiumUtils.get_network_connection(driver)
print(f"网络状态: {network_status}")
```

### GSM操作（Android）

```python
# 模拟电话呼叫
AppiumUtils.make_gsm_call(driver, "10086", "call")

# 设置GSM信号强度
AppiumUtils.set_gsm_signal(driver, "good")

# 设置GSM语音状态
AppiumUtils.set_gsm_voice(driver, "home")
```

### 截图

```python
# 截取屏幕
screenshot_path = AppiumUtils.take_screenshot(driver, filename="app_screenshot.png")
print(f"截图保存到: {screenshot_path}")
```

### 关闭driver

```python
AppiumUtils.close_driver(driver)
```

## 使用 AppiumElement

```python
from btools import AppiumElement

# 创建元素实例
login_button = AppiumElement(driver, "id", "com.example.app:id/login_button")

# 点击元素
login_button.click()

# 检查元素是否可见
if login_button.is_visible():
    print("登录按钮可见")

# 获取元素文本
text = login_button.get_text()
print(f"按钮文本: {text}")

# 输入文本（如果是输入框）
username_input = AppiumElement(driver, "id", "com.example.app:id/username_input")
username_input.send_keys("testuser")
```

## 高级功能

### 显式等待

```python
# 显式等待元素出现
element = AppiumUtils.wait_for_element(
    driver, 
    by="id", 
    value="com.example.app:id/login_button", 
    timeout=10
)
print("找到登录按钮")

# 显式等待元素可点击
AppiumUtils.wait_for_element_clickable(
    driver, 
    by="id", 
    value="com.example.app:id/submit_button", 
    timeout=10
)
print("提交按钮可点击")

# 显式等待元素不可见
AppiumUtils.wait_for_element_invisible(
    driver, 
    by="id", 
    value="com.example.app:id/loading_spinner", 
    timeout=10
)
print("加载 spinner 已隐藏")
```

### 多设备测试

```python
# 启动多个设备的测试
devices = [
    {
        "platform_name": "Android",
        "platform_version": "13",
        "device_name": "emulator-5554",
        "app_package": "com.example.app",
        "app_activity": ".MainActivity"
    },
    {
        "platform_name": "Android",
        "platform_version": "12",
        "device_name": "emulator-5556",
        "app_package": "com.example.app",
        "app_activity": ".MainActivity"
    }
]

# 为每个设备创建driver并执行测试
for device_config in devices:
    driver = AppiumUtils.get_driver(**device_config)
    try:
        # 执行测试...
        print(f"测试设备: {device_config['device_name']}")
        AppiumUtils.click_element(driver, "id", "com.example.app:id/login_button")
    finally:
        AppiumUtils.close_driver(driver)
```

### 测试场景示例

#### 登录测试

```python
def test_login():
    # 初始化driver
    driver = AppiumUtils.get_driver(
        platform_name="Android",
        platform_version="13",
        device_name="Android Emulator",
        app_package="com.example.app",
        app_activity=".MainActivity",
        automation_name="UiAutomator2",
        no_reset=True
    )
    
    try:
        # 点击登录按钮
        AppiumUtils.click_element(driver, "id", "com.example.app:id/login_button")
        
        # 输入用户名和密码
        AppiumUtils.send_keys(driver, "id", "com.example.app:id/username_input", "testuser")
        AppiumUtils.send_keys(driver, "id", "com.example.app:id/password_input", "password123")
        
        # 提交登录
        AppiumUtils.click_element(driver, "id", "com.example.app:id/submit_button")
        
        # 等待登录成功
        AppiumUtils.wait_for_element(
            driver, "id", "com.example.app:id/welcome_message", timeout=10
        )
        
        # 验证登录成功
        welcome_text = AppiumUtils.get_element_text(
            driver, "id", "com.example.app:id/welcome_message"
        )
        assert "Welcome" in welcome_text
        print("登录测试通过")
        
    finally:
        # 关闭driver
        AppiumUtils.close_driver(driver)

# 运行测试
test_login()
```

#### 应用导航测试

```python
def test_app_navigation():
    # 初始化driver
    driver = AppiumUtils.get_driver(
        platform_name="Android",
        platform_version="13",
        device_name="Android Emulator",
        app_package="com.example.app",
        app_activity=".MainActivity",
        automation_name="UiAutomator2",
        no_reset=True
    )
    
    try:
        # 导航到设置页面
        AppiumUtils.click_element(driver, "id", "com.example.app:id/settings_button")
        
        # 验证设置页面
        AppiumUtils.wait_for_element(
            driver, "id", "com.example.app:id/settings_title", timeout=5
        )
        print("进入设置页面")
        
        # 导航到个人资料页面
        AppiumUtils.click_element(driver, "id", "com.example.app:id/profile_button")
        
        # 验证个人资料页面
        AppiumUtils.wait_for_element(
            driver, "id", "com.example.app:id/profile_title", timeout=5
        )
        print("进入个人资料页面")
        
        # 返回主页面
        driver.back()
        driver.back()
        
        # 验证主页面
        AppiumUtils.wait_for_element(
            driver, "id", "com.example.app:id/main_title", timeout=5
        )
        print("返回主页面")
        
        print("应用导航测试通过")
        
    finally:
        # 关闭driver
        AppiumUtils.close_driver(driver)

# 运行测试
test_app_navigation()
```

## 常见问题

### Appium服务器连接问题

如果遇到Appium服务器连接失败，请确保：

1. Appium服务器已启动
2. 网络连接正常
3. 端口未被占用

### 元素定位问题

如果遇到元素定位失败，请检查：

1. 元素选择器是否正确
2. 元素是否在当前页面
3. 元素是否需要滚动才能可见
4. 元素是否有动态加载的延迟（使用显式等待）

### 设备连接问题

如果遇到设备连接失败，请确保：

1. 设备已正确连接到电脑
2. USB调试已开启（Android）
3. 开发者模式已启用
4. 设备在`adb devices`列表中可见

### 应用安装问题

如果遇到应用安装失败，请：

1. 检查应用包是否有效
2. 检查设备存储空间是否充足
3. 检查应用是否与设备系统版本兼容

### 性能问题

移动设备测试可能会遇到性能问题，建议：

1. 使用真机测试（比模拟器性能更好）
2. 合理设置等待时间
3. 优化测试脚本，减少不必要的操作
4. 使用`no_reset=True`减少应用重启时间

### 跨平台测试

`AppiumUtils` 支持跨平台测试，但需要注意：

1. Android和iOS的元素定位方式可能不同
2. 某些操作在不同平台上的实现可能有差异
3. 需要为不同平台准备不同的测试配置

通过合理的配置和脚本设计，可以使用`AppiumUtils`实现跨平台的移动应用自动化测试。