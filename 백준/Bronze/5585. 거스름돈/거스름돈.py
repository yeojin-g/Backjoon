money_list = [500, 100, 50, 10, 5, 1]

i = 1000 - int(input())
m_idx = 0
cnt = 0

while i != 0 and m_idx < len(money_list): 
    m = money_list[m_idx] 
    if m <= i:
        i = i - m
        cnt += 1
    else:
        m_idx += 1

print(cnt)