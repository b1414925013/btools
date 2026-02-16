# 如何打包

要将`btools`项目打包为wheel文件，请按照以下步骤操作：

## 1. 安装所需工具

```bash
pip install --upgrade setuptools wheel build
```

## 2. 打包项目

在项目根目录运行以下命令：

```bash
python setup.py bdist_wheel
```

这将创建一个`dist`目录，包含wheel文件，例如：`btools-1.0.0-py3-none-any.whl`。

## 3. 验证包

您可以通过解压wheel文件来验证其内容：

### 在Windows上

```bash
rename btools-1.0.0-py3-none-any.whl btools-1.0.0-py3-none-any.zip
# 然后使用压缩工具解压
```

### 在Linux/Mac上

```bash
unzip btools-1.0.0-py3-none-any.whl -d whl_contents
```

## 4. 安装包

### 从本地安装

```bash
pip install dist/btools-1.0.0-py3-none-any.whl
```

### 开发模式安装

如果您正在开发包并希望实时反映更改，可以使用开发模式安装：

```bash
pip install -e .
```

## 5. 卸载包

```bash
pip uninstall btools
```

## 6. 常见问题

### 打包时出现编码错误

如果在Windows上打包时出现编码错误，请确保所有Python文件都使用UTF-8编码，并且没有BOM标记。

### 包中缺少模块

确保所有子目录都包含`__init__.py`文件，这样setuptools才能正确识别包结构。

### 依赖项问题

如果打包后安装时出现依赖项错误，请检查`setup.py`文件中的`install_requires`部分，确保所有依赖项都正确列出。

### 版本号管理

要更新包的版本号，请修改`btools/__init__.py`文件中的`__version__`变量，以及`setup.py`文件中的`version`参数。