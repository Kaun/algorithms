def read_input():
    _ = int(input())
    arr = [*input().split()]
    return arr


def less(num1, num2):
    if len(num1) == len(num2):
        return int(num1) > int(num2)
    else:
        item1 = int(num1 + num2)
        item2 = int(num2 + num1)
        return item1 > item2



def insertion_sort(array, key):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and key(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
            array[j] = item_to_insert
    return ''.join(map(str, array))


print(insertion_sort(read_input(), less))

