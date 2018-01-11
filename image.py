from tkinter import *

class SharedPower(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #Here starts the interesting part.
        logo = PhotoImage(file="res/tools_128.png")
        label = Label(self, image=logo)
        label.image = logo
        label.pack()
        #And here it ends.
if __name__ == "__main__":
    app = SharedPower()
    app.mainloop()