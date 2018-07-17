def is_sorted(arr, mode):
    if mode == 'ascending':
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
    if mode == 'descending':
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                return False
    return True

a = [int(s) for s in input().split()]
print(a)
mode = input()
if is_sorted(a, mode):
    print('SORTED')
else:
    print('UNSORTED')