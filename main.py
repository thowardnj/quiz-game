from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

quizb = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    quizb.append(new_question)


quiz = QuizBrain(quizb)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number} ")