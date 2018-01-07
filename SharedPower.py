import tkinter as tk
import tkinter.ttk as tkk
LARGE_FONT = ("Helvetica", 12)
class SharedPower(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Shared Power")
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
        photoimage = tk.PhotoImage(file="res/tools_128.png")
        label = tk.Label(image=photoimage)
        label.image = photoimage
        label.pack()
        label = tk.Label(self, text="Sign in", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(StartPage))
        button2.pack()
class ConnectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Connecting", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.progressbar = tkk.Progressbar()
        self.progressbar.config(maximum=10)
        self.progressbar.pack()

        button = tk.Button(text="Start", command=self.on_start_button_clicked)
        button.pack()

        button = tk.Button(text="Stop", command=self.on_stop_button_clicked)
        button.pack()

    def on_start_button_clicked(self):
        self.progressbar.start(1000)

    def on_stop_button_clicked(self):
        self.progressbar.stop()


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
        label = tk.Label(self, text="Server Down", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        photoimage = tk.PhotoImage(file="res/x_128.png")
        label = tk.Label(image=photoimage)
        label.image = photoimage
        label.pack()
class ResultPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
        listbox = tk.Listbox()
        listbox.insert(tk.END, "Io")
        listbox.insert(tk.END, "Europa")
        listbox.insert(tk.END, "Ganymede")
        listbox.insert(tk.END, "Callisto")
        listbox.pack(fill=tk.BOTH, expand=0)


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
if __name__ == "__main__":
    app = SharedPower()
    app.mainloop()
