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

def m_minus(date):
    day_now = int(date.strftime('%d')) # Определяю текущий день
    date_first = date.replace(day=1) # устанавлюваю 1 число текущего месяца
    date_to_be = date_first - timedelta(days=1) # последний число предыдущего месяца
    day_to_be = int(date_to_be.strftime('%d')) # определение последнего дня месяца

    if day_to_be > day_now: # Если число последнего деня месяца больше текущего числа
        return date_to_be.replace(day=day_now) # установить для предыдущего месяца текущее число
    else:
        return date_to_be # иначе установить последнюю дату предыдущего месяца

date_string = '01/01/17 12:10:03.234567'

date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(d_now)
print(d_minus(d_now, 1))
print(m_minus(d_now))
print(date_dt)
