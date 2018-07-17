max1 = int(input())
max2 = int(input())
if max2 > max1:
    max1, max2 = max2, max1
max3 = int(input())
if max3 > max1:
    max1, max3 = max3, max1
elif max3 > max2:
    max3, max2 = max2, max3
temp = max1
while temp != 0:
    temp = int(input())
    if temp > max1:
        max3 = max2
        max2 = max1
        max1 = temp
    elif temp > max2:
        max3 = max2
        max2 = temp
    elif temp > max3:
        max3 = temp

print(max1, max2, max3, sep = ' ')