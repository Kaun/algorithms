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
            end = middle - 1


def find_pivot(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        middle = (start + end) // 2
        if arr[middle] > arr[middle + 1]:
            return middle + 1
        if arr[middle] < arr[end]:
            end = middle
        else:
            start = middle


def broken_search(nums, target):
    pivot = find_pivot(nums)
    res = None
    if pivot is None:
        pivot = 0
    if nums[0] <= target <= nums[pivot-1]:
        res = binary_search(nums[:pivot], target)
    elif nums[pivot] <= target <= nums[-1]:
        res = binary_search(nums[pivot:], target)
        if res is not None:
            res = pivot + res
    if res is not None:
        return res
    return -1


# if __name__ == '__main__':
#     arr, target = read_input()
#     print(broken_search(arr, target))

a = [1]
print(broken_search(a,1))
