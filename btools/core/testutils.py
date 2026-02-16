import os
import json
import yaml
import random
import string
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Union

class TestUtils:
    """
    自动化测试工具类，提供测试数据生成、测试报告生成等功能
    """
    
    @staticmethod
    def generate_random_string(length: int = 10, include_special: bool = False) -> str:
        """
        生成随机字符串
        
        Args:
            length (int): 字符串长度，默认为10
            include_special (bool): 是否包含特殊字符，默认为False
            
        Returns:
            str: 生成的随机字符串
        """
        chars = string.ascii_letters + string.digits
        if include_special:
            chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))
    
    @staticmethod
    def generate_random_email(domain: str = "example.com") -> str:
        """
        生成随机邮箱地址
        
        Args:
            domain (str): 邮箱域名，默认为example.com
            
        Returns:
            str: 生成的随机邮箱地址
        """
        username = TestUtils.generate_random_string(8)
        return f"{username}@{domain}"
    
    @staticmethod
    def generate_random_phone(prefix: str = "138") -> str:
        """
        生成随机手机号码
        
        Args:
            prefix (str): 手机号前缀，默认为138
            
        Returns:
            str: 生成的随机手机号码
        """
        suffix = ''.join(random.choice(string.digits) for _ in range(8))
        return f"{prefix}{suffix}"
    
    @staticmethod
    def generate_random_date(start_date: Optional[str] = None, end_date: Optional[str] = None, 
                          format: str = "%Y-%m-%d") -> str:
        """
        生成随机日期
        
        Args:
            start_date (str): 开始日期，默认为当前日期
            end_date (str): 结束日期，默认为当前日期后一年
            format (str): 日期格式，默认为%Y-%m-%d
            
        Returns:
            str: 生成的随机日期字符串
        """
        if start_date:
            start = datetime.strptime(start_date, format)
        else:
            start = datetime.now()
        
        if end_date:
            end = datetime.strptime(end_date, format)
        else:
            end = start + timedelta(days=365)
        
        delta = end - start
        random_days = random.randint(0, delta.days)
        random_date = start + timedelta(days=random_days)
        
        return random_date.strftime(format)
    
    @staticmethod
    def generate_test_data(template: Dict[str, Any]) -> Dict[str, Any]:
        """
        根据模板生成测试数据
        
        Args:
            template (dict): 测试数据模板，支持特殊标记
            
        Returns:
            dict: 生成的测试数据
        """
        def process_value(value):
            if isinstance(value, dict):
                return {k: process_value(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [process_value(item) for item in value]
            elif isinstance(value, str):
                if value == "${random_string}":
                    return TestUtils.generate_random_string()
                elif value == "${random_email}":
                    return TestUtils.generate_random_email()
                elif value == "${random_phone}":
                    return TestUtils.generate_random_phone()
                elif value == "${random_date}":
                    return TestUtils.generate_random_date()
                elif value.startswith("${random_string:") and value.endswith(")}":
                    length = int(value.split(":")[1].rstrip(")}"))
                    return TestUtils.generate_random_string(length)
            return value
        
        return process_value(template)
    
    @staticmethod
    def load_test_config(config_path: str) -> Dict[str, Any]:
        """
        加载测试配置文件
        
        Args:
            config_path (str): 配置文件路径，支持json和yaml格式
            
        Returns:
            dict: 配置数据
        """
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"配置文件不存在: {config_path}")
        
        ext = os.path.splitext(config_path)[1].lower()
        
        with open(config_path, 'r', encoding='utf-8') as f:
            if ext in ['.json']:
                return json.load(f)
            elif ext in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            else:
                raise ValueError(f"不支持的配置文件格式: {ext}")
    
    @staticmethod
    def save_test_results(results: Dict[str, Any], output_path: str, format: str = "json") -> str:
        """
        保存测试结果
        
        Args:
            results (dict): 测试结果数据
            output_path (str): 输出文件路径
            format (str): 输出格式，支持json和yaml，默认为json
            
        Returns:
            str: 保存的文件路径
        """
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            if format.lower() == "json":
                json.dump(results, f, ensure_ascii=False, indent=2)
            elif format.lower() == "yaml":
                yaml.dump(results, f, allow_unicode=True, default_flow_style=False)
            else:
                raise ValueError(f"不支持的输出格式: {format}")
        
        return output_path
    
    @staticmethod
    def generate_test_report(test_cases: List[Dict[str, Any]], output_path: str = "test_report.html") -> str:
        """
        生成HTML测试报告
        
        Args:
            test_cases (list): 测试用例结果列表
            output_path (str): 报告输出路径
            
        Returns:
            str: 生成的报告文件路径
        """
        # 统计测试结果
        total = len(test_cases)
        passed = sum(1 for case in test_cases if case.get("status") == "PASS")
        failed = sum(1 for case in test_cases if case.get("status") == "FAIL")
        skipped = sum(1 for case in test_cases if case.get("status") == "SKIP")
        
        # 生成HTML报告
        html_template = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>测试报告</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background-color: #3498db;
            color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .summary {{
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .summary-item {{
            display: inline-block;
            margin: 0 20px 0 0;
        }}
        .test-cases {{
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .test-case {{
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 10px;
        }}
        .test-case.PASS {{
            border-left: 5px solid #27ae60;
        }}
        .test-case.FAIL {{
            border-left: 5px solid #e74c3c;
        }}
        .test-case.SKIP {{
            border-left: 5px solid #f39c12;
        }}
        .test-case h3 {{
            margin-top: 0;
        }}
        .test-case .meta {{
            font-size: 12px;
            color: #666;
            margin-bottom: 10px;
        }}
        .test-case .error {{
            background-color: #ffebee;
            padding: 10px;
            border-radius: 3px;
            margin-top: 10px;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>测试报告</h1>
        <p>生成时间: {generate_time}</p>
    </div>
    
    <div class="summary">
        <h2>测试摘要</h2>
        <div class="summary-item">
            <strong>总用例数:</strong> {total}
        </div>
        <div class="summary-item">
            <strong>通过:</strong> <span style="color: #27ae60;">{passed}</span>
        </div>
        <div class="summary-item">
            <strong>失败:</strong> <span style="color: #e74c3c;">{failed}</span>
        </div>
        <div class="summary-item">
            <strong>跳过:</strong> <span style="color: #f39c12;">{skipped}</span>
        </div>
        <div class="summary-item">
            <strong>通过率:</strong> {pass_rate:.2f}%
        </div>
    </div>
    
    <div class="test-cases">
        <h2>测试用例详情</h2>
        {test_cases_html}
    </div>
</body>
</html>
        """
        
        # 生成测试用例HTML
        test_cases_html = ""
        for case in test_cases:
            status = case.get("status", "UNKNOWN")
            error = case.get("error", "")
            
            case_html = f"""
            <div class="test-case {status}">
                <h3>{case.get('name', 'Unnamed Test')}</h3>
                <div class="meta">
                    <strong>状态:</strong> {status} | 
                    <strong>开始时间:</strong> {case.get('start_time', '-')} | 
                    <strong>结束时间:</strong> {case.get('end_time', '-')} | 
                    <strong>耗时:</strong> {case.get('duration', '-')}s
                </div>
                <p><strong>描述:</strong> {case.get('description', '-')}</p>
                {f'<div class="error"><strong>错误信息:</strong><br>{error}</div>' if error else ''}
            </div>
            """
            test_cases_html += case_html
        
        # 计算通过率
        pass_rate = (passed / total * 100) if total > 0 else 0
        
        # 填充模板
        generate_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html_content = html_template.format(
            generate_time=generate_time,
            total=total,
            passed=passed,
            failed=failed,
            skipped=skipped,
            pass_rate=pass_rate,
            test_cases_html=test_cases_html
        )
        
        # 保存报告
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return output_path
    
    @staticmethod
    def wait_for_element(timeout: int = 30, poll_interval: float = 0.5) -> callable:
        """
        等待元素出现的装饰器
        
        Args:
            timeout (int): 超时时间，单位秒
            poll_interval (float): 轮询间隔，单位秒
            
        Returns:
            callable: 装饰器函数
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                import time
                start_time = time.time()
                last_error = None
                
                while time.time() - start_time < timeout:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_error = e
                        time.sleep(poll_interval)
                
                raise TimeoutError(f"等待元素超时 ({timeout}s): {last_error}")
            return wrapper
        return decorator

class AssertEnhancer:
    """
    断言增强类，提供更强大的断言方法
    """
    
    @staticmethod
    def assert_contains(actual: str, expected: str, message: str = None):
        """
        断言字符串包含
        
        Args:
            actual (str): 实际值
            expected (str): 期望值
            message (str): 断言失败消息
            
        Raises:
            AssertionError: 断言失败时抛出
        """
        if expected not in actual:
            msg = message or f"字符串 '{actual}' 不包含 '{expected}'"
            raise AssertionError(msg)
    
    @staticmethod
    def assert_json_equals(actual: Union[Dict, str], expected: Union[Dict, str], message: str = None):
        """
        断言JSON相等
        
        Args:
            actual (dict或str): 实际JSON
            expected (dict或str): 期望JSON
            message (str): 断言失败消息
            
        Raises:
            AssertionError: 断言失败时抛出
        """
        def to_dict(obj):
            if isinstance(obj, str):
                return json.loads(obj)
            return obj
        
        actual_dict = to_dict(actual)
        expected_dict = to_dict(expected)
        
        if actual_dict != expected_dict:
            msg = message or f"JSON不相等: 实际={actual_dict}, 期望={expected_dict}"
            raise AssertionError(msg)
    
    @staticmethod
    def assert_response_status(response, expected_status: int, message: str = None):
        """
        断言HTTP响应状态码
        
        Args:
            response: HTTP响应对象
            expected_status (int): 期望状态码
            message (str): 断言失败消息
            
        Raises:
            AssertionError: 断言失败时抛出
        """
        if hasattr(response, 'status_code'):
            actual_status = response.status_code
        else:
            raise ValueError("响应对象没有status_code属性")
        
        if actual_status != expected_status:
            msg = message or f"状态码不匹配: 实际={actual_status}, 期望={expected_status}"
            # 尝试获取响应内容作为错误信息的一部分
            try:
                if hasattr(response, 'text'):
                    msg += f"\n响应内容: {response.text[:500]}..."
            except:
                pass
            raise AssertionError(msg)
    
    @staticmethod
    def assert_response_json(response, expected_json: Dict, message: str = None):
        """
        断言HTTP响应JSON
        
        Args:
            response: HTTP响应对象
            expected_json (dict): 期望JSON
            message (str): 断言失败消息
            
        Raises:
            AssertionError: 断言失败时抛出
        """
        try:
            actual_json = response.json()
        except Exception as e:
            raise AssertionError(f"无法解析响应为JSON: {e}")
        
        # 递归比较JSON
        def compare_json(actual, expected, path=""):
            if isinstance(expected, dict):
                if not isinstance(actual, dict):
                    return f"路径 '{path}' 期望dict，实际是 {type(actual)}"
                
                for key, value in expected.items():
                    new_path = f"{path}.{key}" if path else key
                    if key not in actual:
                        return f"路径 '{new_path}' 在实际JSON中不存在"
                    
                    error = compare_json(actual[key], value, new_path)
                    if error:
                        return error
            elif isinstance(expected, list):
                if not isinstance(actual, list):
                    return f"路径 '{path}' 期望list，实际是 {type(actual)}"
                
                if len(actual) != len(expected):
                    return f"路径 '{path}' 列表长度不匹配: 实际={len(actual)}, 期望={len(expected)}"
                
                for i, (a, e) in enumerate(zip(actual, expected)):
                    new_path = f"{path}[{i}]"
                    error = compare_json(a, e, new_path)
                    if error:
                        return error
            else:
                if actual != expected:
                    return f"路径 '{path}' 值不匹配: 实际={actual}, 期望={expected}"
            
            return None
        
        error = compare_json(actual_json, expected_json)
        if error:
            msg = message or f"响应JSON不匹配: {error}"
            raise AssertionError(msg)