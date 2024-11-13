a , b = map(int , input().split())

print(a + b)
print(a - b)
print(a * b)
if b == 0:
    print('INVALID')
else:
    print('%.4f' %( a / b))