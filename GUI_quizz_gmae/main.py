from data import questions
from formatted_question_list import Formatted
from quiz_buzz import Quiz_Buzz
from ui import QuizInterface



# Classes Declaration
UN_PROPER_FRMT = questions
CHANGE_FRMT = Formatted(UN_PROPER_FRMT)
PROPER_FRMT = CHANGE_FRMT.Refine_Data()
# print(PROPER_FRMT)
Quizz = Quiz_Buzz(PROPER_FRMT)
QUIZZ_UI = QuizInterface(Quizz)