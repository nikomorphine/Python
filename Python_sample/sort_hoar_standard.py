import random
def hoar_sort(A):
    if len(A) <= 1:
        return A
    else:
        mid = A[random.randint(0, len(A) - 1)]
        L = []
        M = []
        R = []
        for elem in A:
            if elem < mid:
                L.append(elem)
            elif elem > mid:
                R.append(elem)
            else:
                M.append(elem)
        return hoar_sort(L) + M + hoar_sort(R)
    
arr = [int(s) for s in input().split()]
print(arr)
print(hoar_sort(arr))