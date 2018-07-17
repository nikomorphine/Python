letters = 'abcdefgh'
numbers = '12345678'

graph = {l + n: set() for l in letters for n in numbers}

def add_edge(v1, v2):
	graph[v1].add(v2)
	graph[v2].add(v1)

for i in range(8):
	for j in range(8):
		v1 = letters[i] + numbers[j]
		v2 = ''
		if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
			v2 = letters[i + 2] + numbers[j + 1]
			add_edge(v1, v2)
		if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
			v2 = letters[i - 2] + numbers[j + 1]
			add_edge(v1, v2)
		if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
			v2 = letters[i - 1] + numbers[j + 2]
			add_edge(v1, v2)
		if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
			v2 = letters[i - 1] + numbers[j + 2]
			add_edge(v1, v2)
		if 0 <= i + 2 < 8 and 0 <= j - 1 < 8:
			v2 = letters[i + 2] + numbers[j - 1]
			add_edge(v1, v2)
		if 0 <= i - 2 < 8 and 0 <= j - 1 < 8:
			v2 = letters[i - 2] + numbers[j - 1]
			add_edge(v1, v2)
		if 0 <= i + 1 < 8 and 0 <= j - 2 < 8:
			v2 = letters[i - 1] + numbers[j - 2]
			add_edge(v1, v2)
		if 0 <= i - 1 < 8 and 0 <= j - 2 < 8:
			v2 = letters[i - 1] + numbers[j - 2]
			add_edge(v1, v2)

start = input()
end = input()

parents ={v: None for v in graph}
distances = {v: None for v in graph}

distances[start] = 0
queue = deque([start])

while i < len(queue):
    u = queue[i]
    i += 1 
	for v in graph[u]:
		if distances[v] is None:
			distances[v] = distances[u] + 1
			queue.append(v)
path = [end]
parent = parents[end]

while not parent is None:
	path.append(parent)
	parent = parents[parent]

print(path[::-1])