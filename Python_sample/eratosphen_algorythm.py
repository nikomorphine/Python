def eratosfen(arr):
    for i in range(2, len(arr)):
        for j in range(i + i, len(arr), i):
            arr[j] = True
    return arr[1:]

n = int(input())
arr = [False] * (n + 1)
print(eratosfen(arr))