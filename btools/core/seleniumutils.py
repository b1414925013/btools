from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Optional, Dict, Any, Union
import time
import os
from datetime import datetime

# 导入webdriver-manager
try:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from webdriver_manager.core.driver_cache import DriverCacheManager
    WEBDRIVER_MANAGER_AVAILABLE = True
except ImportError:
    WEBDRIVER_MANAGER_AVAILABLE = False

class SeleniumUtils:
    """
    Selenium工具类，提供常用的Web自动化测试操作
    """
    
    @staticmethod
    def get_driver(browser: str = "chrome", options: Optional[List[str]] = None, 
                  headless: bool = False, implicit_wait: int = 10) -> webdriver:
        """
        获取WebDriver实例
        
        Args:
            browser (str): 浏览器类型，支持 chrome, firefox, edge, safari
            options (list): 浏览器选项列表
            headless (bool): 是否使用无头模式
            implicit_wait (int): 隐式等待时间（秒）
            
        Returns:
            webdriver: WebDriver实例
        """
        if browser.lower() == "chrome":
            from selenium.webdriver.chrome.options import Options as ChromeOptions
            chrome_options = ChromeOptions()
            if headless:
                chrome_options.add_argument("--headless")
            if options:
                for opt in options:
                    chrome_options.add_argument(opt)
            
            if WEBDRIVER_MANAGER_AVAILABLE:
                # 使用webdriver-manager自动管理驱动
                driver = webdriver.Chrome(
                    service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
                    options=chrome_options
                )
            else:
                # 传统方式
                driver = webdriver.Chrome(options=chrome_options)
                
        elif browser.lower() == "firefox":
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            firefox_options = FirefoxOptions()
            if headless:
                firefox_options.add_argument("--headless")
            if options:
                for opt in options:
                    firefox_options.add_argument(opt)
            
            if WEBDRIVER_MANAGER_AVAILABLE:
                # 使用webdriver-manager自动管理驱动
                driver = webdriver.Firefox(
                    service=webdriver.firefox.service.Service(GeckoDriverManager().install()),
                    options=firefox_options
                )
            else:
                # 传统方式
                driver = webdriver.Firefox(options=firefox_options)
                
        elif browser.lower() == "edge":
            from selenium.webdriver.edge.options import Options as EdgeOptions
            edge_options = EdgeOptions()
            if headless:
                edge_options.add_argument("--headless")
            if options:
                for opt in options:
                    edge_options.add_argument(opt)
            
            if WEBDRIVER_MANAGER_AVAILABLE:
                # 使用webdriver-manager自动管理驱动
                driver = webdriver.Edge(
                    service=webdriver.edge.service.Service(EdgeChromiumDriverManager().install()),
                    options=edge_options
                )
            else:
                # 传统方式
                driver = webdriver.Edge(options=edge_options)
                
        elif browser.lower() == "safari":
            # Safari驱动由系统管理
            driver = webdriver.Safari()
        else:
            raise ValueError(f"不支持的浏览器类型: {browser}")
        
        driver.implicitly_wait(implicit_wait)
        return driver
    
    @staticmethod
    def find_element(driver: webdriver, by: str, value: str, 
                    timeout: int = 30, poll_frequency: float = 0.5) -> WebElement:
        """
        查找单个元素
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式，支持 id, name, class_name, tag_name, link_text, partial_link_text, xpath, css_selector
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            WebElement: 找到的元素
        """
        by_map = {
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH,
            "css_selector": By.CSS_SELECTOR
        }
        
        if by not in by_map:
            raise ValueError(f"不支持的定位方式: {by}")
        
        return WebDriverWait(driver, timeout, poll_frequency).until(
            EC.presence_of_element_located((by_map[by], value))
        )
    
    @staticmethod
    def find_elements(driver: webdriver, by: str, value: str, 
                     timeout: int = 30, poll_frequency: float = 0.5) -> List[WebElement]:
        """
        查找多个元素
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            list: 找到的元素列表
        """
        by_map = {
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH,
            "css_selector": By.CSS_SELECTOR
        }
        
        if by not in by_map:
            raise ValueError(f"不支持的定位方式: {by}")
        
        return WebDriverWait(driver, timeout, poll_frequency).until(
            EC.presence_of_all_elements_located((by_map[by], value))
        )
    
    @staticmethod
    def wait_for_element_visible(driver: webdriver, by: str, value: str, 
                                timeout: int = 30, poll_frequency: float = 0.5) -> WebElement:
        """
        等待元素可见
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            WebElement: 找到的可见元素
        """
        by_map = {
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH,
            "css_selector": By.CSS_SELECTOR
        }
        
        if by not in by_map:
            raise ValueError(f"不支持的定位方式: {by}")
        
        return WebDriverWait(driver, timeout, poll_frequency).until(
            EC.visibility_of_element_located((by_map[by], value))
        )
    
    @staticmethod
    def wait_for_element_invisible(driver: webdriver, by: str, value: str, 
                                  timeout: int = 30, poll_frequency: float = 0.5) -> bool:
        """
        等待元素不可见
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            bool: 元素是否不可见
        """
        by_map = {
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH,
            "css_selector": By.CSS_SELECTOR
        }
        
        if by not in by_map:
            raise ValueError(f"不支持的定位方式: {by}")
        
        return WebDriverWait(driver, timeout, poll_frequency).until(
            EC.invisibility_of_element_located((by_map[by], value))
        )
    
    @staticmethod
    def click_element(driver: webdriver, by: str, value: str, 
                     timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        点击元素
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        element.click()
    
    @staticmethod
    def send_keys(driver: webdriver, by: str, value: str, text: str, 
                 timeout: int = 30, poll_frequency: float = 0.5, 
                 clear_first: bool = True) -> None:
        """
        输入文本
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            text (str): 要输入的文本
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            clear_first (bool): 是否先清空输入框
        """
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    @staticmethod
    def get_element_text(driver: webdriver, by: str, value: str, 
                        timeout: int = 30, poll_frequency: float = 0.5) -> str:
        """
        获取元素文本
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            str: 元素文本
        """
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        return element.text
    
    @staticmethod
    def get_element_attribute(driver: webdriver, by: str, value: str, attribute: str, 
                             timeout: int = 30, poll_frequency: float = 0.5) -> str:
        """
        获取元素属性
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            attribute (str): 属性名
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            str: 元素属性值
        """
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        return element.get_attribute(attribute)
    
    @staticmethod
    def is_element_present(driver: webdriver, by: str, value: str, 
                          timeout: int = 10, poll_frequency: float = 0.5) -> bool:
        """
        检查元素是否存在
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            bool: 元素是否存在
        """
        try:
            SeleniumUtils.find_element(driver, by, value, timeout, poll_frequency)
            return True
        except Exception:
            return False
    
    @staticmethod
    def is_element_visible(driver: webdriver, by: str, value: str, 
                          timeout: int = 10, poll_frequency: float = 0.5) -> bool:
        """
        检查元素是否可见
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
            
        Returns:
            bool: 元素是否可见
        """
        try:
            SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
            return True
        except Exception:
            return False
    
    @staticmethod
    def take_screenshot(driver: webdriver, save_path: Optional[str] = None, 
                       filename: Optional[str] = None) -> str:
        """
        截图
        
        Args:
            driver (webdriver): WebDriver实例
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
        driver.save_screenshot(screenshot_path)
        return screenshot_path
    
    @staticmethod
    def scroll_to_element(driver: webdriver, by: str, value: str, 
                         timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        滚动到元素位置
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        element = SeleniumUtils.find_element(driver, by, value, timeout, poll_frequency)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(1)  # 等待滚动完成
    
    @staticmethod
    def scroll_to_top(driver: webdriver) -> None:
        """
        滚动到页面顶部
        
        Args:
            driver (webdriver): WebDriver实例
        """
        driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
        time.sleep(1)
    
    @staticmethod
    def scroll_to_bottom(driver: webdriver) -> None:
        """
        滚动到页面底部
        
        Args:
            driver (webdriver): WebDriver实例
        """
        driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
        time.sleep(1)
    
    @staticmethod
    def switch_to_frame(driver: webdriver, by: str, value: str, 
                       timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        切换到iframe
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        element = SeleniumUtils.find_element(driver, by, value, timeout, poll_frequency)
        driver.switch_to.frame(element)
    
    @staticmethod
    def switch_to_default_content(driver: webdriver) -> None:
        """
        切换回默认内容
        
        Args:
            driver (webdriver): WebDriver实例
        """
        driver.switch_to.default_content()
    
    @staticmethod
    def switch_to_window(driver: webdriver, window_index: int = 1) -> None:
        """
        切换到指定窗口
        
        Args:
            driver (webdriver): WebDriver实例
            window_index (int): 窗口索引，从0开始
        """
        windows = driver.window_handles
        if window_index < len(windows):
            driver.switch_to.window(windows[window_index])
        else:
            raise IndexError(f"窗口索引 {window_index} 超出范围，当前只有 {len(windows)} 个窗口")
    
    @staticmethod
    def close_other_windows(driver: webdriver) -> None:
        """
        关闭其他窗口，只保留当前窗口
        
        Args:
            driver (webdriver): WebDriver实例
        """
        current_window = driver.current_window_handle
        for window in driver.window_handles:
            if window != current_window:
                driver.switch_to.window(window)
                driver.close()
        driver.switch_to.window(current_window)
    
    @staticmethod
    def wait_for_page_load(driver: webdriver, timeout: int = 60) -> None:
        """
        等待页面加载完成
        
        Args:
            driver (webdriver): WebDriver实例
            timeout (int): 超时时间（秒）
        """
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    
    @staticmethod
    def execute_javascript(driver: webdriver, script: str, *args) -> Any:
        """
        执行JavaScript
        
        Args:
            driver (webdriver): WebDriver实例
            script (str): JavaScript代码
            *args: 传递给JavaScript的参数
            
        Returns:
            Any: JavaScript执行结果
        """
        return driver.execute_script(script, *args)
    
    @staticmethod
    def hover_over_element(driver: webdriver, by: str, value: str, 
                         timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        鼠标悬停
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
    
    @staticmethod
    def double_click(driver: webdriver, by: str, value: str, 
                    timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        双击元素
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        actions = ActionChains(driver)
        actions.double_click(element).perform()
    
    @staticmethod
    def right_click(driver: webdriver, by: str, value: str, 
                   timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        右键点击
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        actions = ActionChains(driver)
        actions.context_click(element).perform()
    
    @staticmethod
    def drag_and_drop(driver: webdriver, source_by: str, source_value: str, 
                     target_by: str, target_value: str, 
                     timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        拖拽元素
        
        Args:
            driver (webdriver): WebDriver实例
            source_by (str): 源元素定位方式
            source_value (str): 源元素定位值
            target_by (str): 目标元素定位方式
            target_value (str): 目标元素定位值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        source_element = SeleniumUtils.wait_for_element_visible(driver, source_by, source_value, timeout, poll_frequency)
        target_element = SeleniumUtils.wait_for_element_visible(driver, target_by, target_value, timeout, poll_frequency)
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()
    
    @staticmethod
    def select_dropdown_by_visible_text(driver: webdriver, by: str, value: str, text: str, 
                                       timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        通过可见文本选择下拉框选项
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            text (str): 可见文本
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        from selenium.webdriver.support.ui import Select
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        select = Select(element)
        select.select_by_visible_text(text)
    
    @staticmethod
    def select_dropdown_by_value(driver: webdriver, by: str, value: str, option_value: str, 
                                timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        通过value属性选择下拉框选项
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            option_value (str): option的value属性值
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        from selenium.webdriver.support.ui import Select
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        select = Select(element)
        select.select_by_value(option_value)
    
    @staticmethod
    def select_dropdown_by_index(driver: webdriver, by: str, value: str, index: int, 
                                timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """
        通过索引选择下拉框选项
        
        Args:
            driver (webdriver): WebDriver实例
            by (str): 定位方式
            value (str): 定位值
            index (int): 选项索引
            timeout (int): 超时时间（秒）
            poll_frequency (float): 轮询频率（秒）
        """
        from selenium.webdriver.support.ui import Select
        element = SeleniumUtils.wait_for_element_visible(driver, by, value, timeout, poll_frequency)
        select = Select(element)
        select.select_by_index(index)
    
    @staticmethod
    def get_current_url(driver: webdriver) -> str:
        """
        获取当前页面URL
        
        Args:
            driver (webdriver): WebDriver实例
            
        Returns:
            str: 当前页面URL
        """
        return driver.current_url
    
    @staticmethod
    def get_page_title(driver: webdriver) -> str:
        """
        获取页面标题
        
        Args:
            driver (webdriver): WebDriver实例
            
        Returns:
            str: 页面标题
        """
        return driver.title
    
    @staticmethod
    def refresh_page(driver: webdriver) -> None:
        """
        刷新页面
        
        Args:
            driver (webdriver): WebDriver实例
        """
        driver.refresh()
    
    @staticmethod
    def navigate_back(driver: webdriver) -> None:
        """
        浏览器后退
        
        Args:
            driver (webdriver): WebDriver实例
        """
        driver.back()
    
    @staticmethod
    def navigate_forward(driver: webdriver) -> None:
        """
        浏览器前进
        
        Args:
            driver (webdriver): WebDriver实例
        """
        driver.forward()
    
    @staticmethod
    def close_driver(driver: webdriver) -> None:
        """
        关闭WebDriver
        
        Args:
            driver (webdriver): WebDriver实例
        """
        try:
            driver.quit()
        except Exception as e:
            print(f"关闭WebDriver时出错: {e}")

class SeleniumElement:
    """
    Selenium元素包装类，提供更便捷的元素操作方法
    """
    
    def __init__(self, driver: webdriver, by: str, value: str):
        """
        初始化SeleniumElement
        
        Args:
            driver (webdriver): WebDriver实例
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
            self._element = SeleniumUtils.find_element(self.driver, self.by, self.value)
        return self._element
    
    def click(self) -> None:
        """
        点击元素
        """
        SeleniumUtils.click_element(self.driver, self.by, self.value)
    
    def send_keys(self, text: str, clear_first: bool = True) -> None:
        """
        输入文本
        
        Args:
            text (str): 要输入的文本
            clear_first (bool): 是否先清空输入框
        """
        SeleniumUtils.send_keys(self.driver, self.by, self.value, text, clear_first=clear_first)
    
    def get_text(self) -> str:
        """
        获取元素文本
        
        Returns:
            str: 元素文本
        """
        return SeleniumUtils.get_element_text(self.driver, self.by, self.value)
    
    def get_attribute(self, attribute: str) -> str:
        """
        获取元素属性
        
        Args:
            attribute (str): 属性名
            
        Returns:
            str: 元素属性值
        """
        return SeleniumUtils.get_element_attribute(self.driver, self.by, self.value, attribute)
    
    def is_visible(self) -> bool:
        """
        检查元素是否可见
        
        Returns:
            bool: 元素是否可见
        """
        return SeleniumUtils.is_element_visible(self.driver, self.by, self.value)
    
    def is_present(self) -> bool:
        """
        检查元素是否存在
        
        Returns:
            bool: 元素是否存在
        """
        return SeleniumUtils.is_element_present(self.driver, self.by, self.value)
    
    def scroll_to(self) -> None:
        """
        滚动到元素位置
        """
        SeleniumUtils.scroll_to_element(self.driver, self.by, self.value)
    
    def hover(self) -> None:
        """
        鼠标悬停
        """
        SeleniumUtils.hover_over_element(self.driver, self.by, self.value)
    
    def double_click(self) -> None:
        """
        双击元素
        """
        SeleniumUtils.double_click(self.driver, self.by, self.value)
    
    def right_click(self) -> None:
        """
        右键点击
        """
        SeleniumUtils.right_click(self.driver, self.by, self.value)