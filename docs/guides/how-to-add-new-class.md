# 如何添加新类

要向`btools`包添加新类，请按照以下步骤操作：

## 1. 创建类文件

在`btools/`下的适当目录中创建一个新的Python文件：

- 核心功能：`btools/core/`
- 工具函数：`btools/utils/`

例如，要创建一个新的`Database`类：

```python
# btools/core/database.py

class Database:
    """
    数据库连接和查询工具类
    """
    
    def __init__(self, host, port, username, password, database):
        """
        初始化数据库连接
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        """
        连接到数据库
        """
        # 实现代码
        pass
    
    def query(self, sql, params=None):
        """
        执行SQL查询
        """
        # 实现代码
        pass
    
    def disconnect(self):
        """
        断开数据库连接
        """
        # 实现代码
        pass
```

## 2. 更新__init__.py

将新类添加到`btools`目录下的`__init__.py`文件中：

```python
# btools/__init__.py

__version__ = "1.0.0"

# 导出核心模块
from .core.logger import Logger
from .core.config import Config
from .core.database import Database  # 添加这一行

# 导出工具模块
from .utils.validator import Validator
from .utils.converter import Converter

__all__ = [
    "Logger",
    "Config",
    "Database",  # 添加这一行
    "Validator",
    "Converter"
]
```

## 3. 更新文档

### 3.1 创建使用指南

在`docs/usage/`目录中创建新类的使用指南文档，例如`database.md`：

```markdown
# Database 使用指南

`Database` 类提供了数据库连接和查询的功能。

## 基本使用

```python
from btools import Database

# 创建数据库连接
db = Database(
    host="localhost",
    port=5432,
    username="admin",
    password="password123",
    database="mydb"
)

# 连接数据库
db.connect()

# 执行查询
result = db.query("SELECT * FROM users")
print(result)

# 断开连接
db.disconnect()
```

## 高级功能

### 上下文管理器支持

```python
from btools import Database

# 使用上下文管理器，自动断开连接
with Database(
    host="localhost",
    port=5432,
    username="admin",
    password="password123",
    database="mydb"
) as db:
    # 连接会自动建立
    result = db.query("SELECT * FROM users")
    print(result)
# 连接会在这里自动断开
```
```

### 3.2 更新主README.md

在主README.md文件的文档部分添加新类的链接：

```markdown
## 文档

详细的使用文档请参考：

- **使用指南**:
  - [Logger使用指南](docs/usage/logger.md)
  - [Config使用指南](docs/usage/config.md)
  - [Database使用指南](docs/usage/database.md)  # 添加这一行
  - [HTTPClient使用指南](docs/usage/httpclient.md)
  - ...
```

## 4. 测试新类

创建一个测试脚本来验证新类是否正常工作：

```python
# test_database.py

from btools import Database

# 测试Database类
db = Database(
    host="localhost",
    port=5432,
    username="admin",
    password="password123",
    database="mydb"
)

# 测试连接
db.connect()

# 测试查询
# result = db.query("SELECT * FROM users")

# 测试断开连接
db.disconnect()

print("Database类测试完成！")
```

运行测试脚本：

```bash
python test_database.py
```

## 5. 添加依赖（如果需要）

如果新类需要额外的依赖库，请在`setup.py`文件中添加：

```python
# setup.py
setup(
    # 其他配置...
    install_requires=[
        'pyyaml',
        'requests',
        'psycopg2-binary',  # 例如，添加PostgreSQL驱动
    ],
)
```

同时在`requirements.txt`文件中添加：

```
pyyaml
requests
psycopg2-binary
```

## 6. 常见问题

### 导入错误

如果出现导入错误，请检查：
1. 文件路径是否正确
2. `__init__.py`文件是否已更新
3. 类名是否正确

### 依赖问题

如果新类依赖于外部库，请确保：
1. 在`setup.py`中添加了依赖
2. 在`requirements.txt`中添加了依赖
3. 依赖库已正确安装

### 文档更新

添加新类后，请确保：
1. 创建了对应的使用指南文档
2. 在主README.md中添加了链接
3. 文档中包含了足够的使用示例

### 测试覆盖

为新类添加测试用例，确保：
1. 基本功能正常工作
2. 边界情况得到处理
3. 错误处理正确

## 7. 最佳实践

- **命名规范**：类名使用驼峰命名法（CamelCase），文件名使用小写字母加下划线（snake_case）
- **文档**：为每个类和方法添加详细的文档字符串
- **错误处理**：添加适当的错误处理和异常捕获
- **测试**：为新功能添加测试用例
- **兼容性**：确保代码在不同Python版本上都能正常工作
- **性能**：考虑代码的性能影响，特别是对于频繁调用的方法

通过遵循这些步骤，您可以向`btools`包添加新的功能类，同时保持代码库的一致性和可维护性。