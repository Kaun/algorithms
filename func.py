'''
Написать код функции, вычисляющей y = ax2 + bx + c. Напишите программу, которая будет по коэффициентам a, b, c и числу x выводить значение функции в точке x.

Формат ввода
На вход через пробел подаются целые числа a, x, b, c. В конце ввода находится перенос строки.

Формат вывода
Выведите одно число — значение функции в точке x.

'''

def read_input():
    a, x, b, c = list(map(int, input().split()))
    return a, x, b, c

def quadratic_equation(a, x, b, c):
    return a*x*x + b*x + c


a, x, b, c = read_input()
y = quadratic_equation(a, x, b, c)
print(y)