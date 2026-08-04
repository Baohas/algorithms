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

class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v

#неэффективная хэш таблица
class Hashtable:
    def __init__(self, M=10):
        self.table = [None] * M #заводим массив на М объектов
        self.M = M
    def get(self, k): #определяем номер ячейки по ключу к, для которого вычисляется хэш, если есть - вернет ее
        hc = hash(k) % self.M
        return self.table[hc].value if self.table[hc] else None
    def push(self, k, v): #определяет номер ячейки по ключу k, для него вычисляется хэш, ячейка перезаписывается, если данные есть, если нет, заполняет ячейку
        hc = hash(k) % self.M
        entry = self.table[hc]
        if entry:
            if entry.key == k:
                entry.value = v
            else: #если хэш двух ключей ведет на одну ячейку, то это коллизия, швыряем ошибку
                raise RuntimeError(f"Key collision: {k} and {entry.key}")
        else:
            self.table[hc] = Entry(k, v)

#хэш таблица с открытой адресацией
class Hastable_2:
    def __init__(self, M=10): #М - начальная длина хэш таблицы
        self.table = [None] * M
        self.M, self.N = M, 0
    def get(self, k):
        hc = hash(k) % self.M #вычисляем хэш для конкретного ключа
        while self.table[hc]:
            if self.table[hc].key == k: #если нашлась ячейка
                return self.table[hc].value #выдаем ее значение
            hc = (hc + 1) % self.M #если не нашлось, двигаемся в след ячейку
        return None #если же ячейки пустые, значит такого значения нет
    def put(self, k, v):
        hc = hash(k) % self.M
        while self.table[hc]:
            if self.table[hc].key == k: #ищем ячейку
                self.table[hc].value == v #записываем
                return
            hc = (hc + 1) % self.M #сдвиг на соседнюю ячейку, аналогично функции get()
        if self.N >= self.M - 1: #если ключа нет в таблице, а свободная ячейка осталась одна - швыряем RuntimeError
            raise RuntimeError(f"Hash-table is full")
        self.table[hc] = Entry(k, v) #загоняем пару в свободную ячейку
        self.N += 1 #увеличиваем счетчик
        
#хэш-таблица с раздельным хранением цепочек
class Hashtable_3:
    def __init__(self, M = 10):
        self.table = [[] for i in range(M)]
        self.M, self.N = M, 0
    def get(self, k):
        hc = hash(k) % self.M
        for entry in self.table[hc]:
            if entry.key == k:
                return entry.value
        return None
    def put(self, k, v):
        hc = hash(k) % self.M
        for entry in self.table[hc]:
            if entry.key == k:
                entry.value = v
                return
        self.table[hc].append(Entry(k, v))
        self.N += 1
    def remove(self, k):
        hc = hash(k) % self.M
        for i, entry in enumerate(self.table[hc]): #перебираем все пары (индекс, элемент)
            if entry.key == k:
                del self.table[hc][i]
                self.N -= 1
                return entry.value
        return None


#Динамическая хэш-таблица
class DynamicHashTable:
    def __init__(self, M = 10):
        self.table = [[] for i in range(M)]
        if M < 1:
            raise ValueError("Hashable storage must be at least 1")
        self.M = M
        self.N = 0
        self.load_factor = 0.75 #фактор загруженности
        self.treshold = min(M * self.load_factor, M - 1) #пороговая загруженность
    def get(self, k):
        hc = hash(k) % self.M
        for entry in self.table[hc]:
            if entry.key == k:
                return entry.value
        return None
    def put(self, k, v): #доработанная функция с вызовом resize()
        hc = hash(k) % self.M
        for entry in self.table[hc]:
            if entry.key == k:
                entry.value = v
                return
        self.table[hc].append(Entry(k, v)) #добавляем новую ячейку в конец цепочки
        self.N += 1
        if self.N >= self.treshold: #проверка - не превышен ли порог
            self.resize(2 * self.M + 1) #увеличиваем кол-во ячеек вдвое
    def resize(self, new_size): #динамическое масштабирование хэш-таблицы с открытой адресацией без повторного хэширования
        temp = DynamicHashTable(new_size) #создаем временную хэш-таблицу нужного размера
        for key, value in self.table:
            temp.put(key, value) #добавляем в нее все пары из старой хэш-таблицы
        self.table, self.M = temp.table, temp.M #обновляем массив ячеек и значение М
        self.treshold = self.load_factor * self.M #обновляем пороговую загрузку

    def resize2(self, new_size): #динамическое масштабирование хэш-таблицы с раздельным хранением цепочек путем повторного хэширования
        temp = DynamicHashTable(new_size)
        for bucket in self.table:
            for key, value in bucket:
                temp.put(key, value)
        self.table, self.M = temp.table, temp.M
        self.treshold = self.load_factor * self.M
