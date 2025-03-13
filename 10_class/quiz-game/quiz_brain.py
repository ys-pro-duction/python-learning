from question_model import Question


class QuizeBrain:
    def __init__(self, q_list: list[Question]):
        self.questions = q_list
        self.number = 0
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.questions)

    def check_answer(self, u_answer: str, question: Question):
        if u_answer.lower() == question.answer.lower():
            print("You got right!")
            self.score += 1
        else:
            print("Wrong answer.")
        print(f"Your current score is ({self.score}/{self.number + 1})")

    def finish_report(self):
        print("You have completed the quiz"
              f"\nYour final score was: {self.score}/{self.number}")

    def next_question(self):
        current_question = self.questions[self.number]
        u_answer = input(f"Q {self.number + 1}. {current_question.text} (True/False): ")
        self.check_answer(u_answer, current_question)
        self.number += 1
        print("\n")
