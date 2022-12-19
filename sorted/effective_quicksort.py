# id 79728615

def quicksort(arr, left, right):
    if left >= right:
        return
    i, j = left, right
    pivot = arr[(left+right)//2]

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    quicksort(arr, left, j)
    quicksort(arr, i, right)


def main():
    n = int(input())
    persons = [None] * n
    for i in range(n):
        name, solved, errors = input().split()
        persons[i] = (-int(solved), int(errors), name)

    quicksort(persons, 0, len(persons)-1)
    for person in persons:
        print(person[2])


if __name__ == '__main__':
    main()
