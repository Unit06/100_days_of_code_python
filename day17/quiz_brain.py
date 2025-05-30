class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.quiz_score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.quiz_score += 1
        else:
            print("That's wrong.")
            if self.quiz_score > 0:
                self.quiz_score -= 1
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.quiz_score}/{self.question_number}\n")