# -*- coding: utf-8 -*-
"""
日期时间工具测试
"""
import unittest
import datetime
from btools.core.data.datetimeutils import (
    DateTimeUtils, now, today, format_datetime, parse_datetime, parse_date,
    add_days, add_hours, add_minutes, add_seconds, between, days_between,
    hours_between, minutes_between, seconds_between, is_before, is_after,
    is_equal, is_today, is_yesterday, is_tomorrow, get_weekday, get_month_start,
    get_month_end, get_quarter_start, get_quarter_end, get_year_start, get_year_end,
    timestamp_to_datetime, datetime_to_timestamp, format_relative_time,
    parse_iso_format, to_iso_format
)


class TestDateTimeUtils(unittest.TestCase):
    """
    日期时间工具测试类
    """

    def setUp(self):
        """
        测试前设置
        """
        self.test_date = datetime.date(2024, 1, 1)
        self.test_datetime = datetime.datetime(2024, 1, 1, 12, 0, 0)

    def test_now(self):
        """
        测试获取当前时间
        """
        current = DateTimeUtils.now()
        self.assertIsInstance(current, datetime.datetime)

    def test_today(self):
        """
        测试获取今天的日期
        """
        current_date = DateTimeUtils.today()
        self.assertIsInstance(current_date, datetime.date)

    def test_format_datetime(self):
        """
        测试格式化日期时间
        """
        # 测试格式化日期
        date_str = DateTimeUtils.format_datetime(self.test_date, DateTimeUtils.DATE_FORMAT)
        self.assertEqual(date_str, "2024-01-01")

        # 测试格式化日期时间
        datetime_str = DateTimeUtils.format_datetime(self.test_datetime)
        self.assertEqual(datetime_str, "2024-01-01 12:00:00")

        # 测试自定义格式
        custom_str = DateTimeUtils.format_datetime(self.test_datetime, "%Y/%m/%d")
        self.assertEqual(custom_str, "2024/01/01")

    def test_parse_datetime(self):
        """
        测试解析日期时间字符串
        """
        # 测试解析日期时间
        dt = DateTimeUtils.parse_datetime("2024-01-01 12:00:00")
        self.assertIsInstance(dt, datetime.datetime)
        self.assertEqual(dt.year, 2024)
        self.assertEqual(dt.month, 1)
        self.assertEqual(dt.day, 1)
        self.assertEqual(dt.hour, 12)

        # 测试解析日期
        date = DateTimeUtils.parse_date("2024-01-01")
        self.assertIsInstance(date, datetime.date)
        self.assertEqual(date.year, 2024)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

    def test_add_functions(self):
        """
        测试添加时间函数
        """
        # 测试添加天数
        new_date = DateTimeUtils.add_days(self.test_date, 1)
        self.assertEqual(new_date, datetime.date(2024, 1, 2))

        # 测试添加小时
        new_datetime = DateTimeUtils.add_hours(self.test_datetime, 1)
        self.assertEqual(new_datetime.hour, 13)

        # 测试添加分钟
        new_datetime = DateTimeUtils.add_minutes(self.test_datetime, 30)
        self.assertEqual(new_datetime.minute, 30)

        # 测试添加秒数
        new_datetime = DateTimeUtils.add_seconds(self.test_datetime, 45)
        self.assertEqual(new_datetime.second, 45)

    def test_between_functions(self):
        """
        测试时间差计算函数
        """
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 1, 3)
        
        # 测试天数差
        days = DateTimeUtils.days_between(start_date, end_date)
        self.assertEqual(days, 2)

        start_datetime = datetime.datetime(2024, 1, 1, 12, 0, 0)
        end_datetime = datetime.datetime(2024, 1, 1, 13, 30, 45)
        
        # 测试小时差
        hours = DateTimeUtils.hours_between(start_datetime, end_datetime)
        self.assertAlmostEqual(hours, 1.5125, places=4)

        # 测试分钟差
        minutes = DateTimeUtils.minutes_between(start_datetime, end_datetime)
        self.assertAlmostEqual(minutes, 90.75, places=2)

        # 测试秒数差
        seconds = DateTimeUtils.seconds_between(start_datetime, end_datetime)
        self.assertEqual(seconds, 5445)

    def test_comparison_functions(self):
        """
        测试比较函数
        """
        date1 = datetime.date(2024, 1, 1)
        date2 = datetime.date(2024, 1, 2)
        
        # 测试is_before
        self.assertTrue(DateTimeUtils.is_before(date1, date2))
        self.assertFalse(DateTimeUtils.is_before(date2, date1))

        # 测试is_after
        self.assertTrue(DateTimeUtils.is_after(date2, date1))
        self.assertFalse(DateTimeUtils.is_after(date1, date2))

        # 测试is_equal
        self.assertTrue(DateTimeUtils.is_equal(date1, date1))
        self.assertFalse(DateTimeUtils.is_equal(date1, date2))

    def test_date_checks(self):
        """
        测试日期检查函数
        """
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        tomorrow = today + datetime.timedelta(days=1)
        
        # 测试is_today
        self.assertTrue(DateTimeUtils.is_today(today))
        self.assertFalse(DateTimeUtils.is_today(yesterday))
        
        # 测试is_yesterday
        self.assertTrue(DateTimeUtils.is_yesterday(yesterday))
        self.assertFalse(DateTimeUtils.is_yesterday(today))
        
        # 测试is_tomorrow
        self.assertTrue(DateTimeUtils.is_tomorrow(tomorrow))
        self.assertFalse(DateTimeUtils.is_tomorrow(today))

    def test_get_weekday(self):
        """
        测试获取星期几
        """
        # 2024-01-01 是星期一
        weekday = DateTimeUtils.get_weekday(datetime.date(2024, 1, 1))
        self.assertEqual(weekday, 0)  # 0表示周一

        # 2024-01-07 是星期日
        weekday = DateTimeUtils.get_weekday(datetime.date(2024, 1, 7))
        self.assertEqual(weekday, 6)  # 6表示周日

    def test_get_period_start_end(self):
        """
        测试获取周期的开始和结束
        """
        test_date = datetime.date(2024, 2, 15)
        test_datetime = datetime.datetime(2024, 2, 15, 12, 0, 0)
        
        # 测试获取当月第一天
        month_start = DateTimeUtils.get_month_start(test_date)
        self.assertEqual(month_start, datetime.date(2024, 2, 1))
        
        # 测试获取当月最后一天
        month_end = DateTimeUtils.get_month_end(test_date)
        self.assertEqual(month_end, datetime.date(2024, 2, 29))  # 2024是闰年
        
        # 测试获取当季第一天
        quarter_start = DateTimeUtils.get_quarter_start(test_date)
        self.assertEqual(quarter_start, datetime.date(2024, 1, 1))
        
        # 测试获取当季最后一天
        quarter_end = DateTimeUtils.get_quarter_end(test_date)
        self.assertEqual(quarter_end, datetime.date(2024, 3, 31))
        
        # 测试获取当年第一天
        year_start = DateTimeUtils.get_year_start(test_date)
        self.assertEqual(year_start, datetime.date(2024, 1, 1))
        
        # 测试获取当年最后一天
        year_end = DateTimeUtils.get_year_end(test_date)
        self.assertEqual(year_end, datetime.date(2024, 12, 31))

    def test_timestamp_functions(self):
        """
        测试时间戳转换函数
        """
        test_datetime = datetime.datetime(2024, 1, 1, 0, 0, 0)
        
        # 测试日期时间转时间戳
        timestamp = DateTimeUtils.datetime_to_timestamp(test_datetime)
        self.assertIsInstance(timestamp, float)
        
        # 测试时间戳转日期时间
        converted_datetime = DateTimeUtils.timestamp_to_datetime(timestamp)
        self.assertIsInstance(converted_datetime, datetime.datetime)
        self.assertEqual(converted_datetime.year, 2024)
        self.assertEqual(converted_datetime.month, 1)
        self.assertEqual(converted_datetime.day, 1)

    def test_format_relative_time(self):
        """
        测试格式化相对时间
        """
        # 测试当前时间
        current = DateTimeUtils.now()
        relative_time = DateTimeUtils.format_relative_time(current)
        self.assertIn("秒前", relative_time)

        # 测试1分钟前
        one_minute_ago = DateTimeUtils.now() - datetime.timedelta(minutes=1)
        relative_time = DateTimeUtils.format_relative_time(one_minute_ago)
        self.assertIn("分钟前", relative_time)

    def test_iso_format_functions(self):
        """
        测试ISO格式转换函数
        """
        test_datetime = datetime.datetime(2024, 1, 1, 12, 0, 0)
        
        # 测试转换为ISO格式
        iso_str = DateTimeUtils.to_iso_format(test_datetime)
        self.assertIsInstance(iso_str, str)
        self.assertIn("2024-01-01T12:00:00", iso_str)
        
        # 测试解析ISO格式
        parsed_datetime = DateTimeUtils.parse_iso_format(iso_str)
        self.assertIsInstance(parsed_datetime, datetime.datetime)
        self.assertEqual(parsed_datetime.year, 2024)
        self.assertEqual(parsed_datetime.month, 1)

    def test_convenience_functions(self):
        """
        测试便捷函数
        """
        # 测试now便捷函数
        current = now()
        self.assertIsInstance(current, datetime.datetime)

        # 测试today便捷函数
        current_date = today()
        self.assertIsInstance(current_date, datetime.date)

        # 测试format_datetime便捷函数
        formatted = format_datetime(self.test_datetime)
        self.assertIsInstance(formatted, str)

        # 测试parse_datetime便捷函数
        parsed = parse_datetime("2024-01-01 12:00:00")
        self.assertIsInstance(parsed, datetime.datetime)

        # 测试add_days便捷函数
        new_date = add_days(self.test_date, 1)
        self.assertEqual(new_date.day, 2)

        # 测试days_between便捷函数
        days = days_between(self.test_date, datetime.date(2024, 1, 3))
        self.assertEqual(days, 2)

        # 测试is_today便捷函数
        self.assertTrue(is_today(today()))

        # 测试get_weekday便捷函数
        weekday = get_weekday(self.test_date)
        self.assertIsInstance(weekday, int)

        # 测试get_month_start便捷函数
        month_start = get_month_start(self.test_date)
        self.assertEqual(month_start.day, 1)

        # 测试timestamp_to_datetime便捷函数
        timestamp = datetime_to_timestamp(self.test_datetime)
        converted = timestamp_to_datetime(timestamp)
        self.assertIsInstance(converted, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
