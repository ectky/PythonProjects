# n=int(input())
# a=1
# b=0
# while a <= n:
#     print("*", end="")
#     a += 1
# a = 1
# print()
# for i in range(n-2):
#     print("*", end="")
#     while b<n-2:
#         print(" ", end="")
#         b+=1
#     print("*", end="")
#     print()
#     b=0
# while a <= n:
#     print("*", end="")
#     a += 1
# a = 1
# print()

n = int(input())

print('*' * n)

for i in range(n-2):
    print('*' + ' ' * (n-2) + '*')

print('*' * n)


















