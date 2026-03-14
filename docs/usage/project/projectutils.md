# ProjectUtils 使用指南

`ProjectUtils` 类提供了项目结构管理、依赖分析、版本管理等功能，帮助开发者快速了解和管理项目。

## 方法详解

### 1. get_project_structure

**功能**：获取项目的目录结构，返回一个嵌套的字典表示。

**方法签名**：
```python
@staticmethod
def get_project_structure(project_path: str = ".") -> Dict[str, Any]
```

**参数**：
- `project_path` (str): 项目路径，默认为当前目录 "."

**返回值**：
- `Dict[str, Any]`: 项目结构字典，其中每个目录是一个子字典，文件列表存储在 `__files__` 键中

**使用场景**：
- 快速了解项目的目录结构
- 自动化脚本中需要遍历项目文件
- 生成项目文档时需要展示结构

**使用示例**：
```python
from btools import ProjectUtils

# 获取当前项目结构
structure = ProjectUtils.get_project_structure(".")
print("项目结构:", structure)

# 获取指定路径的项目结构
structure = ProjectUtils.get_project_structure("/path/to/project")
print("指定项目结构:", structure)
```

**返回示例**：
```python
{
    'btools': {
        'core': {
            'basic': {
                '__files__': ['stringutils.py', 'collectionutils.py', '__init__.py']
            }
        },
        '__files__': ['__init__.py']
    },
    '__files__': ['README.md', 'requirements.txt', 'setup.py']
}
```

### 2. analyze_dependencies

**功能**：分析项目的依赖情况，包括 requirements.txt、setup.py 和当前安装的包。

**方法签名**：
```python
@staticmethod
def analyze_dependencies(project_path: str = ".") -> Dict[str, List[str]]
```

**参数**：
- `project_path` (str): 项目路径，默认为当前目录 "."

**返回值**：
- `Dict[str, List[str]]`: 包含三种依赖信息的字典：
  - `pip`: 当前安装的包列表
  - `requirements`: requirements.txt 中的依赖列表
  - `setup`: setup.py 中的依赖列表

**使用场景**：
- 检查项目依赖的完整性
- 比较不同来源的依赖版本
- 自动化依赖管理

**使用示例**：
```python
from btools import ProjectUtils

# 分析当前项目的依赖
dependencies = ProjectUtils.analyze_dependencies(".")

print("Requirements.txt 依赖:", dependencies['requirements'])
print("Setup.py 依赖:", dependencies['setup'])
print("当前安装的包:", dependencies['pip'])
```

**返回示例**：
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

### 3. get_project_info

**功能**：获取项目的基本信息，如名称、版本、描述和作者。

**方法签名**：
```python
@staticmethod
def get_project_info(project_path: str = ".") -> Dict[str, Optional[str]]
```

**参数**：
- `project_path` (str): 项目路径，默认为当前目录 "."

**返回值**：
- `Dict[str, Optional[str]]`: 项目信息字典，包含以下键：
  - `name`: 项目名称
  - `version`: 项目版本
  - `description`: 项目描述
  - `author`: 项目作者

**使用场景**：
- 快速了解项目的基本信息
- 自动化脚本中需要使用项目信息
- 生成项目报告时需要项目元数据

**使用示例**：
```python
from btools import ProjectUtils

# 获取项目信息
info = ProjectUtils.get_project_info(".")
print("项目名称:", info.get('name'))
print("项目版本:", info.get('version'))
print("项目描述:", info.get('description'))
print("项目作者:", info.get('author'))
```

**返回示例**：
```python
{
    'name': 'btools',
    'version': '1.0.0',
    'description': '一个用于Python项目的实用工具类和函数集合',
    'author': 'Author Name'
}
```

### 4. is_python_project

**功能**：检查指定路径是否为Python项目。

**方法签名**：
```python
@staticmethod
def is_python_project(project_path: str = ".") -> bool
```

**参数**：
- `project_path` (str): 项目路径，默认为当前目录 "."

**返回值**：
- `bool`: 如果是Python项目则返回 True，否则返回 False

**使用场景**：
- 自动化脚本中需要判断项目类型
- IDE插件需要识别项目类型
- 批量处理脚本需要过滤Python项目

**使用示例**：
```python
from btools import ProjectUtils

# 检查当前目录是否为Python项目
is_python = ProjectUtils.is_python_project(".")
print(f"当前目录是Python项目: {is_python}")

# 检查指定目录是否为Python项目
is_python = ProjectUtils.is_python_project("/path/to/project")
print(f"指定目录是Python项目: {is_python}")
```

### 5. has_git_repository

**功能**：检查指定路径是否包含Git仓库。

**方法签名**：
```python
@staticmethod
def has_git_repository(project_path: str = ".") -> bool
```

**参数**：
- `project_path` (str): 项目路径，默认为当前目录 "."

**返回值**：
- `bool`: 如果包含Git仓库则返回 True，否则返回 False

**使用场景**：
- 自动化脚本中需要判断是否为Git项目
- 版本控制相关操作前的检查
- 批量处理脚本需要过滤Git项目

**使用示例**：
```python
from btools import ProjectUtils

# 检查当前目录是否有Git仓库
has_git = ProjectUtils.has_git_repository(".")
print(f"当前目录有Git仓库: {has_git}")

# 检查指定目录是否有Git仓库
has_git = ProjectUtils.has_git_repository("/path/to/project")
print(f"指定目录有Git仓库: {has_git}")
```

### 6. validate_project_structure

**功能**：验证项目结构是否符合标准Python项目结构。

**方法签名**：
```python
@staticmethod
def validate_project_structure(project_path: str = ".") -> List[str]
```

**参数**：
- `project_path` (str): 项目路径，默认为当前目录 "."

**返回值**：
- `List[str]`: 问题列表，包含所有不符合标准的问题

**使用场景**：
- 新项目初始化时检查结构完整性
- CI/CD流程中验证项目结构
- 代码审查时检查项目规范

**使用示例**：
```python
from btools import ProjectUtils

# 验证当前项目结构
issues = ProjectUtils.validate_project_structure(".")

if issues:
    print("项目结构问题:")
    for issue in issues:
        print(f"- {issue}")
else:
    print("项目结构符合标准")
```

**返回示例**：
```python
[
    "缺少必要文件: setup.py",
    "缺少必要文件: requirements.txt",
    "缺少 tests 目录",
    "缺少 docs 目录"
]
```

## 综合使用示例

### 项目分析脚本

```python
from btools import ProjectUtils

# 分析项目
project_path = "."

print("=== 项目分析报告 ===")

# 检查项目类型
is_python = ProjectUtils.is_python_project(project_path)
print(f"项目类型: {'Python项目' if is_python else '非Python项目'}")

# 检查Git仓库
has_git = ProjectUtils.has_git_repository(project_path)
print(f"Git仓库: {'存在' if has_git else '不存在'}")

# 获取项目信息
info = ProjectUtils.get_project_info(project_path)
print(f"项目名称: {info.get('name')}")
print(f"项目版本: {info.get('version')}")
print(f"项目描述: {info.get('description')}")

# 分析依赖
dependencies = ProjectUtils.analyze_dependencies(project_path)
print(f"\n依赖分析:")
print(f"- requirements.txt: {len(dependencies['requirements'])} 个依赖")
print(f"- setup.py: {len(dependencies['setup'])} 个依赖")
print(f"- 当前安装: {len(dependencies['pip'])} 个包")

# 验证项目结构
issues = ProjectUtils.validate_project_structure(project_path)
if issues:
    print(f"\n项目结构问题:")
    for issue in issues:
        print(f"- {issue}")
else:
    print("\n项目结构符合标准")

# 获取项目结构
structure = ProjectUtils.get_project_structure(project_path)
print("\n项目结构:")
print(structure)
```

### 项目初始化检查

```python
from btools import ProjectUtils
import os

# 检查多个项目目录
projects = [".", "../other_project", "../another_project"]

for project in projects:
    if os.path.exists(project):
        print(f"\n=== 检查项目: {project} ===")
        
        # 检查是否为Python项目
        is_python = ProjectUtils.is_python_project(project)
        if not is_python:
            print("❌ 不是Python项目")
            continue
        
        print("✅ Python项目")
        
        # 验证项目结构
        issues = ProjectUtils.validate_project_structure(project)
        if issues:
            print("❌ 项目结构存在问题:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("✅ 项目结构符合标准")
            
        # 检查Git仓库
        has_git = ProjectUtils.has_git_repository(project)
        print(f"Git仓库: {'✅ 存在' if has_git else '❌ 不存在'}")
```

## 最佳实践

1. **项目初始化时**：使用 `validate_project_structure` 检查项目结构是否完整
2. **依赖管理**：定期使用 `analyze_dependencies` 检查依赖情况
3. **项目分析**：使用综合脚本定期生成项目分析报告
4. **自动化脚本**：在CI/CD流程中集成项目结构验证
5. **批量处理**：使用 `is_python_project` 和 `has_git_repository` 过滤项目

## 注意事项

- 依赖分析功能依赖于 `pip` 命令，需要确保环境中已安装 pip
- 项目信息提取基于文件解析，可能无法处理复杂的项目配置
- 项目结构验证基于标准Python项目结构，可根据实际需求调整
- 对于大型项目，`get_project_structure` 可能会返回较大的字典结构
