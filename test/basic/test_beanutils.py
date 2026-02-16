"""测试BeanUtils类"""
import unittest
from btools.core.basic.beanutils import BeanUtils


class TestBeanUtils(unittest.TestCase):
    """测试BeanUtils类"""

    def setUp(self):
        """设置测试环境"""
        # 创建测试类
        class User:
            def __init__(self):
                self.name = ""
                self.age = 0
                self.email = ""
                self.address = None
        
        class Address:
            def __init__(self):
                self.street = ""
                self.city = ""
                self.zipcode = ""
        
        self.User = User
        self.Address = Address

    def test_copy_properties(self):
        """测试复制对象属性"""
        # 创建源对象
        source = self.User()
        source.name = "John"
        source.age = 30
        source.email = "john@example.com"
        
        # 创建目标对象
        target = self.User()
        
        # 复制属性
        BeanUtils.copy_properties(source, target)
        
        # 验证结果
        self.assertEqual(target.name, "John")
        self.assertEqual(target.age, 30)
        self.assertEqual(target.email, "john@example.com")

    def test_copy_properties_with_ignore(self):
        """测试复制对象属性（带忽略列表）"""
        # 创建源对象
        source = self.User()
        source.name = "John"
        source.age = 30
        source.email = "john@example.com"
        
        # 创建目标对象
        target = self.User()
        
        # 复制属性，忽略email
        BeanUtils.copy_properties(source, target, ignore_properties=["email"])
        
        # 验证结果
        self.assertEqual(target.name, "John")
        self.assertEqual(target.age, 30)
        self.assertEqual(target.email, "")

    def test_deep_copy(self):
        """测试深拷贝"""
        # 创建对象
        user = self.User()
        user.name = "John"
        user.age = 30
        
        # 创建地址对象
        address = self.Address()
        address.street = "123 Main St"
        address.city = "New York"
        user.address = address
        
        # 深拷贝
        copied_user = BeanUtils.deep_copy(user)
        
        # 验证结果
        self.assertEqual(copied_user.name, "John")
        self.assertEqual(copied_user.age, 30)
        self.assertEqual(copied_user.address.street, "123 Main St")
        
        # 修改原对象，验证深拷贝
        user.name = "Jane"
        user.address.street = "456 Oak Ave"
        
        self.assertEqual(copied_user.name, "John")
        self.assertEqual(copied_user.address.street, "123 Main St")

    def test_shallow_copy(self):
        """测试浅拷贝"""
        # 创建对象
        user = self.User()
        user.name = "John"
        user.age = 30
        
        # 创建地址对象
        address = self.Address()
        address.street = "123 Main St"
        address.city = "New York"
        user.address = address
        
        # 浅拷贝
        copied_user = BeanUtils.shallow_copy(user)
        
        # 验证结果
        self.assertEqual(copied_user.name, "John")
        self.assertEqual(copied_user.age, 30)
        self.assertEqual(copied_user.address.street, "123 Main St")
        
        # 修改原对象，验证浅拷贝
        user.name = "Jane"
        user.address.street = "456 Oak Ave"
        
        self.assertEqual(copied_user.name, "John")  # 基本类型不受影响
        self.assertEqual(copied_user.address.street, "456 Oak Ave")  # 引用类型受影响

    def test_to_dict(self):
        """测试对象转字典"""
        # 创建对象
        user = self.User()
        user.name = "John"
        user.age = 30
        
        # 创建地址对象
        address = self.Address()
        address.street = "123 Main St"
        address.city = "New York"
        user.address = address
        
        # 转换为字典
        user_dict = BeanUtils.to_dict(user)
        
        # 验证结果
        self.assertEqual(user_dict["name"], "John")
        self.assertEqual(user_dict["age"], 30)
        self.assertEqual(user_dict["address"]["street"], "123 Main St")
        self.assertEqual(user_dict["address"]["city"], "New York")

    def test_from_dict(self):
        """测试字典转对象"""
        # 创建字典
        user_dict = {
            "name": "John",
            "age": 30,
            "email": "john@example.com"
        }
        
        # 转换为对象
        user = BeanUtils.from_dict(self.User, user_dict)
        
        # 验证结果
        self.assertEqual(user.name, "John")
        self.assertEqual(user.age, 30)
        self.assertEqual(user.email, "john@example.com")

    def test_equals(self):
        """测试对象比较"""
        # 创建两个相同的对象
        user1 = self.User()
        user1.name = "John"
        user1.age = 30
        
        user2 = self.User()
        user2.name = "John"
        user2.age = 30
        
        # 比较对象
        result = BeanUtils.equals(user1, user2)
        self.assertTrue(result)

    def test_equals_with_ignore(self):
        """测试对象比较（带忽略列表）"""
        # 创建两个对象，只有email不同
        user1 = self.User()
        user1.name = "John"
        user1.age = 30
        user1.email = "john@example.com"
        
        user2 = self.User()
        user2.name = "John"
        user2.age = 30
        user2.email = "john.doe@example.com"
        
        # 比较对象，忽略email
        result = BeanUtils.equals(user1, user2, ignore_properties=["email"])
        self.assertTrue(result)

    def test_get_property(self):
        """测试获取属性值"""
        # 创建对象
        user = self.User()
        user.name = "John"
        
        # 创建地址对象
        address = self.Address()
        address.street = "123 Main St"
        user.address = address
        
        # 获取属性
        name = BeanUtils.get_property(user, "name")
        street = BeanUtils.get_property(user, "address.street")
        
        # 验证结果
        self.assertEqual(name, "John")
        self.assertEqual(street, "123 Main St")

    def test_set_property(self):
        """测试设置属性值"""
        # 创建对象
        user = self.User()
        
        # 创建地址对象
        address = self.Address()
        user.address = address
        
        # 设置属性
        BeanUtils.set_property(user, "name", "John")
        BeanUtils.set_property(user, "address.street", "123 Main St")
        
        # 验证结果
        self.assertEqual(user.name, "John")
        self.assertEqual(user.address.street, "123 Main St")

    def test_has_property(self):
        """测试检查属性是否存在"""
        # 创建对象
        user = self.User()
        
        # 创建地址对象
        address = self.Address()
        user.address = address
        
        # 检查属性
        has_name = BeanUtils.has_property(user, "name")
        has_street = BeanUtils.has_property(user, "address.street")
        has_nonexistent = BeanUtils.has_property(user, "nonexistent")
        
        # 验证结果
        self.assertTrue(has_name)
        self.assertTrue(has_street)
        self.assertFalse(has_nonexistent)

    def test_get_properties(self):
        """测试获取所有属性名"""
        # 创建对象
        user = self.User()
        
        # 获取属性名列表
        properties = BeanUtils.get_properties(user)
        
        # 验证结果
        self.assertIn("name", properties)
        self.assertIn("age", properties)
        self.assertIn("email", properties)
        self.assertIn("address", properties)

    def test_merge(self):
        """测试合并对象"""
        # 创建两个对象
        user1 = self.User()
        user1.name = "John"
        user1.age = 30
        
        user2 = self.User()
        user2.age = 35
        user2.email = "john@example.com"
        
        # 合并对象
        merged_user = BeanUtils.merge(user1, user2)
        
        # 验证结果
        self.assertEqual(merged_user.name, "John")
        self.assertEqual(merged_user.age, 35)  # 来自user2
        self.assertEqual(merged_user.email, "john@example.com")  # 来自user2


if __name__ == "__main__":
    unittest.main()