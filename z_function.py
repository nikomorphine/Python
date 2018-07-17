def z_func(s):
    z = [0] * len(s)
    r = -1
    for i in range(1, len(s)):
        if i > r:
            while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
                z[i] += 1
                r = i + z[i]
                l = i
        elif i <= r and s[z[i]] == s[1 + z[i]]:
            z[i] = min(r - i, z[i - l])
    print(z)
z_func([1,1,2,3,4,1,2,4,1,4,1,4,1])