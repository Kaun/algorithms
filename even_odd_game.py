'''
на экране появляются три случайных числа. Если все три числа оказываются одной чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода
В первой строке записаны три случайных целых числа a, b и c. Числа не превосходят 109 по модулю.
'''

def read_input():
    return list(map(int, input().split()))

def even_odd(arr):
    odd = True if arr[0] % 2 == 0 else False
    for i in arr[1:]:
        next = True if i % 2 == 0 else False
        if next == odd:
           continue
        else:
            return 'FAIL'
    return 'WIN'

print(even_odd(read_input()))