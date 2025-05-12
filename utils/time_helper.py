from datetime import datetime, timedelta

def get_vietnam_time():
    return datetime.utcnow() + timedelta(hours=7)
