name = input("Please enter your name: ")

index = name.index(" ")
new_name = name[index+1:]


if new_name.find(" ") != -1:
    final_index = new_name.index(" ")
    final_name = new_name[final_index+1:]
    print("{name1}. {name2}. {name3}.".format(name1=name[0], name2=new_name[0], name3=final_name[0]))
else:
    print("{name1}. {name}.".format(name1=name[0], name=new_name[0]))








