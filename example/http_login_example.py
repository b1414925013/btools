#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTTP客户端示例 - 实现登录和获取用户信息的接口调用流程

本示例展示如何使用HTTPClient类实现以下流程：
1. 调用登录接口获取access_token
2. 使用获取到的access_token调用获取用户信息接口
"""

from btools.core.network.httputils import HTTPClient


def main():
    """
    主函数，实现登录和获取用户信息的流程
    """
    # 基础URL
    base_url = "http://127.0.0.1:8000"
    
    # 创建HTTP客户端实例
    client = HTTPClient(base_url=base_url)
    
    try:
        # 1. 调用登录接口
        print("=== 调用登录接口 ===")
        login_url = "/api/system/login"
        login_data = {
            "username": "user",
            "password": "123456"
        }
        
        # 发送POST请求
        response = client.post(login_url, json=login_data)
        
        # 检查响应状态
        if response.status_code == 200:
            # 解析响应数据
            login_result = response.json()
            print(f"登录成功！响应数据: {login_result}")
            
            # 获取access_token
            access_token = login_result.get("access_token")
            if access_token:
                print(f"获取到的access_token: {access_token}")
                
                # 将access_token添加到全局headers中
                client.add_headers({"Authorization": f"Bearer {access_token}"})
                
                # 2. 调用获取用户信息接口
                print("\n=== 调用获取用户信息接口 ===")
                user_info_url = "/api/system/users/me"
                
                # 发送GET请求（自动带上Authorization头）
                user_info_response = client.get(user_info_url)
                
                # 检查响应状态
                if user_info_response.status_code == 200:
                    # 解析响应数据
                    user_info = user_info_response.json()
                    print(f"获取用户信息成功！用户信息: {user_info}")
                else:
                    print(f"获取用户信息失败，状态码: {user_info_response.status_code}")
                    print(f"响应内容: {user_info_response.text}")
            else:
                print("登录成功但未获取到access_token")
        else:
            print(f"登录失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text}")
            
    except Exception as e:
        print(f"发生错误: {str(e)}")
    finally:
        # 关闭客户端
        client.close()


if __name__ == "__main__":
    main()