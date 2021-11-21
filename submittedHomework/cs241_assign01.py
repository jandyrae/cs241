import random
from random import randint
#print()
print("Welcome to the number guessing game!")
seed=input("Enter random seed: ")
random.seed(seed)

#print("Please enter a guess: " \n)

play_again = "yes"
while play_again =="yes":
    #Save a random number from 1 to 100 in a variable
    number = random.randint(1,100)
    print()
    #Prompt the user for a guess
    guess = int(input("Please enter a guess: "))
    total_guesses = 1
    #If they guess too high, tell them to guess lower
    while guess != number:
        if guess > number:
            print ("Lower\n")
        #If they guess too low, tell them to guess higher
        elif guess < number:
            print ("Higher\n")
        #If the guess right, tell them how many guesses it took
        guess = int(input("Please enter a guess: "))
        total_guesses = total_guesses + 1
    print ("Congratulations. You guessed it!")
    print("It took you " + str(total_guesses) + " guesses.")
    print()
    play_again = input("Would you like to play again (yes/no)? ")
print("Thank you. Goodbye.")

