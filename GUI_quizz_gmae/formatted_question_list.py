import html

class Formatted():
    def __init__(self,QS_LIST):
        self.Q_LIST = QS_LIST
        self.PROPER_SET = []
    def Refine_Data(self):
        for NEXT_DICT in self.Q_LIST:
            QUESTION = html.unescape(NEXT_DICT["question"])
            ANSWER = html.unescape(NEXT_DICT['correct_answer'])
            self.PROPER_SET.append((QUESTION,ANSWER))
        # print(self.PROPER_SET)
        return self.PROPER_SET