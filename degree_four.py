def read_input():
    k = int(input())
    return k


def degree_4(num):
    n = [4**n for n in range(0, 10000)]
    if num in n:
        return True
    return False


num = read_input()
print(degree_4(num))
