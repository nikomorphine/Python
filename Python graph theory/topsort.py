n_vert, n_edges = (int(s) for s in input().split())

adj_list = [[] for i in range(n_vert)]

for i in range(n_edges):
    temp = [int(s) for s in input().split()]
    adj_list[temp[0]].append(temp[1])

colour = [0] * n_vert  
stack = []

def dfs(v): 
    global answer 
    colour[v] = 'grey'
    for u in adj_list[v]: 
        if colour[u] == 'white': 
            dfs(u) 
        if colour[u] == 'grey': 
            print('NO')
            exit()
            return 
    colour[v] = 'black'
    stack.append(v)

stck.invert()

print(*stack)

n, m = map(int, input().split())
adj = [[] for i in range(n)]
color = [int(0) for i in range(n)]
topSort = []
for i in range(m):
    v, w = map(int, input().split())
    adj[v].append(w)

def topologicalSort(v) :
    if color[v] == 2: return True
    if color[v] == 1: return False
    color[v] = 1
    for w in adj[v]:
        if not topologicalSort(w): return False
    color[v] = 2
    topSort.append(v)
    return True

def run():
    cyclic = False
        for v in range(n):
            if not topologicalSort(v):
                cyclic = True
    if not cyclic:
        topSort.reverse()

for v in topSort:
    print(v + 1, end=' ')
else:
    print('Cyclic')