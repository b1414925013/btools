# 依赖说明

本文档记录了项目依赖的特殊说明和变更。

## psycopg2-binary 依赖说明

### 变更内容
- 在 `requirements.txt` 文件中，`psycopg2-binary` 依赖已被注释掉
- 保留了 `pymysql` 依赖，确保项目仍然可以连接 MySQL 数据库

### 变更原因
- `psycopg2-binary` 依赖在安装时需要 `pg_config` 可执行文件
- `pg_config` 是 PostgreSQL 开发环境的一部分，不是所有环境都默认安装
- 这导致在缺少 PostgreSQL 开发环境的系统上安装失败

### 对项目的影响
- **正面影响**：项目可以在任何环境中成功安装，不会因为缺少 PostgreSQL 开发工具而失败
- **负面影响**：项目将不再默认依赖于 PostgreSQL 数据库

### 如何使用 PostgreSQL
如果您需要使用 PostgreSQL 数据库，可以通过以下命令手动安装 `psycopg2-binary`：

```bash
pip install psycopg2-binary
```

#### 注意事项
1. 在安装 `psycopg2-binary` 之前，您需要确保：
   - 安装了 PostgreSQL 数据库
   - 安装了 PostgreSQL 开发环境（包含 `pg_config` 可执行文件）

2. 或者，您可以尝试使用预编译的轮子版本，避免从源代码构建：
   ```bash
   pip install --only-binary :all: psycopg2-binary
   ```

### 替代方案
如果您只是需要一个轻量级的数据库解决方案，可以考虑使用：
- **SQLite**：Python 内置，无需额外安装
- **MySQL**：通过已安装的 `pymysql` 依赖连接

## 其他依赖说明

### Python 版本兼容性
项目依赖已调整为与 Python 3.8+ 兼容，确保在不同版本的 Python 环境中都能正常运行。

### 依赖版本管理
所有依赖版本都使用了波浪号 (`~=`) 前缀，确保：
- 安装兼容的版本
- 避免破坏性变更
- 允许获取安全补丁和 bug 修复

### 安装依赖
在项目根目录下执行以下命令安装所有依赖：

```bash
pip install -r requirements.txt
```
