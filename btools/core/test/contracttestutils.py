#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
契约测试工具类

提供契约测试工具，确保服务间接口一致性等功能
"""
import json
import os
import hashlib
from typing import Dict, Any, List, Optional, Callable


class ContractTestUtils:
    """
    契约测试工具类
    """

    @staticmethod
    def create_contract(provider: str, consumer: str, interactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        创建契约

        Args:
            provider: 提供者名称
            consumer: 消费者名称
            interactions: 交互列表

        Returns:
            契约字典
        """
        return {
            'provider': provider,
            'consumer': consumer,
            'interactions': interactions,
            'version': '1.0.0'
        }

    @staticmethod
    def validate_contract(contract: Dict[str, Any]) -> List[str]:
        """
        验证契约

        Args:
            contract: 契约字典

        Returns:
            验证问题列表
        """
        issues = []

        # 检查必需字段
        required_fields = ['provider', 'consumer', 'interactions', 'version']
        for field in required_fields:
            if field not in contract:
                issues.append(f"Missing required field: {field}")

        # 检查交互格式
        if 'interactions' in contract:
            for i, interaction in enumerate(contract['interactions']):
                interaction_issues = ContractTestUtils._validate_interaction(interaction)
                for issue in interaction_issues:
                    issues.append(f"Interaction {i}: {issue}")

        return issues

    @staticmethod
    def _validate_interaction(interaction: Dict[str, Any]) -> List[str]:
        """
        验证单个交互

        Args:
            interaction: 交互字典

        Returns:
            验证问题列表
        """
        issues = []

        # 检查交互必需字段
        required_fields = ['description', 'request', 'response']
        for field in required_fields:
            if field not in interaction:
                issues.append(f"Missing required field: {field}")

        # 检查请求格式
        if 'request' in interaction:
            request = interaction['request']
            if 'method' not in request:
                issues.append("Request missing method")
            if 'path' not in request:
                issues.append("Request missing path")

        # 检查响应格式
        if 'response' in interaction:
            response = interaction['response']
            if 'status' not in response:
                issues.append("Response missing status")

        return issues

    @staticmethod
    def save_contract(contract: Dict[str, Any], file_path: str) -> bool:
        """
        保存契约到文件

        Args:
            contract: 契约字典
            file_path: 文件路径

        Returns:
            是否成功
        """
        try:
            # 确保目录存在
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(contract, f, indent=2, ensure_ascii=False)

            return True
        except Exception as e:
            return False

    @staticmethod
    def load_contract(file_path: str) -> Optional[Dict[str, Any]]:
        """
        从文件加载契约

        Args:
            file_path: 文件路径

        Returns:
            契约字典
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            return None

    @staticmethod
    def generate_contract_hash(contract: Dict[str, Any]) -> str:
        """
        生成契约哈希

        Args:
            contract: 契约字典

        Returns:
            哈希值
        """
        contract_json = json.dumps(contract, sort_keys=True, ensure_ascii=False)
        return hashlib.md5(contract_json.encode('utf-8')).hexdigest()

    @staticmethod
    def compare_contracts(contract1: Dict[str, Any], contract2: Dict[str, Any]) -> List[str]:
        """
        比较两个契约

        Args:
            contract1: 第一个契约
            contract2: 第二个契约

        Returns:
            差异列表
        """
        differences = []

        # 比较基本字段
        for field in ['provider', 'consumer', 'version']:
            if contract1.get(field) != contract2.get(field):
                differences.append(f"Field '{field}' differs: {contract1.get(field)} != {contract2.get(field)}")

        # 比较交互
        interactions1 = contract1.get('interactions', [])
        interactions2 = contract2.get('interactions', [])

        if len(interactions1) != len(interactions2):
            differences.append(f"Number of interactions differs: {len(interactions1)} != {len(interactions2)}")

        # 比较每个交互
        for i, (int1, int2) in enumerate(zip(interactions1, interactions2)):
            if int1 != int2:
                differences.append(f"Interaction {i} differs")

        return differences

    @staticmethod
    def test_consumer_contract(contract: Dict[str, Any], client: Callable) -> List[Dict[str, Any]]:
        """
        测试消费者契约

        Args:
            contract: 契约字典
            client: 客户端调用函数

        Returns:
            测试结果列表
        """
        results = []

        for interaction in contract.get('interactions', []):
            result = ContractTestUtils._test_interaction(interaction, client)
            results.append(result)

        return results

    @staticmethod
    def _test_interaction(interaction: Dict[str, Any], client: Callable) -> Dict[str, Any]:
        """
        测试单个交互

        Args:
            interaction: 交互字典
            client: 客户端调用函数

        Returns:
            测试结果
        """
        try:
            request = interaction['request']
            expected_response = interaction['response']

            # 调用客户端
            actual_response = client(request)

            # 验证响应
            is_valid = ContractTestUtils._validate_response(actual_response, expected_response)

            return {
                'description': interaction['description'],
                'success': is_valid,
                'expected': expected_response,
                'actual': actual_response
            }
        except Exception as e:
            return {
                'description': interaction.get('description', 'Unknown'),
                'success': False,
                'error': str(e)
            }

    @staticmethod
    def _validate_response(actual: Dict[str, Any], expected: Dict[str, Any]) -> bool:
        """
        验证响应

        Args:
            actual: 实际响应
            expected: 预期响应

        Returns:
            是否有效
        """
        # 验证状态码
        if actual.get('status') != expected.get('status'):
            return False

        # 验证响应头
        if 'headers' in expected:
            for key, value in expected['headers'].items():
                if actual.get('headers', {}).get(key) != value:
                    return False

        # 验证响应体
        if 'body' in expected:
            if actual.get('body') != expected['body']:
                return False

        return True

    @staticmethod
    def generate_provider_tests(contract: Dict[str, Any], output_dir: str) -> bool:
        """
        生成提供者测试

        Args:
            contract: 契约字典
            output_dir: 输出目录

        Returns:
            是否成功
        """
        try:
            # 确保输出目录存在
            os.makedirs(output_dir, exist_ok=True)

            # 生成测试文件
            test_content = ContractTestUtils._generate_test_content(contract)
            test_file = os.path.join(output_dir, f"test_{contract['provider']}_contract.py")

            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_content)

            return True
        except Exception as e:
            return False

    @staticmethod
    def _generate_test_content(contract: Dict[str, Any]) -> str:
        """
        生成测试内容

        Args:
            contract: 契约字典

        Returns:
            测试内容字符串
        """
        # 构建测试文件内容
        lines = []
        lines.append("#!/usr/bin/env python3")
        lines.append("# -*- coding: utf-8 -*-")
        lines.append('"""Provider contract tests for {}".format(contract["provider"])')
        lines.append('Generated from consumer: {}".format(contract["consumer"])')
        lines.append('"""')
        lines.append("import unittest")
        lines.append("from btools.core.test.contracttestutils import ContractTestUtils")
        lines.append("")
        lines.append("")
        lines.append('class Test{}Contract(unittest.TestCase):'.format(contract["provider"].title()))
        lines.append('    """')
        lines.append('    {} contract tests'.format(contract["provider"]))
        lines.append('    """')
        lines.append("")
        lines.append('    def setUp(self):')
        lines.append('        """')
        lines.append('        Set up test fixtures')
        lines.append('        """')
        lines.append('        # TODO: Initialize your provider here')
        lines.append('        pass')
        lines.append("")
        lines.append('    def test_contract_interactions(self):')
        lines.append('        """')
        lines.append('        Test all contract interactions')
        lines.append('        """')
        lines.append('        contract = {')
        lines.append('            \'provider\': \'{} \'.format(contract["provider"]),')
        lines.append('            \'consumer\': \'{} \'.format(contract["consumer"]),')
        lines.append('            \'interactions\': [')
        
        # 添加交互
        for interaction in contract['interactions']:
            interaction_str = json.dumps(interaction, indent=8, ensure_ascii=False)
            lines.append('                ' + interaction_str + ',')
        
        # 完成测试文件
        lines.append('            ],')
        lines.append('            \'version\': \'{} \'.format(contract["version"]))')
        lines.append('        }')
        lines.append("")
        lines.append('        # Validate contract')
        lines.append('        issues = ContractTestUtils.validate_contract(contract)')
        lines.append('        self.assertEqual(len(issues), 0, f"Contract validation failed: {issues}")')
        lines.append("")
        lines.append('        # TODO: Implement actual provider tests here')
        lines.append('        # For each interaction, test that your provider returns the expected response')
        lines.append("")
        lines.append("")
        lines.append('if __name__ == \'__main__\':')
        lines.append('    unittest.main()')
        
        return '\n'.join(lines)

    @staticmethod
    def mock_provider_response(interaction: Dict[str, Any]) -> Dict[str, Any]:
        """
        模拟提供者响应

        Args:
            interaction: 交互字典

        Returns:
            模拟响应
        """
        return interaction.get('response', {})

    @staticmethod
    def validate_provider_implementation(contract: Dict[str, Any], provider: Callable) -> List[Dict[str, Any]]:
        """
        验证提供者实现

        Args:
            contract: 契约字典
            provider: 提供者调用函数

        Returns:
            验证结果列表
        """
        results = []

        for interaction in contract.get('interactions', []):
            try:
                request = interaction['request']
                expected_response = interaction['response']

                # 调用提供者
                actual_response = provider(request)

                # 验证响应
                is_valid = ContractTestUtils._validate_response(actual_response, expected_response)

                results.append({
                    'description': interaction['description'],
                    'success': is_valid,
                    'expected': expected_response,
                    'actual': actual_response
                })
            except Exception as e:
                results.append({
                    'description': interaction.get('description', 'Unknown'),
                    'success': False,
                    'error': str(e)
                })

        return results

    @staticmethod
    def diff_contracts(contract1: Dict[str, Any], contract2: Dict[str, Any]) -> Dict[str, Any]:
        """
        生成契约差异

        Args:
            contract1: 第一个契约
            contract2: 第二个契约

        Returns:
            差异字典
        """
        differences = {
            'added': [],
            'removed': [],
            'modified': []
        }

        # 比较交互
        interactions1 = {int['description']: int for int in contract1.get('interactions', [])}
        interactions2 = {int['description']: int for int in contract2.get('interactions', [])}

        # 检查添加的交互
        for desc, interaction in interactions2.items():
            if desc not in interactions1:
                differences['added'].append(interaction)

        # 检查删除的交互
        for desc, interaction in interactions1.items():
            if desc not in interactions2:
                differences['removed'].append(interaction)

        # 检查修改的交互
        for desc, interaction1 in interactions1.items():
            if desc in interactions2:
                interaction2 = interactions2[desc]
                if interaction1 != interaction2:
                    differences['modified'].append({
                        'description': desc,
                        'old': interaction1,
                        'new': interaction2
                    })

        return differences

    @staticmethod
    def store_contract(contract: Dict[str, Any], directory: str) -> str:
        """
        存储契约到目录

        Args:
            contract: 契约字典
            directory: 存储目录

        Returns:
            存储路径
        """
        # 生成文件名
        provider = contract['provider']
        consumer = contract['consumer']
        contract_hash = ContractTestUtils.generate_contract_hash(contract)
        filename = f"{provider}_{consumer}_{contract_hash}.json"

        # 存储文件
        filepath = os.path.join(directory, filename)
        ContractTestUtils.save_contract(contract, filepath)

        return filepath

    @staticmethod
    def load_contracts(directory: str) -> List[Dict[str, Any]]:
        """
        从目录加载所有契约

        Args:
            directory: 目录路径

        Returns:
            契约列表
        """
        contracts = []

        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                filepath = os.path.join(directory, filename)
                contract = ContractTestUtils.load_contract(filepath)
                if contract:
                    contracts.append(contract)

        return contracts