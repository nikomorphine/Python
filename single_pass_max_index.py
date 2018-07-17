max1 = int(input())
temp = max1
index = 0
max_index = 0
while temp != 0:
    index += 1
    temp = int(input())
    if temp > max1:
        max1 = temp
        max_index = index

print(max_index)