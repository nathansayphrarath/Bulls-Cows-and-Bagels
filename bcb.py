"""
Project: Bulls and Cows.py
Author : Nathan Sayphrarath <nsayphrarath2709522@woonsocketschools.com>
Author : Nolan Pierce < npierce2709337@woonsocketschools.com>

Date written : 10/18/24


Description : This is a Bulls and Cows game where we replaced Bulls and Cows with Burritos and Tacos

"""

import random

# Generates a random three digit number
digits = random.sample("0123456789", 3)
secret_number = digits[0] + digits[1] + digits[2]


playerName = input("Please enter your name: ") 
# Variables
game = True
Tries = 10
Burritos = 0
Tacos = 0
while game:
    
    
    player_guess = input("Please guess the three digit number : ")


    if player_guess == secret_number:
        print("CONGRATULATIONS!! You guessed the code")
        game = False


    else:
        Burritos = 0
        Tacos = 0

    # the logic to determine the score 
        if player_guess[0] == secret_number[0]:
            Burritos += 1
        if player_guess[1] == secret_number[1]:
            Burritos += 1
        if player_guess[2] == secret_number[2]:
            Burritos += 1
        if player_guess[0] == secret_number[1]:
            Tacos += 1
        if player_guess[0] == secret_number[2]:
            Tacos += 1
        if player_guess[1] == secret_number[0]:
            Tacos += 1
        if player_guess[1] == secret_number[2]:
            Tacos += 1
        if player_guess[2] == secret_number[1]:
            Tacos += 1
        if player_guess[2] == secret_number[0]:
            Tacos += 1

        print(f"You have {Burritos} burritos")
        print(f"You have {Tacos} tacos")

    Tries -= 1

    if Tries < 1:
        print("You have no more tries remaining. ")
        game = False 
