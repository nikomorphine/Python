n_vert = int(input())
n_edges = int(input())

def bfs(graph, n, i):
	global ch
	ch[n] = i
	for x in graph[n]:
		if ch[x] == -1:
			bfs(graph, x, i)

def dfs(array, x): 
	visited[x] = True
	for y in array[x]: 
		if visited[y] is False: 
			dfs(array, y) 
	return 

if n_edges == 0 or n_vert == 0: 
	print(n_vert, n_vert) 
else: 
	visited = [False] * n_vert   
	adj_list = [[] for i in range(n_vert)]
	weak_list = [[] for i in range(n_vert)] 
	for i in range(n_edges):
		temp = [int(s) for s in input().split()] 
		adj_list[temp[0]].append(temp[1]) 
		weak_list[temp[0]].append(temp[1]) 
		weak_list[temp[1]].append(temp[0]) 

	ch = [-1] * n_vert
	i = 1
	while -1 in ch:
		for j in range(n_vert):
			if ch[j] == -1:
			    break
		bfs(weak_list, j, i)
		i += 1

	temp = [[] for i in range(n_vert)] 
	visited = [False] * n_vert 

	for i in range(n_vert): 
		dfs(adj_list, i) 
		temp[i] = visited
		visited = [False] * n_vert

	counter_strong = n_vert 
	visited_1 = [] 
	for i in range(n_vert): 
		if i not in visited_1: 
			for j in range(n_vert): 
				if j != i and temp[i][j] and temp[j][i]: 
					visited_1.append(j) 
					counter_strong -= 1 

	print(max(ch), counter_strong)