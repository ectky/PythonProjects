class Sale:
    def __init__(self, town, product, price, quantity):
        self.town = town
        self.product = product
        self.price = price
        self.quantity = quantity


def read_sale(inp):
    inp = [item for item in inp.split(' ')]
    town = inp[0]
    product = inp[1]
    price = float(inp[2])
    quantity = float(inp[3])
    return Sale(town, product, price, quantity)

n = int(input())
dictionary_for_sales = {}
for i in range(n):
    inp = input()
    sale = read_sale(inp)
    total_sale = float(sale.price) * float(sale.quantity)
    if sale.town in dictionary_for_sales:
        dictionary_for_sales[sale.town] += total_sale
    else:
        dictionary_for_sales[sale.town] = total_sale

list = []
sorted_list=sorted(dictionary_for_sales.items(), key=lambda x: x[0])
for key, sth in sorted(dictionary_for_sales.items(), key=lambda x: x[0]):
    list.append(key)

for town in list:
    print('{} -> {:.2f}'.format(town, dictionary_for_sales[town]))
