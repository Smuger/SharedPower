import tkinter as tk
LARGE_FONT = ("Helvetica", 12)
class SharedPower(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, ConnectPage, SignInPage, SearchPage, ServerDownPage, ResultPage, AddPage, MyToolsPage, ProductPage, SuccessPage, ErrorPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login"  , command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class SignInPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sign in", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(StartPage))
        button2.pack()
class ConnectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class ServerDownPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class ResultPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class MyToolsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class ProductPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class SuccessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class ErrorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
app = SharedPower()
app.mainloop()
