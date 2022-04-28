from questions import question_data
from quiz import Quiz
from art import logo
print(question_data)

# create a games with Quiz
# create a quiz with questions

while True:
    print(logo)
    print("Welcome to the quiz game!")
    print("Please enter your name: ")
    name = input()
    print("Hello " + name + "!")
    # print("How many questions would you like to answer?")
    # number_of_questions = int(input())
    quiz = Quiz()
    quiz.play(question_data)


    print("Would you like to play again? (y/n)")
    play_again = input()
    if play_again == "n":
        print("Thank you for playing!")
        break