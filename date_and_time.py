from datetime import datetime, timedelta, date

d_now = datetime.now()

def d_minus(date, num_of_days=0): # Можно передать любое количесво дней на "-"
    '''
    Не знаю как проверить на соответсвие,
    что date - это дата. Проверять исключение TypeError на timedelta?
    '''
    if type(num_of_days) is not int: # Если передано не число
        return None
    num_of_days = timedelta(days=num_of_days)
    return date - num_of_days

def m_minus(date, num_of_month=0):
    if type(num_of_month) is not int:
        return None
    month = int(date.strftime('%m'))
    year = int(date.strftime('%Y'))
    month = month - num_of_month
    if month <= 0:
        while month <= 0:
            year = year - 1
            month = 12 - num_of_month
    return date.replace(year=year, month=month)

date_string = '01/01/17 12:10:03.234567'

date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(d_now)
print(d_minus(d_now, 1))
print(m_minus(d_now, 2))
print(date_dt)
