import random


def partition(arr, pivot):
    left = [x for x in arr if x < pivot]
    center = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left, center, right


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        left, center, right = partition(arr, pivot)
        return quicksort(left) + center + quicksort(right)

a = [4, 8, 12, 6, 8, 10, 5, 9, 144]
print(quicksort(a))