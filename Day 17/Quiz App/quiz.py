class Quiz:
    def __init__(self):
        """
        this is a Quiz constructor
        """

    def ask_question(self, questions, score):

        # store a question item and one answer

        # ask from the list

        question = questions[score]["text"]
        answer = questions[score]["answer"]
        print("Question: " + question)
        guess = input("Your answer(True / False): ")
        return self.check_answer(guess, answer)


    def check_answer(self, guess, answer):
        return answer == guess

    def play(self, questions_data):
        score = 0
        while score < len(questions_data):
            if self.ask_question(questions_data, score):
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
                break

        if(score == len(questions_data)):
            print("Congratulations! 🎉 You have completed the quiz!")
        else:
            print("You have failed the quiz!")

        print("Your score is " + str(score))
