def power(unicorn, pony):
    if pony == 1:
        return unicorn
    elif pony % 2 == 0:
        return power(unicorn * unicorn, pony // 2)
    elif pony % 2 == 1:
        return unicorn * power(unicorn * unicorn, pony // 2)
    
unicorn = int(input())
pony = int(input())
print(power(unicorn, pony))
