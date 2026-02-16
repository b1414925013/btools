# -*- coding: utf-8 -*-
"""
增强的日期时间工具模块
"""
import datetime
import time
from typing import Any, Optional, Union


class DateTimeUtils:
    """
    日期时间工具类
    提供增强的日期时间处理功能
    """

    # 常用日期格式
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    ISO_FORMAT = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def now() -> datetime.datetime:
        """
        获取当前时间

        Returns:
            当前时间
        """
        return datetime.datetime.now()

    @staticmethod
    def today() -> datetime.date:
        """
        获取今天的日期

        Returns:
            今天的日期
        """
        return datetime.date.today()

    @staticmethod
    def format_datetime(dt: Union[datetime.datetime, datetime.date], 
                       fmt: str = DATETIME_FORMAT) -> str:
        """
        格式化日期时间

        Args:
            dt: 日期时间对象
            fmt: 格式字符串，默认 "%Y-%m-%d %H:%M:%S"

        Returns:
            格式化后的字符串
        """
        return dt.strftime(fmt)

    @staticmethod
    def parse_datetime(date_str: str, fmt: str = DATETIME_FORMAT) -> datetime.datetime:
        """
        解析日期时间字符串

        Args:
            date_str: 日期时间字符串
            fmt: 格式字符串，默认 "%Y-%m-%d %H:%M:%S"

        Returns:
            解析后的日期时间对象
        """
        return datetime.datetime.strptime(date_str, fmt)

    @staticmethod
    def parse_date(date_str: str, fmt: str = DATE_FORMAT) -> datetime.date:
        """
        解析日期字符串

        Args:
            date_str: 日期字符串
            fmt: 格式字符串，默认 "%Y-%m-%d"

        Returns:
            解析后的日期对象
        """
        return datetime.datetime.strptime(date_str, fmt).date()

    @staticmethod
    def add_days(dt: Union[datetime.datetime, datetime.date], days: int) -> Union[datetime.datetime, datetime.date]:
        """
        添加天数

        Args:
            dt: 日期时间对象
            days: 天数

        Returns:
            计算后的日期时间对象
        """
        delta = datetime.timedelta(days=days)
        return dt + delta

    @staticmethod
    def add_hours(dt: datetime.datetime, hours: int) -> datetime.datetime:
        """
        添加小时

        Args:
            dt: 日期时间对象
            hours: 小时数

        Returns:
            计算后的日期时间对象
        """
        delta = datetime.timedelta(hours=hours)
        return dt + delta

    @staticmethod
    def add_minutes(dt: datetime.datetime, minutes: int) -> datetime.datetime:
        """
        添加分钟

        Args:
            dt: 日期时间对象
            minutes: 分钟数

        Returns:
            计算后的日期时间对象
        """
        delta = datetime.timedelta(minutes=minutes)
        return dt + delta

    @staticmethod
    def add_seconds(dt: datetime.datetime, seconds: int) -> datetime.datetime:
        """
        添加秒数

        Args:
            dt: 日期时间对象
            seconds: 秒数

        Returns:
            计算后的日期时间对象
        """
        delta = datetime.timedelta(seconds=seconds)
        return dt + delta

    @staticmethod
    def between(start: Union[datetime.datetime, datetime.date], 
                end: Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        """
        计算两个日期时间之间的差值

        Args:
            start: 开始日期时间
            end: 结束日期时间

        Returns:
            时间差对象
        """
        return end - start

    @staticmethod
    def days_between(start: Union[datetime.datetime, datetime.date], 
                    end: Union[datetime.datetime, datetime.date]) -> int:
        """
        计算两个日期之间的天数差

        Args:
            start: 开始日期
            end: 结束日期

        Returns:
            天数差
        """
        delta = end - start
        return delta.days

    @staticmethod
    def hours_between(start: datetime.datetime, end: datetime.datetime) -> float:
        """
        计算两个时间之间的小时差

        Args:
            start: 开始时间
            end: 结束时间

        Returns:
            小时差
        """
        delta = end - start
        return delta.total_seconds() / 3600

    @staticmethod
    def minutes_between(start: datetime.datetime, end: datetime.datetime) -> float:
        """
        计算两个时间之间的分钟差

        Args:
            start: 开始时间
            end: 结束时间

        Returns:
            分钟差
        """
        delta = end - start
        return delta.total_seconds() / 60

    @staticmethod
    def seconds_between(start: datetime.datetime, end: datetime.datetime) -> float:
        """
        计算两个时间之间的秒数差

        Args:
            start: 开始时间
            end: 结束时间

        Returns:
            秒数差
        """
        delta = end - start
        return delta.total_seconds()

    @staticmethod
    def is_before(dt1: Union[datetime.datetime, datetime.date], 
                 dt2: Union[datetime.datetime, datetime.date]) -> bool:
        """
        判断dt1是否在dt2之前

        Args:
            dt1: 第一个日期时间
            dt2: 第二个日期时间

        Returns:
            是否在之前
        """
        return dt1 < dt2

    @staticmethod
    def is_after(dt1: Union[datetime.datetime, datetime.date], 
                dt2: Union[datetime.datetime, datetime.date]) -> bool:
        """
        判断dt1是否在dt2之后

        Args:
            dt1: 第一个日期时间
            dt2: 第二个日期时间

        Returns:
            是否在之后
        """
        return dt1 > dt2

    @staticmethod
    def is_equal(dt1: Union[datetime.datetime, datetime.date], 
                dt2: Union[datetime.datetime, datetime.date]) -> bool:
        """
        判断两个日期时间是否相等

        Args:
            dt1: 第一个日期时间
            dt2: 第二个日期时间

        Returns:
            是否相等
        """
        return dt1 == dt2

    @staticmethod
    def is_today(dt: Union[datetime.datetime, datetime.date]) -> bool:
        """
        判断是否是今天

        Args:
            dt: 日期时间对象

        Returns:
            是否是今天
        """
        if isinstance(dt, datetime.datetime):
            dt = dt.date()
        return dt == DateTimeUtils.today()

    @staticmethod
    def is_yesterday(dt: Union[datetime.datetime, datetime.date]) -> bool:
        """
        判断是否是昨天

        Args:
            dt: 日期时间对象

        Returns:
            是否是昨天
        """
        if isinstance(dt, datetime.datetime):
            dt = dt.date()
        yesterday = DateTimeUtils.today() - datetime.timedelta(days=1)
        return dt == yesterday

    @staticmethod
    def is_tomorrow(dt: Union[datetime.datetime, datetime.date]) -> bool:
        """
        判断是否是明天

        Args:
            dt: 日期时间对象

        Returns:
            是否是明天
        """
        if isinstance(dt, datetime.datetime):
            dt = dt.date()
        tomorrow = DateTimeUtils.today() + datetime.timedelta(days=1)
        return dt == tomorrow

    @staticmethod
    def get_weekday(dt: Union[datetime.datetime, datetime.date]) -> int:
        """
        获取星期几（0-6，0表示周一）

        Args:
            dt: 日期时间对象

        Returns:
            星期几
        """
        if isinstance(dt, datetime.datetime):
            dt = dt.date()
        # dt.weekday()已经返回0-6，其中0表示周一
        return dt.weekday()

    @staticmethod
    def get_month_start(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
        """
        获取当月第一天

        Args:
            dt: 日期时间对象

        Returns:
            当月第一天
        """
        if isinstance(dt, datetime.datetime):
            return dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            return dt.replace(day=1)

    @staticmethod
    def get_month_end(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
        """
        获取当月最后一天

        Args:
            dt: 日期时间对象

        Returns:
            当月最后一天
        """
        if isinstance(dt, datetime.datetime):
            # 获取下个月第一天，然后减去一天
            if dt.month == 12:
                next_month = dt.replace(year=dt.year + 1, month=1, day=1)
            else:
                next_month = dt.replace(month=dt.month + 1, day=1)
            return next_month - datetime.timedelta(days=1)
        else:
            # 获取下个月第一天，然后减去一天
            if dt.month == 12:
                next_month = dt.replace(year=dt.year + 1, month=1, day=1)
            else:
                next_month = dt.replace(month=dt.month + 1, day=1)
            return next_month - datetime.timedelta(days=1)

    @staticmethod
    def get_quarter_start(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
        """
        获取当季第一天

        Args:
            dt: 日期时间对象

        Returns:
            当季第一天
        """
        quarter_month = ((dt.month - 1) // 3) * 3 + 1
        if isinstance(dt, datetime.datetime):
            return dt.replace(month=quarter_month, day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            return dt.replace(month=quarter_month, day=1)

    @staticmethod
    def get_quarter_end(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
        """
        获取当季最后一天

        Args:
            dt: 日期时间对象

        Returns:
            当季最后一天
        """
        quarter_month = ((dt.month - 1) // 3) * 3 + 3
        if isinstance(dt, datetime.datetime):
            # 获取下一季度第一天，然后减去一天
            if quarter_month == 12:
                next_quarter = dt.replace(year=dt.year + 1, month=1, day=1)
            else:
                next_quarter = dt.replace(month=quarter_month + 1, day=1)
            return next_quarter - datetime.timedelta(days=1)
        else:
            # 获取下一季度第一天，然后减去一天
            if quarter_month == 12:
                next_quarter = dt.replace(year=dt.year + 1, month=1, day=1)
            else:
                next_quarter = dt.replace(month=quarter_month + 1, day=1)
            return next_quarter - datetime.timedelta(days=1)

    @staticmethod
    def get_year_start(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
        """
        获取当年第一天

        Args:
            dt: 日期时间对象

        Returns:
            当年第一天
        """
        if isinstance(dt, datetime.datetime):
            return dt.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            return dt.replace(month=1, day=1)

    @staticmethod
    def get_year_end(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
        """
        获取当年最后一天

        Args:
            dt: 日期时间对象

        Returns:
            当年最后一天
        """
        if isinstance(dt, datetime.datetime):
            return dt.replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
        else:
            return dt.replace(month=12, day=31)

    @staticmethod
    def timestamp_to_datetime(timestamp: Union[int, float]) -> datetime.datetime:
        """
        时间戳转日期时间

        Args:
            timestamp: 时间戳

        Returns:
            日期时间对象
        """
        return datetime.datetime.fromtimestamp(timestamp)

    @staticmethod
    def datetime_to_timestamp(dt: datetime.datetime) -> float:
        """
        日期时间转时间戳

        Args:
            dt: 日期时间对象

        Returns:
            时间戳
        """
        return dt.timestamp()

    @staticmethod
    def format_relative_time(dt: Union[datetime.datetime, datetime.date]) -> str:
        """
        格式化相对时间

        Args:
            dt: 日期时间对象

        Returns:
            相对时间字符串
        """
        now = DateTimeUtils.now()
        if isinstance(dt, datetime.date) and not isinstance(dt, datetime.datetime):
            dt = datetime.datetime.combine(dt, datetime.time.min)

        delta = now - dt
        seconds = delta.total_seconds()

        if seconds < 60:
            return f"{int(seconds)}秒前"
        elif seconds < 3600:
            return f"{int(seconds / 60)}分钟前"
        elif seconds < 86400:
            return f"{int(seconds / 3600)}小时前"
        elif seconds < 604800:
            return f"{int(seconds / 86400)}天前"
        elif seconds < 2592000:
            return f"{int(seconds / 604800)}周前"
        elif seconds < 31536000:
            return f"{int(seconds / 2592000)}个月前"
        else:
            return f"{int(seconds / 31536000)}年前"

    @staticmethod
    def parse_iso_format(date_str: str) -> datetime.datetime:
        """
        解析ISO格式的日期时间字符串

        Args:
            date_str: ISO格式的日期时间字符串

        Returns:
            日期时间对象
        """
        return datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))

    @staticmethod
    def to_iso_format(dt: datetime.datetime) -> str:
        """
        转换为ISO格式的日期时间字符串

        Args:
            dt: 日期时间对象

        Returns:
            ISO格式的字符串
        """
        return dt.isoformat()


# 便捷函数

def now() -> datetime.datetime:
    """
    获取当前时间

    Returns:
        当前时间
    """
    return DateTimeUtils.now()


def today() -> datetime.date:
    """
    获取今天的日期

    Returns:
        今天的日期
    """
    return DateTimeUtils.today()


def format_datetime(dt: Union[datetime.datetime, datetime.date], 
                   fmt: str = DateTimeUtils.DATETIME_FORMAT) -> str:
    """
    格式化日期时间

    Args:
        dt: 日期时间对象
        fmt: 格式字符串，默认 "%Y-%m-%d %H:%M:%S"

    Returns:
        格式化后的字符串
    """
    return DateTimeUtils.format_datetime(dt, fmt)


def parse_datetime(date_str: str, fmt: str = DateTimeUtils.DATETIME_FORMAT) -> datetime.datetime:
    """
    解析日期时间字符串

    Args:
        date_str: 日期时间字符串
        fmt: 格式字符串，默认 "%Y-%m-%d %H:%M:%S"

    Returns:
        解析后的日期时间对象
    """
    return DateTimeUtils.parse_datetime(date_str, fmt)


def parse_date(date_str: str, fmt: str = DateTimeUtils.DATE_FORMAT) -> datetime.date:
    """
    解析日期字符串

    Args:
        date_str: 日期字符串
        fmt: 格式字符串，默认 "%Y-%m-%d"

    Returns:
        解析后的日期对象
    """
    return DateTimeUtils.parse_date(date_str, fmt)


def add_days(dt: Union[datetime.datetime, datetime.date], days: int) -> Union[datetime.datetime, datetime.date]:
    """
    添加天数

    Args:
        dt: 日期时间对象
        days: 天数

    Returns:
        计算后的日期时间对象
    """
    return DateTimeUtils.add_days(dt, days)


def add_hours(dt: datetime.datetime, hours: int) -> datetime.datetime:
    """
    添加小时

    Args:
        dt: 日期时间对象
        hours: 小时数

    Returns:
        计算后的日期时间对象
    """
    return DateTimeUtils.add_hours(dt, hours)


def add_minutes(dt: datetime.datetime, minutes: int) -> datetime.datetime:
    """
    添加分钟

    Args:
        dt: 日期时间对象
        minutes: 分钟数

    Returns:
        计算后的日期时间对象
    """
    return DateTimeUtils.add_minutes(dt, minutes)


def add_seconds(dt: datetime.datetime, seconds: int) -> datetime.datetime:
    """
    添加秒数

    Args:
        dt: 日期时间对象
        seconds: 秒数

    Returns:
        计算后的日期时间对象
    """
    return DateTimeUtils.add_seconds(dt, seconds)


def between(start: Union[datetime.datetime, datetime.date], 
            end: Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
    """
    计算两个日期时间之间的差值

    Args:
        start: 开始日期时间
        end: 结束日期时间

    Returns:
        时间差对象
    """
    return DateTimeUtils.between(start, end)


def days_between(start: Union[datetime.datetime, datetime.date], 
                end: Union[datetime.datetime, datetime.date]) -> int:
    """
    计算两个日期之间的天数差

    Args:
        start: 开始日期
        end: 结束日期

    Returns:
        天数差
    """
    return DateTimeUtils.days_between(start, end)


def hours_between(start: datetime.datetime, end: datetime.datetime) -> float:
    """
    计算两个时间之间的小时差

    Args:
        start: 开始时间
        end: 结束时间

    Returns:
        小时差
    """
    return DateTimeUtils.hours_between(start, end)


def minutes_between(start: datetime.datetime, end: datetime.datetime) -> float:
    """
    计算两个时间之间的分钟差

    Args:
        start: 开始时间
        end: 结束时间

    Returns:
        分钟差
    """
    return DateTimeUtils.minutes_between(start, end)


def seconds_between(start: datetime.datetime, end: datetime.datetime) -> float:
    """
    计算两个时间之间的秒数差

    Args:
        start: 开始时间
        end: 结束时间

    Returns:
        秒数差
    """
    return DateTimeUtils.seconds_between(start, end)


def is_before(dt1: Union[datetime.datetime, datetime.date], 
             dt2: Union[datetime.datetime, datetime.date]) -> bool:
    """
    判断dt1是否在dt2之前

    Args:
        dt1: 第一个日期时间
        dt2: 第二个日期时间

    Returns:
        是否在之前
    """
    return DateTimeUtils.is_before(dt1, dt2)


def is_after(dt1: Union[datetime.datetime, datetime.date], 
            dt2: Union[datetime.datetime, datetime.date]) -> bool:
    """
    判断dt1是否在dt2之后

    Args:
        dt1: 第一个日期时间
        dt2: 第二个日期时间

    Returns:
        是否在之后
    """
    return DateTimeUtils.is_after(dt1, dt2)


def is_equal(dt1: Union[datetime.datetime, datetime.date], 
            dt2: Union[datetime.datetime, datetime.date]) -> bool:
    """
    判断两个日期时间是否相等

    Args:
        dt1: 第一个日期时间
        dt2: 第二个日期时间

    Returns:
        是否相等
    """
    return DateTimeUtils.is_equal(dt1, dt2)


def is_today(dt: Union[datetime.datetime, datetime.date]) -> bool:
    """
    判断是否是今天

    Args:
        dt: 日期时间对象

    Returns:
        是否是今天
    """
    return DateTimeUtils.is_today(dt)


def is_yesterday(dt: Union[datetime.datetime, datetime.date]) -> bool:
    """
    判断是否是昨天

    Args:
        dt: 日期时间对象

    Returns:
        是否是昨天
    """
    return DateTimeUtils.is_yesterday(dt)


def is_tomorrow(dt: Union[datetime.datetime, datetime.date]) -> bool:
    """
    判断是否是明天

    Args:
        dt: 日期时间对象

    Returns:
        是否是明天
    """
    return DateTimeUtils.is_tomorrow(dt)


def get_weekday(dt: Union[datetime.datetime, datetime.date]) -> int:
    """
    获取星期几（0-6，0表示周一）

    Args:
        dt: 日期时间对象

    Returns:
        星期几
    """
    return DateTimeUtils.get_weekday(dt)


def get_month_start(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
    """
    获取当月第一天

    Args:
        dt: 日期时间对象

    Returns:
        当月第一天
    """
    return DateTimeUtils.get_month_start(dt)


def get_month_end(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
    """
    获取当月最后一天

    Args:
        dt: 日期时间对象

    Returns:
        当月最后一天
    """
    return DateTimeUtils.get_month_end(dt)


def get_quarter_start(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
    """
    获取当季第一天

    Args:
        dt: 日期时间对象

    Returns:
        当季第一天
    """
    return DateTimeUtils.get_quarter_start(dt)


def get_quarter_end(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
    """
    获取当季最后一天

    Args:
        dt: 日期时间对象

    Returns:
        当季最后一天
    """
    return DateTimeUtils.get_quarter_end(dt)


def get_year_start(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
    """
    获取当年第一天

    Args:
        dt: 日期时间对象

    Returns:
        当年第一天
    """
    return DateTimeUtils.get_year_start(dt)


def get_year_end(dt: Union[datetime.datetime, datetime.date]) -> Union[datetime.datetime, datetime.date]:
    """
    获取当年最后一天

    Args:
        dt: 日期时间对象

    Returns:
        当年最后一天
    """
    return DateTimeUtils.get_year_end(dt)


def timestamp_to_datetime(timestamp: Union[int, float]) -> datetime.datetime:
    """
    时间戳转日期时间

    Args:
        timestamp: 时间戳

    Returns:
        日期时间对象
    """
    return DateTimeUtils.timestamp_to_datetime(timestamp)


def datetime_to_timestamp(dt: datetime.datetime) -> float:
    """
    日期时间转时间戳

    Args:
        dt: 日期时间对象

    Returns:
        时间戳
    """
    return DateTimeUtils.datetime_to_timestamp(dt)


def format_relative_time(dt: Union[datetime.datetime, datetime.date]) -> str:
    """
    格式化相对时间

    Args:
        dt: 日期时间对象

    Returns:
        相对时间字符串
    """
    return DateTimeUtils.format_relative_time(dt)


def parse_iso_format(date_str: str) -> datetime.datetime:
    """
    解析ISO格式的日期时间字符串

    Args:
        date_str: ISO格式的日期时间字符串

    Returns:
        日期时间对象
    """
    return DateTimeUtils.parse_iso_format(date_str)


def to_iso_format(dt: datetime.datetime) -> str:
    """
    转换为ISO格式的日期时间字符串

    Args:
        dt: 日期时间对象

    Returns:
        ISO格式的字符串
    """
    return DateTimeUtils.to_iso_format(dt)
