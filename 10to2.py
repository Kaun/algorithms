def read_input():
    n = int(input())
    return n

def ten_to_two(n):
    arr =[]
    if n == 0:
        return [0]
    while n>0:
        arr.append(n%2)
        n = n//2
    return arr


n = read_input()
print("".join(map(str,reversed(ten_to_two(n)))))