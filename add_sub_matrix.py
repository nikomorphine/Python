def sub_add_matrix(matrix1, matrix2, mode):
    res = [[0] * n for i in range(m)]
    if mode == 'add':
        for i in range(m):
            for j in range(n):
                res[i][j] = matrix1[i][j] + matrix2[i][j]
    else:
        for i in range(m):
            for j in range(n):
                res[i][j] = matrix1[i][j] - matrix2[i][j]
    return res

n = int(input())
m = int(input())
matrix1 = [[0] * n for i in range(m)]
matrix2 = [[0] * n for i in range(m)]
mode = input()

for i in range(m):
    for j in range(n):
        matrix1[i][j] = int(input())2

for i in range(m):
    for j in range(n):
        matrix2[i][j] = int(input())

print(sub_add_matrix(matrix1, matrix2, mode))