"""测试ContractTestUtils类"""
import unittest
from btools.core.test.contracttestutils import ContractTestUtils


class TestContractTestUtils(unittest.TestCase):
    """测试ContractTestUtils类"""

    def test_create_request_contract(self):
        """测试创建请求契约"""
        contract = ContractTestUtils.create_request_contract(
            method="POST",
            path="/api/test",
            headers={"Content-Type": "application/json"},
            body={"name": "string"}
        )
        self.assertIsInstance(contract, dict)
        self.assertEqual(contract['method'], "POST")
        self.assertEqual(contract['path'], "/api/test")

    def test_create_response_contract(self):
        """测试创建响应契约"""
        contract = ContractTestUtils.create_response_contract(
            status=200,
            headers={"Content-Type": "application/json"},
            body={"result": "string"}
        )
        self.assertIsInstance(contract, dict)
        self.assertEqual(contract['status'], 200)

    def test_validate_request(self):
        """测试验证请求"""
        contract = ContractTestUtils.create_request_contract(
            method="POST",
            path="/api/test",
            headers={"Content-Type": "application/json"}
        )
        actual = {
            "method": "POST",
            "path": "/api/test",
            "headers": {"Content-Type": "application/json"}
        }
        is_valid = ContractTestUtils.validate_request(contract, actual)
        self.assertTrue(is_valid)


if __name__ == "__main__":
    unittest.main()
