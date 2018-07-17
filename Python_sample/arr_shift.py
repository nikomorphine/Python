def sdvig(arr, mode):
    arr_temp = [0] * len(a)
    if mode == 'clockwise':
        arr_temp[0] = arr[-1]
        for i in range(0, len(arr) - 1):
            arr_temp[i + 1] = arr[i]
    if mode == 'counter clockwise':
        arr_temp[-1] = arr[0]
        for i in range(1, len(arr)):
            arr_temp[i - 1] = arr[i]
    return(arr_temp)

a = [int(s) for s in input().split()]
print(a)
mode = input()
print(sdvig(a, mode))