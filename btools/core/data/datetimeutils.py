from datetime import datetime, date, time, timedelta
import time as time_module
import calendar
from typing import Optional, Union, List, Dict
import pytz


class DateTimeUtils:
    """
    时间日期工具类，提供增强的时间日期处理功能
    """

    # 常用时间格式
    FORMAT_DATE = "%Y-%m-%d"
    FORMAT_TIME = "%H:%M:%S"
    FORMAT_DATETIME = "%Y-%m-%d %H:%M:%S"
    FORMAT_DATETIME_MS = "%Y-%m-%d %H:%M:%S.%f"
    FORMAT_ISO = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def now() -> datetime:
        """
        获取当前时间
        
        Returns:
            当前时间的datetime对象
        """
        return datetime.now()

    @staticmethod
    def today() -> date:
        """
        获取今天的日期
        
        Returns:
            今天日期的date对象
        """
        return date.today()

    @staticmethod
    def format_datetime(dt: datetime, format: str = FORMAT_DATETIME) -> str:
        """
        格式化时间日期
        
        Args:
            dt: datetime对象
            format: 格式化字符串，默认为FORMAT_DATETIME
            
        Returns:
            格式化后的字符串
        """
        return dt.strftime(format)

    @staticmethod
    def parse_datetime(dt_str: str, format: str = FORMAT_DATETIME) -> datetime:
        """
        解析时间日期字符串
        
        Args:
            dt_str: 时间日期字符串
            format: 格式化字符串，默认为FORMAT_DATETIME
            
        Returns:
            解析后的datetime对象
        """
        return datetime.strptime(dt_str, format)

    @staticmethod
    def format_date(d: date, format: str = FORMAT_DATE) -> str:
        """
        格式化日期
        
        Args:
            d: date对象
            format: 格式化字符串，默认为FORMAT_DATE
            
        Returns:
            格式化后的字符串
        """
        return d.strftime(format)

    @staticmethod
    def parse_date(date_str: str, format: str = FORMAT_DATE) -> date:
        """
        解析日期字符串
        
        Args:
            date_str: 日期字符串
            format: 格式化字符串，默认为FORMAT_DATE
            
        Returns:
            解析后的date对象
        """
        return datetime.strptime(date_str, format).date()

    @staticmethod
    def format_time(t: time, format: str = FORMAT_TIME) -> str:
        """
        格式化时间
        
        Args:
            t: time对象
            format: 格式化字符串，默认为FORMAT_TIME
            
        Returns:
            格式化后的字符串
        """
        return t.strftime(format)

    @staticmethod
    def parse_time(time_str: str, format: str = FORMAT_TIME) -> time:
        """
        解析时间字符串
        
        Args:
            time_str: 时间字符串
            format: 格式化字符串，默认为FORMAT_TIME
            
        Returns:
            解析后的time对象
        """
        return datetime.strptime(time_str, format).time()

    @staticmethod
    def timestamp() -> float:
        """
        获取当前时间戳（秒）
        
        Returns:
            当前时间戳
        """
        return time_module.time()

    @staticmethod
    def timestamp_ms() -> float:
        """
        获取当前时间戳（毫秒）
        
        Returns:
            当前时间戳（毫秒）
        """
        return time_module.time() * 1000

    @staticmethod
    def datetime_from_timestamp(timestamp: float) -> datetime:
        """
        从时间戳创建datetime对象
        
        Args:
            timestamp: 时间戳
            
        Returns:
            datetime对象
        """
        return datetime.fromtimestamp(timestamp)

    @staticmethod
    def timestamp_from_datetime(dt: datetime) -> float:
        """
        从datetime对象获取时间戳
        
        Args:
            dt: datetime对象
            
        Returns:
            时间戳
        """
        return dt.timestamp()

    @staticmethod
    def time_difference(start: datetime, end: datetime) -> timedelta:
        """
        计算时间差
        
        Args:
            start: 开始时间
            end: 结束时间
            
        Returns:
            时间差
        """
        return end - start

    @staticmethod
    def days_between(start: date, end: date) -> int:
        """
        计算两个日期之间的天数
        
        Args:
            start: 开始日期
            end: 结束日期
            
        Returns:
            天数差
        """
        return (end - start).days

    @staticmethod
    def add_days(dt: Union[date, datetime], days: int) -> Union[date, datetime]:
        """
        添加天数
        
        Args:
            dt: 日期或时间日期对象
            days: 要添加的天数
            
        Returns:
            新的日期或时间日期对象
        """
        return dt + timedelta(days=days)

    @staticmethod
    def add_hours(dt: datetime, hours: int) -> datetime:
        """
        添加小时
        
        Args:
            dt: datetime对象
            hours: 要添加的小时数
            
        Returns:
            新的datetime对象
        """
        return dt + timedelta(hours=hours)

    @staticmethod
    def add_minutes(dt: datetime, minutes: int) -> datetime:
        """
        添加分钟
        
        Args:
            dt: datetime对象
            minutes: 要添加的分钟数
            
        Returns:
            新的datetime对象
        """
        return dt + timedelta(minutes=minutes)

    @staticmethod
    def add_seconds(dt: datetime, seconds: int) -> datetime:
        """
        添加秒数
        
        Args:
            dt: datetime对象
            seconds: 要添加的秒数
            
        Returns:
            新的datetime对象
        """
        return dt + timedelta(seconds=seconds)

    @staticmethod
    def is_weekend(dt: Union[date, datetime]) -> bool:
        """
        判断是否为周末
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            是周末返回True，否则返回False
        """
        return dt.weekday() in [5, 6]

    @staticmethod
    def is_weekday(dt: Union[date, datetime]) -> bool:
        """
        判断是否为工作日
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            是工作日返回True，否则返回False
        """
        return dt.weekday() in [0, 1, 2, 3, 4]

    @staticmethod
    def get_weekday(dt: Union[date, datetime]) -> int:
        """
        获取星期几（0-6，0表示周一）
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            星期几
        """
        return dt.weekday()

    @staticmethod
    def get_weekday_name(dt: Union[date, datetime], language: str = 'zh') -> str:
        """
        获取星期几的名称
        
        Args:
            dt: 日期或时间日期对象
            language: 语言，可选值：zh（中文）, en（英文）
            
        Returns:
            星期几的名称
        """
        weekdays_zh = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        weekdays_en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        if language == 'zh':
            return weekdays_zh[dt.weekday()]
        else:
            return weekdays_en[dt.weekday()]

    @staticmethod
    def get_month_name(dt: Union[date, datetime], language: str = 'zh') -> str:
        """
        获取月份名称
        
        Args:
            dt: 日期或时间日期对象
            language: 语言，可选值：zh（中文）, en（英文）
            
        Returns:
            月份名称
        """
        months_zh = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
        months_en = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        if language == 'zh':
            return months_zh[dt.month - 1]
        else:
            return months_en[dt.month - 1]

    @staticmethod
    def get_quarter(dt: Union[date, datetime]) -> int:
        """
        获取季度
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            季度（1-4）
        """
        return (dt.month - 1) // 3 + 1

    @staticmethod
    def get_days_in_month(year: int, month: int) -> int:
        """
        获取月份的天数
        
        Args:
            year: 年份
            month: 月份
            
        Returns:
            天数
        """
        return calendar.monthrange(year, month)[1]

    @staticmethod
    def get_first_day_of_month(dt: Union[date, datetime]) -> date:
        """
        获取月份的第一天
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            月份的第一天
        """
        return date(dt.year, dt.month, 1)

    @staticmethod
    def get_last_day_of_month(dt: Union[date, datetime]) -> date:
        """
        获取月份的最后一天
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            月份的最后一天
        """
        last_day = calendar.monthrange(dt.year, dt.month)[1]
        return date(dt.year, dt.month, last_day)

    @staticmethod
    def get_first_day_of_quarter(dt: Union[date, datetime]) -> date:
        """
        获取季度的第一天
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            季度的第一天
        """
        quarter = DateTimeUtils.get_quarter(dt)
        month = (quarter - 1) * 3 + 1
        return date(dt.year, month, 1)

    @staticmethod
    def get_last_day_of_quarter(dt: Union[date, datetime]) -> date:
        """
        获取季度的最后一天
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            季度的最后一天
        """
        quarter = DateTimeUtils.get_quarter(dt)
        month = quarter * 3
        last_day = calendar.monthrange(dt.year, month)[1]
        return date(dt.year, month, last_day)

    @staticmethod
    def get_first_day_of_year(dt: Union[date, datetime]) -> date:
        """
        获取年份的第一天
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            年份的第一天
        """
        return date(dt.year, 1, 1)

    @staticmethod
    def get_last_day_of_year(dt: Union[date, datetime]) -> date:
        """
        获取年份的最后一天
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            年份的最后一天
        """
        return date(dt.year, 12, 31)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        判断是否为闰年
        
        Args:
            year: 年份
            
        Returns:
            是闰年返回True，否则返回False
        """
        return calendar.isleap(year)

    @staticmethod
    def get_timezone(timezone_name: str) -> pytz.tzinfo.DstTzInfo:
        """
        获取时区对象
        
        Args:
            timezone_name: 时区名称，例如：Asia/Shanghai
            
        Returns:
            时区对象
        """
        return pytz.timezone(timezone_name)

    @staticmethod
    def localize(dt: datetime, timezone: Union[str, pytz.tzinfo.DstTzInfo]) -> datetime:
        """
        本地化时间
        
        Args:
            dt: naive datetime对象
            timezone: 时区名称或时区对象
            
        Returns:
            本地化后的datetime对象
        """
        if isinstance(timezone, str):
            timezone = pytz.timezone(timezone)
        return timezone.localize(dt)

    @staticmethod
    def convert_timezone(dt: datetime, target_timezone: Union[str, pytz.tzinfo.DstTzInfo]) -> datetime:
        """
        转换时区
        
        Args:
            dt: aware datetime对象
            target_timezone: 目标时区名称或时区对象
            
        Returns:
            转换后的datetime对象
        """
        if isinstance(target_timezone, str):
            target_timezone = pytz.timezone(target_timezone)
        return dt.astimezone(target_timezone)

    @staticmethod
    def get_utc_now() -> datetime:
        """
        获取当前UTC时间
        
        Returns:
            当前UTC时间
        """
        return datetime.utcnow().replace(tzinfo=pytz.utc)

    @staticmethod
    def parse_iso_datetime(iso_str: str) -> datetime:
        """
        解析ISO格式的时间字符串
        
        Args:
            iso_str: ISO格式的时间字符串
            
        Returns:
            datetime对象
        """
        return datetime.fromisoformat(iso_str)

    @staticmethod
    def format_iso_datetime(dt: datetime) -> str:
        """
        格式化为ISO格式的时间字符串
        
        Args:
            dt: datetime对象
            
        Returns:
            ISO格式的时间字符串
        """
        return dt.isoformat()

    @staticmethod
    def get_business_days(start: date, end: date, holidays: List[date] = None) -> List[date]:
        """
        获取两个日期之间的工作日
        
        Args:
            start: 开始日期
            end: 结束日期
            holidays: 节假日列表
            
        Returns:
            工作日列表
        """
        if holidays is None:
            holidays = []
        
        business_days = []
        current = start
        while current <= end:
            if current.weekday() in [0, 1, 2, 3, 4] and current not in holidays:
                business_days.append(current)
            current += timedelta(days=1)
        return business_days

    @staticmethod
    def get_next_business_day(dt: date, holidays: List[date] = None) -> date:
        """
        获取下一个工作日
        
        Args:
            dt: 日期
            holidays: 节假日列表
            
        Returns:
            下一个工作日
        """
        if holidays is None:
            holidays = []
        
        next_day = dt + timedelta(days=1)
        while next_day.weekday() in [5, 6] or next_day in holidays:
            next_day += timedelta(days=1)
        return next_day

    @staticmethod
    def get_previous_business_day(dt: date, holidays: List[date] = None) -> date:
        """
        获取上一个工作日
        
        Args:
            dt: 日期
            holidays: 节假日列表
            
        Returns:
            上一个工作日
        """
        if holidays is None:
            holidays = []
        
        prev_day = dt - timedelta(days=1)
        while prev_day.weekday() in [5, 6] or prev_day in holidays:
            prev_day -= timedelta(days=1)
        return prev_day

    @staticmethod
    def format_duration(seconds: float) -> str:
        """
        格式化持续时间
        
        Args:
            seconds: 持续时间（秒）
            
        Returns:
            格式化后的持续时间字符串
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        
        parts = []
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        if secs > 0 or not parts:
            parts.append(f"{secs}s")
        
        return " ".join(parts)

    @staticmethod
    def parse_duration(duration_str: str) -> float:
        """
        解析持续时间字符串
        
        Args:
            duration_str: 持续时间字符串，例如："1h 30m 45s"
            
        Returns:
            持续时间（秒）
        """
        total_seconds = 0
        parts = duration_str.split()
        
        for part in parts:
            if part.endswith('h'):
                total_seconds += float(part[:-1]) * 3600
            elif part.endswith('m'):
                total_seconds += float(part[:-1]) * 60
            elif part.endswith('s'):
                total_seconds += float(part[:-1])
        
        return total_seconds

    @staticmethod
    def get_age(birth_date: date) -> int:
        """
        计算年龄
        
        Args:
            birth_date: 出生日期
            
        Returns:
            年龄
        """
        today = date.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    @staticmethod
    def is_birthday(birth_date: date) -> bool:
        """
        判断今天是否是生日
        
        Args:
            birth_date: 出生日期
            
        Returns:
            是生日返回True，否则返回False
        """
        today = date.today()
        return (today.month, today.day) == (birth_date.month, birth_date.day)

    @staticmethod
    def get_next_birthday(birth_date: date) -> date:
        """
        获取下一个生日
        
        Args:
            birth_date: 出生日期
            
        Returns:
            下一个生日日期
        """
        today = date.today()
        next_birthday = date(today.year, birth_date.month, birth_date.day)
        if next_birthday < today:
            next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
        return next_birthday

    @staticmethod
    def get_date_range(start: date, end: date) -> List[date]:
        """
        获取两个日期之间的所有日期
        
        Args:
            start: 开始日期
            end: 结束日期
            
        Returns:
            日期列表
        """
        dates = []
        current = start
        while current <= end:
            dates.append(current)
            current += timedelta(days=1)
        return dates

    @staticmethod
    def get_week_range(dt: Union[date, datetime]) -> Dict[str, date]:
        """
        获取所在周的开始和结束日期
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            包含开始和结束日期的字典
        """
        # 获取本周一
        start = dt - timedelta(days=dt.weekday())
        # 获取本周日
        end = start + timedelta(days=6)
        
        if isinstance(start, datetime):
            start = start.date()
        if isinstance(end, datetime):
            end = end.date()
        
        return {
            'start': start,
            'end': end
        }

    @staticmethod
    def get_month_range(dt: Union[date, datetime]) -> Dict[str, date]:
        """
        获取所在月的开始和结束日期
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            包含开始和结束日期的字典
        """
        start = DateTimeUtils.get_first_day_of_month(dt)
        end = DateTimeUtils.get_last_day_of_month(dt)
        
        if isinstance(start, datetime):
            start = start.date()
        if isinstance(end, datetime):
            end = end.date()
        
        return {
            'start': start,
            'end': end
        }

    @staticmethod
    def get_quarter_range(dt: Union[date, datetime]) -> Dict[str, date]:
        """
        获取所在季度的开始和结束日期
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            包含开始和结束日期的字典
        """
        start = DateTimeUtils.get_first_day_of_quarter(dt)
        end = DateTimeUtils.get_last_day_of_quarter(dt)
        
        if isinstance(start, datetime):
            start = start.date()
        if isinstance(end, datetime):
            end = end.date()
        
        return {
            'start': start,
            'end': end
        }

    @staticmethod
    def get_year_range(dt: Union[date, datetime]) -> Dict[str, date]:
        """
        获取所在年的开始和结束日期
        
        Args:
            dt: 日期或时间日期对象
            
        Returns:
            包含开始和结束日期的字典
        """
        start = DateTimeUtils.get_first_day_of_year(dt)
        end = DateTimeUtils.get_last_day_of_year(dt)
        
        if isinstance(start, datetime):
            start = start.date()
        if isinstance(end, datetime):
            end = end.date()
        
        return {
            'start': start,
            'end': end
        }