'''
для каждого участка знать расстояние до ближайшего пустого участка. 
Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. 
Дома в городе Тимофея нумеровались в том порядке, в котором строились, 
поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.
'''

def read_input():
    a = input()
    n = [*map(int, (input().split()))]
    return n

def find_zero(arr):
    index_zero = []
    for i in range(len(arr)):
        if arr[i] == 0:
            index_zero.append(i)
    return index_zero
            

def nearest_zero(arr, index_zero):
    res = [1000000] * len(arr)
    for i in index_zero:
        for j in range(len(arr)):
            if abs(i-j)<res[j] and i!=j:
                res[j] = abs(j-i)
            if j == i:
                res[j] = 0
    return res
            


a = read_input()
zero = find_zero(a)
print(" ".join(map(str,nearest_zero(a, zero)))
