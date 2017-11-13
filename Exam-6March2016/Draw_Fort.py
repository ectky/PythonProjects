n = int(input())

chavka = n // 2
dolna = 2 * n - 2 *(2 + chavka)

print('/' + '^' * chavka + '\\' + '_' * dolna + '/' + '^' * chavka + '\\')

for i in range(n-3):
    print('|' + ' ' * (2 * n - 2) + '|')

if dolna != 0:
    print('|' + ' ' * (chavka + 1) + '_' * dolna + ' ' * (chavka + 1) + '|')
else:
    print('|' + ' ' * (2 * n - 2) + '|')

print('\\' + '_' * chavka + '/' + ' ' * dolna + '\\' + '_' * chavka + '/')



