class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].question}"
                       f" (True/False)?: ").lower()
        self.question_number += 1
        self.check_answer(answer.lower(), self.question_list[self.question_number].answer.lower())



    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            print("You are right!")
            self.score += 1
        else:
            print("You are wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def still_has_questions(self):
        return len(self.question_list) != self.question_number