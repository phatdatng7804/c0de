n = int(input())

years = n // 365

dayCheck = n % 365

weeks = dayCheck // 7

days = dayCheck % 7

print(f'{years} {weeks} {days}')