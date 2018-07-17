def reverse_arr(arr):
    n = len(arr)
    for i in range(len(arr) // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr

a = [int(s) for s in input().split()]
print(a)
a = reverse_arr(a)
print(a)