n_vert = int(input())
n_edges = int(input())

arr_cohesion = [[0 for j in range(n_vert)] for i in range(n_vert)]

visited = [False] * n_vert  

def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if visited[w] == False:
            dfs(w)

s = 0

adj_list = [[] for i in range(n_vert)]

for i in range(n_edges):
    a = [int(s) for s in input().split()]
    adj_list[a[0]].append(a[1])
    adj_list[a[1]].append(a[0])
    if a[0] != a[1]:
            arr_cohesion[a[0]][a[1]] = 1

dfs(s)

counter_weak = 1

while False in visited:
    for i in range(len(visited)):
        if not visited[i]:
            dfs(i)
            counter_weak += 1

for i in range(n_vert):
    arr_cohesion[i][i] = 1
for i in range(n_vert):
    for j in range(n_vert):
        if arr_cohesion[i][j] == 1:
            for k in range(n_vert):
                if arr_cohesion[j][k] == 1:
                    arr_cohesion[i][k] = 1


arr_cohesion_strong = [[0 for j in range(n_vert)] for i in range(n_vert)] 
for i in range(n_vert):
    for j in range(n_vert):
        if arr_cohesion[i][j] == arr_cohesion[j][i] == 1:
            arr_cohesion_strong[i][j] = 1

c = 0
counter_strong = 0

for i in range(n_vert):
    for j in range(i + 1, n_vert):
        if arr_cohesion_strong[i] == arr_cohesion_strong[j]:
            c += 1
    if c == 0:
        counter_strong += 1
    else:
        c = 0

print(counter_weak, counter_strong)
