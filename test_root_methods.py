"""
测试 SSHClient 的两种 root 权限执行方法

此脚本演示了两种执行 root 命令的方法：
1. execute_as_root - 直接执行 root 命令
2. 保持 root shell 会话 - 启动一次 root shell，多次执行命令
"""

import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from btools.core.network.sshutils import SSHClient


def test_execute_as_root():
    """
    测试 execute_as_root 方法
    """
    print("=" * 60)
    print("测试方法一：execute_as_root - 直接执行 root 命令")
    print("=" * 60)
    
    # 创建SSH客户端实例
    ssh = SSHClient()
    
    try:
        # 连接到服务器（请根据实际情况修改）
        print("\n正在连接到服务器...")
        ssh.connect(
            hostname="192.168.1.100",  # 请修改为实际的服务器地址
            username="user",            # 请修改为实际的用户名
            password="user_password"    # 请修改为实际的密码
        )
        print("连接成功！")
        
        # 测试1：执行单条 root 命令
        print("\n--- 测试1：执行单条 root 命令 ---")
        result = ssh.execute_as_root('whoami', root_password='root_password')
        print(f"命令: whoami")
        print(f"输出: {result['stdout'].strip()}")
        print(f"返回码: {result['returncode']}")
        print(f"错误: {result['stderr']}")
        
        # 测试2：执行多条 root 命令
        print("\n--- 测试2：执行多条 root 命令 ---")
        commands = [
            'whoami',
            'pwd',
            'ls -la /root',
            'cat /etc/passwd | head -5'
        ]
        
        for cmd in commands:
            result = ssh.execute_as_root(cmd, root_password='root_password')
            print(f"\n命令: {cmd}")
            print(f"输出: {result['stdout'].strip()[:100]}...")
            print(f"返回码: {result['returncode']}")
        
        # 测试3：执行系统管理命令
        print("\n--- 测试3：执行系统管理命令 ---")
        result = ssh.execute_as_root('systemctl status sshd', root_password='root_password')
        print(f"命令: systemctl status sshd")
        print(f"输出（前200字符）: {result['stdout'][:200]}...")
        print(f"返回码: {result['returncode']}")
        
        print("\n✓ execute_as_root 方法测试完成")
        
    except Exception as e:
        print(f"\n✗ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 关闭连接
        ssh.close()
        print("\nSSH 连接已关闭")


def test_root_shell_session():
    """
    测试保持 root shell 会话的方法
    """
    print("\n" + "=" * 60)
    print("测试方法二：保持 root shell 会话")
    print("=" * 60)
    
    # 创建SSH客户端实例
    ssh = SSHClient()
    
    try:
        # 连接到服务器（请根据实际情况修改）
        print("\n正在连接到服务器...")
        ssh.connect(
            hostname="192.168.1.100",  # 请修改为实际的服务器地址
            username="user",            # 请修改为实际的用户名
            password="user_password"    # 请修改为实际的密码
        )
        print("连接成功！")
        
        # 启动 root shell 会话
        print("\n--- 启动 root shell 会话 ---")
        result = ssh.start_root_shell('root_password')
        
        if not result['success']:
            print(f"✗ 启动 root shell 失败: {result['stderr']}")
            return
        
        print("✓ root shell 启动成功")
        print(f"当前用户: {result['current_user']}")
        
        # 测试1：执行单条命令
        print("\n--- 测试1：执行单条命令 ---")
        result = ssh.execute_in_root_shell('whoami')
        print(f"命令: whoami")
        print(f"输出: {result['stdout'].strip()}")
        print(f"成功: {result['success']}")
        
        # 测试2：测试会话状态保持（工作目录）
        print("\n--- 测试2：测试会话状态保持（工作目录）---")
        result1 = ssh.execute_in_root_shell('cd /tmp')
        print(f"命令: cd /tmp")
        print(f"成功: {result1['success']}")
        
        result2 = ssh.execute_in_root_shell('pwd')
        print(f"命令: pwd")
        print(f"输出: {result2['stdout'].strip()}")
        print(f"成功: {result2['success']}")
        
        # 测试3：执行多条命令
        print("\n--- 测试3：执行多条命令 ---")
        commands = [
            'whoami',
            'pwd',
            'ls -la /root',
            'cat /etc/passwd | head -5'
        ]
        
        for cmd in commands:
            result = ssh.execute_in_root_shell(cmd)
            print(f"\n命令: {cmd}")
            print(f"输出: {result['stdout'].strip()[:100]}...")
            print(f"成功: {result['success']}")
        
        # 测试4：执行系统管理命令
        print("\n--- 测试4：执行系统管理命令 ---")
        result = ssh.execute_in_root_shell('systemctl status sshd')
        print(f"命令: systemctl status sshd")
        print(f"输出（前200字符）: {result['stdout'][:200]}...")
        print(f"成功: {result['success']}")
        
        # 关闭 root shell
        print("\n--- 关闭 root shell 会话 ---")
        ssh.close_root_shell()
        print("✓ root shell 已关闭")
        
        print("\n✓ 保持 root shell 会话方法测试完成")
        
    except Exception as e:
        print(f"\n✗ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 关闭连接
        ssh.close()
        print("\nSSH 连接已关闭")


def compare_methods():
    """
    对比两种方法的性能和特点
    """
    print("\n" + "=" * 60)
    print("对比两种方法")
    print("=" * 60)
    
    import time
    
    # 创建SSH客户端实例
    ssh = SSHClient()
    
    try:
        # 连接到服务器（请根据实际情况修改）
        print("\n正在连接到服务器...")
        ssh.connect(
            hostname="192.168.1.100",  # 请修改为实际的服务器地址
            username="user",            # 请修改为实际的用户名
            password="user_password"    # 请修改为实际的密码
        )
        print("连接成功！")
        
        # 测试 execute_as_root 的性能
        print("\n--- 测试 execute_as_root 性能 ---")
        commands = ['whoami', 'pwd', 'ls -la /root']
        
        start_time = time.time()
        for cmd in commands:
            ssh.execute_as_root(cmd, root_password='root_password')
        end_time = time.time()
        
        execute_time = end_time - start_time
        print(f"执行 {len(commands)} 条命令耗时: {execute_time:.2f} 秒")
        print(f"平均每条命令: {execute_time/len(commands):.2f} 秒")
        
        # 测试保持 root shell 会话的性能
        print("\n--- 测试保持 root shell 会话性能 ---")
        ssh.start_root_shell('root_password')
        
        start_time = time.time()
        for cmd in commands:
            ssh.execute_in_root_shell(cmd)
        end_time = time.time()
        
        shell_time = end_time - start_time
        print(f"执行 {len(commands)} 条命令耗时: {shell_time:.2f} 秒")
        print(f"平均每条命令: {shell_time/len(commands):.2f} 秒")
        
        # 关闭 root shell
        ssh.close_root_shell()
        
        # 性能对比
        print("\n--- 性能对比 ---")
        print(f"execute_as_root 总耗时: {execute_time:.2f} 秒")
        print(f"保持 root shell 会话总耗时: {shell_time:.2f} 秒")
        print(f"性能提升: {(execute_time - shell_time) / execute_time * 100:.1f}%")
        
        print("\n✓ 性能对比测试完成")
        
    except Exception as e:
        print(f"\n✗ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 关闭连接
        ssh.close()
        print("\nSSH 连接已关闭")


def main():
    """
    主函数
    """
    print("\n" + "=" * 60)
    print("SSHClient Root 权限执行方法测试")
    print("=" * 60)
    print("\n请确保以下配置正确：")
    print("1. 服务器地址、用户名、密码")
    print("2. root 用户密码")
    print("3. 服务器支持 su 命令")
    print("\n注意：请修改脚本中的连接信息后再运行！")
    print("=" * 60)
    
    # 询问用户要运行哪些测试
    print("\n请选择要运行的测试：")
    print("1. 测试 execute_as_root 方法")
    print("2. 测试保持 root shell 会话方法")
    print("3. 对比两种方法的性能")
    print("4. 运行所有测试")
    print("0. 退出")
    
    choice = input("\n请输入选项 (0-4): ").strip()
    
    if choice == '1':
        test_execute_as_root()
    elif choice == '2':
        test_root_shell_session()
    elif choice == '3':
        compare_methods()
    elif choice == '4':
        test_execute_as_root()
        test_root_shell_session()
        compare_methods()
    elif choice == '0':
        print("退出测试")
        return
    else:
        print("无效的选项")
    
    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)


if __name__ == "__main__":
    main()