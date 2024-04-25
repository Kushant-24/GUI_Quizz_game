from tkinter import *
from quiz_buzz import Quiz_Buzz
COLOR_THEME = "#375362"

class QuizInterface:
    def __init__(self,quiz_buzz: Quiz_Buzz):
        self.quiz = quiz_buzz
        self.score = 0
        self.answer = ''
        self.window = Tk()
        self.window.title("Quizzler")
        self.game_over = self.quiz.IS_STILL_QUESTION()
        self.timer = ''
        self.window.config(padx=20,pady=20,bg=COLOR_THEME)

        self.Score_Label = Label(text=f"Score:{self.score}",font=("arial",15,"italic"),
                                 bg=COLOR_THEME,
                                 fg="white")
        self.Score_Label.grid(row=0,column=1)


        self.canvas = Canvas(
                             self.window,
                             width=400,
                             height=350,
                             highlightthickness=0,
                             bg="white"
                             )
        
        self.Question_Text = self.canvas.create_text(
            200,
            175,
            text="Question",
            font=("arial",20,"italic"),
            fill=COLOR_THEME,
            width=350
            )
        

        FalseImage = PhotoImage(file="C:\\HardCore_Projects(py) - 3\\GUI_quizz_gmae\\Images\\wrong.png")
        TrueImage = PhotoImage(file="C:\\HardCore_Projects(py) - 3\\GUI_quizz_gmae\\Images\\right.png")

        self.canvas.grid(row=1,column=0,columnspan=2,pady=30)
        self.FalseButton = Button(image=FalseImage,
                                  highlightthickness=0,
                                  command=self.FalseAnswer
                                  )
        self.FalseButton.grid(row=2,column=0)


        self.TrueButton  = Button(image=TrueImage,
                                  highlightthickness=0,
                                  command=self.TrueAnswer
                                  )
        self.TrueButton.grid(row=2,column=1)        


        self.ChangeQuestion()
        self.window.mainloop()

    def CheckAnswer(self):
        print(self.quiz.Check_Answer(),self.answer)
        if self.quiz.Check_Answer() == self.answer:
            self.score += 1
            self.GiveFeedback(True)
        else:
            self.GiveFeedback(False)

        self.ScoreLabel()


    def GiveFeedback(self,is_right):
        if is_right == True:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.ChangeQuestion)


    def TrueAnswer(self):
        self.answer = 'True'
        self.CheckAnswer()
        

    def FalseAnswer(self):
        self.answer = 'False'
        self.CheckAnswer()


    def ScoreLabel(self):
        self.Score_Label.config(text=f"Score:{self.score}")

    def ChangeQuestion(self):
        if self.quiz.IS_STILL_QUESTION():
            self.canvas.config(bg="white")
            self.ScoreLabel()
            q_text = self.quiz.Next_Question()
            self.canvas.itemconfig(self.Question_Text,text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.Question_Text,text="You Have Reached to End of the Quiz.")
            self.TrueButton.config(command=self.WindowExit)
            self.FalseButton.config(command=self.WindowExit)

    def WindowExit(self):
        self.window.destroy()
