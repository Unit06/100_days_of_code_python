from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    data_text = data["text"]
    data_answer = data["answer"]
    new_qusetion = Question(q_text=data_text, q_answer=data_answer)
    question_bank.append(new_qusetion)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You completed the quiz.")
print(f"Your final score was: {quiz.quiz_score}/{quiz.question_number}")