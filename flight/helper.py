from datetime import datetime, time, timedelta, date

def sum_time_timedelta(a_time: time, a_timedelta: timedelta):
    dt = datetime.combine(date.today(), a_time) + a_timedelta
    return dt.time()
