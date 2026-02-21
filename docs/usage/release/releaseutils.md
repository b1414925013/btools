# ReleaseUtils 使用指南

`ReleaseUtils` 类提供了发布工具，包括自动化版本号管理、CHANGELOG 生成等功能。

## 基本使用

### 版本管理

```python
from btools import ReleaseUtils

# 获取当前版本
current_version = ReleaseUtils.get_current_version(".")
print(f"当前版本: {current_version}")

# 增加主版本号 (1.0.0 -> 2.0.0)
new_version = ReleaseUtils.bump_major_version(".")
print(f"新版本: {new_version}")

# 增加次版本号 (1.0.0 -> 1.1.0)
new_version = ReleaseUtils.bump_minor_version(".")

# 增加修订版本号 (1.0.0 -> 1.0.1)
new_version = ReleaseUtils.bump_patch_version(".")

# 设置特定版本
success = ReleaseUtils.set_version(".", "1.2.3")
```

### 生成 CHANGELOG

```python
from btools import ReleaseUtils

# 生成 CHANGELOG
changelog = ReleaseUtils.generate_changelog(".")
print(changelog)

# 保存 CHANGELOG 到文件
success = ReleaseUtils.save_changelog(".", "CHANGELOG.md")

# 从 Git 提交生成 CHANGELOG
changelog = ReleaseUtils.generate_changelog_from_git(
    ".",
    from_commit="v1.0.0",
    to_commit="HEAD"
)
```

### 创建发布

```python
from btools import ReleaseUtils

# 创建发布
success = ReleaseUtils.create_release(
    version="1.0.0",
    notes="发布说明",
    project_path="."
)

# 创建预发布
success = ReleaseUtils.create_prerelease(
    version="1.0.0",
    prerelease_type="rc",  # alpha, beta, rc
    notes="预发布说明"
)
```

## 高级功能

### Git 标签

```python
from btools import ReleaseUtils

# 创建 Git 标签
success = ReleaseUtils.create_git_tag(
    version="1.0.0",
    message="Release 1.0.0",
    project_path="."
)

# 推送标签到远程
success = ReleaseUtils.push_git_tag(
    version="1.0.0",
    remote="origin",
    project_path="."
)

# 删除 Git 标签
success = ReleaseUtils.delete_git_tag(
    version="1.0.0",
    project_path="."
)
```

### 版本验证

```python
from btools import ReleaseUtils

# 验证版本号格式
is_valid = ReleaseUtils.validate_version("1.2.3")
is_valid_pre = ReleaseUtils.validate_version("1.2.3-beta.1")

# 比较版本
result = ReleaseUtils.compare_versions("1.2.0", "1.1.0")
# 返回: 1 (大于), 0 (等于), -1 (小于)

# 检查是否为预发布
is_prerelease = ReleaseUtils.is_prerelease("1.2.3-beta.1")
```

### 发布检查清单

```python
from btools import ReleaseUtils

# 检查发布准备情况
checklist = ReleaseUtils.check_release_readiness(".")
print(checklist)

# 生成发布报告
report = ReleaseUtils.generate_release_report(
    version="1.0.0",
    previous_version="0.9.0",
    project_path="."
)
print(report)
```

### 自动化发布流程

```python
from btools import ReleaseUtils

# 完整的发布流程
success = ReleaseUtils.full_release(
    version="1.0.0",
    release_notes="发布说明",
    create_tag=True,
    push_tag=True,
    project_path="."
)

# 预发布流程
success = ReleaseUtils.full_prerelease(
    version="1.0.0",
    prerelease_type="rc",
    release_notes="预发布说明",
    project_path="."
)
```

## CHANGELOG 格式

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2024-01-01

### Added
- 新功能 A
- 新功能 B

### Changed
- 修改了功能 C

### Fixed
- 修复了 Bug D

### Removed
- 移除了功能 E
```

## 语义化版本规范

- **主版本号 (MAJOR)**: 不兼容的 API 修改
- **次版本号 (MINOR)**: 向下兼容的功能性新增
- **修订版本号 (PATCH)**: 向下兼容的问题修正

示例：
- `1.0.0` - 稳定版本
- `1.0.0-alpha.1` - Alpha 预发布
- `1.0.0-beta.2` - Beta 预发布
- `1.0.0-rc.1` - 发布候选
