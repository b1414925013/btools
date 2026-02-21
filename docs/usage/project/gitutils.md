# GitUtils 使用指南

`GitUtils` 类提供了 Git 操作封装，包括分支管理、提交规范检查等功能。

## 基本使用

### 获取分支信息

```python
from btools import GitUtils

# 获取当前分支
current_branch = GitUtils.get_current_branch(".")
print(f"当前分支: {current_branch}")

# 获取所有分支
branches = GitUtils.get_branches(".")
print(f"所有分支: {branches}")
```

### 分支操作

```python
from btools import GitUtils

# 创建新分支
success = GitUtils.create_branch("feature/new-feature", ".")
if success:
    print("分支创建成功")

# 切换分支
success = GitUtils.checkout_branch("main", ".")
if success:
    print("分支切换成功")

# 删除分支
success = GitUtils.delete_branch("feature/old-feature", ".")
if success:
    print("分支删除成功")
```

### 提交操作

```python
from btools import GitUtils

# 添加文件到暂存区
success = GitUtils.add(".", ".")

# 提交更改
success = GitUtils.commit("feat: 添加新功能", ".")

# 推送到远程仓库
success = GitUtils.push("origin", "main", ".")

# 拉取远程更改
success = GitUtils.pull("origin", "main", ".")
```

### 查看状态和日志

```python
from btools import GitUtils

# 查看状态
status = GitUtils.get_status(".")
print(status)

# 查看最近的提交
commits = GitUtils.get_commits(".", count=10)
for commit in commits:
    print(f"{commit['hash']}: {commit['message']}")
```

### 提交规范检查

```python
from btools import GitUtils

# 检查提交信息是否符合规范
is_valid = GitUtils.validate_commit_message("feat: 添加新功能")
if is_valid:
    print("提交信息规范")

# 检查最近的提交
invalid_commits = GitUtils.check_recent_commits(".", count=10)
if invalid_commits:
    print("不符合规范的提交:", invalid_commits)
```

## 高级功能

### 合并和变基

```python
from btools import GitUtils

# 合并分支
success = GitUtils.merge("feature/branch", ".")

# 变基
success = GitUtils.rebase("main", ".")
```

### 标签操作

```python
from btools import GitUtils

# 创建标签
success = GitUtils.create_tag("v1.0.0", "Release version 1.0.0", ".")

# 列出所有标签
tags = GitUtils.get_tags(".")
print("标签:", tags)

# 推送标签
success = GitUtils.push_tags("origin", ".")
```

### 暂存操作

```python
from btools import GitUtils

# 暂存更改
success = GitUtils.stash("save my changes", ".")

# 列出暂存
stashes = GitUtils.list_stashes(".")
print("暂存列表:", stashes)

# 应用暂存
success = GitUtils.stash_pop(".")
```

## 提交规范

支持的提交类型：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建/工具链相关

提交信息格式：`<type>: <description>`
