# XmlUtils 使用指南

`XmlUtils` 类提供了XML的解析、生成、转换、验证等功能，支持XML与字典/JSON的相互转换，是处理XML数据的综合工具类。

## 基本使用

### 导入方式

```python
from btools import XmlUtils

# 或使用便捷函数
from btools import (
    parse_xml, parse_xml_file, to_xml_string, write_xml_file,
    create_xml_element, append_xml_child, xml_to_dict,
    xml_from_dict, xml_to_json, xml_from_json, xml_pretty_print
)
```

## XML 解析

### 解析 XML 字符串

```python
from btools import parse_xml, to_xml_string

# XML 字符串
xml_str = """
<root>
    <person>
        <name>张三</name>
        <age>25</age>
        <address>
            <city>北京</city>
            <street>中山路</street>
        </address>
    </person>
</root>
"""

# 解析 XML
root = parse_xml(xml_str)

# 获取元素
person = root.find('person')
name = person.find('name').text
age = person.find('age').text

print(f"姓名: {name}")
print(f"年龄: {age}")

# 转换回字符串
result_str = to_xml_string(root)
print(f"XML 字符串: {result_str}")
```

### 从文件解析 XML

```python
from btools import parse_xml_file

# 从文件解析
root = parse_xml_file('data.xml')

# 获取元素
print(f"根元素: {root.tag}")

# 遍历子元素
for child in root:
    print(f"子元素: {child.tag}, 文本: {child.text}")
```

## XML 生成

### 创建 XML 元素

```python
from btools import create_xml_element, append_xml_child, to_xml_string

# 创建根元素
root = create_xml_element('company')

# 添加子元素
info = append_xml_child(root, 'info')
append_xml_child(info, 'name', '科技公司')
append_xml_child(info, 'established', '2020')

# 添加带属性的元素
employee = append_xml_child(root, 'employee', attributes={'id': '1'})
append_xml_child(employee, 'name', '李四')
append_xml_child(employee, 'position', '工程师')
append_xml_child(employee, 'salary', '10000')

# 添加多个员工
employee2 = append_xml_child(root, 'employee', attributes={'id': '2'})
append_xml_child(employee2, 'name', '王五')
append_xml_child(employee2, 'position', '经理')
append_xml_child(employee2, 'salary', '15000')

# 转换为字符串
xml_str = to_xml_string(root, encoding='utf-8', xml_declaration=True)
print(xml_str)

# 写入文件
from btools import write_xml_file
write_xml_file(root, 'company.xml', encoding='utf-8')
```

## XML 操作

### 查找元素

```python
from btools import parse_xml

xml_str = """
<library>
    <book category="fiction">
        <title>小说标题</title>
        <author>作者A</author>
        <price>29.99</price>
    </book>
    <book category="nonfiction">
        <title>非小说标题</title>
        <author>作者B</author>
        <price>39.99</price>
    </book>
</library>
"""

root = parse_xml(xml_str)

# 查找单个元素
first_book = root.find('book')
print(f"第一本书: {first_book.find('title').text}")

# 查找多个元素
books = root.findall('book')
print(f"共有 {len(books)} 本书")

# 按属性查找
for book in books:
    category = book.get('category')
    title = book.find('title').text
    print(f"分类: {category}, 标题: {title}")
```

### 修改 XML

```python
from btools import parse_xml, to_xml_string

xml_str = """
<user>
    <id>1</id>
    <name>张三</name>
    <email>zhangsan@example.com</email>
</user>
"""

root = parse_xml(xml_str)

# 修改元素文本
name_elem = root.find('name')
name_elem.text = '李四'

# 修改属性
root.set('updated', 'true')

# 添加新元素
phone_elem = root.makeelement('phone', {})
phone_elem.text = '13800138000'
root.append(phone_elem)

# 删除元素
email_elem = root.find('email')
root.remove(email_elem)

# 查看结果
print(to_xml_string(root))
```

## XML 转换

### XML 转字典

```python
from btools import parse_xml, xml_to_dict

xml_str = """
<response>
    <code>200</code>
    <message>success</message>
    <data>
        <user>
            <id>123</id>
            <name>张三</name>
            <tags>
                <tag>admin</tag>
                <tag>user</tag>
            </tags>
        </user>
    </data>
</response>
"""

root = parse_xml(xml_str)

# 转换为字典
data = xml_to_dict(root)
print(f"转换结果: {data}")

# 访问数据
print(f"状态码: {data['code']}")
print(f"消息: {data['message']}")
print(f"用户名: {data['data']['user']['name']}")
print(f"标签: {data['data']['user']['tags']['tag']}")
```

### 字典转 XML

```python
from btools import xml_from_dict, to_xml_string

# 准备字典数据
data = {
    'students': {
        'student': [
            {
                '@attributes': {'id': '1'},
                'name': '张三',
                'age': '20',
                'grade': 'A'
            },
            {
                '@attributes': {'id': '2'},
                'name': '李四',
                'age': '21',
                'grade': 'B'
            }
        ]
    }
}

# 转换为 XML
root = xml_from_dict(data, root_tag='school')

# 查看结果
print(to_xml_string(root, xml_declaration=True))
```

### XML 转 JSON

```python
from btools import parse_xml, xml_to_json

xml_str = """
<config>
    <server>
        <host>localhost</host>
        <port>8080</port>
        <ssl>false</ssl>
    </server>
    <database>
        <url>jdbc:mysql://localhost:3306/db</url>
        <username>root</username>
        <password>password</password>
    </database>
</config>
"""

root = parse_xml(xml_str)

# 转换为 JSON
json_str = xml_to_json(root, indent=2)
print(json_str)
```

### JSON 转 XML

```python
from btools import xml_from_json, to_xml_string

json_str = '''
{
  "api": {
    "endpoint": "/api/v1/users",
    "method": "GET",
    "headers": {
      "Content-Type": "application/json",
      "Authorization": "Bearer token"
    },
    "params": {
      "page": "1",
      "limit": "10"
    }
  }
}
'''

# 转换为 XML
root = xml_from_json(json_str, root_tag='request')

# 查看结果
print(to_xml_string(root, xml_declaration=True))
```

## XML 美化

### 美化 XML 输出

```python
from btools import parse_xml, xml_pretty_print

xml_str = "<root><person><name>张三</name><age>25</age></person></root>"

root = parse_xml(xml_str)

# 美化输出
pretty_xml = xml_pretty_print(root)
print(pretty_xml)
```

## XML 验证

### 使用 XSD 验证 XML

```python
from btools import parse_xml, XmlUtils

xml_str = """
<product>
    <id>1</id>
    <name>手机</name>
    <price>2999</price>
    <stock>100</stock>
</product>
"""

# XSD 文件内容 (保存为 product.xsd)
"""
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="product">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="id" type="xs:integer"/>
                <xs:element name="name" type="xs:string"/>
                <xs:element name="price" type="xs:decimal"/>
                <xs:element name="stock" type="xs:integer"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>
"""

root = parse_xml(xml_str)

# 验证 (需要安装 lxml 库)
is_valid = XmlUtils.validate(xml_str, 'product.xsd')
print(f"XML 验证结果: {is_valid}")
```

## 命名空间处理

### 处理命名空间

```python
from btools import parse_xml, XmlUtils

xml_str = """
<ns:root xmlns:ns="http://example.com">
    <ns:item id="1">
        <ns:name>测试</ns:name>
    </ns:item>
</ns:root>
"""

root = parse_xml(xml_str)

# 获取命名空间
namespaces = XmlUtils.get_namespaces(root)
print(f"命名空间: {namespaces}")

# 使用命名空间查找
# 注意: 标准库的 find 方法需要指定完整的标签名
# 或者使用 XPath
items = root.findall('.//{http://example.com}item')
for item in items:
    print(f"项目 ID: {item.get('id')}")
    name = item.find('.//{http://example.com}name').text
    print(f"项目名称: {name}")
```

## 实际应用示例

### 配置文件处理

```python
from btools import parse_xml_file, xml_to_dict, xml_from_dict, write_xml_file

# 读取配置文件
root = parse_xml_file('config.xml')

# 转换为字典
config_dict = xml_to_dict(root)
print(f"配置: {config_dict}")

# 修改配置
config_dict['database']['password'] = 'new_password'
config_dict['server']['port'] = '8081'

# 转换回 XML
new_root = xml_from_dict(config_dict, root_tag='config')

# 保存配置
write_xml_file(new_root, 'config.xml')
print("配置已更新")
```

### Web 服务响应处理

```python
from btools import parse_xml, xml_to_dict
import requests

# 假设这是一个返回 XML 的 API
response = requests.get('https://api.example.com/users')
xml_response = response.text

# 解析响应
root = parse_xml(xml_response)

# 转换为字典以便处理
data = xml_to_dict(root)

# 处理数据
users = data.get('users', {}).get('user', [])
print(f"共获取 {len(users)} 个用户")

for user in users:
    print(f"用户: {user['name']}, 邮箱: {user['email']}")
```

### 生成 RSS 订阅

```python
from btools import create_xml_element, append_xml_child, write_xml_file

# 创建 RSS 根元素
rss = create_xml_element('rss', attributes={
    'version': '2.0',
    'xmlns:atom': 'http://www.w3.org/2005/Atom'
})

# 添加频道
channel = append_xml_child(rss, 'channel')
append_xml_child(channel, 'title', '博客订阅')
append_xml_child(channel, 'link', 'https://blog.example.com')
append_xml_child(channel, 'description', '技术博客更新')
append_xml_child(channel, 'language', 'zh-CN')

# 添加文章
items = [
    {
        'title': 'Python 入门教程',
        'link': 'https://blog.example.com/python-basics',
        'description': 'Python 基础语法学习',
        'pubDate': 'Thu, 01 Jan 2024 12:00:00 GMT'
    },
    {
        'title': 'XML 处理技巧',
        'link': 'https://blog.example.com/xml-tips',
        'description': 'XML 数据处理的实用技巧',
        'pubDate': 'Fri, 02 Jan 2024 10:30:00 GMT'
    }
]

for item_data in items:
    item = append_xml_child(channel, 'item')
    for key, value in item_data.items():
        append_xml_child(item, key, value)

# 保存为文件
write_xml_file(rss, 'rss.xml')
print("RSS 订阅文件已生成")
```

## 高级功能

### 使用 XPath 查找

```python
from btools import parse_xml

xml_str = """
<library>
    <book category="fiction">
        <title>小说1</title>
        <author>作者A</author>
        <price>29.99</price>
    </book>
    <book category="nonfiction">
        <title>非小说1</title>
        <author>作者B</author>
        <price>39.99</price>
    </book>
    <book category="fiction">
        <title>小说2</title>
        <author>作者C</author>
        <price>25.99</price>
    </book>
</library>
"""

root = parse_xml(xml_str)

# 使用 XPath 查找所有小说
fiction_books = root.findall(".//book[@category='fiction']")
print(f"小说数量: {len(fiction_books)}")

# 查找所有书的标题
for book in root.findall(".//title"):
    print(f"书名: {book.text}")
```

### 复杂数据结构转换

```python
from btools import xml_from_dict, to_xml_string

# 复杂数据结构
data = {
    'company': {
        '@attributes': {'id': '123'},
        'name': '科技有限公司',
        'employees': {
            'employee': [
                {
                    '@attributes': {'id': '1'},
                    'name': '张三',
                    'department': '开发部',
                    'skills': {
                        'skill': ['Python', 'Java', 'SQL']
                    }
                },
                {
                    '@attributes': {'id': '2'},
                    'name': '李四',
                    'department': '设计部',
                    'skills': {
                        'skill': ['Photoshop', 'Illustrator']
                    }
                }
            ]
        },
        'address': {
            'city': '北京',
            'district': '朝阳区',
            'street': '建国路',
            'zipcode': '100000'
        }
    }
}

# 转换为 XML
root = xml_from_dict(data)

# 查看结果
print(to_xml_string(root, xml_declaration=True))
```

## 常见问题

### Q: 如何处理 XML 中的特殊字符？

A: XML 中的特殊字符需要进行转义，或者使用 CDATA 部分：

```python
from btools import create_xml_element, append_xml_child, to_xml_string

root = create_xml_element('data')

# 使用转义字符
text_elem = append_xml_child(root, 'text', '这是 <b>加粗</b> 文本')

# 使用 CDATA
cdata_elem = root.makeelement('cdata', {})
cdata_elem.text = '<![CDATA[这是 <b>加粗</b> 文本]]>'
root.append(cdata_elem)

print(to_xml_string(root))
```

### Q: 如何处理大型 XML 文件？

A: 对于大型 XML 文件，建议使用迭代解析：

```python
import xml.etree.ElementTree as ET

# 迭代解析大型 XML
for event, elem in ET.iterparse('large_file.xml'):
    if elem.tag == 'record':
        # 处理记录
        print(f"处理记录: {elem.find('id').text}")
        # 清理元素以节省内存
        elem.clear()
```

### Q: 如何处理 XML 命名空间？

A: 可以使用 lxml 库获得更好的命名空间支持：

```python
# 需要安装 lxml: pip install lxml
from lxml import etree

xml_str = """
<ns:root xmlns:ns="http://example.com">
    <ns:item>测试</ns:item>
</ns:root>
"""

# 使用 lxml 解析
tree = etree.fromstring(xml_str)

# 定义命名空间映射
nsmap = {'ns': 'http://example.com'}

# 使用命名空间查找
item = tree.xpath('//ns:item', namespaces=nsmap)
print(f"找到: {item[0].text}")
```

## 总结

`XmlUtils` 提供了全面的 XML 处理功能，包括：

- **解析与生成**：支持从字符串、文件解析 XML，以及创建新的 XML 文档
- **转换功能**：支持 XML 与字典/JSON 的相互转换
- **操作与修改**：支持查找、修改、添加、删除 XML 元素
- **验证与美化**：支持 XSD 验证和 XML 美化输出
- **命名空间处理**：支持处理带有命名空间的 XML

这些功能使得 `XmlUtils` 成为处理 XML 数据的强大工具，可以应用于配置文件、Web 服务、数据交换等多种场景。