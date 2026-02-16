# TemplateUtils 使用指南

`TemplateUtils` 是一个模板工具类，提供了丰富的模板操作方法，包括模板渲染、HTML转义等功能。

## 功能特性

- 模板渲染
- HTML转义

## 基本用法

### 导入

```python
from btools import TemplateUtils
```

### 示例

#### 模板渲染

```python
# 渲染模板
template = "Hello, {{ name }}!"
data = {"name": "World"}
result = TemplateUtils.render_template(template, data)
print(result)  # 输出: Hello, World!

# 渲染复杂模板
template = "Name: {{ name }}, Age: {{ age }}, City: {{ city }}"
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
result = TemplateUtils.render_template(template, data)
print(result)  # 输出: Name: John, Age: 30, City: New York
```

#### HTML转义

```python
# HTML转义
data = "<html>Hello</html>"
escaped = TemplateUtils.escape_html(data)
print(escaped)  # 输出: &lt;html&gt;Hello&lt;/html&gt;

# 渲染包含HTML的模板
template = "Content: {{ content }}"
data = {
    "content": "<script>alert('XSS')</script>"
}
result = TemplateUtils.render_template(template, data)
print(result)  # 输出: Content: &lt;script&gt;alert('XSS')&lt;/script&gt;
```

## 高级用法

### 嵌套模板

```python
# 嵌套模板
user_template = "Name: {{ name }}, Email: {{ email }}"
address_template = "City: {{ city }}, Country: {{ country }}"

data = {
    "user": {
        "name": "John",
        "email": "john@example.com"
    },
    "address": {
        "city": "New York",
        "country": "USA"
    }
}

# 渲染用户信息
user_html = TemplateUtils.render_template(user_template, data["user"])

# 渲染地址信息
address_html = TemplateUtils.render_template(address_template, data["address"])

# 组合结果
result = f"<h2>User Info</h2>{user_html}<h2>Address</h2>{address_html}"
print(result)
# 输出:
# <h2>User Info</h2>Name: John, Email: john@example.com<h2>Address</h2>City: New York, Country: USA
```

### 条件渲染

```python
# 条件渲染
template = "{% if is_admin %}Admin Panel{% else %}User Panel{% endif %}"

# 渲染管理员面板
data1 = {"is_admin": True}
result1 = TemplateUtils.render_template(template, data1)
print(result1)  # 输出: Admin Panel

# 渲染用户面板
data2 = {"is_admin": False}
result2 = TemplateUtils.render_template(template, data2)
print(result2)  # 输出: User Panel
```

### 循环渲染

```python
# 循环渲染
template = "<ul>{% for item in items %}<li>{{ item }}</li>{% endfor %}</ul>"
data = {"items": ["Item 1", "Item 2", "Item 3"]}
result = TemplateUtils.render_template(template, data)
print(result)
# 输出:
# <ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>
```

## 注意事项

1. 模板渲染默认会对变量进行HTML转义，以防止XSS攻击。
2. 模板语法支持基本的条件判断和循环操作。

## 总结

`TemplateUtils` 提供了基本的模板操作功能，简化了模板处理的复杂度，使代码更加简洁易读。无论是基本的模板渲染还是高级的模板操作，`TemplateUtils` 都能满足你的需求。