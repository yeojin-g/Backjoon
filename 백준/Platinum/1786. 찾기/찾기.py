t = input().rstrip()
p = input().rstrip()

lp, lt = len(p), len(t)

pi = [0] * lp
i = 0

for j in range(1, lp):
    while 0 < i and p[i] != p[j]:
        i = pi[i-1]
    if p[i] == p[j]:
        i += 1
        pi[j] = i

idx = []
i = 0
for j in range(lt):
    while 0 < i and p[i] != t[j]:
        i = pi[i-1]
    if p[i] == t[j]:
        i += 1
        if i == lp:
            idx.append(j-lp+2)
            i = pi[i-1]

print(len(idx))
print(*idx)