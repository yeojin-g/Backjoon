def kmp(a):
    n = len(a)
    kmp_l = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and a[i] != a[j]:
            j = kmp_l[j - 1]
        if a[i] == a[j]:
            j += 1
            kmp_l[i] = j
    return kmp_l


l = int(input())
n = input().rstrip()

print(l - kmp(n)[-1])