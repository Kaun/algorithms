# id 79834778

def read_input():
    _ = input()
    target = int(input())
    arr = [*map(int, (input().split()))]
    return arr, target


def binary_search(nums, target, left, right):
    if left >= right:
        return -1
    middle = (left + right) // 2
    if nums[middle] == target:
        return middle
    elif target < nums[middle]:
        return binary_search(nums, target, left, middle)
    else:
        return binary_search(nums, target, middle + 1, right)


def divide_and_search(nums, target, left, right):
    if right - left == 1:
        return [left, right]
    middle = (left + right) // 2
    if nums[left] <= nums[middle]:
        if nums[left] <= target <= nums[middle]:
            return [left, middle + 1]
        else:
            return divide_and_search(nums, target, middle, right)
    else:
        if nums[middle] <= target <= nums[-1]:
            return [middle, right]
        else:
            return divide_and_search(nums, target, left, middle)


def broken_search(nums, target):
    left, right = divide_and_search(nums, target, 0, len(nums))
    return binary_search(nums, target, left, right)


if __name__ == '__main__':
    arr, target = read_input()
    print(broken_search(arr, target))
