def prime_test(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
if prime_test(n):
    print('ptime')
else:
    print('not prime')