import copy
import random

class Animal:
    def __init__(self, spicies, number_of_legs, color):
        self.spicies = spicies
        self.number_of_legs = number_of_legs
        self.color = color
'''
harry = Animal("hippo", 6, "pink")
harriet = copy.copy(harry)
num = random.randint(1, 100)

while True:
    print("guess a number between 1 and 100")
    guess = input()
    i = int(guess)
    if i == num:
        print("you guessed right!")
        break
    elif i < num:
        print("try higher")
    elif i > num:
        print("try lower")
'''

desserts = ["ice cream", 'pancakes', 'brownies', 'cookies', 'steaks', 'suchi']

#print(random.choice(desserts))
print(desserts)
random.shuffle(desserts)

print(desserts)












