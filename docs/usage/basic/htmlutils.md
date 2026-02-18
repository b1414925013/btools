# HtmlUtil - HTML工具类

## 功能特性

`HtmlUtil` 是一个HTML工具类，提供了丰富的HTML处理功能，包括：

- HTML转义与反转义
- 移除HTML标签
- 提取HTML文本内容
- 获取和设置HTML标签属性
- 格式化和压缩HTML
- 检查字符串是否为HTML
- 包装HTML文档
- 创建HTML标签
- 获取和替换HTML标签
- 添加和移除HTML标签的类
- 获取和设置HTML标签的内部内容

## 基本用法

### 导入模块

```python
from btools.core.basic import HtmlUtil
```

### 1. HTML转义与反转义

```python
# HTML转义
html = "<div>hello & world</div>"
escaped = HtmlUtil.escape(html)
print(f"转义后: {escaped}")
# 输出: 转义后: &lt;div&gt;hello &amp; world&lt;/div&gt;

# HTML反转义
unescaped = HtmlUtil.unescape(escaped)
print(f"反转义后: {unescaped}")
# 输出: 反转义后: <div>hello & world</div>
```

### 2. 移除HTML标签

```python
# 移除HTML标签
html = "<div>hello <b>world</b></div>"
text = HtmlUtil.removeHtmlTags(html)
print(f"移除标签后: {text}")
# 输出: 移除标签后: hello world
```

### 3. 提取HTML文本内容

```python
# 提取HTML文本内容（会自动反转义）
html = "<div>hello &lt;b&gt;world&lt;/b&gt;</div>"
text = HtmlUtil.extractText(html)
print(f"提取文本后: {text}")
# 输出: 提取文本后: hello <b>world</b>
```

### 4. 获取和设置HTML标签属性

```python
# 获取HTML标签的属性值
html = '<div class="test" id="test-id">content</div>'
class_attr = HtmlUtil.getAttribute(html, "div", "class")
print(f"class属性: {class_attr}")
# 输出: class属性: test

# 设置HTML标签的属性值
updated_html = HtmlUtil.setAttribute(html, "div", "class", "new-class")
print(f"设置属性后: {updated_html}")
# 输出: 设置属性后: <div class="new-class" id="test-id">content</div>

# 移除HTML标签的属性
updated_html = HtmlUtil.removeAttribute(html, "div", "class")
print(f"移除属性后: {updated_html}")
# 输出: 移除属性后: <div  id="test-id">content</div>
```

### 5. 格式化和压缩HTML

```python
# 格式化HTML
html = '<div><p>hello</p><p>world</p></div>'
formatted = HtmlUtil.formatHtml(html)
print(f"格式化后:\n{formatted}")
# 输出:
# <div>
#   <p>hello</p>
#   <p>world</p>
# </div>

# 压缩HTML
html = '''
<div>
    <p>hello</p>
    <p>world</p>
</div>
'''
minified = HtmlUtil.minifyHtml(html)
print(f"压缩后: {minified}")
# 输出: 压缩后: <div><p>hello</p><p>world</p></div>
```

### 6. 检查字符串是否为HTML

```python
# 检查字符串是否为HTML
text = "hello"
is_html = HtmlUtil.isHtml(text)
print(f"'hello'是否为HTML: {is_html}")
# 输出: 'hello'是否为HTML: False

html = "<div>hello</div>"
is_html = HtmlUtil.isHtml(html)
print(f"'<div>hello</div>'是否为HTML: {is_html}")
# 输出: '<div>hello</div>'是否为HTML: True
```

### 7. 包装HTML文档

```python
# 包装HTML文档
body = "<p>Hello, World!</p>"
html = HtmlUtil.wrapHtml(body, "Test Page")
print(f"包装后:\n{html}")
# 输出:
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Test Page</title>
# </head>
# <body>
#     <p>Hello, World!</p>
# </body>
# </html>
```

### 8. 创建HTML标签

```python
# 创建无属性无内容的标签
tag = HtmlUtil.createTag("div")
print(f"创建的标签: {tag}")
# 输出: 创建的标签: <div />

# 创建有属性无内容的标签
tag = HtmlUtil.createTag("img", {"src": "test.jpg", "alt": "test"})
print(f"创建的标签: {tag}")
# 输出: 创建的标签: <img src="test.jpg" alt="test" />

# 创建有属性有内容的标签
tag = HtmlUtil.createTag("div", {"class": "test"}, "hello")
print(f"创建的标签: {tag}")
# 输出: 创建的标签: <div class="test">hello</div>
```

### 9. 获取和替换HTML标签

```python
# 获取HTML中指定标签的所有实例
html = '<div>first</div><div>second</div>'
tags = HtmlUtil.getTags(html, "div")
print(f"获取的标签数量: {len(tags)}")
print(f"第一个标签: {tags[0]}")
print(f"第二个标签: {tags[1]}")
# 输出:
# 获取的标签数量: 2
# 第一个标签: <div>first</div>
# 第二个标签: <div>second</div>

# 替换HTML标签名
updated_html = HtmlUtil.replaceTag(html, "div", "span")
print(f"替换标签后: {updated_html}")
# 输出: 替换标签后: <span>first</span><span>second</span>
```

### 10. 添加和移除HTML标签的类

```python
# 为HTML标签添加类
html = '<div>hello</div>'
updated_html = HtmlUtil.addClass(html, "div", "test")
print(f"添加类后: {updated_html}")
# 输出: 添加类后: <div  class="test">hello</div>

# 为已有类的标签添加类
html = '<div class="old">hello</div>'
updated_html = HtmlUtil.addClass(html, "div", "new")
print(f"添加类后: {updated_html}")
# 输出: 添加类后: <div class="old new">hello</div>

# 从HTML标签移除类
html = '<div class="old new">hello</div>'
updated_html = HtmlUtil.removeClass(html, "div", "old")
print(f"移除类后: {updated_html}")
# 输出: 移除类后: <div class="new">hello</div>
```

### 11. 获取和设置HTML标签的内部内容

```python
# 获取HTML标签的内部内容
html = '<div>hello <b>world</b></div>'
inner_html = HtmlUtil.getInnerHtml(html, "div")
print(f"内部内容: {inner_html}")
# 输出: 内部内容: hello <b>world</b>

# 设置HTML标签的内部内容
updated_html = HtmlUtil.setInnerHtml(html, "div", "new content")
print(f"设置内部内容后: {updated_html}")
# 输出: 设置内部内容后: <div>new content</div>
```

## 高级用法

### 1. 批量处理HTML标签

```python
# 批量处理HTML标签
html = '''
<div class="item">item 1</div>
<div class="item">item 2</div>
<div class="item">item 3</div>
'''

# 为所有div标签添加类
updated_html = html
for i in range(3):
    updated_html = HtmlUtil.addClass(updated_html, "div", f"item-{i+1}")

print(f"批量添加类后:\n{updated_html}")
# 输出:
# <div class="item item-1">item 1</div>
# <div class="item item-2">item 2</div>
# <div class="item item-3">item 3</div>
```

### 2. 构建复杂的HTML结构

```python
# 构建复杂的HTML结构
def build_nav_menu(items):
    """构建导航菜单"""
    # 创建ul标签
    ul_attrs = {"class": "nav-menu"}
    ul_content = ""
    
    # 创建li标签
    for item in items:
        li_attrs = {"class": "nav-item"}
        a_attrs = {"href": item["href"]}
        a_tag = HtmlUtil.createTag("a", a_attrs, item["text"])
        li_tag = HtmlUtil.createTag("li", li_attrs, a_tag)
        ul_content += li_tag
    
    return HtmlUtil.createTag("ul", ul_attrs, ul_content)

# 测试构建导航菜单
menu_items = [
    {"text": "Home", "href": "/"},
    {"text": "About", "href": "/about"},
    {"text": "Contact", "href": "/contact"}
]

nav_menu = build_nav_menu(menu_items)
print(f"构建的导航菜单: {nav_menu}")
# 输出: 构建的导航菜单: <ul class="nav-menu"><li class="nav-item"><a href="/">Home</a></li><li class="nav-item"><a href="/about">About</a></li><li class="nav-item"><a href="/contact">Contact</a></li></ul>
```

### 3. HTML模板处理

```python
# HTML模板处理
def render_template(template, context):
    """渲染HTML模板"""
    html = template
    for key, value in context.items():
        # 转义值以防止XSS攻击
        escaped_value = HtmlUtil.escape(str(value))
        html = html.replace(f"{{{{{key}}}}}", escaped_value)
    return html

# 测试渲染模板
template = '''
<div class="user-profile">
    <h1>{{name}}</h1>
    <p>{{email}}</p>
    <p>{{bio}}</p>
</div>
'''

context = {
    "name": "John Doe",
    "email": "john@example.com",
    "bio": "<b>Software Engineer</b>"
}

rendered = render_template(template, context)
print(f"渲染后的模板:\n{rendered}")
# 输出:
# <div class="user-profile">
#     <h1>John Doe</h1>
#     <p>john@example.com</p>
#     <p>&lt;b&gt;Software Engineer&lt;/b&gt;</p>
# </div>
```

### 4. 清理用户输入的HTML

```python
# 清理用户输入的HTML
def sanitize_html(html):
    """清理用户输入的HTML"""
    # 移除所有标签，只保留文本
    text = HtmlUtil.removeHtmlTags(html)
    # 转义文本，确保安全显示
    return HtmlUtil.escape(text)

# 测试清理HTML
user_input = '<script>alert("XSS")</script> <b>Hello</b>'
sanitized = sanitize_html(user_input)
print(f"清理前: {user_input}")
print(f"清理后: {sanitized}")
# 输出:
# 清理前: <script>alert("XSS")</script> <b>Hello</b>
# 清理后: alert("XSS") Hello
```

## 注意事项

1. **安全考虑**：处理用户输入的HTML时，应使用 `escape` 方法转义，以防止XSS攻击。

2. **性能考虑**：对于大型HTML文档，频繁的正则表达式操作可能会影响性能，建议使用专业的HTML解析库（如BeautifulSoup）。

3. **HTML格式**：`HtmlUtil` 使用正则表达式处理HTML，对于格式不规范的HTML可能会出现意外结果。

4. **标签嵌套**：`getTags` 方法在处理嵌套标签时可能会返回包含子标签的完整内容，这是正则表达式的局限性。

5. **属性值**：`getAttribute` 方法只支持引号包裹的属性值，不支持无引号的属性值。

6. **字符编码**：处理HTML时应注意字符编码，确保使用正确的编码（如UTF-8）。

## 总结

`HtmlUtil` 提供了全面的HTML处理功能，简化了HTML的操作和管理。通过这些工具方法，您可以更方便地处理HTML相关的任务，如转义、标签处理、属性操作等。