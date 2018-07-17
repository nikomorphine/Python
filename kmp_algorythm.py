def kmp(sub, s):
    enter = []
    pi = pi_function(sub + '#' + s)
    for i in range(len(sub) + 1, len(sub) + len(s) + 1):
        if pi[i] == len(sub):
            enter.append(i - 2 * len(sub))
    return(enter)

def pi_function(s):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        p = pi[i - 1]
        while p > 0 and s[p] != s[i]:
            p = pi[p - 1]
        if s[i] == s[p]:
            p += 1
        pi[i] = p
    return pi

s = 'abccabcbcab'
sub = 'cab'
print(kmp(sub, s))