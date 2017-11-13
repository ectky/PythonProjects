n = int(input())

wardrobe = {}
unique = []
unique_clothe = []

for item in range(n):
    line = input().split(' -> ')
    colour = line[0]
    clothes = line[1].split(',')
    if colour in wardrobe:
        for i in clothes:
            if i in wardrobe[colour]:
                wardrobe[colour][i] += 1
            else:
                wardrobe[colour][i] = 1
    else:
        quantity = 1
        wardrobe[colour] = {clothes[0]: quantity}
        for clothe in clothes[1:]:
            wardrobe[colour].update({clothe: quantity})
        unique.append(colour)

searched = input().split(' ')

for x in unique:
    print('{} clothes:'.format(x))
    if searched[0] == x:
        for cl in wardrobe[x]:
            if cl == searched[1]:
                print('* {} - {} (found)!'.format(cl, wardrobe[x][cl]))
            else:
                print('* {} - {}'.format(cl, wardrobe[x][cl]))
    else:
        for cl in wardrobe[x]:
            print('* {} - {}'.format(cl, wardrobe[x][cl]))
