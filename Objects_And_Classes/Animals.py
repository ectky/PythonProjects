class Dog:
    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        print('I’m a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.')


class Cat:
    def __init__(self, name, age, intelligence_quotient):
        self.name = name
        self.age = age
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        print('I’m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.')


class Snake:
    def __init__(self, name, age, cruelty_coefficient):
        self.name = name
        self.age = age
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        print('I’m a Sophistisnake, and I will now produce a sophisticated sound! Honey, I’m home.')


def read_input(string):
    string = string.split(' ')
    if len(string) == 2:
        return read_command(string)
    else:
        return read_animal(string)


def read_command(string):
    return string[1], 'talk'

dogs = {}
l_dogs = []
cats = {}
l_cats = []
snakes = {}
l_snakes = []

def read_animal(string):
    if string[0] == 'Dog':
        dog = Dog(string[1], string[2], string[3])
        dogs[string[1]] = dog
        l_dogs.append(string[1])
        return dog, 'a'
    elif string[0] == 'Cat':
        cat = Cat(string[1], string[2], string[3])
        cats[string[1]] = cat
        l_cats.append(string[1])
        return cat, 'a'
    elif string[0] == 'Snake':
        snake = Snake(string[1], string[2], string[3])
        snakes[string[1]] = snake
        l_snakes.append(string[1])
        return snake, 'a'

def find_sound(string):
    if string in dogs:
        dogs[string].produce_sound()
    elif string in cats:
        cats[string].produce_sound()
    elif string in snakes:
        snakes[string].produce_sound()


string = input()
while string != 'I’m your Huckleberry':
    animal, command = read_input(string)
    if command == 'talk':
        find_sound(animal)
    string = input()


for dog in l_dogs:
    print('Dog: {}, Age: {}, Number Of Legs: {}'.format(dog, dogs[dog].age, dogs[dog].number_of_legs))

for cat in l_cats:
    print('Cat: {}, Age: {}, Number Of Legs: {}'.format(cat, cats[cat].age, cats[cat].intelligence_quotient))

for snake in l_snakes:
    print('Snake: {}, Age: {}, Number Of Legs: {}'.format(snake, snakes[snake].age, snakes[snake].cruelty_coefficient))

