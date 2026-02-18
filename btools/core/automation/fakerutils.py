# -*- coding: utf-8 -*-
"""
测试数据生成工具类模块
提供类似于Faker的测试数据生成功能
"""
import random
import string
import datetime
from typing import Dict, List, Optional, Union


class FakerUtils:
    """
    测试数据生成工具类
    提供类似于Faker的测试数据生成功能
    """

    # 常用姓名列表
    FIRST_NAMES = [
        "张", "李", "王", "刘", "陈", "杨", "赵", "黄", "周", "吴",
        "徐", "孙", "马", "朱", "胡", "郭", "何", "高", "林", "罗"
    ]
    LAST_NAMES = [
        "伟", "芳", "娜", "敏", "静", "丽", "强", "磊", "军", "洋",
        "勇", "艳", "杰", "娟", "涛", "明", "超", "秀英", "霞", "平"
    ]

    # 常用城市列表
    CITIES = [
        "北京", "上海", "广州", "深圳", "杭州", "南京", "成都", "武汉", "西安", "重庆",
        "苏州", "天津", "郑州", "长沙", "青岛", "宁波", "东莞", "厦门", "福州", "济南"
    ]

    # 常用街道列表
    STREETS = [
        "中山路", "人民路", "解放路", "建设路", "和平路", "新华街", "东风路", "朝阳路", "公园路", "友谊路"
    ]

    # 常用公司名称
    COMPANIES = [
        "阿里巴巴", "腾讯", "百度", "京东", "美团", "字节跳动", "小米", "华为", "网易", "新浪",
        "搜狐", "携程", "拼多多", "快手", "B站", "滴滴", "顺丰", "菜鸟", "蚂蚁金服", "腾讯云"
    ]

    # 常用职位列表
    POSITIONS = [
        "产品经理", "软件工程师", "UI设计师", "数据分析师", "市场经理", "运营专员", "销售经理",
        "人力资源专员", "财务经理", "行政助理"
    ]

    # 常用身份证号前缀（部分）
    ID_CARD_PREFIXES = [
        "110101", "110102", "110103", "110104", "110105", "310101", "310104", "310105",
        "440106", "440105", "440301", "440303", "440304", "330102", "330103", "330104"
    ]

    # 常用银行卡号前缀
    BANK_CARD_PREFIXES = [
        "622202", "622208", "622848", "622845", "622846", "622849", "622200", "622203",
        "622682", "622686", "622685", "622688", "622689", "622690", "622691", "622692"
    ]

    @staticmethod
    def random_string(length: int = 10, include_special: bool = False) -> str:
        """
        生成随机字符串

        Args:
            length: 字符串长度
            include_special: 是否包含特殊字符

        Returns:
            随机字符串
        """
        chars = string.ascii_letters + string.digits
        if include_special:
            chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def random_integer(min_val: int = 0, max_val: int = 1000) -> int:
        """
        生成随机整数

        Args:
            min_val: 最小值
            max_val: 最大值

        Returns:
            随机整数
        """
        return random.randint(min_val, max_val)

    @staticmethod
    def random_float(min_val: float = 0.0, max_val: float = 1000.0, decimal_places: int = 2) -> float:
        """
        生成随机浮点数

        Args:
            min_val: 最小值
            max_val: 最大值
            decimal_places: 小数位数

        Returns:
            随机浮点数
        """
        value = random.uniform(min_val, max_val)
        return round(value, decimal_places)

    @staticmethod
    def random_boolean() -> bool:
        """
        生成随机布尔值

        Returns:
            随机布尔值
        """
        return random.choice([True, False])

    @staticmethod
    def random_date(start_date: Optional[datetime.date] = None, end_date: Optional[datetime.date] = None) -> datetime.date:
        """
        生成随机日期

        Args:
            start_date: 开始日期
            end_date: 结束日期

        Returns:
            随机日期
        """
        if start_date is None:
            start_date = datetime.date(1970, 1, 1)
        if end_date is None:
            end_date = datetime.date.today()

        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        return start_date + datetime.timedelta(days=random_days)

    @staticmethod
    def random_datetime(start_datetime: Optional[datetime.datetime] = None, end_datetime: Optional[datetime.datetime] = None) -> datetime.datetime:
        """
        生成随机 datetime

        Args:
            start_datetime: 开始 datetime
            end_datetime: 结束 datetime

        Returns:
            随机 datetime
        """
        if start_datetime is None:
            start_datetime = datetime.datetime(1970, 1, 1, 0, 0, 0)
        if end_datetime is None:
            end_datetime = datetime.datetime.now()

        delta = end_datetime - start_datetime
        random_seconds = random.randint(0, int(delta.total_seconds()))
        return start_datetime + datetime.timedelta(seconds=random_seconds)

    @staticmethod
    def random_email(domain: str = None) -> str:
        """
        生成随机邮箱地址

        Args:
            domain: 邮箱域名

        Returns:
            随机邮箱地址
        """
        if domain is None:
            domain = random.choice(["example.com", "test.com", "gmail.com", "hotmail.com", "yahoo.com"])
        username = FakerUtils.random_string(8)
        return f"{username}@{domain}"

    @staticmethod
    def random_phone(prefix: str = None) -> str:
        """
        生成随机手机号码

        Args:
            prefix: 手机号前缀

        Returns:
            随机手机号码
        """
        if prefix is None:
            prefix = random.choice(["138", "139", "137", "136", "135", "134", "159", "158", "157", "150"])
        suffix = ''.join(random.choice(string.digits) for _ in range(8))
        return f"{prefix}{suffix}"

    @staticmethod
    def random_name() -> str:
        """
        生成随机中文姓名

        Returns:
            随机中文姓名
        """
        first_name = random.choice(FakerUtils.FIRST_NAMES)
        last_name = random.choice(FakerUtils.LAST_NAMES)
        return f"{first_name}{last_name}"

    @staticmethod
    def random_address() -> str:
        """
        生成随机地址

        Returns:
            随机地址
        """
        city = random.choice(FakerUtils.CITIES)
        street = random.choice(FakerUtils.STREETS)
        building = random.randint(1, 100)
        unit = random.randint(1, 20)
        room = random.randint(101, 999)
        return f"{city}{street}{building}号{unit}单元{room}室"

    @staticmethod
    def random_company() -> str:
        """
        生成随机公司名称

        Returns:
            随机公司名称
        """
        company = random.choice(FakerUtils.COMPANIES)
        suffix = random.choice(["科技有限公司", "信息技术有限公司", "网络科技有限公司", "电子商务有限公司"])
        return f"{company}{suffix}"

    @staticmethod
    def random_position() -> str:
        """
        生成随机职位

        Returns:
            随机职位
        """
        return random.choice(FakerUtils.POSITIONS)

    @staticmethod
    def random_id_card() -> str:
        """
        生成随机身份证号

        Returns:
            随机身份证号
        """
        # 前6位：地区码
        prefix = random.choice(FakerUtils.ID_CARD_PREFIXES)
        
        # 7-14位：出生日期
        birth_date = FakerUtils.random_date(datetime.date(1950, 1, 1), datetime.date(2000, 12, 31))
        birth_str = birth_date.strftime("%Y%m%d")
        
        # 15-17位：顺序码
        sequence = str(random.randint(100, 999))
        
        # 18位：校验码
        # 这里简化处理，实际身份证号的校验码有复杂的算法
        check_code = random.choice(string.digits + ["X"])
        
        return f"{prefix}{birth_str}{sequence}{check_code}"

    @staticmethod
    def random_bank_card() -> str:
        """
        生成随机银行卡号

        Returns:
            随机银行卡号
        """
        prefix = random.choice(FakerUtils.BANK_CARD_PREFIXES)
        # 银行卡号长度通常为16-19位
        length = random.randint(16, 19)
        suffix_length = length - len(prefix)
        suffix = ''.join(random.choice(string.digits) for _ in range(suffix_length))
        return f"{prefix}{suffix}"

    @staticmethod
    def random_ip() -> str:
        """
        生成随机IP地址

        Returns:
            随机IP地址
        """
        return '.'.join(str(random.randint(0, 255)) for _ in range(4))

    @staticmethod
    def random_url() -> str:
        """
        生成随机URL

        Returns:
            随机URL
        """
        protocol = random.choice(["http", "https"])
        domain = FakerUtils.random_string(10) + ".com"
        path = FakerUtils.random_string(5)
        return f"{protocol}://{domain}/{path}"

    @staticmethod
    def random_user_agent() -> str:
        """
        生成随机User-Agent

        Returns:
            随机User-Agent
        """
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
        ]
        return random.choice(user_agents)

    @staticmethod
    def random_credit_card() -> Dict[str, str]:
        """
        生成随机信用卡信息

        Returns:
            信用卡信息字典
        """
        return {
            "number": FakerUtils.random_bank_card(),
            "expiry": f"{random.randint(1, 12)}/{random.randint(26, 30)}",
            "cvv": str(random.randint(100, 999))
        }

    @staticmethod
    def random_user() -> Dict[str, str]:
        """
        生成随机用户信息

        Returns:
            用户信息字典
        """
        return {
            "name": FakerUtils.random_name(),
            "email": FakerUtils.random_email(),
            "phone": FakerUtils.random_phone(),
            "address": FakerUtils.random_address(),
            "company": FakerUtils.random_company(),
            "position": FakerUtils.random_position(),
            "id_card": FakerUtils.random_id_card(),
            "bank_card": FakerUtils.random_bank_card(),
            "ip": FakerUtils.random_ip()
        }

    @staticmethod
    def random_product() -> Dict[str, Union[str, float, int]]:
        """
        生成随机产品信息

        Returns:
            产品信息字典
        """
        product_names = ["手机", "电脑", "平板", "相机", "耳机", "手表", "音箱", "键盘", "鼠标", "显示器"]
        return {
            "name": random.choice(product_names),
            "price": FakerUtils.random_float(100, 10000),
            "stock": FakerUtils.random_integer(0, 1000),
            "sku": FakerUtils.random_string(10),
            "category": random.choice(["电子产品", "办公用品", "家居用品", "服装鞋帽"]),
            "description": f"这是一个{random.choice(product_names)}产品"
        }

    @staticmethod
    def random_order() -> Dict[str, Union[str, float, int, datetime.datetime]]:
        """
        生成随机订单信息

        Returns:
            订单信息字典
        """
        return {
            "order_id": FakerUtils.random_string(12),
            "user_id": FakerUtils.random_string(8),
            "total_amount": FakerUtils.random_float(100, 10000),
            "order_time": FakerUtils.random_datetime(),
            "status": random.choice(["待付款", "待发货", "待收货", "已完成", "已取消"]),
            "payment_method": random.choice(["支付宝", "微信支付", "银行卡", "现金"])
        }

    @staticmethod
    def generate_test_data(template: Dict[str, str]) -> Dict[str, str]:
        """
        根据模板生成测试数据

        Args:
            template: 测试数据模板，键为字段名，值为数据类型

        Returns:
            生成的测试数据
        """
        result = {}
        for key, value_type in template.items():
            if value_type == "string":
                result[key] = FakerUtils.random_string()
            elif value_type == "integer":
                result[key] = FakerUtils.random_integer()
            elif value_type == "float":
                result[key] = FakerUtils.random_float()
            elif value_type == "boolean":
                result[key] = FakerUtils.random_boolean()
            elif value_type == "email":
                result[key] = FakerUtils.random_email()
            elif value_type == "phone":
                result[key] = FakerUtils.random_phone()
            elif value_type == "name":
                result[key] = FakerUtils.random_name()
            elif value_type == "address":
                result[key] = FakerUtils.random_address()
            elif value_type == "company":
                result[key] = FakerUtils.random_company()
            elif value_type == "position":
                result[key] = FakerUtils.random_position()
            elif value_type == "id_card":
                result[key] = FakerUtils.random_id_card()
            elif value_type == "bank_card":
                result[key] = FakerUtils.random_bank_card()
            elif value_type == "ip":
                result[key] = FakerUtils.random_ip()
            elif value_type == "url":
                result[key] = FakerUtils.random_url()
            elif value_type == "user_agent":
                result[key] = FakerUtils.random_user_agent()
            elif value_type == "date":
                result[key] = FakerUtils.random_date().strftime("%Y-%m-%d")
            elif value_type == "datetime":
                result[key] = FakerUtils.random_datetime().strftime("%Y-%m-%d %H:%M:%S")
            elif value_type == "user":
                result[key] = FakerUtils.random_user()
            elif value_type == "product":
                result[key] = FakerUtils.random_product()
            elif value_type == "order":
                result[key] = FakerUtils.random_order()
            else:
                result[key] = FakerUtils.random_string()
        return result


# 便捷函数

def random_string(length: int = 10, include_special: bool = False) -> str:
    """
    生成随机字符串

    Args:
        length: 字符串长度
        include_special: 是否包含特殊字符

    Returns:
        随机字符串
    """
    return FakerUtils.random_string(length, include_special)


def random_integer(min_val: int = 0, max_val: int = 1000) -> int:
    """
    生成随机整数

    Args:
        min_val: 最小值
        max_val: 最大值

    Returns:
        随机整数
    """
    return FakerUtils.random_integer(min_val, max_val)


def random_float(min_val: float = 0.0, max_val: float = 1000.0, decimal_places: int = 2) -> float:
    """
    生成随机浮点数

    Args:
        min_val: 最小值
        max_val: 最大值
        decimal_places: 小数位数

    Returns:
        随机浮点数
    """
    return FakerUtils.random_float(min_val, max_val, decimal_places)


def random_boolean() -> bool:
    """
    生成随机布尔值

    Returns:
        随机布尔值
    """
    return FakerUtils.random_boolean()


def random_date(start_date: Optional[datetime.date] = None, end_date: Optional[datetime.date] = None) -> datetime.date:
    """
    生成随机日期

    Args:
        start_date: 开始日期
        end_date: 结束日期

    Returns:
        随机日期
    """
    return FakerUtils.random_date(start_date, end_date)


def random_datetime(start_datetime: Optional[datetime.datetime] = None, end_datetime: Optional[datetime.datetime] = None) -> datetime.datetime:
    """
    生成随机 datetime

    Args:
        start_datetime: 开始 datetime
        end_datetime: 结束 datetime

    Returns:
        随机 datetime
    """
    return FakerUtils.random_datetime(start_datetime, end_datetime)


def random_email(domain: str = None) -> str:
    """
    生成随机邮箱地址

    Args:
        domain: 邮箱域名

    Returns:
        随机邮箱地址
    """
    return FakerUtils.random_email(domain)


def random_phone(prefix: str = None) -> str:
    """
    生成随机手机号码

    Args:
        prefix: 手机号前缀

    Returns:
        随机手机号码
    """
    return FakerUtils.random_phone(prefix)


def random_name() -> str:
    """
    生成随机中文姓名

    Returns:
        随机中文姓名
    """
    return FakerUtils.random_name()


def random_address() -> str:
    """
    生成随机地址

    Returns:
        随机地址
    """
    return FakerUtils.random_address()


def random_company() -> str:
    """
    生成随机公司名称

    Returns:
        随机公司名称
    """
    return FakerUtils.random_company()


def random_position() -> str:
    """
    生成随机职位

    Returns:
        随机职位
    """
    return FakerUtils.random_position()


def random_id_card() -> str:
    """
    生成随机身份证号

    Returns:
        随机身份证号
    """
    return FakerUtils.random_id_card()


def random_bank_card() -> str:
    """
    生成随机银行卡号

    Returns:
        随机银行卡号
    """
    return FakerUtils.random_bank_card()


def random_ip() -> str:
    """
    生成随机IP地址

    Returns:
        随机IP地址
    """
    return FakerUtils.random_ip()


def random_url() -> str:
    """
    生成随机URL

    Returns:
        随机URL
    """
    return FakerUtils.random_url()


def random_user_agent() -> str:
    """
    生成随机User-Agent

    Returns:
        随机User-Agent
    """
    return FakerUtils.random_user_agent()


def random_credit_card() -> Dict[str, str]:
    """
    生成随机信用卡信息

    Returns:
        信用卡信息字典
    """
    return FakerUtils.random_credit_card()


def random_user() -> Dict[str, str]:
    """
    生成随机用户信息

    Returns:
        用户信息字典
    """
    return FakerUtils.random_user()


def random_product() -> Dict[str, Union[str, float, int]]:
    """
    生成随机产品信息

    Returns:
        产品信息字典
    """
    return FakerUtils.random_product()


def random_order() -> Dict[str, Union[str, float, int, datetime.datetime]]:
    """
    生成随机订单信息

    Returns:
        订单信息字典
    """
    return FakerUtils.random_order()


def generate_test_data(template: Dict[str, str]) -> Dict[str, str]:
    """
    根据模板生成测试数据

    Args:
        template: 测试数据模板，键为字段名，值为数据类型

    Returns:
        生成的测试数据
    """
    return FakerUtils.generate_test_data(template)