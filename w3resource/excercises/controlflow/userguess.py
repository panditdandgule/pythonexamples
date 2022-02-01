import random

target, guess = 0, random.randint(1, 10)

while target != guess:
    guess = int(input("Enter Your guess until 1 to 10:"))
print("Your guess is correct!")
