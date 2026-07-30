#вывод календаря за указанный месяц/год
from datetime import date
import calendar
month_length = 31,28,31,30,31,30,31,31,30,31,30,31
key_array = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
def print_month(month, year):
    idx = key_array.index(month) #находим номер месяца
    wd = date(year, idx + 1, 1).weekday()  #получаем первый день недели данного месяца в данном году
    days = month_length[idx]
    if calendar.isleap(year) and idx == 1: #если год високосный и месяц февраль
        days += 1
    print(f"{month} {year}".center(20))
    print("Пн Вт Ср Чт Пт Сб Вс")
    print('   ' * wd, end='')
    for day in range(days):
        wd = (wd + 1) % 7
        eow = ' ' if wd % 7 else '\n'
        print(f"{day+1:2}", end=eow)
    print()

#перегон строки в base32
def base32(s):
    val = 0
    for ch in s.lower():
        next_digit = ord(ch) - ord('а') #вычисляем значение очередной цифры
        val = 32 * val + next_digit #приписываем в конец
    return val


