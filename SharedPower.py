"""
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <krzysiek.kwietniewski@gmail.com> wrote this file.  As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return.   Krzysztof Kwietniewski
 * ----------------------------------------------------------------------------
"""

from tkinter import *
from tkinter.ttk import *

# fonts
LARGE_FONT = ("Helvetica", 12)
SMALL_FONT = ("Helvetica", 8)

# storage
DESCRIPTION = ""
LOGIN = ""
LOGIN_NEW = ""
PASSWORD = ""
PASSWORD_NEW = ""
SEARCH = ""
SEARCH_RESULT = ""
NAME = ""
TYPE = ""
PRICE_DAY = 0
PRICE_HOUR = 0
WALLET = 0

class SharedPower(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # title of the pages
        self.title("Shared Power")
        self.iconbitmap("res/favicon.ico")

        # store pages
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # list of pages
        for F in (StartPage, ConnectPage, SignInPage, SearchPage, ServerDownPage, ResultPage, AddPage, MyToolsPage, ProductPage, SuccessPage, ErrorPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    # this function stacks pages and displays the current one
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Every class is a new page
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # logo
        logo = PhotoImage(file="res/tools_128.png")
        label = Label(self, image=logo)
        label.image = logo
        label.pack()

        # topic
        topic = Label(self, text="Welcome to SharedPower", font=LARGE_FONT).pack(pady=10, padx=10)

        # sign up
        signUp = Button(self, text="Sing up", command=lambda: controller.show_frame(SignInPage)).pack(pady=10, padx=10)

        # login
        login = Entry(self, textvariable=LOGIN).pack()

        # password
        password = Entry(self, show="*", textvariable=PASSWORD).pack()

        # sign in
        signIn = Button(self, text="Sign in", command=lambda: controller.show_frame(ConnectPage)).pack(pady=10, padx=10)

class ConnectPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # topic
        topic = Label(self, text="Connecting", font=LARGE_FONT).pack(pady=10, padx=10)

        # progressbar
        progressbar = Progressbar(self)
        progressbar.config(maximum=10)
        progressbar.pack()

        # start moving the indicator every interval
        def start_progressbar():
            progressbar.start(1000)

        # stop moving
        def stop_progressbar():
            progressbar.stop()

        # start progressbar on startup
        start_progressbar()

        # next page
        next = Button(self, text="test// Next", command=lambda: controller.show_frame(SearchPage)).pack()

        # show server down page
        test = Button(self, text="test// Failed", command=lambda: controller.show_frame(ServerDownPage)).pack()

class SignInPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # topic
        topic = Label(self, text="Welcome to SharedPower", font=LARGE_FONT).pack(pady=10, padx=10)

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(StartPage)).pack(pady=10, padx=10)

        # login
        Label(self, text="Login:", font=SMALL_FONT).pack()
        login = Entry(self, show="*", textvariable=LOGIN_NEW).pack()

        # password
        Label(self, text="Password:", font=SMALL_FONT).pack()
        password = Entry(self, show="*", textvariable=PASSWORD_NEW).pack()
        Label(self, text="Password again:", font=SMALL_FONT).pack()
        password_is_same = Entry(self, show="*", textvariable=PASSWORD_NEW).pack()

        # Sign in
        sign_in = Button(self, text="Sign in", command=lambda: controller.show_frame(StartPage)).pack(pady=10, padx=10)

class SearchPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # user avatar
        avatar_file = PhotoImage(file="res/user_64.png")
        avatar = Label(self, image=avatar_file)
        avatar.image = avatar_file
        avatar.pack()

        # user name
        username = Label(self, text="Luke Logan", font=SMALL_FONT).pack()

        # logout
        logout = Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).pack()

        # mytools
        mytools = Button(self, text="My tools", command=lambda: controller.show_frame(MyToolsPage)).pack()

        # addtool
        addtool = Button(self, text="Add tool", command=lambda: controller.show_frame(AddPage)).pack()

        # Search part
        search_entry = Entry(self, show="*", textvariable=SEARCH).pack(pady=10, padx=10)
        search = Button(self, text="Search", command=lambda: controller.show_frame(ResultPage)).pack()

class ServerDownPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # topic
        topic = Label(self, text="Server Down", font=LARGE_FONT).pack(pady=10, padx=10)

        # error
        error_file = PhotoImage(file="res/x_128.png")
        error = Label(self, image=error_file)
        error.image = error_file
        error.pack()

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(StartPage)).pack()

class ResultPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # logout
        logout = Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).pack()

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack()

        # search
        search_entry = Entry(self, show="*", textvariable=SEARCH_RESULT).pack(pady=10, padx=10)
        search = Button(self, text="Search", command=lambda: controller.show_frame(ResultPage)).pack()

        # scrollbar NOT-WORK
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        record = Listbox(self, yscrollcommand=scrollbar.set)
        for line in range(100):
            record.insert(END, "Tool number" + str(line))
        record.pack(fill=BOTH)
        scrollbar.config(command=record.yview())
        # scrollbar

class AddPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).pack()

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack(pady=10, padx=10)

        # topic
        topic = Label(self, text="Add tool", font=LARGE_FONT).pack(pady=10, padx=10)

        # DATA
        Label(self, text="Name:", font=SMALL_FONT).pack()
        name = Entry(self, textvariable=NAME).pack()

        Label(self, text="Type:", font=SMALL_FONT).pack()
        type = Entry(self, textvariable=TYPE).pack()

        Label(self, text="Condition:", font=LARGE_FONT).pack()
        condition = Combobox(self).pack()

        # add pic NOT-WORK
        Label(self, text="Photo:", font=LARGE_FONT).pack()
        product_file = PhotoImage(file="res/image_128.png")
        product = Label(self, image=product_file)
        product.image = product_file
        product.pack()
        # add PIC

        Label(self, text="Describe product:", font=LARGE_FONT).pack()
        description = Entry(self, textvariable=DESCRIPTION).pack()

        Label(self, text="Choose last day of rent:", font=LARGE_FONT).pack()

        Label(self, text="Day:", font=SMALL_FONT).pack()
        day = Combobox(self).pack()
        Label(self, text="Month:", font=SMALL_FONT).pack()
        month = Combobox(self).pack()
        Label(self, text="Year:", font=SMALL_FONT).pack()
        year = Combobox(self).pack()

        Label(self, text="Price in £", font=LARGE_FONT).pack()

        Label(self, text="Per day:", font=SMALL_FONT).pack()
        price_hour = Entry(self, textvariable=PRICE_DAY).pack()
        Label(self, text="Per hour:", font=SMALL_FONT).pack()
        price_day = Entry(self, textvariable=PRICE_HOUR).pack()

        # DATA
        add_tool = Button(self, text="Add tool", command=lambda: controller.show_frame(SuccessPage)).pack(pady=10, padx=10)

class MyToolsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).pack()

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack(pady=10, padx=10)

        # topic
        topic = Label(self, text="Your balance is: " + str(WALLET) + "£", font=LARGE_FONT).pack(pady=10, padx=10)

        # what tools you leased
        Label(self, text="Leased:", font=LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar NOT-WORK
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        record = Listbox(self, yscrollcommand=scrollbar.set)
        for line in range(100):
            record.insert(END, "Tool number" + str(line))
        record.pack(fill=BOTH)
        scrollbar.config(command=record.yview())
        # scrollbar

        # what tools you rented
        Label(self, text="Rented:", font=LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar NOT-WORK
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        record = Listbox(self, yscrollcommand=scrollbar.set)
        for line in range(100):
            record.insert(END, "Tool number" + str(line))
        record.pack(fill=BOTH)
        scrollbar.config(command=record.yview())
        # scrollbar

class ProductPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # logout
        logout = Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).pack()

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack()

class SuccessPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # green success
        Label(self, text="Success", foreground="green", font=LARGE_FONT).pack(pady=10, padx=10)

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack()

class ErrorPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # red error
        Label(self, text="Error", foreground="red", font=LARGE_FONT).pack(pady=10, padx=10)

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack()

#main loop
if __name__ == "__main__":
    app = SharedPower()
    app.mainloop()