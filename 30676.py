a = int(input())

"""if 620 <= a:
    print('Red')
elif 590 <= a:
    print('Orange')
elif 570 <= a:
    print('Yellow')
elif 495 <= a:
    print('Green')
elif 450 <= a:
    print('Blue')
elif 425 <= a:
    print('Indigo')
else: print('Violet')""" # 정석

l = [620, 590, 570, 495, 450, 425, 380]
color = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
idx = 0

while a < l[idx]: idx += 1 #while문 사용
print(color[idx])


