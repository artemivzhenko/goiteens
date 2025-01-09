#my_module

from my_module import print_message

print("1. my_module:")
print_message("Привет, мир!")


#my_math

from my_math import add, subtract

print(" ")
print("2. my_math:")
x = 10
y = 5
print("Сложение:", add(x, y))
print("Вычитание:", subtract(x, y))


#my_geometry

from my_geometry import circle_area, rectangle_area

print(" ")
print("3. my_geometry:")
radius = 5
width = 10
height = 4

print("Площадь круга:", circle_area(radius))
print("Площадь прямоугольника:", rectangle_area(width, height))


#my_data

from my_data import data

print(" ")
print("4. my_data:")
print("Список данных:", data)


#my_statistics

from my_data import data
from my_statistics import mean, median, variance

print(" ")
print("5. my_statistics:")
print("Среднее значение:", mean(data))
print("Медиана:", median(data))
print("Дисперсия:", variance(data))