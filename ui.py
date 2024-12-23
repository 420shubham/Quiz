import tkinter

THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self):

        self.window = tkinter.Tk()
        self.window.title("Quiz-Brains")
        self.window.config(padx=10, pady=10, bg=THEME_COLOR)
        self.window.minsize(width=400, height=600)

        self.score = tkinter.Label(text="Score: 0",fg="white",background=THEME_COLOR)
        self.score.grid(row=0,column=1)

        self.canvas =tkinter.Canvas(width=380, height=500)
        self.canvas.grid(row=1, column=0, columnspan=2,padx=10,pady=10)
        self.canvas.create_text(200,250,text="is it true that the capital city of nepal is kathmandu?",font=("Ariel",20,"bold"),width=300)
        
        self.img1 = tkinter.PhotoImage(file= "D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-34/images/false.png")
        self.right = tkinter.Button(image=self.img1, borderwidth=0, highlightthickness=0)
        self.right.grid(row=2, column=0)
        
        img2 = tkinter.PhotoImage(file="images/true.png")
        self.wrong = tkinter.Button(image=img2, borderwidth=0, highlightthickness=0)
        self.wrong.grid(row=2, column=1)


        self.window.mainloop()

