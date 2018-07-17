n_vert = int(input())
n_edges = int(input())

answer = True

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

dfs(s)

if False in visited:
    print('NO')
else:
    answer = True
    for i in range(n_vert):
        if len(adj_list[i]) % 2 != 0:
            answer = False
            break
    if answer:
        print('YES')
    else:
        print('NO')