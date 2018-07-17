def top_sort(matrix):
    stack = []
    color = {}
    for i in matrix.keys():
        color[i] = 0
    def topological_sort():
        def dfs(v):
            if color[v] == 1: 
            	return True
            if color[v] == 2: 
            	return False
            color[v] = 1
            for i in range(len(matrix[v]) - 1):
                if dfs(matrix[v][i]): 
                	return True
            stack.append(v)
            color[v] = 2
            return False

        for i in matrix.keys():
            cycle = dfs(i)
            if cycle: 
                print('NO')
                exit()  
        stack.reverse()
        return stack
    return topological_sort()

n_vert, n_edges = (int(s) for s in input().split())
matrix = {}
for i in range(n_edges):
	temp = [int(s) for s in input().split()]
	if temp[0] not in matrix:
		matrix[temp[0]] = []
	matrix[temp].append[temp[1]]

stack1 = top_sort(matrix)