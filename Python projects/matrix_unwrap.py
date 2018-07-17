from math import ceil
def rotation(a, n):
    i_temp, j_temp = 0, 0
    a1_temp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n):
            a1_temp[i_temp][j_temp] = a[j][i]
            j_temp += 1
        i_temp += 1
        j_temp = 0
    return(a1_temp)

def layer(a, n):
    if n == 1:
        c.append(a[0][0])
    else:
        for j in range(4):
            for i in range(n-1):
                c.append(a[0][i])
            a = rotation(a, n)

def reduction(a, n):
    if n == 1 or n == 2:
        return(a)
    else:
        i_temp, j_temp =0, 0
        temp = [[0 for j in range(n - 2)] for i in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                temp[i_temp][j_temp] = a[i][j]
                j_temp += 1
            i_temp += 1
            j_temp = 0
        return(temp)

n = int(input())
a = []
for i in range(n):
    c = [int(s) for s in input().split()]
    a.append(c)
    c = []

for i in range(ceil(n / 2)):
    layer(a, n)
    a = reduction(a, n)
    n -= 2

for i in range(len(c)):
    print(c[i], end = ' ')

if len(c) == 0:
    print(-1)
