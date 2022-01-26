import random

target_num = 0

n = random.randint(0, 9)

while target_num != n:
    n = int(input("Guess a number between 0 and 9 until you get right:"))

print("Well Guessed..!")
