
# Number Guessing Game


<img align= "right" height="240" src="https://i.giphy.com/media/UDU4oUJIHDJgQ/giphy.webp">
Objective:

- To create a number guessing game.

- The game will ask the user to guess a number between 1 and 100.

- The game will tell the user if the guess is too high or too low.

- The game will tell the user if the guess is correct.

- Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

- If they run out of turns, provide feedback to the player to play again.

- If they got the answer correct, show the actual answer to the player.



# `Logo`

```
/ _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  

```


# `Create a function that will generate a random number between 1 and 100.`
```python
def random_number():
    """generates a random number between 1 and 100"""
    return randint(1,100)

```
# `Create a function that check the guess and the random number and return turns left`
```python
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

```
<br>
<br>




# `Create a function that will check the number of turns remaining.`

<img align="left" src="https://i.giphy.com/media/PXfGn5XiPyhFXKajLa/giphy.webp" height=240>

```python
def turns_remaining(turns):
    """returns the number of turns remaining"""
    if turns == 0:
        return "You ran out of turns."
    else:
        return "You have {} turns remaining.".format(turns)
```
<br>
<br>
<br>
<br>

# `Create a function that will check the difficulty level.`

<img align="right" src="https://i.giphy.com/media/2J3VPYmnhO2jjKAX0X/giphy.webp" height=340>

```python
def difficulty():
    """returns the number of turns based on difficulty"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5
    
```
<br>
<br>
<br>
<br>
<br>
<br>

# `create a function that will run single instance of the game`.

<img align="right" src="https://media2.giphy.com/media/OmxPCq8ATFXig/giphy.gif?cid=ecf05e47xg5yymdn8j0b5nvec8fw28oyn714es34npq10oh2&rid=giphy.gif&ct=s" height=240>

```python
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
```


<br>
<br>
<br>
<br>

# `Create a function that will run the game`.

<img align="left" src="https://media0.giphy.com/media/1hMbkOaFfYmZvvEBq9/giphy.gif?cid=ecf05e4721d5x13ddc51ssm6l0d7j3bxxiy5yeyszz766rms&rid=giphy.gif&ct=ts" height=454>

<br>

```python
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
```




# `Run the game`.
```python
game_loop()
```
<img src="https://i.giphy.com/media/Dh5q0sShxgp13DwrvG/giphy.webp">