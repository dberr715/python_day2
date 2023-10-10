import random


user_input = int(input("Guess a number 1- 10: "))

magic_number = random.randint(1, 10)

if user_input == magic_number:
    print("ARE YOU A MIND READER???")
elif user_input > 10 or user_input < 1:
    print("Read the directions!!!! Out of range")
else:
    print("Not the right number. Try again!")
