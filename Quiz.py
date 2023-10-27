class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def display_question(self):
        question = self.questions[self.current_question_index]
        print(question.text)
        for index, choice in enumerate(question.choices):
            print(f"{index + 1}. {choice}")

    def get_user_choice(self):
        choice = input("Enter your answer (number): ")
        return choice

    def check_user_answer(self, user_choice):
        question = self.questions[self.current_question_index]
        if question.check_answer(question.choices[int(user_choice) - 1]):
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")

    def display_score(self):
        print(f"Your score is {self.score}/{len(self.questions)}.")

    def start(self):
        print("Welcome to the Quiz!")
        for i in range(len(self.questions)):
            self.display_question()
            user_choice = self.get_user_choice()
            self.check_user_answer(user_choice)
            self.current_question_index += 1
            if self.current_question_index < len(self.questions):
                input("Press Enter to continue...")
        self.display_score()


# Create question objects
question1 = Question("What is the capital of France?", ["London", "Paris", "Madrid", "Rome"], "Paris")
question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "Mars")
question3 = Question("What is the largest ocean in the world?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean")

# Create quiz object
quiz = Quiz()

# Add questions to the quiz
quiz.add_question(question1)
quiz.add_question(question2)
quiz.add_question(question3)

# Start the quiz
quiz.start()

# Wait for user input before exiting
input("Press Enter to exit...")
