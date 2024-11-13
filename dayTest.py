month,year = map(int,input().split())
if 1 <= month <= 12 and year > 0:
    if month in {1,3,5,7,8,10,12}:
        print('31')
    elif month in{4,6,9,11}:
        print('30')
    elif month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print('29')
        else:
            print('28')    
else:
    print('INVALID')
