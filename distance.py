def read_input():
    a = input()
    n = [*map(int, (input().split()))]
    return n


def distance(arr):
    new_arr = [0 for _ in range(len(arr))]
    start_pos = 0
    end_pos = 0
    count=0
    while end_pos < len(arr):
        if arr[end_pos] == 0:
            count += 1
            while start_pos < end_pos:
                l = end_pos - start_pos
                if l < new_arr[start_pos] or count==1:
                    new_arr[start_pos] = l
                    start_pos += 1
                else:
                    start_pos += 1
            start_pos = end_pos
            end_pos += 1
        else:
            new_arr[end_pos] = end_pos - start_pos
            end_pos += 1
            
        
    return new_arr


a = read_input()
print(" ".join(map(str,distance(a))))