# 自动化测试工具类
from .testutils import TestUtils
from .seleniumutils import SeleniumUtils
from .playwrightutils import PlaywrightUtils
from .appiumutils import AppiumUtils
from .fakerutils import FakerUtils, random_string, random_integer, random_float, random_boolean, random_date, random_datetime, random_email, random_phone, random_name, random_address, random_company, random_position, random_id_card, random_bank_card, random_ip, random_url, random_user_agent, random_credit_card, random_user, random_product, random_order, generate_test_data

__all__ = [
    'TestUtils',
    'SeleniumUtils',
    'PlaywrightUtils',
    'AppiumUtils',
    'FakerUtils',
    'random_string',
    'random_integer',
    'random_float',
    'random_boolean',
    'random_date',
    'random_datetime',
    'random_email',
    'random_phone',
    'random_name',
    'random_address',
    'random_company',
    'random_position',
    'random_id_card',
    'random_bank_card',
    'random_ip',
    'random_url',
    'random_user_agent',
    'random_credit_card',
    'random_user',
    'random_product',
    'random_order',
    'generate_test_data'
]