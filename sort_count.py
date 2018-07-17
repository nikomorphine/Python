def count_sort(arr, min_elem, max_elem):
    arr_count = [0] * (max_elem - min_elem + 1)
    for i in arr:
        arr_count[i] += 1
    arr_temp = []
    for i in range(min_elem, 0):
        for j in range(arr_count[i]):
            arr_temp.append(i)
    for i in range(0, max_elem + 1):
        for j in range(arr_count[i]):
            arr_temp.append(i)
    return arr_temp
    
def SimpleCountingSort(A):
    count = max(A) + 1
    C = [0] * count
    for x in A:
        C[x] += 1
    A[:] = []
    for number in range(count):
        A += [number] * C[number]  
    
a = [int(s) for s in input().split()]
print(a)
max_a = max(a[0], a[1])
min_a = min(a[0], a[1])
for i in range(2, ((len(a) // 2) * 2), 2):
    max_temp = max(a[i], a[i + 1])
    min_temp = a[i] + a[i + 1] - max_temp
    if max_temp > max_a:
        max_a = max_temp
    if min_temp < min_a:
        min_a = min_temp
if len(a) % 2 == 1:
    if a[-1] > max_a:
        max_a = a[-1]
    elif a[-1] < min_a:
        min_a = a[-1]
        
a = count_sort(a, min_a, max_a)
print(a)
