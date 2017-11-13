#print("CASH RECEIPT\n------------------------------\nCharged to____________________\nReceived by___________________\n------------------------------\n© SoftUni")

def print_header():
    print("------------------------------")

def print_middle(a):
    print("_" * a)

print("CASH RECEIPT")
print_header()
print("Charged to", end='')
print_middle(20)
print("Received by", end='')
print_middle(19)
print_header()
print("© SoftUni")
