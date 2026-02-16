from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
from appium.webdriver.extensions.android.network import Network
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Optional, Dict, Any, Union
import os
from datetime import datetime

class AppiumUtils:
    """
    Appium工具类，提供常用的移动应用自动化测试操作
    """
    
    @staticmethod
    def get_driver(platform_name: str = "Android", platform_version: Optional[str] = None, 
                  device_name: str = "Android Emulator", app: Optional[str] = None, 
                  app_package: Optional[str] = None, app_activity: Optional[str] = None, 
                  automation_name: str = "UiAutomator2", udid: Optional[str] = None, 
                  no_reset: bool = False, full_reset: bool = False, 
                  new_command_timeout: int = 60, implicit_wait: int = 10) -> webdriver.Remote:
        """
        获取Appium driver实例
        
        Args:
            platform_name (str): 平台名称，支持 Android, iOS
            platform_version (str): 平台版本
            device_name (str): 设备名称
            app (str): 应用路径
            app_package (str): 应用包名
            app_activity (str): 应用启动Activity
            automation_name (str): 自动化引擎名称
            udid (str): 设备UDID
            no_reset (bool): 是否不重置应用
            full_reset (bool): 是否完全重置应用
            new_command_timeout (int): 新命令超时时间（秒）
            implicit_wait (int): 隐式等待时间（秒）
            
        Returns:
            webdriver.Remote: Appium driver实例
        """
        desired_caps = {
            "platformName": platform_name,
            "deviceName": device_name,
            "automationName": automation_name,
            "newCommandTimeout": new_command_timeout
        }
        
        if platform_version:
            desired_caps["platformVersion"] = platform_version
        
        if app:
            desired_caps["app"] = app
        
        if app_package:
            desired_caps["appPackage"] = app_package
        
        if app_activity:
            desired_caps["appActivity"] = app_activity
        
        if udid:
            desired_caps["udid"] = udid
        
        desired_caps["noReset"] = no_reset
        desired_caps["fullReset"] = full_reset
        
        # 连接Appium服务器
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        driver.implicitly_wait(implicit_wait)
        
        return driver
    
    @staticmethod
    def find_element(driver: webdriver.Remote, by: str, value: str, 
                    timeout: int = 30, poll_frequency: float = 0.5) -> WebElement:
        """
        查找单个元素
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式，支持 id, xpath, accessibility_id, class_name, android_uiautomator, ios_predicate
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            WebElement: 找到的元素
        """
        by_map = {
            "id": AppiumBy.ID,
            "xpath": AppiumBy.XPATH,
            "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
            "class_name": AppiumBy.CLASS_NAME,
            "android_uiautomator": AppiumBy.ANDROID_UIAUTOMATOR,
            "ios_predicate": AppiumBy.IOS_PREDICATE_STRING
        }
        
        if by not in by_map:
            raise ValueError(f"不支持的定位方式: {by}")
        
        return WebDriverWait(driver, timeout, poll_frequency).until(
            EC.presence_of_element_located((by_map[by], value))
        )
    
    @staticmethod
    def find_elements(driver: webdriver.Remote, by: str, value: str, 
                     timeout: int = 30, poll_frequency: float = 0.5) -> List[WebElement]:
        """
        查找多个元素
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            list: 找到的元素列表
        """
        by_map = {
            "id": AppiumBy.ID,
            "xpath": AppiumBy.XPATH,
            "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
            "class_name": AppiumBy.CLASS_NAME,
            "android_uiautomator": AppiumBy.ANDROID_UIAUTOMATOR,
            "ios_predicate": AppiumBy.IOS_PREDICATE_STRING
        }
        
        if by not in by_map:
            raise ValueError(f"不支持的定位方式: {by}")
        
        return WebDriverWait(driver, timeout, poll_frequency).until(
            EC.presence_of_all_elements_located((by_map[by], value))
        )
    
    @staticmethod
    def wait_for_element_visible(driver: webdriver.Remote, by: str, value: str, 
                                timeout: int = 30, poll_frequency: float = 0.5) -> WebElement:
        """
        等待元素可见
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            WebElement: 找到的可见元素
        """
        by_map = {
            "id": AppiumBy.ID,
            "xpath": AppiumBy.XPATH,
            "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
            "class_name": AppiumBy.CLASS_NAME,
            "android_uiautomator": AppiumBy.ANDROID_UIAUTOMATOR,
            "ios_predicate": AppiumBy.IOS_PREDICATE_STRING
        }
        
        if by not in by_map:
            raise ValueError(f"不支持的定位方式: {by}")
        
        return WebDriverWait(driver, timeout, poll_frequency).until(
            EC.visibility_of_element_located((by_map[by], value))
        )
    
    @staticmethod
    def wait_for_element_invisible(driver: webdriver.Remote, by: str, value: str, 
                                  timeout: int = 30, poll_frequency: float = 0.5) -> bool:
        """
        等待元素不可见
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            bool: 元素是否不可见
        """
        by_map = {
            "id": AppiumBy.ID,
            "xpath": AppiumBy.XPATH,
            "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
            "class_name": AppiumBy.CLASS_NAME,
            "android_uiautomator": AppiumBy.ANDROID_UIAUTOMATOR,
            "ios_predicate": AppiumBy.IOS_PREDICATE_STRING
        }
        
        if by not in by_map:
            raise ValueError(f"不支持的定位方式: {by}")
        
        return WebDriverWait(driver, timeout, poll_frequency).until(
            EC.invisibility_of_element_located((by_map[by], value))
        )
    
    @staticmethod
    def click_element(driver: webdriver.Remote, by: str, value: str, 
                     timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        点击元素
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        element = AppiumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        element.click()
    
    @staticmethod
    def send_keys(driver: webdriver.Remote, by: str, value: str, text: str, 
                 timeout: int = 30, poll_frequency: float = 0.5, 
                 clear_first: bool = True) -> None:
        """
        输入文本
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            text (str): 要输入的文本
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            clear_first (bool): 是否先清空输入框
        """
        element = AppiumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    @staticmethod
    def get_element_text(driver: webdriver.Remote, by: str, value: str, 
                        timeout: int = 30, poll_frequency: float = 0.5) -> str:
        """
        获取元素文本
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            str: 元素文本
        """
        element = AppiumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        return element.text
    
    @staticmethod
    def get_element_attribute(driver: webdriver.Remote, by: str, value: str, attribute: str, 
                             timeout: int = 30, poll_frequency: float = 0.5) -> str:
        """
        获取元素属性
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            attribute (str): 属性名
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            str: 元素属性值
        """
        element = AppiumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        return element.get_attribute(attribute)
    
    @staticmethod
    def is_element_present(driver: webdriver.Remote, by: str, value: str, 
                          timeout: int = 10, poll_frequency: float = 0.5) -> bool:
        """
        检查元素是否存在
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            bool: 元素是否存在
        """
        try:
            AppiumUtils.find_element(driver, by, value, timeout, poll_frequency)
            return True
        except Exception:
            return False
    
    @staticmethod
    def is_element_visible(driver: webdriver.Remote, by: str, value: str, 
                          timeout: int = 10, poll_frequency: float = 0.5) -> bool:
        """
        检查元素是否可见
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            bool: 元素是否可见
        """
        try:
            AppiumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
            return True
        except Exception:
            return False
    
    @staticmethod
    def take_screenshot(driver: webdriver.Remote, save_path: Optional[str] = None, 
                       filename: Optional[str] = None) -> str:
        """
        截图
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            save_path (str): 保存路径
            filename (str): 文件名
            
        Returns:
            str: 截图保存路径
        """
        if not save_path:
            save_path = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(save_path):
            os.makedirs(save_path, exist_ok=True)
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
        
        screenshot_path = os.path.join(save_path, filename)
        screenshot = driver.get_screenshot_as_file(screenshot_path)
        if screenshot:
            return screenshot_path
        else:
            raise Exception("截图失败")
    
    @staticmethod
    def scroll_to_element(driver: webdriver.Remote, by: str, value: str, 
                         timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        滚动到元素位置
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        # 尝试使用不同的滚动方法
        try:
            # 方法1: 使用元素的location_once_scrolled_into_view
            element = AppiumUtils.find_element(driver, by, value, timeout, poll_frequency)
            element.location_once_scrolled_into_view
        except Exception:
            # 方法2: 使用UIAutomator滚动（Android）
            if driver.capabilities.get("platformName").lower() == "android":
                if by == "id":
                    scroll_script = f"new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().resourceId(\"{value}\"))"
                    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_script)
                elif by == "xpath":
                    # 对于XPath，尝试获取text或其他属性进行滚动
                    pass
    
    @staticmethod
    def swipe(driver: webdriver.Remote, start_x: int, start_y: int, end_x: int, end_y: int, 
              duration: int = 500) -> None:
        """
        滑动操作
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            start_x (int): 起始X坐标
            start_y (int): 起始Y坐标
            end_x (int): 结束X坐标
            end_y (int): 结束Y坐标
            duration (int): 滑动持续时间（毫秒）
        """
        driver.swipe(start_x, start_y, end_x, end_y, duration)
    
    @staticmethod
    def swipe_up(driver: webdriver.Remote, duration: int = 500, percentage: float = 0.8) -> None:
        """
        向上滑动
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            duration (int): 滑动持续时间（毫秒）
            percentage (float): 滑动距离百分比
        """
        size = driver.get_window_size()
        start_x = size["width"] // 2
        start_y = int(size["height"] * percentage)
        end_x = start_x
        end_y = int(size["height"] * (1 - percentage))
        AppiumUtils.swipe(driver, start_x, start_y, end_x, end_y, duration)
    
    @staticmethod
    def swipe_down(driver: webdriver.Remote, duration: int = 500, percentage: float = 0.8) -> None:
        """
        向下滑动
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            duration (int): 滑动持续时间（毫秒）
            percentage (float): 滑动距离百分比
        """
        size = driver.get_window_size()
        start_x = size["width"] // 2
        start_y = int(size["height"] * (1 - percentage))
        end_x = start_x
        end_y = int(size["height"] * percentage)
        AppiumUtils.swipe(driver, start_x, start_y, end_x, end_y, duration)
    
    @staticmethod
    def swipe_left(driver: webdriver.Remote, duration: int = 500, percentage: float = 0.8) -> None:
        """
        向左滑动
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            duration (int): 滑动持续时间（毫秒）
            percentage (float): 滑动距离百分比
        """
        size = driver.get_window_size()
        start_x = int(size["width"] * percentage)
        start_y = size["height"] // 2
        end_x = int(size["width"] * (1 - percentage))
        end_y = start_y
        AppiumUtils.swipe(driver, start_x, start_y, end_x, end_y, duration)
    
    @staticmethod
    def swipe_right(driver: webdriver.Remote, duration: int = 500, percentage: float = 0.8) -> None:
        """
        向右滑动
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            duration (int): 滑动持续时间（毫秒）
            percentage (float): 滑动距离百分比
        """
        size = driver.get_window_size()
        start_x = int(size["width"] * (1 - percentage))
        start_y = size["height"] // 2
        end_x = int(size["width"] * percentage)
        end_y = start_y
        AppiumUtils.swipe(driver, start_x, start_y, end_x, end_y, duration)
    
    @staticmethod
    def tap(driver: webdriver.Remote, x: int, y: int, count: int = 1) -> None:
        """
        点击指定坐标
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            x (int): X坐标
            y (int): Y坐标
            count (int): 点击次数
        """
        action = TouchAction(driver)
        action.tap(x=x, y=y, count=count).perform()
    
    @staticmethod
    def long_press(driver: webdriver.Remote, by: str, value: str, duration: int = 2000, 
                  timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        长按元素
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
            duration (int): 长按持续时间（毫秒）
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        element = AppiumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        action = TouchAction(driver)
        action.long_press(element, duration=duration).perform()
    
    @staticmethod
    def get_device_size(driver: webdriver.Remote) -> Dict[str, int]:
        """
        获取设备屏幕尺寸
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            
        Returns:
            dict: 包含width和height的字典
        """
        return driver.get_window_size()
    
    @staticmethod
    def get_current_activity(driver: webdriver.Remote) -> str:
        """
        获取当前Activity（Android）
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            
        Returns:
            str: 当前Activity
        """
        if driver.capabilities.get("platformName").lower() == "android":
            return driver.current_activity
        else:
            raise ValueError("此方法仅适用于Android平台")
    
    @staticmethod
    def get_current_package(driver: webdriver.Remote) -> str:
        """
        获取当前包名（Android）
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            
        Returns:
            str: 当前包名
        """
        if driver.capabilities.get("platformName").lower() == "android":
            return driver.current_package
        else:
            raise ValueError("此方法仅适用于Android平台")
    
    @staticmethod
    def launch_app(driver: webdriver.Remote) -> None:
        """
        启动应用
        
        Args:
            driver (webdriver.Remote): Appium driver实例
        """
        driver.launch_app()
    
    @staticmethod
    def close_app(driver: webdriver.Remote) -> None:
        """
        关闭应用
        
        Args:
            driver (webdriver.Remote): Appium driver实例
        """
        driver.close_app()
    
    @staticmethod
    def reset_app(driver: webdriver.Remote) -> None:
        """
        重置应用
        
        Args:
            driver (webdriver.Remote): Appium driver实例
        """
        driver.reset()
    
    @staticmethod
    def background_app(driver: webdriver.Remote, seconds: int = 5) -> None:
        """
        将应用切换到后台
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            seconds (int): 后台停留时间（秒）
        """
        driver.background_app(seconds)
    
    @staticmethod
    def set_network_connection(driver: webdriver.Remote, connection_type: int) -> int:
        """
        设置网络连接
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            connection_type (int): 网络连接类型
                0: 无网络
                1: 飞行模式
                2: 仅WiFi
                4: 仅数据
                6: WiFi + 数据
            
        Returns:
            int: 设置后的网络连接类型
        """
        return driver.set_network_connection(connection_type)
    
    @staticmethod
    def get_network_connection(driver: webdriver.Remote) -> int:
        """
        获取网络连接状态
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            
        Returns:
            int: 网络连接类型
        """
        return driver.network_connection
    
    @staticmethod
    def make_gsm_call(driver: webdriver.Remote, phone_number: str, action: str) -> None:
        """
        模拟GSM通话（Android）
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            phone_number (str): 电话号码
            action (str): 操作类型，支持: call, accept, cancel, hold
        """
        if driver.capabilities.get("platformName").lower() == "android":
            action_map = {
                "call": GsmCallActions.CALL,
                "accept": GsmCallActions.ACCEPT,
                "cancel": GsmCallActions.CANCEL,
                "hold": GsmCallActions.HOLD
            }
            if action in action_map:
                driver.make_gsm_call(phone_number, action_map[action])
            else:
                raise ValueError(f"不支持的操作类型: {action}")
        else:
            raise ValueError("此方法仅适用于Android平台")
    
    @staticmethod
    def set_gsm_signal(driver: webdriver.Remote, strength: str) -> None:
        """
        设置GSM信号强度（Android）
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            strength (str): 信号强度，支持: none, poor, moderate, good, great
        """
        if driver.capabilities.get("platformName").lower() == "android":
            driver.set_gsm_signal(strength)
        else:
            raise ValueError("此方法仅适用于Android平台")
    
    @staticmethod
    def set_gsm_voice(driver: webdriver.Remote, state: str) -> None:
        """
        设置GSM语音状态（Android）
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            state (str): 语音状态，支持: unregistered, home, roaming, searching, denied
        """
        if driver.capabilities.get("platformName").lower() == "android":
            driver.set_gsm_voice(state)
        else:
            raise ValueError("此方法仅适用于Android平台")
    
    @staticmethod
    def close_driver(driver: webdriver.Remote) -> None:
        """
        关闭Appium driver
        
        Args:
            driver (webdriver.Remote): Appium driver实例
        """
        try:
            driver.quit()
        except Exception as e:
            print(f"关闭driver时出错: {e}")

class AppiumElement:
    """
    Appium元素包装类，提供更便捷的元素操作方法
    """
    
    def __init__(self, driver: webdriver.Remote, by: str, value: str):
        """
        初始化AppiumElement
        
        Args:
            driver (webdriver.Remote): Appium driver实例
            by (str): 定位方式
            value (str): 定位值
        """
        self.driver = driver
        self.by = by
        self.value = value
        self._element = None
    
    @property
    def element(self) -> WebElement:
        """
        获取WebElement实例
        
        Returns:
            WebElement: WebElement实例
        """
        if not self._element:
            self._element = AppiumUtils.find_element(self.driver, self.by, self.value)
        return self._element
    
    def click(self, timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        点击元素
        
        Args:
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        AppiumUtils.click_element(self.driver, self.by, self.value, timeout, poll_frequency)
    
    def send_keys(self, text: str, clear_first: bool = True, 
                 timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        输入文本
        
        Args:
            text (str): 要输入的文本
            clear_first (bool): 是否先清空输入框
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        AppiumUtils.send_keys(self.driver, self.by, self.value, text, timeout, poll_frequency, clear_first)
    
    def get_text(self, timeout: int = 30, poll_frequency: float = 0.5) -> str:
        """
        获取元素文本
        
        Args:
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            str: 元素文本
        """
        return AppiumUtils.get_element_text(self.driver, self.by, self.value, timeout, poll_frequency)
    
    def get_attribute(self, attribute: str, timeout: int = 30, poll_frequency: float = 0.5) -> str:
        """
        获取元素属性
        
        Args:
            attribute (str): 属性名
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            str: 元素属性值
        """
        return AppiumUtils.get_element_attribute(self.driver, self.by, self.value, attribute, timeout, poll_frequency)
    
    def is_visible(self, timeout: int = 10, poll_frequency: float = 0.5) -> bool:
        """
        检查元素是否可见
        
        Args:
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            bool: 元素是否可见
        """
        return AppiumUtils.is_element_visible(self.driver, self.by, self.value, timeout, poll_frequency)
    
    def is_present(self, timeout: int = 10, poll_frequency: float = 0.5) -> bool:
        """
        检查元素是否存在
        
        Args:
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            bool: 元素是否存在
        """
        return AppiumUtils.is_element_present(self.driver, self.by, self.value, timeout, poll_frequency)
    
    def scroll_to(self, timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        滚动到元素位置
        
        Args:
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        AppiumUtils.scroll_to_element(self.driver, self.by, self.value, timeout, poll_frequency)
    
    def long_press(self, duration: int = 2000, 
                  timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        长按元素
        
        Args:
            duration (int): 长按持续时间（毫秒）
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        AppiumUtils.long_press(self.driver, self.by, self.value, duration, timeout, poll_frequency)