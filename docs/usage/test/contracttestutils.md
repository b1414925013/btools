# ContractTestUtils 使用指南

`ContractTestUtils` 类提供了契约测试工具，用于确保服务间接口一致性。

## 基本使用

### 创建契约

```python
from btools import ContractTestUtils

# 创建请求契约
request_contract = ContractTestUtils.create_request_contract(
    method="POST",
    path="/api/users",
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}"
    },
    body={
        "name": "string",
        "email": "string",
        "age": "number"
    }
)

# 创建响应契约
response_contract = ContractTestUtils.create_response_contract(
    status=201,
    headers={
        "Content-Type": "application/json"
    },
    body={
        "id": "number",
        "name": "string",
        "email": "string",
        "created_at": "string"
    }
)
```

### 验证契约

```python
from btools import ContractTestUtils

# 验证请求是否符合契约
is_valid = ContractTestUtils.validate_request(
    request_contract,
    actual_request={
        "method": "POST",
        "path": "/api/users",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "name": "John",
            "email": "john@example.com",
            "age": 30
        }
    }
)

print(f"请求验证: {is_valid}")

# 验证响应是否符合契约
is_valid = ContractTestUtils.validate_response(
    response_contract,
    actual_response={
        "status": 201,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "id": 1,
            "name": "John",
            "email": "john@example.com",
            "created_at": "2024-01-01T00:00:00Z"
        }
    }
)

print(f"响应验证: {is_valid}")
```

## 高级功能

### 保存和加载契约

```python
from btools import ContractTestUtils

# 保存契约到文件
ContractTestUtils.save_contract(
    contract={
        "request": request_contract,
        "response": response_contract
    },
    file_path="contracts/user_creation.json"
)

# 从文件加载契约
contract = ContractTestUtils.load_contract("contracts/user_creation.json")
```

### 比较契约

```python
from btools import ContractTestUtils

# 比较两个契约
differences = ContractTestUtils.compare_contracts(
    contract1=old_contract,
    contract2=new_contract
)

if differences:
    print("契约变更:")
    for diff in differences:
        print(f"  - {diff}")
```

### 生成测试

```python
from btools import ContractTestUtils

# 从契约生成测试用例
test_code = ContractTestUtils.generate_test_from_contract(
    contract=contract,
    test_name="test_user_creation",
    base_url="https://api.example.com"
)

print(test_code)

# 保存生成的测试
ContractTestUtils.save_generated_test(
    test_code,
    "test_generated_contract.py"
)
```

## Pact 集成

```python
from btools import ContractTestUtils

# 创建 Pact 契约
pact_contract = ContractTestUtils.create_pact_contract(
    consumer="ConsumerService",
    provider="ProviderService",
    interactions=[
        {
            "description": "a request for user creation",
            "request": request_contract,
            "response": response_contract
        }
    ]
)

# 验证 Pact 契约
is_valid = ContractTestUtils.validate_pact_contract(pact_contract)
```

## 契约版本管理

```python
from btools import ContractTestUtils

# 获取契约版本
version = ContractTestUtils.get_contract_version(contract)

# 升级契约版本
new_contract = ContractTestUtils.bump_contract_version(
    contract,
    version_type="minor"  # major, minor, patch
)

# 检查契约兼容性
is_compatible = ContractTestUtils.check_contract_compatibility(
    old_contract,
    new_contract
)
```

## 契约验证器

```python
from btools import ContractTestUtils

# 创建自定义验证器
def custom_validator(contract, actual):
    # 自定义验证逻辑
    return True

# 注册验证器
ContractTestUtils.register_validator("custom", custom_validator)

# 使用自定义验证器
is_valid = ContractTestUtils.validate_with_custom_validator(
    contract,
    actual,
    validator_name="custom"
)
```

## 契约格式示例

### JSON Schema 格式

```json
{
  "request": {
    "method": "POST",
    "path": "/api/users",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "number"}
      },
      "required": ["name", "email"]
    }
  },
  "response": {
    "status": 201,
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "type": "object",
      "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"}
      }
    }
  }
}
```

## 最佳实践

1. **在开发初期定义契约**
2. **使用版本控制管理契约**
3. **定期运行契约测试**
4. **契约变更时更新版本**
5. **使用自动化工具生成契约测试**
