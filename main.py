from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data['text'], data['answer']))
print(question_bank)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("Congratulations! you have completed the quiz")
print(f"Your final score: {quiz_brain.score}/{quiz_brain.question_number}")