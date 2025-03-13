import json

from data import question_data
from question_model import Question
from quiz_brain import QuizeBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

qb = QuizeBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()
qb.finish_report()
