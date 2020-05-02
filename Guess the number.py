#This is a number guessing game

import random

print("Hello random stranger! What is your name?")
name_input = input()
random_number = random.randint(1,10)
guesstaken = 1

print("Well, " + name_input + ". I am getting bored cooped up in the house. Let's play a game. I am thinking of a number between 1 and 10.")

for guesstaken in range (1,11):
    print("Take a guess")
    guess = int(input())
    if guess == random_number:
        print("Good job, " + name_input + ". You took " + str(guesstaken) + " guesses")
        break
    elif guess < random_number:
        print("Your guess is too low " + name_input)
    elif guess > random_number:
        print("Your guess is too high " + name_input)

print("Congratulations for completing the game. Hope you had fun. Stay tuned for more")