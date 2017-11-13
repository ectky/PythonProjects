def findPolindrome(string):
    checker = False
    for i in range((len(string) - 1) // 2):
        if string[i] == string[len(string) - 1 - i]:
            checker = True
        else:
            checker = False

    if checker:
        return string

text = [i for i in input().strip(' ', ',', '.', '?', '!')]
polindromes = []

for word in text:
    polindromes.append(findPolindrome(word))

print(polindromes)
