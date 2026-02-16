#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试Selenium中使用webdriver-manager自动管理浏览器驱动
"""

from btools.core.seleniumutils import SeleniumUtils

def test_webdriver_manager():
    """
    测试webdriver-manager自动管理浏览器驱动
    """
    print("测试Chrome浏览器驱动自动管理...")
    try:
        # 获取Chrome驱动
        driver = SeleniumUtils.get_driver(browser="chrome", headless=True)
        print("✓ Chrome驱动初始化成功")
        
        # 访问测试页面
        driver.get("https://www.baidu.com")
        print(f"✓ 成功访问百度首页，标题: {driver.title}")
        
        # 关闭驱动
        SeleniumUtils.close_driver(driver)
        print("✓ Chrome驱动关闭成功")
    except Exception as e:
        print(f"✗ Chrome驱动测试失败: {e}")
    
    print("\n测试Firefox浏览器驱动自动管理...")
    try:
        # 获取Firefox驱动
        driver = SeleniumUtils.get_driver(browser="firefox", headless=True)
        print("✓ Firefox驱动初始化成功")
        
        # 访问测试页面
        driver.get("https://www.baidu.com")
        print(f"✓ 成功访问百度首页，标题: {driver.title}")
        
        # 关闭驱动
        SeleniumUtils.close_driver(driver)
        print("✓ Firefox驱动关闭成功")
    except Exception as e:
        print(f"✗ Firefox驱动测试失败: {e}")
    
    print("\n测试Edge浏览器驱动自动管理...")
    try:
        # 获取Edge驱动
        driver = SeleniumUtils.get_driver(browser="edge", headless=True)
        print("✓ Edge驱动初始化成功")
        
        # 访问测试页面
        driver.get("https://www.baidu.com")
        print(f"✓ 成功访问百度首页，标题: {driver.title}")
        
        # 关闭驱动
        SeleniumUtils.close_driver(driver)
        print("✓ Edge驱动关闭成功")
    except Exception as e:
        print(f"✗ Edge驱动测试失败: {e}")

if __name__ == "__main__":
    test_webdriver_manager()
