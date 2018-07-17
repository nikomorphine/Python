def gen_num(N, M, prefix = None):
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        gen_num(N, M - 1, prefix)
        prefix.pop()

gen_num(10, 3)    