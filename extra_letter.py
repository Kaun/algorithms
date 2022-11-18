'''
Есть 2 строки s и t, состоящие только из строчных букв. 
Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. 
Нужно найти добавленную букву.
Формат ввода
На вход подаются строки s и t, разделённые переносом строки. 
Длины строк не превосходят 1000 символов. Строки не бывают пустыми.
'''

def read_input():
    s = list(input())
    t = list(input())
    return s,t

def extra_letter(s,t):
    for i in s:
        if i in t:
            t.remove(i)
        else:
            return i
    return t

s, t = read_input()
print("".join(extra_letter(s, t)))