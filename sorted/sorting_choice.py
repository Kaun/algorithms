def sort_choice(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

a = [11, 2, 9, 7, 1]
print(sort_choice(a))