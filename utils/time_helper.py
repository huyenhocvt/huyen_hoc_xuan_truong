from datetime import datetime, timedelta
import pytz

def get_current_time_str():
    tz = pytz.timezone("Asia/Ho_Chi_Minh")
    now = datetime.now(tz)
    return now.strftime("%H:%M - %d/%m/%Y")

def get_today_date():
    tz = pytz.timezone("Asia/Ho_Chi_Minh")
    return datetime.now(tz).date()

def get_tomorrow_date():
    return get_today_date() + timedelta(days=1)
