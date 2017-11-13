class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


def read_account(string):
    string = [item for item in string.split(' | ')]
    return BankAccount(string[1], string[0], float(string[2]))
string = input()


def order_list(l):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(l)-1):
            if len(l[i].bank) > len(l[i+1].bank):
                helper = l[i]
                l[i]= l[i+1]
                l[i+1] = helper
                swapped = True
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(l)-1):
            if l[i].balance < l[i+1].balance:
                helper = l[i]
                l[i]= l[i+1]
                l[i+1] = helper
                swapped = True
    return l

list_of_accounts = []
while string != 'end':
    bank_account = read_account(string)
    list_of_accounts.append(bank_account)
    string = input()

list_of_accounts = order_list(list_of_accounts)

for account in list_of_accounts:
    print('{} -> {} ({})'.format(account.name, account.balance, account.bank))
