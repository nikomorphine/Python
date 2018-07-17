n = int(input())
mult = 1
summ = 0
count = 0
while n != 0:
    count += 1
    summ += n
    mult *= n
    n = int(input())

print(count, summ, mult)