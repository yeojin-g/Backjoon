def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def set_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def kmp(text, pattern, table):
    count = 0
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                count += 1
                j = table[j]
            else:
                j += 1
    return count

def main():
    n = int(input())
    ptr = input().replace(" ", "")
    tmp = input().replace(" ", "")
    text = "".join([tmp[i % n] for i in range(2 * n - 1)])

    table = set_table(ptr)

    result = kmp(text, ptr, table)

    divisor = gcd(n, result)
    print(f"1/{n // result}")

if __name__ == "__main__":
    main()
