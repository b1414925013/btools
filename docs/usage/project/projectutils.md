# ProjectUtils 使用指南

`ProjectUtils` 类提供了项目结构管理、依赖分析、版本管理等功能。

## 基本使用

### 获取项目结构

```python
from btools import ProjectUtils

# 获取当前项目结构
structure = ProjectUtils.get_project_structure(".")
print(structure)

# 获取指定路径的项目结构
structure = ProjectUtils.get_project_structure("/path/to/project")
```

### 分析项目依赖

```python
from btools import ProjectUtils

# 分析当前项目的依赖
dependencies = ProjectUtils.analyze_dependencies(".")

print("Requirements.txt:", dependencies['requirements'])
print("Setup.py:", dependencies['setup'])
print("当前安装的包:", dependencies['pip'])
```

### 获取项目信息

```python
from btools import ProjectUtils

# 获取项目信息
info = ProjectUtils.get_project_info(".")
print("项目名称:", info.get('name'))
print("项目版本:", info.get('version'))
print("项目描述:", info.get('description'))
```

### 检查项目结构

```python
from btools import ProjectUtils

# 检查项目是否为Python项目
is_python = ProjectUtils.is_python_project(".")

# 检查项目是否有Git仓库
has_git = ProjectUtils.has_git_repository(".")

# 检查项目是否有虚拟环境
has_venv = ProjectUtils.has_virtual_environment(".")
```

## 高级功能

### 创建标准项目结构

```python
from btools import ProjectUtils

# 创建标准的Python项目结构
ProjectUtils.create_standard_structure("my_new_project", {
    'name': 'my_project',
    'version': '0.1.0',
    'description': 'My new project'
})
```

### 生成项目报告

```python
from btools import ProjectUtils

# 生成项目报告
report = ProjectUtils.generate_project_report(".")
print(report)

# 保存项目报告到文件
ProjectUtils.save_project_report(".", "project_report.json")
```

### 依赖管理

```python
from btools import ProjectUtils

# 更新依赖
ProjectUtils.update_dependencies(".")

# 检查过时的依赖
outdated = ProjectUtils.get_outdated_dependencies(".")
print("过时的依赖:", outdated)
```

## 项目结构示例

`get_project_structure` 返回的项目结构示例：

```python
{
    'btools': {
        'core': {
            'basic': {
                '__files__': ['stringutils.py', 'collectionutils.py', '__init__.py']
            },
            'config': {
                '__files__': ['configutils.py', 'environmentutils.py', '__init__.py']
            }
        },
        '__files__': ['__init__.py']
    },
    'docs': {
        'usage': {
            '__files__': [...]
        },
        '__files__': []
    },
    'test': {
        '__files__': [...]
    },
    '__files__': ['README.md', 'requirements.txt', 'setup.py']
}
```

## 依赖分析示例

`analyze_dependencies` 返回的依赖信息示例：

```python
{
    'pip': [
        'requests==2.31.0',
        'pyyaml==6.0.1',
        'pytest==7.4.0'
    ],
    'requirements': [
        'requests~=2.31.0',
        'pyyaml~=6.0.1',
        'pytest~=7.4.0'
    ],
    'setup': [
        'requests>=2.31.0',
        'pyyaml>=6.0.1'
    ]
}
```
