# Part 2 Loops
# In this exercise you will create a number guess game. It will prompt the user to guess the
# magic number between 1 and 10. If the user guesses correctly, it will print a winner
# message and exit. If the user guesses incorrectly, he/she will be prompted again. The user
# will be given three go's after which, if he/she has not guessed correctly the script will
# print a loser message.
# 1. Create a script named loops_exercise.py.
# 2. Import the random module as follows:
# import random
# 3. Declare and assign a variable that produces a random number in the range 1-10, as follows:
# magic_number = random.randint(1, 10)
# 4. Code a loop that iterates three times.
# 5. Inside the loop…
# a. Prompt the user to input a guess and capture it in a variable named
# user_guess.
# b. If the user's guess equals the magic number, print a winner message to the
# console and break out of the loop.
# c. If the user's guess does not equal the magic number, print an appropriate
# message, e.g. too low or too high.
# 6. If the loop exits normally, the user has not guessed correctly so print a suitable
# consolation message to the console.

# EXTENSION (time permitting)
# Taking the code from your number guess game, wrap the WHOLE CODE in a while loop 
# that will give the user any number of games before they type a special symbol or word to quit.

# EXTENSION 2 (time permitting)
# giv ethe user the option of difficulty level:
# level 1 is 3 goes in range 1-10
# level 2 is 5 goes in range 1-20
# level 3 is 10 goes in range 1-100

import random
# 1
# magic_number = random.randint(1,10)
# print(magic_number)#test for win case
# num_guess = 0
# while num_guess < 3:
#     num_guess += 1#important!
#     user_guess = input("guess the number 1-10")
#     user_guess = int(user_guess)
#     if user_guess == magic_number:
#         print(f"{user_guess} You guessed it!")
#         break 
#     elif user_guess > magic_number:
#         print("too high")
#     elif user_guess < magic_number:
#         print("too low")
# else:
#     print("no more guesses left")

# 2
# more_games = True
# while more_games:
#     magic_number = random.randint(1,10)
#     print(magic_number)#test for win case
#     num_guess = 0
#     while num_guess < 3:
#         num_guess += 1#important!
#         user_guess = input("guess the number 1-10")
#         user_guess = int(user_guess)
#         if user_guess == magic_number:
#             print(f"{user_guess} You guessed it!")
#             break 
#         elif user_guess > magic_number:
#             print("too high")
#         elif user_guess < magic_number:
#             print("too low")
#     else:
#         print("no more guesses left")
#     more_games = input("play again? Y for yes, N for no")
#     if more_games.upper() == "N":
#         more_games = False

# 3
more_levels = True

while more_levels:
    max_guesses = 0
    max_range = 0
    level = input("choose difficulty level 1 (easiest), 2, 3 (hardest)")
    if level =="3":
        max_guesses = 10
        max_range = 100
    elif level =="2":
        max_guesses = 5
        max_range = 20
    else: # will act as default level if no match
        max_guesses = 3
        max_range = 10

    # move into outer while loop
    more_games = True
    while more_games:
        magic_number = random.randint(1, max_range)
        print(magic_number)#test for win case
        num_guess = 0
        while num_guess < max_guesses:
            num_guess += 1#important!
            user_guess = input(f"guess the number 1-{max_range}")##
            user_guess = int(user_guess)
            if user_guess == magic_number:
                print(f"{user_guess} You guessed it!")
                break 
            elif user_guess > magic_number:
                print("too high")
            elif user_guess < magic_number:
                print("too low")
        else:
            print("no more guesses left")
        more_games = input("play again? Y for yes, N for no")
        if more_games.upper() == "N":
            more_games = False
    more_levels = input("play another level? Y for yes, N for no")
    if more_levels.upper() == "N":
        more_levels = False