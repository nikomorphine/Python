def factorize_number(x):
    if x == 0:
        print('все числа являются делителем')
    elif x == 1:
        print(1)
    else:
        devisor = 2
        while x > 1:
            if x % devisor == 0:
                print(devisor)
                x //= devisor
            else:
                devisor += 1
            
n = int(input())
factorize_number(n)