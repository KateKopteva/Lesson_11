"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран.
Примечание: в рамках задание создать два файла:classes.py и main.py. В
первом будут описаны все классы, во втором классы будут
импортированы и использованы."""
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure:
     def __init__(self, p1:Point, p2:Point=None, p3:Point=None, r=None):
         self.p1 = p1
         self.p2 = p2
         self.p3 = p3
         self.r = r

class Triangle(Figure):
    def sq(self):
        s_tr = 0.5 * abs((self.p1.x-self.p3.x)*(self.p1.y-self.p3.y) -
                      (self.p2.x - self.p3.x)*(self.p2.y - self.p3.y))
        return f'Площадь треугольника равна {s_tr}'
    def p(self):
        AB = (((self.p2.x - self.p1.x)**2) + (self.p2.y - self.p1.y)**2)**0.5
        AC = (((self.p3.x - self.p1.x)**2) + (self.p3.y - self.p1.y)**2)**0.5
        BC = (((self.p2.x - self.p3.x)**2) + (self.p2.y - self.p3.y)**2)**0.5
        p_tr = AB + AC + BC
        return f'Периметр треугольника равен {p_tr}'

class Circle(Figure):
     def p(self):
         p_cir = 2 * math.pi * self.r
         return f'Периметр окружности равен {p_cir}'
     def sq(self):
         s_cir = math.pi * self.r**2
         return f'Площадь окружности равна {s_cir}'

class Square(Figure):
    def p(self):
        AB = (((self.p2.x - self.p1.x) ** 2) + (self.p2.y - self.p1.y) ** 2) ** 0.5
        p_sq = AB * 4
        return f'Периметр квадрата равен {p_sq}'
    def sq(self):
        AB = (((self.p2.x - self.p1.x) ** 2) + (self.p2.y - self.p1.y) ** 2) ** 0.5
        s_sq = AB**2
        return f'Площадь квадрата равна {s_sq}'

