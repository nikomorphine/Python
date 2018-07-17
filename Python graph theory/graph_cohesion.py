n_vert = int(input())
n_edges = int(input())

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

dfs(s)

if False in visited:
    print('NO')
else:
    print('YES')