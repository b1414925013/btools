# -*- coding: utf-8 -*-
"""
XML工具类模块
提供XML的解析、生成、转换等功能
"""
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Union, Any, Tuple
import json
import io


class XmlUtils:
    """
    XML工具类
    提供XML的解析、生成、转换等功能
    """

    @staticmethod
    def parse(xml_data: Union[str, bytes, io.BytesIO]) -> ET.Element:
        """
        解析XML数据

        Args:
            xml_data: XML数据，可以是字符串、字节或BytesIO对象

        Returns:
            ET.Element: XML根元素
        """
        if isinstance(xml_data, bytes):
            return ET.fromstring(xml_data)
        elif isinstance(xml_data, io.BytesIO):
            return ET.parse(xml_data).getroot()
        else:
            return ET.fromstring(xml_data)

    @staticmethod
    def parse_file(file_path: str) -> ET.Element:
        """
        从文件解析XML

        Args:
            file_path: XML文件路径

        Returns:
            ET.Element: XML根元素
        """
        tree = ET.parse(file_path)
        return tree.getroot()

    @staticmethod
    def to_string(element: ET.Element, encoding: str = 'utf-8', xml_declaration: bool = True, 
                  default_namespace: Optional[str] = None) -> str:
        """
        将XML元素转换为字符串

        Args:
            element: XML元素
            encoding: 编码
            xml_declaration: 是否包含XML声明
            default_namespace: 默认命名空间

        Returns:
            str: XML字符串
        """
        if default_namespace:
            # 处理默认命名空间
            ET.register_namespace('', default_namespace)
        
        xml_str = ET.tostring(element, encoding=encoding, xml_declaration=xml_declaration, 
                              method='xml').decode(encoding)
        return xml_str

    @staticmethod
    def write_to_file(element: ET.Element, file_path: str, encoding: str = 'utf-8', 
                      xml_declaration: bool = True):
        """
        将XML元素写入文件

        Args:
            element: XML元素
            file_path: 文件路径
            encoding: 编码
            xml_declaration: 是否包含XML声明
        """
        tree = ET.ElementTree(element)
        tree.write(file_path, encoding=encoding, xml_declaration=xml_declaration)

    @staticmethod
    def create_element(tag: str, text: Optional[str] = None, 
                      attributes: Optional[Dict[str, str]] = None) -> ET.Element:
        """
        创建XML元素

        Args:
            tag: 标签名
            text: 文本内容
            attributes: 属性字典

        Returns:
            ET.Element: XML元素
        """
        element = ET.Element(tag)
        if text:
            element.text = text
        if attributes:
            element.attrib.update(attributes)
        return element

    @staticmethod
    def append_child(parent: ET.Element, tag: str, text: Optional[str] = None, 
                    attributes: Optional[Dict[str, str]] = None) -> ET.Element:
        """
        向父元素添加子元素

        Args:
            parent: 父元素
            tag: 子元素标签名
            text: 子元素文本内容
            attributes: 子元素属性字典

        Returns:
            ET.Element: 新创建的子元素
        """
        child = XmlUtils.create_element(tag, text, attributes)
        parent.append(child)
        return child

    @staticmethod
    def find(element: ET.Element, path: str) -> Optional[ET.Element]:
        """
        查找单个元素

        Args:
            element: 起始元素
            path: XPath路径

        Returns:
            Optional[ET.Element]: 找到的元素，未找到返回None
        """
        return element.find(path)

    @staticmethod
    def find_all(element: ET.Element, path: str) -> List[ET.Element]:
        """
        查找多个元素

        Args:
            element: 起始元素
            path: XPath路径

        Returns:
            List[ET.Element]: 找到的元素列表
        """
        return element.findall(path)

    @staticmethod
    def get_text(element: ET.Element, default: str = '') -> str:
        """
        获取元素文本

        Args:
            element: XML元素
            default: 默认值

        Returns:
            str: 元素文本
        """
        return element.text.strip() if element.text else default

    @staticmethod
    def get_attribute(element: ET.Element, name: str, default: str = '') -> str:
        """
        获取元素属性

        Args:
            element: XML元素
            name: 属性名
            default: 默认值

        Returns:
            str: 属性值
        """
        return element.attrib.get(name, default)

    @staticmethod
    def set_attribute(element: ET.Element, name: str, value: str):
        """
        设置元素属性

        Args:
            element: XML元素
            name: 属性名
            value: 属性值
        """
        element.set(name, value)

    @staticmethod
    def remove(element: ET.Element, child: ET.Element):
        """
        移除子元素

        Args:
            element: 父元素
            child: 要移除的子元素
        """
        element.remove(child)

    @staticmethod
    def to_dict(element: ET.Element) -> Dict[str, Any]:
        """
        将XML转换为字典

        Args:
            element: XML元素

        Returns:
            Dict[str, Any]: 转换后的字典
        """
        result = {}
        
        # 处理属性
        if element.attrib:
            result['@attributes'] = element.attrib
        
        # 处理子元素
        children = list(element)
        if children:
            child_dict = {}
            for child in children:
                child_result = XmlUtils.to_dict(child)
                child_tag = child.tag
                
                if child_tag in child_dict:
                    if not isinstance(child_dict[child_tag], list):
                        child_dict[child_tag] = [child_dict[child_tag]]
                    child_dict[child_tag].append(child_result)
                else:
                    child_dict[child_tag] = child_result
            result.update(child_dict)
        
        # 处理文本
        if element.text and element.text.strip():
            if children or element.attrib:
                result['#text'] = element.text.strip()
            else:
                result = element.text.strip()
        
        return result

    @staticmethod
    def from_dict(data: Dict[str, Any], root_tag: str = 'root') -> ET.Element:
        """
        从字典创建XML元素

        Args:
            data: 字典数据
            root_tag: 根元素标签名

        Returns:
            ET.Element: XML根元素
        """
        def _build_element(parent: ET.Element, data: Any, tag: str):
            element = ET.SubElement(parent, tag)
            
            if isinstance(data, dict):
                # 处理属性
                if '@attributes' in data:
                    element.attrib.update(data['@attributes'])
                
                # 处理文本
                if '#text' in data:
                    element.text = data['#text']
                
                # 处理子元素
                for key, value in data.items():
                    if key not in ('@attributes', '#text'):
                        if isinstance(value, list):
                            for item in value:
                                _build_element(element, item, key)
                        else:
                            _build_element(element, value, key)
            elif isinstance(data, list):
                for item in data:
                    _build_element(parent, item, tag)
            else:
                element.text = str(data)
        
        root = ET.Element(root_tag)
        # 直接处理数据，而不是将整个数据作为root_tag的子元素
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, list):
                    for item in value:
                        _build_element(root, item, key)
                else:
                    _build_element(root, value, key)
        else:
            # 如果数据不是字典，直接作为根元素的文本
            root.text = str(data)
        return root

    @staticmethod
    def to_json(element: ET.Element, indent: Optional[int] = 2) -> str:
        """
        将XML转换为JSON

        Args:
            element: XML元素
            indent: 缩进空格数

        Returns:
            str: JSON字符串
        """
        data = XmlUtils.to_dict(element)
        return json.dumps(data, ensure_ascii=False, indent=indent)

    @staticmethod
    def from_json(json_str: str, root_tag: str = 'root') -> ET.Element:
        """
        从JSON创建XML元素

        Args:
            json_str: JSON字符串
            root_tag: 根元素标签名

        Returns:
            ET.Element: XML根元素
        """
        data = json.loads(json_str)
        return XmlUtils.from_dict(data, root_tag)

    @staticmethod
    def validate(xml_data: Union[str, bytes], xsd_file: str) -> bool:
        """
        使用XSD验证XML

        Args:
            xml_data: XML数据
            xsd_file: XSD文件路径

        Returns:
            bool: 是否验证通过
        """
        try:
            from lxml import etree
            
            # 解析XSD
            xsd_tree = etree.parse(xsd_file)
            xsd_schema = etree.XMLSchema(xsd_tree)
            
            # 解析XML
            if isinstance(xml_data, bytes):
                xml_tree = etree.fromstring(xml_data)
            else:
                xml_tree = etree.fromstring(xml_data.encode('utf-8'))
            
            # 验证
            return xsd_schema.validate(xml_tree)
        except ImportError:
            # lxml库未安装
            print("Warning: lxml library not installed, validation skipped")
            return False
        except Exception:
            return False

    @staticmethod
    def pretty_print(element: ET.Element, encoding: str = 'utf-8') -> str:
        """
        美化XML输出

        Args:
            element: XML元素
            encoding: 编码

        Returns:
            str: 美化后的XML字符串
        """
        try:
            from lxml import etree
            
            # 转换为lxml元素
            xml_str = ET.tostring(element, encoding=encoding)
            lxml_element = etree.fromstring(xml_str)
            
            # 美化
            pretty_xml = etree.tostring(lxml_element, encoding=encoding, pretty_print=True, 
                                       xml_declaration=True).decode(encoding)
            return pretty_xml
        except ImportError:
            # lxml库未安装，使用默认方法并添加基本缩进
            def _indent(element, level=0):
                indent = "  " * level
                if len(element):
                    if not element.text or not element.text.strip():
                        element.text = "\n" + indent + "  "
                    for child in element:
                        _indent(child, level + 1)
                        if not child.tail or not child.tail.strip():
                            child.tail = "\n" + indent + "  "
                    if not element.tail or not element.tail.strip():
                        element.tail = "\n" + indent
            
            # 创建元素的深拷贝，避免修改原始元素
            import copy
            element_copy = copy.deepcopy(element)
            _indent(element_copy)
            
            # 生成字符串
            xml_str = ET.tostring(element_copy, encoding=encoding, xml_declaration=True).decode(encoding)
            return xml_str

    @staticmethod
    def find_by_xpath(element: ET.Element, xpath: str) -> List[ET.Element]:
        """
        使用XPath查找元素

        Args:
            element: 起始元素
            xpath: XPath表达式

        Returns:
            List[ET.Element]: 找到的元素列表
        """
        return element.findall(xpath)

    @staticmethod
    def get_namespaces(element: ET.Element) -> Dict[str, str]:
        """
        获取XML中的命名空间

        Args:
            element: XML元素

        Returns:
            Dict[str, str]: 命名空间字典
        """
        namespaces = {}
        
        # 检查元素的tag是否包含命名空间
        if '}' in element.tag:
            namespace = element.tag.split('}')[0].strip('{')
            prefix = element.tag.split('}')[1]
            namespaces[prefix] = namespace
        
        # 递归检查子元素
        for child in element:
            child_namespaces = XmlUtils.get_namespaces(child)
            namespaces.update(child_namespaces)
        
        return namespaces

    @staticmethod
    def add_namespace(element: ET.Element, prefix: str, namespace: str):
        """
        添加命名空间

        Args:
            element: XML元素
            prefix: 命名空间前缀
            namespace: 命名空间URI
        """
        ET.register_namespace(prefix, namespace)


# 便捷函数

def parse(xml_data: Union[str, bytes, io.BytesIO]) -> ET.Element:
    """
    解析XML数据

    Args:
        xml_data: XML数据

    Returns:
        ET.Element: XML根元素
    """
    return XmlUtils.parse(xml_data)


def parse_file(file_path: str) -> ET.Element:
    """
    从文件解析XML

    Args:
        file_path: XML文件路径

    Returns:
        ET.Element: XML根元素
    """
    return XmlUtils.parse_file(file_path)


def to_string(element: ET.Element, encoding: str = 'utf-8', xml_declaration: bool = True, 
              default_namespace: Optional[str] = None) -> str:
    """
    将XML元素转换为字符串

    Args:
        element: XML元素
        encoding: 编码
        xml_declaration: 是否包含XML声明
        default_namespace: 默认命名空间

    Returns:
        str: XML字符串
    """
    return XmlUtils.to_string(element, encoding, xml_declaration, default_namespace)


def write_to_file(element: ET.Element, file_path: str, encoding: str = 'utf-8', 
                  xml_declaration: bool = True):
    """
    将XML元素写入文件

    Args:
        element: XML元素
        file_path: 文件路径
        encoding: 编码
        xml_declaration: 是否包含XML声明
    """
    XmlUtils.write_to_file(element, file_path, encoding, xml_declaration)


def create_element(tag: str, text: Optional[str] = None, 
                  attributes: Optional[Dict[str, str]] = None) -> ET.Element:
    """
    创建XML元素

    Args:
        tag: 标签名
        text: 文本内容
        attributes: 属性字典

    Returns:
        ET.Element: XML元素
    """
    return XmlUtils.create_element(tag, text, attributes)


def append_child(parent: ET.Element, tag: str, text: Optional[str] = None, 
                attributes: Optional[Dict[str, str]] = None) -> ET.Element:
    """
    向父元素添加子元素

    Args:
        parent: 父元素
        tag: 子元素标签名
        text: 子元素文本内容
        attributes: 子元素属性字典

    Returns:
        ET.Element: 新创建的子元素
    """
    return XmlUtils.append_child(parent, tag, text, attributes)


def to_dict(element: ET.Element) -> Dict[str, Any]:
    """
    将XML转换为字典

    Args:
        element: XML元素

    Returns:
        Dict[str, Any]: 转换后的字典
    """
    return XmlUtils.to_dict(element)


def from_dict(data: Dict[str, Any], root_tag: str = 'root') -> ET.Element:
    """
    从字典创建XML元素

    Args:
        data: 字典数据
        root_tag: 根元素标签名

    Returns:
        ET.Element: XML根元素
    """
    return XmlUtils.from_dict(data, root_tag)


def to_json(element: ET.Element, indent: Optional[int] = 2) -> str:
    """
    将XML转换为JSON

    Args:
        element: XML元素
        indent: 缩进空格数

    Returns:
        str: JSON字符串
    """
    return XmlUtils.to_json(element, indent)


def from_json(json_str: str, root_tag: str = 'root') -> ET.Element:
    """
    从JSON创建XML元素

    Args:
        json_str: JSON字符串
        root_tag: 根元素标签名

    Returns:
        ET.Element: XML根元素
    """
    return XmlUtils.from_json(json_str, root_tag)


def pretty_print(element: ET.Element, encoding: str = 'utf-8') -> str:
    """
    美化XML输出

    Args:
        element: XML元素
        encoding: 编码

    Returns:
        str: 美化后的XML字符串
    """
    return XmlUtils.pretty_print(element, encoding)
