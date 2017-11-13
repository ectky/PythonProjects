def multiply(n):
    return even_sum(n) * odd_sum(n)


def even_sum(n):
    sum = 0
    while n != 0:
        sum += n % 10 if (n % 10) % 2 == 0 else 0
        n //= 10
    return sum


def odd_sum(n):
    sum = 0
    while n != 0:
        sum += n % 10 if (n % 10) % 2 != 0 else 0
        n //= 10
    return sum

num = abs(int(input()))
print(multiply(num))
