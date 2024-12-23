import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self, q_text: QuizBrain):
        self.quiz = q_text


        self.window = tkinter.Tk()
        self.window.title("Quiz-Brains")
        self.window.config(padx=10, pady=10, bg=THEME_COLOR)
        self.window.minsize(width=400, height=600)

        self.score = tkinter.Label(text="Score: 0",fg="white",background=THEME_COLOR)
        self.score.grid(row=0,column=1)

        self.canvas =tkinter.Canvas(width=380, height=500)
        self.canvas.grid(row=1, column=0, columnspan=2,padx=10,pady=10)
        self.text = self.canvas.create_text(200,250,text="is it true that the capital city of nepal is kathmandu?",font=("Ariel",20,"bold"),width=300)
        
        self.img1 = tkinter.PhotoImage(file= "images/true.png")
        self.right = tkinter.Button(image=self.img1, borderwidth=0, highlightthickness=0,command=self.is_right)
        self.right.grid(row=2, column=0)
        
        img2 = tkinter.PhotoImage(file="images/false.png")
        self.wrong = tkinter.Button(image=img2, borderwidth=0, highlightthickness=0)
        self.wrong.grid(row=2, column=1)

        self.next_que_display()

        self.window.mainloop()
    
    def next_que_display(self):
        q_question = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text= q_question)

    def is_right(self):
        check =self.quiz.check_answer("true")
        if check:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

    def is_wrong(self):
        self.quiz.check_answer("false")
