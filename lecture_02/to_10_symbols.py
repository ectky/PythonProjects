user_input=input("Please enter a sentence: ")
if len(user_input)>=10:
    to_tenth_symbol = user_input[:10]
    print(to_tenth_symbol+"...")
else:
    print(user_input)
