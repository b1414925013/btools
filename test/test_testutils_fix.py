#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试testutils.py文件修复是否成功
"""

from btools.core.testutils import TestUtils

def test_random_string_with_length():
    """
    测试带有长度参数的随机字符串模板
    """
    print("测试带有长度参数的随机字符串模板...")
    
    # 测试模板
    test_data_template = {
        "username": "${random_string}",
        "email": "${random_email}",
        "phone": "${random_phone}",
        "register_date": "${random_date}",
        "profile": {
            "first_name": "${random_string:5}",
            "last_name": "${random_string:8}"
        }
    }
    
    try:
        generated_data = TestUtils.generate_test_data(test_data_template)
        print("✓ 模板数据生成成功")
        
        # 验证生成的数据
        print(f"生成的username: {generated_data['username']}")
        print(f"生成的email: {generated_data['email']}")
        print(f"生成的phone: {generated_data['phone']}")
        print(f"生成的register_date: {generated_data['register_date']}")
        print(f"生成的first_name: {generated_data['profile']['first_name']}")
        print(f"生成的last_name: {generated_data['profile']['last_name']}")
        
        # 验证长度是否正确
        first_name_length = len(generated_data['profile']['first_name'])
        last_name_length = len(generated_data['profile']['last_name'])
        
        print(f"first_name长度: {first_name_length}")
        print(f"last_name长度: {last_name_length}")
        
        if first_name_length == 5:
            print("✓ first_name长度正确")
        else:
            print(f"✗ first_name长度错误，期望5，实际{first_name_length}")
        
        if last_name_length == 8:
            print("✓ last_name长度正确")
        else:
            print(f"✗ last_name长度错误，期望8，实际{last_name_length}")
        
        print("\n测试成功完成！")
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")

if __name__ == "__main__":
    test_random_string_with_length()
