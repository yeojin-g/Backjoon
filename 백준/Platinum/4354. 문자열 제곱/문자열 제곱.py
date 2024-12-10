while True:
    s = input().strip()
    if s == ".":
        break
    pi = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j

    n = len(s)
    pr = n - pi[-1]
    if n % pr == 0:
        print(n // pr)
    else:
        print(1)
