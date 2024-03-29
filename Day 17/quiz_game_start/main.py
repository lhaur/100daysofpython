from question_model import Question
from data import new_question_data
from quiz_brain import QuizBrain

question_bank = []
for question in new_question_data:
  text = question["question"].replace("&quot;", "'").replace("&#039;", "'")
  answer = question["correct_answer"]
  question = Question(text, answer)
  question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.has_questions():
  quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}.")