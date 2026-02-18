# -*- coding: utf-8 -*-
"""
XML工具类测试
"""
import unittest
import tempfile
import os
# 直接导入实现文件，避免加载整个包结构
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from btools.core.data.xmlutils import (
    XmlUtils, parse, parse_file, to_string, write_to_file,
    create_element, append_child, to_dict, from_dict,
    to_json, from_json, pretty_print
)


class TestXmlUtils(unittest.TestCase):
    """
    XML工具类测试
    """

    def setUp(self):
        """
        测试前的准备工作
        """
        self.test_xml = """
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
        
        # 创建临时文件，指定编码为UTF-8
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.xml', delete=False)
        self.temp_file.write(self.test_xml)
        self.temp_file.close()

    def tearDown(self):
        """
        测试后的清理工作
        """
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_parse(self):
        """
        测试XML解析
        """
        # 测试字符串解析
        root = parse(self.test_xml)
        self.assertEqual(root.tag, 'root')
        
        # 测试文件解析
        # 先读取文件内容，检查是否正确写入
        with open(self.temp_file.name, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"文件内容: {content}")
        
        root_from_file = parse_file(self.temp_file.name)
        self.assertEqual(root_from_file.tag, 'root')

    def test_to_string(self):
        """
        测试XML转换为字符串
        """
        root = parse(self.test_xml)
        xml_str = to_string(root)
        self.assertIn('<root>', xml_str)
        self.assertIn('<person>', xml_str)
        self.assertIn('张三', xml_str)

    def test_write_to_file(self):
        """
        测试XML写入文件
        """
        root = parse(self.test_xml)
        
        # 写入临时文件
        temp_out = tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False)
        temp_out.close()
        
        write_to_file(root, temp_out.name)
        
        # 验证文件存在且包含内容
        self.assertTrue(os.path.exists(temp_out.name))
        with open(temp_out.name, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('<root>', content)
        
        os.unlink(temp_out.name)

    def test_create_element(self):
        """
        测试创建XML元素
        """
        # 创建元素
        root = create_element('test')
        self.assertEqual(root.tag, 'test')
        
        # 创建带文本的元素
        elem = create_element('name', '测试')
        self.assertEqual(elem.tag, 'name')
        self.assertEqual(elem.text, '测试')
        
        # 创建带属性的元素
        elem_with_attr = create_element('item', '值', {'id': '1'})
        self.assertEqual(elem_with_attr.tag, 'item')
        self.assertEqual(elem_with_attr.text, '值')
        self.assertEqual(elem_with_attr.get('id'), '1')

    def test_append_child(self):
        """
        测试添加子元素
        """
        root = create_element('parent')
        child = append_child(root, 'child', '测试')
        
        self.assertEqual(child.tag, 'child')
        self.assertEqual(child.text, '测试')
        self.assertEqual(len(list(root)), 1)

    def test_xml_to_dict(self):
        """
        测试XML转字典
        """
        root = parse(self.test_xml)
        data = to_dict(root)
        
        self.assertIsInstance(data, dict)
        self.assertIn('person', data)
        self.assertEqual(data['person']['name'], '张三')
        self.assertEqual(data['person']['age'], '25')
        self.assertEqual(data['person']['address']['city'], '北京')

    def test_xml_from_dict(self):
        """
        测试字典转XML
        """
        data = {
            'person': {
                'name': '李四',
                'age': '30',
                'address': {
                    'city': '上海'
                }
            }
        }
        
        root = from_dict(data, 'root')
        self.assertEqual(root.tag, 'root')
        
        person = root.find('person')
        self.assertEqual(person.find('name').text, '李四')
        self.assertEqual(person.find('age').text, '30')
        self.assertEqual(person.find('address').find('city').text, '上海')

    def test_xml_to_json(self):
        """
        测试XML转JSON
        """
        root = parse(self.test_xml)
        json_str = to_json(root)
        
        self.assertIsInstance(json_str, str)
        self.assertIn('"name": "张三"', json_str)
        self.assertIn('"age": "25"', json_str)
        self.assertIn('"city": "北京"', json_str)

    def test_xml_from_json(self):
        """
        测试JSON转XML
        """
        json_str = '''
        {
            "person": {
                "name": "王五",
                "age": "35"
            }
        }
        '''
        
        root = from_json(json_str, 'root')
        self.assertEqual(root.tag, 'root')
        
        person = root.find('person')
        self.assertEqual(person.find('name').text, '王五')
        self.assertEqual(person.find('age').text, '35')

    def test_xml_pretty_print(self):
        """
        测试XML美化
        """
        xml_str = '<root><person><name>张三</name><age>25</age></person></root>'
        root = parse(xml_str)
        pretty_xml = pretty_print(root)
        
        self.assertIsInstance(pretty_xml, str)
        self.assertIn('\n', pretty_xml)  # 应该包含换行
        self.assertIn('  <name>', pretty_xml)  # 应该包含缩进

    def test_find_elements(self):
        """
        测试查找元素
        """
        root = parse(self.test_xml)
        
        # 查找单个元素
        person = root.find('person')
        self.assertIsNotNone(person)
        
        name = person.find('name')
        self.assertEqual(name.text, '张三')
        
        # 查找多个元素
        persons = root.findall('person')
        self.assertEqual(len(persons), 1)

    def test_modify_elements(self):
        """
        测试修改元素
        """
        root = parse(self.test_xml)
        
        # 修改元素文本
        name = root.find('.//name')
        name.text = '李四'
        self.assertEqual(name.text, '李四')
        
        # 修改元素属性
        person = root.find('person')
        person.set('id', '1')
        self.assertEqual(person.get('id'), '1')
        
        # 添加新元素
        phone = create_element('phone', '13800138000')
        person.append(phone)
        self.assertEqual(person.find('phone').text, '13800138000')

    def test_complex_structure(self):
        """
        测试复杂结构
        """
        # 创建复杂的XML结构
        root = create_element('company')
        
        info = append_child(root, 'info')
        append_child(info, 'name', '科技公司')
        append_child(info, 'established', '2020')
        
        # 添加多个员工
        for i in range(2):
            employee = append_child(root, 'employee', attributes={'id': str(i+1)})
            append_child(employee, 'name', f'员工{i+1}')
            append_child(employee, 'position', '工程师')
        
        # 转换为字典
        data = to_dict(root)
        self.assertIn('info', data)
        self.assertIn('employee', data)
        self.assertEqual(len(data['employee']), 2)
        
        # 转换回XML
        new_root = from_json(to_json(root), 'company')
        self.assertEqual(new_root.tag, 'company')

    def test_namespace_handling(self):
        """
        测试命名空间处理
        """
        namespace_xml = """
        <ns:root xmlns:ns="http://example.com">
            <ns:item id="1">
                <ns:name>测试</ns:name>
            </ns:item>
        </ns:root>
        """
        
        root = parse(namespace_xml)
        self.assertEqual(root.tag, '{http://example.com}root')
        
        # 测试获取命名空间
        namespaces = XmlUtils.get_namespaces(root)
        self.assertIsInstance(namespaces, dict)


if __name__ == '__main__':
    unittest.main()
