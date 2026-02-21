# PackagingUtils 使用指南

`PackagingUtils` 类提供了 Python 项目打包功能，支持 wheel、egg、sdist 等格式。

## 基本使用

### 打包项目

```python
from btools import PackagingUtils

# 打包为 sdist (源码分发包)
success = PackagingUtils.package_sdist(".")

# 打包为 wheel
success = PackagingUtils.package_wheel(".")

# 打包为 egg
success = PackagingUtils.package_egg(".")

# 打包所有格式
success = PackagingUtils.package_all(".")
```

### 构建选项

```python
from btools import PackagingUtils

# 指定输出目录
success = PackagingUtils.package_wheel(
    project_path=".",
    output_dir="dist"
)

# 清理构建缓存
success = PackagingUtils.clean_build(".")

# 清理所有构建文件
success = PackagingUtils.clean_all(".")
```

### 检查打包文件

```python
from btools import PackagingUtils

# 获取项目信息
info = PackagingUtils.get_project_info(".")
print(f"项目名称: {info['name']}")
print(f"项目版本: {info['version']}")

# 列出构建产物
artifacts = PackagingUtils.list_artifacts("dist")
print(artifacts)

# 验证包文件
is_valid = PackagingUtils.validate_package("dist/myapp-1.0.0-py3-none-any.whl")
```

## 高级功能

### 自定义构建

```python
from btools import PackagingUtils

# 使用自定义 setup.py 参数
success = PackagingUtils.package_wheel(
    project_path=".",
    args=["--universal"]
)

# 构建前执行命令
success = PackagingUtils.build_with_pre_commands(
    project_path=".",
    pre_commands=[
        ["python", "scripts/pre_build.py"],
        ["npm", "install"]
    ]
)
```

### 签名和验证

```python
from btools import PackagingUtils

# 签名包文件
success = PackagingUtils.sign_package(
    "dist/myapp-1.0.0-py3-none-any.whl",
    identity="my-signing-key"
)

# 验证包签名
is_valid = PackagingUtils.verify_package_signature(
    "dist/myapp-1.0.0-py3-none-any.whl"
)
```

### 元数据管理

```python
from btools import PackagingUtils

# 更新版本号
success = PackagingUtils.update_version(".", "1.1.0")

# 获取当前版本
version = PackagingUtils.get_current_version(".")

# 更新元数据
success = PackagingUtils.update_metadata(
    ".",
    {
        "description": "新的描述",
        "author": "新作者"
    }
)
```

## 构建配置

### setup.py 示例

```python
from setuptools import setup, find_packages

setup(
    name="myapp",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "pyyaml>=6.0.1"
    ],
    python_requires=">=3.8",
)
```

### pyproject.toml 示例

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "myapp"
version = "1.0.0"
authors = [
  { name="Your Name", email="your.email@example.com" }
]
description = "A description of your project"
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
  "requests>=2.31.0",
  "pyyaml>=6.0.1"
]
```

## 常见打包格式

| 格式 | 说明 | 命令 |
|------|------|------|
| sdist | 源码分发包 | `python setup.py sdist` |
| wheel | 预编译包 | `python setup.py bdist_wheel` |
| egg | Setuptools 包 | `python setup.py bdist_egg` |
