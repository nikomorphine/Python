string, column = (int(s) for s in input().split())

temp = [int(s) for s in input().split()]
start = temp[0] * column + temp[1]

temp = [int(s) for s in input().split()]
fin = temp[0] * column + temp[1]

arr = []
for i in range(string):
	temp = [s for s in input()]
	arr += temp

adj_list = [[] for i in range(string * column)]

for i in range(string * column):
	if i % column > 0 and arr[i - 1] == ' ' and arr[i] != 'X':
		adj_list[i].append(i - 1)
	if (i + 1) % column != 0:
	    if arr[i + 1] == ' ' and arr[i] != 'X':
		    adj_list[i].append(i + 1)
	if i > column - 1 and arr[i - column] == ' ' and arr[i] != 'X':
		adj_list[i].append(i - column)
	if i  < column * (string - 1):
	    if arr[i + column] == ' ' and arr[i] != 'X':
		    adj_list[i].append(i + column)

distance = [None] * string * column
distance[start] = 0
queue = [start]
i = 0
while i < len(queue):
    y = queue[i]
    i += 1 
    for x in adj_list[y]: 
        if distance[x] is None: 
            distance[x] = distance[y] + 1 
            queue.append(x)
        if x == fin:
            i = len(queue)

if distance[fin] != None:
	print(distance[fin])
else:
	print('INF')