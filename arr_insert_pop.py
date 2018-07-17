def pop_arr(arr, mode):
    arr_temp = [0] * (len(arr) - 1)
    if mode == 'top':
        for i in range(len(arr) - 1):
            arr_temp[i] = arr[i]
    else:
        for i in range(1, len(arr)):
            arr_temp[i - 1] = arr[i]
    return arr_temp

def insert_arr(arr, insert_elem, mode):
    arr_temp = [0] * (len(arr) + 1)
    if mode == 'top':
        for i in range(len(arr)):
            arr_temp[i] = arr[i]
        arr_temp[len(arr)] = insert_elem
    else:
        for i in range(1, len(arr) + 1):
            arr_temp[i] = arr[i - 1]
        arr_temp[0] = insert_elem
    return arr_temp

n = int(input())
a = [0] * n
for i in range(len(a)):
    a[i] = int(input())
print(a)
insert_element = int(input())
mode = input()
a = insert_arr(a, insert_element, mode)
print(a)
a = pop_arr(a, mode)
print(a)