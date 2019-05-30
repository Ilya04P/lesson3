from datetime import datetime, timedelta, date

d_now = datetime.now()

def d_minus(date, num_of_days=0):
    num_of_days = timedelta(days=num_of_days)
    return date - num_of_days

def m_minus(date, num_of_month=0):
    pass

date_string = '01/01/17 12:10:03.234567'

date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(d_now)
print(d_minus(d_now, 1))
print(date_dt)
