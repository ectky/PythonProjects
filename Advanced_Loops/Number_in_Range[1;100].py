n = int(input("Еnter a number in the range [1...100]: "))

while 1 > n or n > 100:
    print("Invalid number!")
    n = int(input("Еnter a number in the range [1...100]: "))

print("The number is: {0}".format(n))

