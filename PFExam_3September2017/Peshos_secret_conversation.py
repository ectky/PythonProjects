line1 = input()
line2 = input()
penkas_key = []
peshos_key = []
original_message_pesho = []
encr_message_penka = []
alphabet = []
alphabet2 = []
for i in range(26):
    alphabet2.append(chr(i + 97))
for i in range(26):
    alphabet2.append(chr(i + 65))


for i in range(26):
    alphabet.append(chr(i + 65))
for i in range(26):
    alphabet.append(chr(i + 97))

for i in range(52):
    peshos_key.append(line2[i])
    penkas_key.append(line1[i])

for j in range(52, len(line2)):
    if line2[j] in alphabet:
        original_message_pesho.append(line2[j])

for j in range(52, len(line1), 2):
    number = line1[j] + line1[j+1]
    index = alphabet[int(number)]
    index = penkas_key.index(index)
    print(alphabet2[index], end='')
print()

print(''.join(peshos_key),end='')
for l in original_message_pesho:
    index = alphabet2.index(l)
    index = peshos_key[index]
    if alphabet.index(index) < 10:
        print('0{0}'.format(alphabet.index(index)), end='')
    else:
        print(alphabet.index(index), end='')
print()

