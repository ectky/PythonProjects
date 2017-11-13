class PC:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = float(price)
        self.products = []

dict_of_prdoucts = {}
pcs = []
product = input()

while product != 'PC':
    product = product.split(' ')
    name, price = product[0], float(product[1])
    dict_of_prdoucts[name] = price
    product = input()

command = input()

while command != 'END':
    if 'ADDPC' in command:
        command = command.split(' ')
        name, model, price = command[1], command[2], command[3]
        pcs.append(PC(name, model, price))
    elif 'REMOVEPC' in command:
        command = command.split(' ')
        name = command[1]
        for element in pcs:
            if element.name == name:
                pcs.remove(element)
    elif 'ADDPRODUCT' in command:
        command = command.split(' ')
        name, product = command[1], command[2]
        for element in pcs:
            if element.name == name:
                element.products.append(product)
                element.price += dict_of_prdoucts[product]
    elif 'REMOVEPRODUCT' in command:
        command = command.split(' ')
        name, product = command[1], command[2]
        for element in pcs:
            if element.name == name:
                while product in element.products:
                    element.products.remove(product)
                    element.price -= dict_of_prdoucts[product]
    elif 'PRINT' in command:
        for element in pcs:
            print('PC: {0} {1} {2:.2f}'.format(element.name, element.model, element.price))
            if element.products:
                print('--- Products: {0}'.format(', '.join(element.products)))
            else:
                print('--- Products: None')
    command = input()
