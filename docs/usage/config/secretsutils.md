# SecretsUtils 使用指南

`SecretsUtils` 类提供了密钥管理功能，支持安全存储和访问敏感信息，包括密钥加密、密钥文件管理、密码哈希等功能。

## 基本使用

### 密钥文件管理

```python
from btools import SecretsUtils

# 创建密钥字典
secrets = {
    'database_password': 'my_db_password',
    'api_key': 'sk_abc123xyz',
    'private_key': '-----BEGIN PRIVATE KEY-----...'
}

# 保存密钥（不加密）
SecretsUtils.save_secrets('secrets.json', secrets)

# 保存密钥（加密）
SecretsUtils.save_secrets('secrets.encrypted.json', secrets, password='my_secure_password')

# 加载密钥
unencrypted_secrets = SecretsUtils.load_secrets('secrets.json')
encrypted_secrets = SecretsUtils.load_secrets('secrets.encrypted.json', password='my_secure_password')
```

### 获取和设置密钥

```python
from btools import SecretsUtils

# 获取密钥（从默认文件 secrets.json）
db_password = SecretsUtils.get_secret('database_password', 'default_password')

# 获取密钥（从指定文件）
api_key = SecretsUtils.get_secret('api_key', secrets_file='config/secrets.json', password='secret')

# 设置密钥
SecretsUtils.set_secret('new_secret', 'new_value', secrets_file='secrets.json', password=None)

# 删除密钥
SecretsUtils.delete_secret('old_secret', secrets_file='secrets.json')
```

### 生成随机密钥

```python
from btools import SecretsUtils

# 生成随机密钥（默认32位）
random_secret = SecretsUtils.generate_secret()

# 生成指定长度的密钥
long_secret = SecretsUtils.generate_secret(length=64)

# 生成 API 密钥（带前缀）
api_key = SecretsUtils.generate_api_key(prefix='sk', length=48)
```

## 密码哈希

```python
from btools import SecretsUtils

# 哈希密码
hashed = SecretsUtils.hash_password('my_password')

# 验证密码
is_valid = SecretsUtils.check_password('my_password', hashed)
```

## 环境变量集成

```python
from btools import SecretsUtils

# 从密钥文件加载到环境变量
SecretsUtils.load_env_secrets(prefix='SECRET_', secrets_file='secrets.json')

# 从环境变量存储到密钥文件
SecretsUtils.store_env_secrets(prefix='SECRET_', secrets_file='secrets.json')
```

## 高级功能

### 密钥验证

```python
from btools import SecretsUtils

# 验证必需的密钥
required = ['database_password', 'api_key', 'private_key']
missing = SecretsUtils.validate_secrets(required, secrets_file='secrets.json')

if missing:
    print(f"缺失的密钥: {missing}")
```

### 密钥轮换

```python
from btools import SecretsUtils

# 轮换密钥
new_secret = SecretsUtils.rotate_secret('api_key', secrets_file='secrets.json')
if new_secret:
    print(f"新密钥: {new_secret}")
```

### 备份和恢复

```python
from btools import SecretsUtils

# 备份密钥文件
SecretsUtils.backup_secrets(
    source_file='secrets.json',
    backup_file='secrets.backup.json'
)

# 恢复密钥文件
SecretsUtils.restore_secrets(
    backup_file='secrets.backup.json',
    target_file='secrets.json'
)
```

### 密钥摘要

```python
from btools import SecretsUtils

# 获取密钥摘要
summary = SecretsUtils.get_secrets_summary('secrets.json')
print(f"密钥总数: {summary['total_secrets']}")
print(f"密钥列表: {summary['secret_keys']}")
```

### 安全检查

```python
from btools import SecretsUtils

# 检查密钥文件是否安全
is_secure = SecretsUtils.is_secret_file_secure('secrets.json')

# 清除所有密钥
SecretsUtils.clear_secrets('secrets.json')
```

## 云服务集成

### AWS Secrets Manager

```python
from btools import SecretsUtils

# 从 AWS Secrets Manager 获取密钥
aws_secrets = SecretsUtils.get_aws_secrets(
    secret_name='my-app-secrets',
    region_name='us-east-1'
)

if aws_secrets:
    db_password = aws_secrets.get('database_password')
```

### GCP Secret Manager

```python
from btools import SecretsUtils

# 从 GCP Secret Manager 获取密钥
gcp_secrets = SecretsUtils.get_gcp_secrets(
    secret_name='my-app-secrets',
    version_id='latest'
)

if gcp_secrets:
    api_key = gcp_secrets.get('api_key')
```

## 密钥文件格式

### 未加密的密钥文件

```json
{
  "encrypted": false,
  "data": {
    "database_password": "my_db_password",
    "api_key": "sk_abc123xyz"
  }
}
```

### 加密的密钥文件

```json
{
  "encrypted": true,
  "data": "gAAAAAB...加密后的字符串..."
}
```

## 安全最佳实践

1. **始终加密生产环境的密钥文件**
2. **不要将密钥文件提交到版本控制系统**
3. **使用强密码加密密钥文件**
4. **定期轮换敏感密钥**
5. **在生产环境使用云密钥管理服务（AWS Secrets Manager、GCP Secret Manager 等）**
6. **限制密钥文件的访问权限**
