from playwright.sync_api import sync_playwright, Page, Locator, Browser, BrowserContext
from typing import List, Optional, Dict, Any, Union
import os
from datetime import datetime

class PlaywrightUtils:
    """
    Playwright工具类，提供常用的Web自动化测试操作
    """
    
    @staticmethod
    def get_browser(browser: str = "chromium", headless: bool = False, 
                   slow_mo: int = 0, timeout: int = 30000) -> tuple:
        """
        获取Playwright浏览器实例
        
        Args:
            browser (str): 浏览器类型，支持 chromium, firefox, webkit
            headless (bool): 是否使用无头模式
            slow_mo (int): 操作延迟（毫秒）
            timeout (int): 默认超时时间（毫秒）
            
        Returns:
            tuple: (playwright, browser, context, page)
        """
        playwright = sync_playwright().start()
        
        if browser.lower() == "chromium":
            browser_instance = playwright.chromium.launch(
                headless=headless,
                slow_mo=slow_mo
            )
        elif browser.lower() == "firefox":
            browser_instance = playwright.firefox.launch(
                headless=headless,
                slow_mo=slow_mo
            )
        elif browser.lower() == "webkit":
            browser_instance = playwright.webkit.launch(
                headless=headless,
                slow_mo=slow_mo
            )
        else:
            raise ValueError(f"不支持的浏览器类型: {browser}")
        
        context = browser_instance.new_context(timeout=timeout)
        page = context.new_page()
        
        return playwright, browser_instance, context, page
    
    @staticmethod
    def find_locator(page: Page, locator: str, timeout: Optional[int] = None) -> Locator:
        """
        查找元素
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器，支持CSS、XPath等
            timeout (int): 超时时间（毫秒）
            
        Returns:
            Locator: 找到的元素定位器
        """
        return page.locator(locator, timeout=timeout)
    
    @staticmethod
    def wait_for_element(page: Page, locator: str, timeout: Optional[int] = None) -> None:
        """
        等待元素可见
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
        """
        page.locator(locator).wait_for(state="visible", timeout=timeout)
    
    @staticmethod
    def wait_for_element_hidden(page: Page, locator: str, timeout: Optional[int] = None) -> None:
        """
        等待元素隐藏
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
        """
        page.locator(locator).wait_for(state="hidden", timeout=timeout)
    
    @staticmethod
    def click_element(page: Page, locator: str, timeout: Optional[int] = None) -> None:
        """
        点击元素
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
        """
        page.locator(locator).click(timeout=timeout)
    
    @staticmethod
    def double_click_element(page: Page, locator: str, timeout: Optional[int] = None) -> None:
        """
        双击元素
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
        """
        page.locator(locator).dblclick(timeout=timeout)
    
    @staticmethod
    def right_click_element(page: Page, locator: str, timeout: Optional[int] = None) -> None:
        """
        右键点击元素
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
        """
        page.locator(locator).click(button="right", timeout=timeout)
    
    @staticmethod
    def send_keys(page: Page, locator: str, text: str, clear_first: bool = True, 
                 timeout: Optional[int] = None) -> None:
        """
        输入文本
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            text (str): 要输入的文本
            clear_first (bool): 是否先清空输入框
            timeout (int): 超时时间（毫秒）
        """
        if clear_first:
            page.locator(locator).fill("", timeout=timeout)
        page.locator(locator).fill(text, timeout=timeout)
    
    @staticmethod
    def get_element_text(page: Page, locator: str, timeout: Optional[int] = None) -> str:
        """
        获取元素文本
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
            
        Returns:
            str: 元素文本
        """
        return page.locator(locator).text_content(timeout=timeout)
    
    @staticmethod
    def get_element_attribute(page: Page, locator: str, attribute: str, 
                             timeout: Optional[int] = None) -> str:
        """
        获取元素属性
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            attribute (str): 属性名
            timeout (int): 超时时间（毫秒）
            
        Returns:
            str: 元素属性值
        """
        return page.locator(locator).get_attribute(attribute, timeout=timeout)
    
    @staticmethod
    def is_element_visible(page: Page, locator: str, timeout: Optional[int] = None) -> bool:
        """
        检查元素是否可见
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
            
        Returns:
            bool: 元素是否可见
        """
        try:
            page.locator(locator).wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False
    
    @staticmethod
    def is_element_hidden(page: Page, locator: str, timeout: Optional[int] = None) -> bool:
        """
        检查元素是否隐藏
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
            
        Returns:
            bool: 元素是否隐藏
        """
        try:
            page.locator(locator).wait_for(state="hidden", timeout=timeout)
            return True
        except Exception:
            return False
    
    @staticmethod
    def take_screenshot(page: Page, save_path: Optional[str] = None, 
                       filename: Optional[str] = None, full_page: bool = False) -> str:
        """
        截图
        
        Args:
            page (Page): Playwright Page实例
            save_path (str): 保存路径
            filename (str): 文件名
            full_page (bool): 是否截取整页
            
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
        page.screenshot(path=screenshot_path, full_page=full_page)
        return screenshot_path
    
    @staticmethod
    def scroll_to_element(page: Page, locator: str, timeout: Optional[int] = None) -> None:
        """
        滚动到元素位置
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
        """
        page.locator(locator).scroll_into_view_if_needed(timeout=timeout)
    
    @staticmethod
    def scroll_to_top(page: Page) -> None:
        """
        滚动到页面顶部
        
        Args:
            page (Page): Playwright Page实例
        """
        page.evaluate("window.scrollTo({top: 0, behavior: 'smooth'});")
    
    @staticmethod
    def scroll_to_bottom(page: Page) -> None:
        """
        滚动到页面底部
        
        Args:
            page (Page): Playwright Page实例
        """
        page.evaluate("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
    
    @staticmethod
    def switch_to_frame(page: Page, locator: str, timeout: Optional[int] = None) -> None:
        """
        切换到iframe
        
        Args:
            page (Page): Playwright Page实例
            locator (str): iframe定位器
            timeout (int): 超时时间（毫秒）
        """
        frame = page.frame_locator(locator)
        # 可以通过frame继续操作iframe内的元素
        return frame
    
    @staticmethod
    def switch_to_window(page: Page, index: int = 1) -> Page:
        """
        切换到指定窗口
        
        Args:
            page (Page): Playwright Page实例
            index (int): 窗口索引，从0开始
            
        Returns:
            Page: 切换后的Page实例
        """
        contexts = page.context.browser.contexts
        if contexts:
            pages = contexts[0].pages
            if index < len(pages):
                return pages[index]
            else:
                raise IndexError(f"窗口索引 {index} 超出范围，当前只有 {len(pages)} 个窗口")
        else:
            raise ValueError("没有可用的浏览器上下文")
    
    @staticmethod
    def close_other_windows(page: Page) -> None:
        """
        关闭其他窗口，只保留当前窗口
        
        Args:
            page (Page): Playwright Page实例
        """
        current_page = page
        for p in page.context.pages:
            if p != current_page:
                p.close()
    
    @staticmethod
    def wait_for_load_state(page: Page, state: str = "networkidle", 
                          timeout: Optional[int] = None) -> None:
        """
        等待页面加载状态
        
        Args:
            page (Page): Playwright Page实例
            state (str): 加载状态，支持 load, domcontentloaded, networkidle
            timeout (int): 超时时间（毫秒）
        """
        page.wait_for_load_state(state=state, timeout=timeout)
    
    @staticmethod
    def execute_javascript(page: Page, script: str, *args) -> Any:
        """
        执行JavaScript
        
        Args:
            page (Page): Playwright Page实例
            script (str): JavaScript代码
            *args: 传递给JavaScript的参数
            
        Returns:
            Any: JavaScript执行结果
        """
        return page.evaluate(script, args)
    
    @staticmethod
    def hover_over_element(page: Page, locator: str, timeout: Optional[int] = None) -> None:
        """
        鼠标悬停
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
            timeout (int): 超时时间（毫秒）
        """
        page.locator(locator).hover(timeout=timeout)
    
    @staticmethod
    def drag_and_drop(page: Page, source_locator: str, target_locator: str, 
                     timeout: Optional[int] = None) -> None:
        """
        拖拽元素
        
        Args:
            page (Page): Playwright Page实例
            source_locator (str): 源元素定位器
            target_locator (str): 目标元素定位器
            timeout (int): 超时时间（毫秒）
        """
        page.locator(source_locator).drag_to(
            page.locator(target_locator),
            timeout=timeout
        )
    
    @staticmethod
    def select_dropdown_option(page: Page, locator: str, option: Union[str, int], 
                              timeout: Optional[int] = None) -> None:
        """
        选择下拉框选项
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 下拉框定位器
            option (str or int): 选项值或索引
            timeout (int): 超时时间（毫秒）
        """
        if isinstance(option, int):
            page.locator(locator).select_option(index=option, timeout=timeout)
        else:
            page.locator(locator).select_option(option, timeout=timeout)
    
    @staticmethod
    def get_current_url(page: Page) -> str:
        """
        获取当前页面URL
        
        Args:
            page (Page): Playwright Page实例
            
        Returns:
            str: 当前页面URL
        """
        return page.url
    
    @staticmethod
    def get_page_title(page: Page) -> str:
        """
        获取页面标题
        
        Args:
            page (Page): Playwright Page实例
            
        Returns:
            str: 页面标题
        """
        return page.title()
    
    @staticmethod
    def refresh_page(page: Page) -> None:
        """
        刷新页面
        
        Args:
            page (Page): Playwright Page实例
        """
        page.reload()
    
    @staticmethod
    def navigate_back(page: Page) -> None:
        """
        浏览器后退
        
        Args:
            page (Page): Playwright Page实例
        """
        page.go_back()
    
    @staticmethod
    def navigate_forward(page: Page) -> None:
        """
        浏览器前进
        
        Args:
            page (Page): Playwright Page实例
        """
        page.go_forward()
    
    @staticmethod
    def fill_form(page: Page, form_data: Dict[str, str], timeout: Optional[int] = None) -> None:
        """
        填充表单
        
        Args:
            page (Page): Playwright Page实例
            form_data (dict): 表单数据，键为定位器，值为要填写的内容
            timeout (int): 超时时间（毫秒）
        """
        for locator, value in form_data.items():
            page.locator(locator).fill(value, timeout=timeout)
    
    @staticmethod
    def wait_for_navigation(page: Page, timeout: Optional[int] = None) -> None:
        """
        等待导航完成
        
        Args:
            page (Page): Playwright Page实例
            timeout (int): 超时时间（毫秒）
        """
        page.wait_for_url("*", timeout=timeout)
    
    @staticmethod
    def close_browser(playwright, browser, context=None) -> None:
        """
        关闭浏览器
        
        Args:
            playwright: Playwright实例
            browser: Browser实例
            context: BrowserContext实例
        """
        try:
            if context:
                context.close()
            if browser:
                browser.close()
            if playwright:
                playwright.stop()
        except Exception as e:
            print(f"关闭浏览器时出错: {e}")

class PlaywrightElement:
    """
    Playwright元素包装类，提供更便捷的元素操作方法
    """
    
    def __init__(self, page: Page, locator: str):
        """
        初始化PlaywrightElement
        
        Args:
            page (Page): Playwright Page实例
            locator (str): 定位器
        """
        self.page = page
        self.locator = locator
    
    def click(self, timeout: Optional[int] = None) -> None:
        """
        点击元素
        
        Args:
            timeout (int): 超时时间（毫秒）
        """
        PlaywrightUtils.click_element(self.page, self.locator, timeout)
    
    def double_click(self, timeout: Optional[int] = None) -> None:
        """
        双击元素
        
        Args:
            timeout (int): 超时时间（毫秒）
        """
        PlaywrightUtils.double_click_element(self.page, self.locator, timeout)
    
    def right_click(self, timeout: Optional[int] = None) -> None:
        """
        右键点击元素
        
        Args:
            timeout (int): 超时时间（毫秒）
        """
        PlaywrightUtils.right_click_element(self.page, self.locator, timeout)
    
    def send_keys(self, text: str, clear_first: bool = True, 
                 timeout: Optional[int] = None) -> None:
        """
        输入文本
        
        Args:
            text (str): 要输入的文本
            clear_first (bool): 是否先清空输入框
            timeout (int): 超时时间（毫秒）
        """
        PlaywrightUtils.send_keys(self.page, self.locator, text, clear_first, timeout)
    
    def get_text(self, timeout: Optional[int] = None) -> str:
        """
        获取元素文本
        
        Args:
            timeout (int): 超时时间（毫秒）
            
        Returns:
            str: 元素文本
        """
        return PlaywrightUtils.get_element_text(self.page, self.locator, timeout)
    
    def get_attribute(self, attribute: str, timeout: Optional[int] = None) -> str:
        """
        获取元素属性
        
        Args:
            attribute (str): 属性名
            timeout (int): 超时时间（毫秒）
            
        Returns:
            str: 元素属性值
        """
        return PlaywrightUtils.get_element_attribute(self.page, self.locator, attribute, timeout)
    
    def is_visible(self, timeout: Optional[int] = None) -> bool:
        """
        检查元素是否可见
        
        Args:
            timeout (int): 超时时间（毫秒）
            
        Returns:
            bool: 元素是否可见
        """
        return PlaywrightUtils.is_element_visible(self.page, self.locator, timeout)
    
    def is_hidden(self, timeout: Optional[int] = None) -> bool:
        """
        检查元素是否隐藏
        
        Args:
            timeout (int): 超时时间（毫秒）
            
        Returns:
            bool: 元素是否隐藏
        """
        return PlaywrightUtils.is_element_hidden(self.page, self.locator, timeout)
    
    def scroll_to(self, timeout: Optional[int] = None) -> None:
        """
        滚动到元素位置
        
        Args:
            timeout (int): 超时时间（毫秒）
        """
        PlaywrightUtils.scroll_to_element(self.page, self.locator, timeout)
    
    def hover(self, timeout: Optional[int] = None) -> None:
        """
        鼠标悬停
        
        Args:
            timeout (int): 超时时间（毫秒）
        """
        PlaywrightUtils.hover_over_element(self.page, self.locator, timeout)
    
    def wait_for(self, state: str = "visible", timeout: Optional[int] = None) -> None:
        """
        等待元素状态
        
        Args:
            state (str): 状态，支持 visible, hidden, attached
            timeout (int): 超时时间（毫秒）
        """
        self.page.locator(self.locator).wait_for(state=state, timeout=timeout)