from datetime import datetime, timedelta, date

d_now = datetime.now()
d_yesterday = d_now - timedelta(days=1)
d_month_befor = d_now - timedelta(days=30)

date_string = '01/01/17 12:10:03.234567'

date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(d_now)
print(d_yesterday)
print(d_month_befor)
print(date_dt)