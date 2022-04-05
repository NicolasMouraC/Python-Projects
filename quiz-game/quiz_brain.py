class QuizBrain:
    def __init__(self, question_list):
        self.question_number =  0
        self.question_list = question_list
        self.score = 0
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1} {current_question.text} (True/False)")
        self.question_number += 1
        if self.check_answer(answer, current_question.answer):
            print("correct")
            self.score += 1
        else:
            print("False")
        print(f"The correct answer was {current_question.answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
    def still_has_questions(self):
        if len(self.question_list) < (self.question_number + 1):
            print("You have completed the quiz")
            print(f"Your final score was: {self.score}/{self.question_number}")
            return False
        else:
            return True