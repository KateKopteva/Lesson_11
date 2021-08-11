from task_11_2_classes import *
figs = []
figs.append(Triangle(Point(10,2), Point(5,2), Point(3,3)))
figs.append(Circle(Point(10,2), r = 5))
figs.append(Square(Point(10,2), Point(5,2)))
for i in figs:
    print(i.sq())
