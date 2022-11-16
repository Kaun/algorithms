'''
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

В первой строке записано количество фишек n, 2 ≤ n ≤ 104.
Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне от -105 до 105.
В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.
'''

def two_sum(arr, num):
    arr.sort()
    start_pos = 0
    end_pos = len(arr)-1
    while start_pos < end_pos:
        res = arr[start_pos] + arr[end_pos]
        if res == num:
            return arr[start_pos], arr[end_pos]
        if res < num:
            start_pos += 1
        else:
            end_pos -= 1
    return None


number_elements = int(input())
arr = list(map(int, input().split()))
required_value = int(input())

res = two_sum(arr, required_value)
if res != None:
    print(" ".join(map(str, res)))
else:
    print(None)