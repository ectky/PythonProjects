class Plokijuh:
    def __init__(self, name):
        self.name = name
        self.price = 0.0
        self.components = []

request = input()
bozatronic = ['SAHRA', 'BINGIL', 'AMZGA']
plokijuhs = []

while request != 'STOPAAJUHIT!':
    request = request.split(' ')
    if request[0] == 'NEW':
        name = request[1]
        if name in [x.name for x in plokijuhs]:
            print('STUPIDO!!1')
        else:
            plokijuhs.append(Plokijuh(name))
    elif request[0] == 'GEPRISEN':
        name = request[1]
        price = float(request[2])
        for plokijuh in plokijuhs:
            if name == plokijuh.name:
                plokijuh.price = price
                break
    elif request[0] == 'KOMPONENTUNG':
        name = request[1]
        component = request[2]
        if component not in bozatronic:
            print('BLAH!')
        else:
            for plokijuh in plokijuhs:
                if name == plokijuh.name:
                    plokijuh.components.append(component)
                    break
    elif request[0] == 'DECOMPING':
        name = request[1]
        component = request[2]
        if component not in bozatronic:
            print('YACK!')
        else:
            for plokijuh in plokijuhs:
                if name == plokijuh.name:
                    if component not in plokijuh.components:
                        print('YACK!')
                    else:
                        plokijuh.components.remove(component)
                    break
    elif request[0] == 'BLUSS':
        name1 = request[1]
        name2 = request[2]
        name = name1[:len(name1) // 2] + name2[len(name2) // 2:]

        for plokijuh in plokijuhs:
            if name2 == plokijuh.name:
                plokijuh2 = plokijuh
                break

        for plokijuh in plokijuhs:
            if name1 == plokijuh.name:
                plokijuh.name = name
                plokijuh.price = (plokijuh.price + plokijuh2.price) / 2
                for component in plokijuh2.components:
                    plokijuh.components.append(component)
                break

        plokijuhs.remove(plokijuh2)
    else:
        if plokijuhs:
            plokijuhs = sorted(plokijuhs, key=lambda x: (x.price, -len(x.components)))

            for plokijuh in plokijuhs:
                print('$$# PLOKIJUH: {0}'.format(plokijuh.name))
                print('$#$ Price: {0:.1f}'.format(plokijuh.price))
                if plokijuh.components:
                    print('#$$ Components: {0}'.format(', '.join(plokijuh.components)))
                else:
                    print('#$$ Components:')
        else:
            print('INTEPLOKIJUHAR:(')
    request = input()
