'''
Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.

Измерения велись n секунд.

В секунду i поступает qi запросов.

Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.
'''



def moving_average(arr, k):
    res = []
    average = sum(arr[:k])
    res.append(average/k)
    for i in range(0, len(arr)-k):
        average = average - arr[i] + arr[i+k]
        res.append(average/k)
    return res


number_mesur = int(input())
mesur = list(map(int, input().split()))
window = int(input())

print(" ".join(map(str, moving_average(mesur, window))))

