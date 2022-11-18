'''
Есть два числа в двоичной системе счисления, требуется вывести их сумму, также в двоичной системе.
Нельзя использовать встроенные библиотеки
'''

def read_input():
    a = input()
    b = input()
    add_str = '0'*abs(len(a) - len(b))
    if len(a) < len(b):
        a = add_str + a
    elif len(a) > len(b):
        b = add_str + b
    return a, b


def sum(num1, num2, buff):
    s = num1 + num2 + buff
    if s == 3:
        return 1, 1
    if s == 2:
        return 0, 1
    if s == 1:
        return 1, 0
    return 0, 0

def bin_sum(a, b):
    buff = 0
    result = []
    for i in range(len(a)-1, -1, -1):
        el1 = int(a[i])
        el2 = int(b[i])
        el, buff = sum(el1, el2, buff)
        result.append(el)
    if buff != 0:
        result.append(buff)
    return result   
        
   
a, b = read_input()
print("".join(map(str, reversed(bin_sum(a, b)))))
