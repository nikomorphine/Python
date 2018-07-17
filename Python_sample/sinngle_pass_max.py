max1 = int(input())
temp = max1
counter = 0
while temp != 0:
    if temp == max1:
        counter += 1
    elif temp > max1:
        max1 = temp
        counter = 1
    temp = int(input())

print(max1, counter, sep = ' ')