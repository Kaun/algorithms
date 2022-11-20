def num_to_list(num):
    num_int = int(num)
    res = ''
    for i in range(len(num)):
        res += str(num_int % 10)
        num_int //= 10
    return list(map(int, reversed(list(res))))



def read_input():
    _ = input()
    num_list = list(map(int, input().split()))
    num2 = input()
    num2_list = num_to_list(num2)
    return num_list, num2_list



a, b = read_input()
a = [0]*(len(b)-len(a)) + a
b = [0]*(len(a)-len(b)) + b
print(" ".join(map(str, map(sum, zip(a, b)))))
