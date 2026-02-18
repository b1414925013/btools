#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RuntimeUtil 测试文件
"""
import os
import subprocess
import sys
import time
import unittest
from btools.core.basic import RuntimeUtil


class TestRuntimeUtil(unittest.TestCase):
    """
    RuntimeUtil 测试类
    """

    def test_exec(self):
        """
        测试执行命令并返回结果
        """
        # 测试简单命令
        if RuntimeUtil.isWindows():
            cmd = "echo hello"
        else:
            cmd = "echo hello"
        
        returncode, stdout, stderr = RuntimeUtil.exec(cmd)
        self.assertEqual(returncode, 0)
        self.assertIn("hello", stdout)
        self.assertEqual(stderr, "")

    def test_execForStr(self):
        """
        测试执行命令并返回标准输出
        """
        if RuntimeUtil.isWindows():
            cmd = "echo hello"
        else:
            cmd = "echo hello"
        
        output = RuntimeUtil.execForStr(cmd)
        self.assertEqual(output, "hello")

    def test_execForLines(self):
        """
        测试执行命令并返回标准输出的行列表
        """
        if RuntimeUtil.isWindows():
            cmd = "echo hello && echo world"
        else:
            cmd = "echo hello; echo world"
        
        lines = RuntimeUtil.execForLines(cmd)
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], "hello")
        self.assertEqual(lines[1], "world")

    def test_execWait(self):
        """
        测试执行命令并等待完成，返回是否执行成功
        """
        if RuntimeUtil.isWindows():
            cmd = "echo hello"
        else:
            cmd = "echo hello"
        
        success = RuntimeUtil.execWait(cmd)
        self.assertTrue(success)

    def test_execAsync(self):
        """
        测试异步执行命令，返回进程对象
        """
        if RuntimeUtil.isWindows():
            cmd = "echo hello"
        else:
            cmd = "echo hello"
        
        process = RuntimeUtil.execAsync(cmd)
        self.assertIsNotNone(process)
        
        # 等待进程完成
        process.wait()

    def test_getProcessOutput(self):
        """
        测试获取进程的输出
        """
        if RuntimeUtil.isWindows():
            cmd = "echo hello"
        else:
            cmd = "echo hello"
        
        process = RuntimeUtil.execAsync(cmd)
        stdout, stderr = RuntimeUtil.getProcessOutput(process)
        
        self.assertEqual(stdout, "hello")
        self.assertEqual(stderr, "")

    def test_getSystemInfo(self):
        """
        测试获取系统信息
        """
        system_info = RuntimeUtil.getSystemInfo()
        self.assertIsInstance(system_info, dict)
        self.assertIn("system", system_info)
        self.assertIn("release", system_info)
        self.assertIn("version", system_info)
        self.assertIn("machine", system_info)
        self.assertIn("processor", system_info)
        self.assertIn("python_version", system_info)
        self.assertIn("python_implementation", system_info)
        self.assertIn("python_compiler", system_info)
        self.assertIn("os_name", system_info)

    def test_getRuntimeInfo(self):
        """
        测试获取运行时信息
        """
        runtime_info = RuntimeUtil.getRuntimeInfo()
        self.assertIsInstance(runtime_info, dict)
        self.assertIn("cwd", runtime_info)
        self.assertIn("pid", runtime_info)
        self.assertIn("ppid", runtime_info)
        self.assertIn("python_path", runtime_info)
        self.assertIn("python_version", runtime_info)
        self.assertIn("sys_platform", runtime_info)
        self.assertIn("argv", runtime_info)
        self.assertIn("env", runtime_info)

    def test_env_operations(self):
        """
        测试环境变量操作
        """
        # 测试获取不存在的环境变量
        value = RuntimeUtil.getEnv("TEST_ENV_VAR", "default")
        self.assertEqual(value, "default")

        # 测试设置环境变量
        RuntimeUtil.setEnv("TEST_ENV_VAR", "test_value")
        value = RuntimeUtil.getEnv("TEST_ENV_VAR")
        self.assertEqual(value, "test_value")

        # 测试移除环境变量
        RuntimeUtil.unsetEnv("TEST_ENV_VAR")
        value = RuntimeUtil.getEnv("TEST_ENV_VAR")
        self.assertIsNone(value)

    def test_getOsName(self):
        """
        测试获取操作系统名称
        """
        os_name = RuntimeUtil.getOsName()
        self.assertIsInstance(os_name, str)

    def test_os_detection(self):
        """
        测试操作系统检测
        """
        is_windows = RuntimeUtil.isWindows()
        is_linux = RuntimeUtil.isLinux()
        is_mac = RuntimeUtil.isMac()
        
        # 确保只有一个操作系统检测为True
        os_count = sum([is_windows, is_linux, is_mac])
        self.assertEqual(os_count, 1)

    def test_runScript(self):
        """
        测试运行脚本文件
        """
        # 创建临时Python脚本
        script_content = "print('Hello from script')"
        script_path = "test_script.py"
        
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(script_content)
        
        try:
            # 运行脚本
            returncode, stdout, stderr = RuntimeUtil.runScript(script_path)
            self.assertEqual(returncode, 0)
            self.assertEqual(stdout, "Hello from script")
            self.assertEqual(stderr, "")
        finally:
            # 清理临时文件
            if os.path.exists(script_path):
                os.remove(script_path)

    def test_sleep(self):
        """
        测试线程休眠
        """
        start_time = time.time()
        RuntimeUtil.sleep(0.1)  # 休眠0.1秒
        end_time = time.time()
        
        # 确保至少休眠了0.05秒
        self.assertGreaterEqual(end_time - start_time, 0.05)

    def test_killProcess(self):
        """
        测试终止指定进程
        """
        # 创建一个会休眠的进程
        if RuntimeUtil.isWindows():
            cmd = "timeout 1"
        else:
            cmd = "sleep 1"
        
        process = RuntimeUtil.execAsync(cmd)
        self.assertIsNotNone(process)
        
        # 等待一小段时间确保进程已启动
        time.sleep(0.1)
        
        # 终止进程
        success = RuntimeUtil.killProcess(process.pid)
        self.assertTrue(success)
        
        # 等待进程终止
        process.wait()


if __name__ == '__main__':
    unittest.main()