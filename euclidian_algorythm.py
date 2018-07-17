def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)
    
print(gcd(9, 3))
a = 9

while a!= 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)