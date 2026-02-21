# DistributionUtils 使用指南

`DistributionUtils` 类提供了分发工具，支持上传到 PyPI、私有仓库等功能。

## 基本使用

### 上传到 PyPI

```python
from btools import DistributionUtils

# 上传到 PyPI
success = DistributionUtils.upload_to_pypi(
    package_path="dist/myapp-1.0.0-py3-none-any.whl",
    username="__token__",
    password="pypi-xxxxxx"
)

# 上传多个文件
success = DistributionUtils.upload_to_pypi(
    package_path="dist/*",
    username="__token__",
    password="pypi-xxxxxx"
)
```

### 上传到 TestPyPI

```python
from btools import DistributionUtils

# 上传到 TestPyPI (测试环境)
success = DistributionUtils.upload_to_testpypi(
    package_path="dist/myapp-1.0.0-py3-none-any.whl",
    username="__token__",
    password="pypi-xxxxxx"
)
```

### 上传到私有仓库

```python
from btools import DistributionUtils

# 上传到私有 PyPI 仓库
success = DistributionUtils.upload_to_private_repo(
    package_path="dist/myapp-1.0.0-py3-none-any.whl",
    repository_url="https://pypi.example.com",
    username="your_username",
    password="your_password"
)
```

## 高级功能

### 使用 twine 上传

```python
from btools import DistributionUtils

# 使用 twine 上传
success = DistributionUtils.upload_with_twine(
    package_paths=["dist/myapp-1.0.0-py3-none-any.whl"],
    repository_url="https://upload.pypi.org/legacy/",
    username="__token__",
    password="pypi-xxxxxx",
    sign=True,  # 签名
    identity="your-signing-key"
)
```

### 验证包

```python
from btools import DistributionUtils

# 验证包文件
is_valid = DistributionUtils.validate_package(
    "dist/myapp-1.0.0-py3-none-any.whl"
)

# 检查包元数据
metadata = DistributionUtils.get_package_metadata(
    "dist/myapp-1.0.0-py3-none-any.whl"
)
print(f"包名: {metadata['name']}")
print(f"版本: {metadata['version']}")
```

### 检查 PyPI 包信息

```python
from btools import DistributionUtils

# 获取 PyPI 上的包信息
package_info = DistributionUtils.get_pypi_package_info("myapp")
print(package_info)

# 检查包是否已存在
exists = DistributionUtils.package_exists_on_pypi("myapp", "1.0.0")

# 获取最新版本
latest_version = DistributionUtils.get_latest_version_on_pypi("myapp")
```

### 下载包

```python
from btools import DistributionUtils

# 从 PyPI 下载包
success = DistributionUtils.download_from_pypi(
    package_name="myapp",
    version="1.0.0",
    output_dir="downloads"
)

# 下载最新版本
success = DistributionUtils.download_from_pypi(
    package_name="myapp",
    output_dir="downloads"
)
```

## 配置管理

### 使用配置文件

```python
from btools import DistributionUtils

# 从 ~/.pypirc 读取配置
config = DistributionUtils.load_pypirc_config()
print(config)

# 使用配置文件上传
success = DistributionUtils.upload_using_config(
    package_path="dist/myapp-1.0.0-py3-none-any.whl",
    config_section="pypi"
)
```

### 环境变量

```python
import os
from btools import DistributionUtils

# 设置环境变量
os.environ["TWINE_USERNAME"] = "__token__"
os.environ["TWINE_PASSWORD"] = "pypi-xxxxxx"

# 使用环境变量上传
success = DistributionUtils.upload_to_pypi(
    package_path="dist/myapp-1.0.0-py3-none-any.whl"
)
```

## 分发工作流

### 完整的分发流程

```python
from btools import DistributionUtils, PackagingUtils, ReleaseUtils

# 1. 更新版本
ReleaseUtils.bump_patch_version(".")

# 2. 打包
PackagingUtils.package_all(".")

# 3. 验证包
is_valid = DistributionUtils.validate_package("dist/myapp-1.0.1-py3-none-any.whl")

if is_valid:
    # 4. 上传到 TestPyPI 测试
    success = DistributionUtils.upload_to_testpypi("dist/*")
    
    if success:
        # 5. 测试安装
        # pip install --index-url https://test.pypi.org/simple/ myapp
        
        # 6. 上传到 PyPI
        success = DistributionUtils.upload_to_pypi("dist/*")
```

## 安全最佳实践

1. **使用 API Token 而非密码**
   ```python
   DistributionUtils.upload_to_pypi(
       package_path="dist/*",
       username="__token__",
       password="pypi-xxxxxx"
   )
   ```

2. **先上传到 TestPyPI 测试**

3. **签名发布的包**
   ```python
   DistributionUtils.upload_with_twine(
       package_paths=["dist/*"],
       sign=True,
       identity="your-signing-key"
   )
   ```

4. **使用 2FA (双因素认证)**

5. **不要将凭据提交到版本控制**
