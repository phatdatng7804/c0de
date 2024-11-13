a, b, c, d = map(float,input().split())

if 0 <= a <= 10 and 0 <= b<= 10 and 0 <= c <= 10 and 0 <= d <= 10:
    point = (a  + b  + c * 2 + d * 3) / 7

    if point >= 8:
        print('GIOI')
    elif 6.5 <= point < 8:
        print('KHA')
    elif 5 <= point < 6.5:
        print('TRUNGBINH')
    else:
        print('YEU')