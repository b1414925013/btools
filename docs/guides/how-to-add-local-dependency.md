# 如何添加本地依赖库

要添加本地的库文件作为`btools`项目的依赖，请按照以下步骤操作：

## 1. 准备本地库文件

确保您的本地库已经打包为wheel文件。如果尚未打包，请按照以下步骤操作：

```bash
# 进入本地库项目目录
cd /path/to/your/local/library

# 安装打包工具
pip install --upgrade setuptools wheel

# 打包为wheel文件
python setup.py bdist_wheel
```

这将在本地库项目的`dist`目录中生成wheel文件，例如：`local_library-1.0.0-py3-none-any.whl`。

## 2. 在setup.py中添加本地依赖

有两种方法可以添加本地依赖：

### 方法一：使用相对路径引用wheel文件

```python
# setup.py
from setuptools import setup, find_packages

setup(
    # 其他配置...
    install_requires=[
        'pyyaml',
        'requests',
        # 添加本地依赖
        'local_library @ file:///path/to/your/local/library/dist/local_library-1.0.0-py3-none-any.whl'
    ],
)
```

### 方法二：使用本地目录路径

```python
# setup.py
from setuptools import setup, find_packages

setup(
    # 其他配置...
    install_requires=[
        'pyyaml',
        'requests',
        # 添加本地依赖
        'local_library @ file:///path/to/your/local/library'
    ],
)
```

## 3. 安装本地依赖

在`btools`项目目录中运行以下命令来安装依赖：

```bash
pip install -e .
```

或者，当您打包`btools`项目时，本地依赖也会被包含在安装过程中：

```bash
# 打包btools项目
python setup.py bdist_wheel

# 安装btools包（会自动安装所有依赖，包括本地依赖）
pip install dist/btools-1.0.0-py3-none-any.whl
```

## 4. 验证依赖安装

运行以下命令来验证本地依赖是否已正确安装：

```bash
pip list | grep local_library
```

如果输出显示了本地库的版本信息，则说明依赖安装成功。

## 5. 常见问题

### 依赖路径问题

确保使用正确的文件路径格式：
- Windows: `file:///C:/path/to/library`
- Linux/Mac: `file:///path/to/library`

### 依赖版本冲突

如果本地依赖与其他依赖存在版本冲突，请检查版本兼容性并进行相应调整。

### 安装失败

如果安装失败，请检查：
1. 本地库是否已正确打包
2. 路径是否正确
3. 本地库是否有自己的依赖项

### 开发模式下的依赖

在开发模式下，本地依赖的更改不会自动反映到`btools`项目中。如果您修改了本地依赖，需要重新安装：

```bash
# 重新安装本地依赖
pip install -e /path/to/your/local/library

# 重新安装btools
pip install -e .
```