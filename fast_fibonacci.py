phi = (1 + 5 ** (1/2))/2


def power(x1, x2):
    if x2 == 1:
        return x1
    elif x2 % 2 == 0:
        return power(x1 * x1, x2 // 2)
    elif x2 % 2 == 1:
        return x1 * power(x1 * x1, x2 // 2)

def fibonacci(n):
    if n == 0:
        return 0
    else:
        return (round((power(phi, n)+power((1 - phi), n))/(5 ** (1/2))))

print(fibonacci(int(input())))

