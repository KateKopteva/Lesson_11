"""Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров"""

from functools import total_ordering
@total_ordering

class MyTime:
    def __init__(self, str_time = None, mytime_obj = None, hours = 0, minutes = 0, seconds = 0):
        if str_time:
            s = str_time.split(':')
            self.hours = int(s[0])
            self.minutes = int(s[1])
            self.seconds = int(s[2])
        elif mytime_obj:
            self.hours = mytime_obj.hours
            self.minutes = mytime_obj.minutes
            self.seconds = mytime_obj.seconds
        else:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def __eq__(self, other): # сравнение ==
        return (self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds)

    def __lt__(self, other): # меньше <
        if self.hours < other.hours:
            return True
        if self.hours > other.hours:
            return False
        if self.minutes < other.minutes:
            return True
        if self.minutes > other.minutes:
            return False
        if self.seconds < other.seconds:
            return True
        if self.seconds > other.seconds:
            return False

    def __add__(self, other): # сложение
        h = self.hours + other.hours
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        return MyTime(hours=h, minutes=m, seconds=s)

    def __sub__(self, other): # вычитание
        self.hours -= other.hours
        self.minutes -= other.minutes
        self.seconds -= other.seconds
        return self

obj_1 = MyTime(str_time= '12:13:14')
obj_2 = MyTime(hours=22, minutes=32, seconds=52)
print(obj_1+obj_2)
print(obj_1)