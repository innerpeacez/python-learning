score = int(input('你的成绩是多少分'))

if score >= 90:
    print('A')
elif 90 > score >= 75:
    print('B')
elif 75 > score > 60:
    print('C')
else:
    print('D')
