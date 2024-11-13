from math import *
import math
"""""
n = int(input())
temp = n // 1000
print(temp)
"""""

"""""
a,b = map(int, input().split())

print(a % b)
"""
"""""
n = int(input())

print(n * 2)
print(n * 10)
print(n // 2)
print(f"{n/2:.3f}")
"""
"""""
x,y = map(int, input().split())

F = 5 * x + 2 * y + x * y

print(F)
"""
"""""
x,y,z,t = map(int,input().split())

print(max(x,y))
print(min(z,t))
print(max(x,y,z))
print(min(x,y,z,t))
"""
"""
x,y = map(int, input().split())

temp = y - x  + 1

print(temp)
"""
"""
N, X = map(int,input().split())

temp = N // X 

print('SO VO MUA DUOC LA : ' ,temp,end = ' !!!!!')
"""
"""
x,y,z,t = map(int,input().split())

print(x,y,z,t,sep='  ')
print(y,z,x,t, sep = '--')
print(2* x,3 * y,4 * z,5 * t, sep= ',')
print('KET THUC !!')
"""
"""
length, width =  map(int,input().split())

chuvi = (length + width) * 2
dientinh = length * width
print('Chu vi HCN la : ',chuvi)
print('Dien tich HCN la : ',dientinh)
"""
"""
a, b = map(int,input().split())

a,b = b,a

print(128 * a + 97 * b + 1000)
"""
"""
n = float(input())

tmp = int(n)

temp = n - tmp
print(tmp)
print('%.2f' % temp)
"""
"""
N = int(input())

print('{:06d}'.format(N))
print('{:>6d}'.format(N).replace(' ','#' )) #replace() thay thế các khoảng thành kí tự mong muốn
"""
"""
#tính giá trị của biểu thức
x = int(input())

A = x**3 + 3*x**2 + x + 1

print(A)
"""
"""
a ,b,c = map(int,input().split())

S = a *(b+c)+b*(a+c)
print(S)
"""
"""
C = int(input())

F = C * 9 /5 + 32
print('%.2f'% F)
"""
"""
pi = 3.14
R = int(input())

chuvi = 2*pi*R
dientich = pi*R**2
print('%.4f' %chuvi)
print('%.4f' %dientich)
"""
#Khoảng cách eculid 
"""
x1,y1,x2, y2 = map(int,input().split())


result = sqrt((x2 - x1)**2 +(y2 - y1)**2)

print('%.2f' % result)
"""
N = int(input())

if N % 2 == 0:
    print('YES')
else: 
 print('NO')
if N % 3 == 0 and N % 5 == 0:
    print('YES')
else:
    print("No")
if N % 3 == 0 and N % 7 != 0:
    print('YES')
else: 
    print('NO')
if N % 3 == 0 or N % 7 == 0:
    print('YES')
else: 
    print('NO')
if N < 30 and N > 50:
    print('YES')
else:
    print('NO')
if N >= 30 and (N % 2 == 0 or N % 3 == 0 or N % 5 == 0):
    print('YES')
else:
    print('NO')
r = N % 10
if N >= 10 and N <= 99 and (r == 2 or r == 3 or r == 5 or r == 7):
    print('YES')
else:
    print('NO')
if N <= 100 and N % 23 == 0:
    print('YES')
else:
    print('NO')
if N < 10 or N > 20:
    print('YES')
else:
    print('NO') 
if r % 3 == 0:
    print('YES')
else:
    print('NO')
