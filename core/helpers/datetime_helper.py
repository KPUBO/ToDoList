from datetime import datetime


class DateTimeHelper:
    @classmethod
    def to_datetime(cls, date_time_str: str):
        return datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S').date()

    @classmethod
    def to_str(cls, date_time: datetime):
        return date_time.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def without_tzinfo(cls, date_time: datetime):
        return date_time.replace(tzinfo=None)

    @classmethod
    def get_suffix_by_file(cls):
        return datetime.now().strftime('%Y-%m-%d_%H:%M:%S_%f')

    @staticmethod
    def to_datetime_minutes(timestamp: datetime):
        return timestamp.strftime('%d.%m.%Y %H:%M')
