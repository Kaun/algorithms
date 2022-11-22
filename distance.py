# id 75671532

'''
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить,
имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего
пустого участка. Если участок пустой, эта величина будет равна нулю —
расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта
улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились,
поэтому их номера на карте никак не упорядочены.
Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106).
В следующей строке записаны n целых неотрицательных чисел — номера домов и
обозначения пустых участков на карте (нули).
Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля.
Числа выводите в одну строку, разделяя их пробелами.
'''


def read_input():
    _ = input()
    arr = [*map(int, (input().split()))]
    return arr


def distance(arr):
    new_arr = [0 for _ in range(len(arr))]
    start_pos = 0
    end_pos = 0
    count = 0
    while end_pos < len(arr):
        if arr[end_pos] == 0:
            count += 1
            while start_pos < end_pos:
                distance = end_pos - start_pos
                if distance < new_arr[start_pos] or count == 1:
                    new_arr[start_pos] = distance
                start_pos += 1
            start_pos = end_pos
        else:
            new_arr[end_pos] = end_pos - start_pos
        end_pos += 1
    return new_arr


if __name__ == '__main__':
    input_arr = read_input()
    print(" ".join(map(str, distance(input_arr))))
