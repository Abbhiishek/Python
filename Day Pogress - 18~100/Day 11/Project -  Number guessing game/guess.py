


from random import randint

#Number Guessing Game Objectives:

# Include an ASCII art logo.

from art import logo
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


# Create a function that will generate a random number between 1 and 100.
def random_number():
    """generates a random number between 1 and 100"""
    return randint(1,100)




def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


# Create a function that will check the number of turns remaining.
def turns_remaining(turns):
    """returns the number of turns remaining"""
    if turns == 0:
        return "You ran out of turns."
    else:
        return "You have {} turns remaining.".format(turns)


# Create a function that will check the difficulty level.
def difficulty():
    """returns the number of turns based on difficulty"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5
    




# create a function that will run the game.
def game():
    """runs the single instance of the game """
    answer = random_number()
    turns = difficulty()
    print("Welcome to the Number Guessing Game!")
    print("You have {} turns to guess the number.".format(turns))
    guess=0
    while guess != answer and turns != 0:
        guess = int(input("Guess a number between 1 and 100: "))
        turns = check_answer(guess, answer, turns)
        print(turns_remaining(turns))
    print("Game over.")




# Create a function that will run the game.
def game_loop():
    """run the game in loop until user quits"""
    print(logo)
    while True:
        game()
        play_again = input("Would you like to play again? (y/n): ")
        if play_again == "y":
            continue
        else:
            print("Thanks for playing!")
            break






# Run the game.
game_loop()
