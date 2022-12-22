# id   79890018

def read_input():
    _ = input()
    target = int(input())
    arr = [int(i) for i in input().split()]
    return arr, target


def broken_search(arr, target):
    left,  right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        if arr[mid] <= arr[right]:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


if __name__ == '__main__':
    arr, target = read_input()
    print(broken_search(arr, target))
