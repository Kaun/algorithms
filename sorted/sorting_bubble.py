def read_input():
    _ = int(input())
    arr = [*map(int, input().split())]
    return arr


def sort_bubble(arr):
    is_be_ = True
    for i in range(len(arr)-1):
        is_be_sort = False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                is_be_ = False
                is_be_sort = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if is_be_sort:
            print(*arr)
    if is_be_:
        print(*arr)


if __name__ == '__main__':
    arr = read_input()
    sort_bubble(arr)

    # a = [11, 2, 9, 7, 1]
    # print(sort_bubble(a))