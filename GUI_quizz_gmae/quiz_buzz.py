class Quiz_Buzz():
    def __init__(self,Q_LIST):
        self.QUES_ANS = Q_LIST
        self.QUES_ANS_LEN = len(self.QUES_ANS)-1
        self.ATTEMPTED_QUES = 0
        self.Q_AND_A = ''


    def Next_Question(self):
        self.Q_AND_A = self.QUES_ANS[self.ATTEMPTED_QUES]
        QUESTION = self.Q_AND_A[0]
        self.ATTEMPTED_QUES += 1
        QUES = f"Q-{self.ATTEMPTED_QUES}.  {QUESTION}"
        return QUES


    def Check_Answer(self):
        ANSWER = self.Q_AND_A[1]
        return ANSWER


    def IS_STILL_QUESTION(self):
        return self.ATTEMPTED_QUES <= self.QUES_ANS_LEN