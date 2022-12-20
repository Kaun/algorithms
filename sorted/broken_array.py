def read_input():
    _ = input()
    target = int(input())
    arr = [*map(int, (input().split()))]
    return arr, target



def binary_search(arr, value):
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == value:
            return middle
        if arr[middle] < value:
            start = middle + 1
        else:
            end = middle -1
    return -1
    


def broken_search(nums, target):
    pivot = find_pivot(nums)
    if pivot is not None:
        pivot += 1
    else:
        pivot = 0
    if target < pivot:
        return binary_search(nums[:pivot], target)
    return pivot + binary_search(nums[pivot:], target)


def find_pivot(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        middle = (start + end) // 2
        if arr[middle] > arr[middle + 1]:
            return middle
        if arr[middle] < arr[end]:
            end = middle
        else:
            start = middle
    

if __name__ == '__main__':
    arr, target = read_input()
    print(broken_search(arr, target))


# arr = [5,1]
# print(broken_search(arr, 1))