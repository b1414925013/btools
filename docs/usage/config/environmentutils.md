# EnvironmentUtils 使用指南

`EnvironmentUtils` 类提供了环境变量管理的功能，支持加载、读取、设置环境变量，以及不同环境配置的切换。

## 基本使用

### 加载环境变量文件

```python
from btools import EnvironmentUtils

# 加载默认的 .env 文件
EnvironmentUtils.load_env('.env')

# 加载指定环境的配置
EnvironmentUtils.load_environment('production')  # 会尝试加载 .env.production, .env.production.local, .env
```

### 获取环境变量

```python
from btools import EnvironmentUtils

# 获取字符串环境变量
api_key = EnvironmentUtils.get_env('API_KEY', 'default_key')

# 获取整型环境变量
port = EnvironmentUtils.get_env_int('PORT', 8080)

# 获取布尔型环境变量
debug = EnvironmentUtils.get_env_bool('DEBUG', False)

# 获取浮点型环境变量
timeout = EnvironmentUtils.get_env_float('TIMEOUT', 30.5)

# 获取列表型环境变量（逗号分隔）
features = EnvironmentUtils.get_env_list('FEATURES', separator=',')

# 获取字典型环境变量（格式: key1=value1,key2=value2）
config = EnvironmentUtils.get_env_dict('CONFIG', pair_separator=',', kv_separator='=')
```

### 设置和删除环境变量

```python
from btools import EnvironmentUtils

# 设置环境变量
EnvironmentUtils.set_env('API_KEY', 'new_secret_key')

# 取消设置环境变量
EnvironmentUtils.unset_env('TEMP_VAR')

# 检查环境变量是否存在
exists = EnvironmentUtils.has_env('API_KEY')
```

### 环境切换

```python
from btools import EnvironmentUtils

# 加载指定环境
EnvironmentUtils.load_environment('development')  # 开发环境
EnvironmentUtils.load_environment('test')         # 测试环境
EnvironmentUtils.load_environment('production')   # 生产环境

# 获取当前环境
current_env = EnvironmentUtils.get_current_environment()

# 检查当前环境
if EnvironmentUtils.is_development():
    print("开发环境")
elif EnvironmentUtils.is_test():
    print("测试环境")
elif EnvironmentUtils.is_production():
    print("生产环境")
```

## 高级功能

### 获取所有环境变量

```python
from btools import EnvironmentUtils

# 获取所有环境变量
all_env = EnvironmentUtils.get_all_env()

# 获取指定前缀的环境变量
app_env = EnvironmentUtils.get_env_prefix('APP_')
```

### 验证必需的环境变量

```python
from btools import EnvironmentUtils

# 验证必需的环境变量
required = ['DATABASE_URL', 'API_KEY', 'SECRET_KEY']
missing = EnvironmentUtils.validate_environment(required)

if missing:
    print(f"缺失的环境变量: {missing}")
else:
    print("所有必需的环境变量都已设置")
```

### 导出和合并环境变量

```python
from btools import EnvironmentUtils

# 导出环境变量到文件
EnvironmentUtils.export_env('.env.export')

# 合并多个环境变量文件
EnvironmentUtils.merge_env_files(
    ['.env.base', '.env.local', '.env.override'],
    '.env.merged'
)
```

### 创建环境变量文件

```python
from btools import EnvironmentUtils

# 创建环境变量文件
vars = {
    'DATABASE_URL': 'postgresql://user:pass@localhost/db',
    'API_KEY': 'secret_key',
    'DEBUG': 'true'
}
EnvironmentUtils.create_env_file('.env', vars)
```

### 重新加载环境变量

```python
from btools import EnvironmentUtils

# 重新加载环境变量
EnvironmentUtils.reload_env()
```

## .env 文件示例

```env
# 数据库配置
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
DATABASE_HOST=localhost
DATABASE_PORT=5432

# API配置
API_KEY=your_api_key_here
API_TIMEOUT=30

# 应用配置
DEBUG=true
SECRET_KEY=your_secret_key
FEATURES=feature1,feature2,feature3
CONFIG=key1=value1,key2=value2
```

## 环境特定文件

支持多环境配置文件：
- `.env` - 默认配置
- `.env.local` - 本地覆盖配置（不提交到版本控制）
- `.env.{environment}` - 特定环境配置
- `.env.{environment}.local` - 特定环境的本地覆盖配置
