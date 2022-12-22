# id   79834778

def read_input():
    _ = input()
    target = int(input())
    arr = [int(i) for i in input().split()]
    return arr, target


def binary_search(nums, target, left, right):
    if left >= right:
        return -1
    middle = (left + right) // 2
    if nums[middle] == target:
        return middle
    if target < nums[middle]:
        return binary_search(nums, target, left, middle)
    return binary_search(nums, target, middle + 1, right)


def divide_and_search(nums, target, left, right):
    if right - left == 1:
        return [left, right]
    middle = (left + right) // 2
    if nums[left] <= nums[middle]:
        if nums[left] <= target <= nums[middle]:
            return [left, middle + 1]
        return divide_and_search(nums, target, middle, right)
    if nums[middle] <= target <= nums[-1]:
        return [middle, right]
    return divide_and_search(nums, target, left, middle)


def broken_search(nums, target):
    left, right = divide_and_search(nums, target, 0, len(nums))
    return binary_search(nums, target, left, right)


if __name__ == '__main__':
    arr, target = read_input()
    print(broken_search(arr, target))
