first_input = input('Enter first string: ')
second_input = input('Enter second string: ')

if first_input.find(second_input)==-1:
    print(first_input)
else:
    index = first_input.find(second_input)+len(second_input)
    print(first_input[index:])
