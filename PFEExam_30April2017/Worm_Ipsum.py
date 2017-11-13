sentence = input()
count = 0
index = 0
i = 0


while sentence != 'Worm Ipsum':
    dot_index = sentence.find('.')
    if sentence.find('.', dot_index + 1) != -1:
        sentence = input()
        continue

    sentence = sentence.replace('.', '')
    list_of_words = sentence.split(' ')

    output = []
    for word in list_of_words:
        dict = {}
        for char in word:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        max_char = list(dict.keys())[0]
        for c in dict.keys():
            if dict[c] > dict[max_char]:
                max_char = c
        if dict[max_char] >= 2:
            output.append(max_char * len(word))
        else:
            output.append(word)
    print('{}.'.format(' '.join(output)))
    sentence = input()
