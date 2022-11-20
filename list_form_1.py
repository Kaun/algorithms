def read_input():
    _ = input()
    num_str = "".join(input().split())
    num_1 = int(num_str)
    num_2 = int(input())
    return num_1, num_2


num1, num2 = read_input()
res = num1 + num2
print(" ".join(str(res)))