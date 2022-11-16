def zipper(a, b):
    res = []
    for i in range(0, len(a)):
        res.append(a[i])
        res.append(b[i])
    return res


def read_input():
    len_mas = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    return arr1, arr2

a, b = read_input()
print(" ".join(map(str, zipper(a,b))))
