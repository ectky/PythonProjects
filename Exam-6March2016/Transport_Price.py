n = int(input())
day_night = input()

price = 0

if n < 20:
    if day_night == 'day':
        price = 0.7 + 0.79 * n
    else:
        price = 0.7 + 0.9 * n
elif 20 <= n < 100:
    price = 0.09 * n
elif n >= 100:
    price = 0.06 * n

print(price)
