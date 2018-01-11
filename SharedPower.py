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
from tinydb import *
import time
from time import mktime
from datetime import datetime
from getpass import getpass

# fonts
LARGE_FONT = ("Helvetica", 12)
SMALL_FONT = ("Helvetica", 8)

# storage
DESCRIPTION = "The Bosch GSA18V-125 EC Brushless 1.25 In.-Stroke Multi-Grip Reciprocating Saw is the first cordless " \
              "recip saw with orbital and non-orbital sawing action for superior cutting in materials from wood to " \
              "metal. It is engineered to be the most effective 18V demolition recip saw available. With an innovative " \
              "and easy-to-handle angled-motor design, it has extremely versatile ergonomic multi-position grip areas " \
              "with soft-grip."
LOGIN = ""
LOGIN_NEW = ""
PASSWORD = ""
PASSWORD_NEW = ""
SEARCH = ""
SEARCH_RESULT = ""
NAME = ""
TYPE = ""
LOGIN_EMAIL = ""
LOGIN_POSTCODE = ""
LOGIN_ADDRESS = ""
LOGIN_CODE = ""
LOGIN_CODE_BACK = ""
PRODUCT_NAME = "Bosch Saw GSA18V-125N"
PRODUCT_AVAILABLE_DAY = 00
PRODUCT_AVAILABLE_MONTH = 00
PRODUCT_AVAILABLE_YEAR = 0000
PRICE_DAY = 0
PRICE_HOUR = 0
WALLET = 0
CALCULATED_PRICE = 0

IS_LOGIN = False

SIGN_UP_DICT = {}
#dict['one'] = "This is one"
#dict[2]     = "This is two"
#tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

class SharedPower(Tk):
    def __init__(self, *args, **kwargs):
        root = Tk.__init__(self, *args, **kwargs)


        # images of products
        PRODUCT_IMAGE_SAW = PhotoImage(file="res/saw_GSA18V-125N_128.png")



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
    """
    def show_frame_and_login(self, cont):
        global IS_LOGIN
        IS_LOGIN = True
        frame = self.frames[cont]
        frame.tkraise()
        return IS_LOGIN
    def show_frame_and_logout(self, cont):
        global IS_LOGIN
        IS_LOGIN = False
        frame = self.frames[cont]
        frame.tkraise()
    """
    def show_frame_and_signup(self, cont):
        global IS_LOGIN
        IS_LOGIN = False
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
        signUp = Button(self, text="Sign up", command=lambda: controller.show_frame(SignInPage)).pack(pady=10, padx=10)

        # login
        login = Entry(self, textvariable=LOGIN).pack()

        # password
        password = Entry(self, show="*", textvariable=PASSWORD).pack()

        # sign in
        signIn = Button(self, text="Sign in", command=lambda: controller.show_frame(ConnectPage)).pack(pady=10, padx=10)

        # Search part
        search_entry = Entry(self, textvariable=SEARCH).pack(pady=10, padx=10)
        search = Button(self, text="Search", command=lambda: controller.show_frame(ResultPage)).pack()

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
        topic = Label(self, text="Create Account", font=LARGE_FONT).pack(pady=10, padx=10)

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(StartPage)).pack(pady=10, padx=10)

        # login
        Label(self, text="Login:", font=SMALL_FONT).pack()
        login = Entry(self, textvariable=LOGIN_NEW).pack()

        # password
        Label(self, text="Password:", font=SMALL_FONT).pack()
        password = Entry(self, show="*", textvariable=PASSWORD_NEW).pack()
        Label(self, text="Password again:", font=SMALL_FONT).pack()
        password_is_same = Entry(self, show="*", textvariable=PASSWORD_NEW).pack()

        # email
        Label(self, text="Email:", font=SMALL_FONT).pack()
        login = Entry(self, textvariable=LOGIN_EMAIL).pack()

        # postcode
        Label(self, text="Postcode:", font=SMALL_FONT).pack()
        login = Entry(self, textvariable=LOGIN_POSTCODE).pack()

        # address
        Label(self, text="Address:", font=SMALL_FONT).pack()
        login = Entry(self, textvariable=LOGIN_ADDRESS).pack()

        # card
        Label(self, text="Card owner name:", font=SMALL_FONT).pack()
        login = Entry(self, textvariable=LOGIN_CODE).pack()

        # card back
        Label(self, text="Card details:", font=SMALL_FONT).pack()
        login = Entry(self, textvariable=LOGIN_CODE_BACK).pack()

        # Sign up
        sign_up = Button(self, text="Sign up", command=lambda: controller.show_frame_and_signup(StartPage)).pack(pady=10, padx=10)

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

        # Search part
        search_entry = Entry(self, textvariable=SEARCH).pack(pady=10, padx=10)
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

        logout = Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).pack()

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack()

        # search
        search_entry = Entry(self, show="*", textvariable=SEARCH_RESULT).pack(pady=10, padx=10)
        search = Button(self, text="Search", command=lambda: controller.show_frame(ResultPage)).pack()

        """
        # scrollbar NOT-WORK
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        record = Listbox(self, yscrollcommand=scrollbar.set)
        for line in range(100):
            record.insert(END, "Tool number" + str(line))
        record.pack(fill=BOTH)
        scrollbar.config(command=record.yview())
        # scrollbar
        # to product NOT-WORK
        """
        next = Button(self, text="test// Next", command=lambda: controller.show_frame(ProductPage)).pack()

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

        # addtool
        addtool = Button(self, text="Add tool", command=lambda: controller.show_frame(AddPage)).pack()

        # what tools you leased
        Label(self, text="Leased:", font=LARGE_FONT).pack(pady=10, padx=10)

        Label(self, text="Condition:", font=LARGE_FONT).pack()
        condition = Combobox(self).pack()

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

        # name
        name = Label(self, text=PRODUCT_NAME, font=LARGE_FONT).pack(pady=10, padx=10)

        # photo
        photo_file = PhotoImage(file="res/saw_GSA18V-125N_256.png")
        photo = Label(self, image=photo_file)
        photo.image = photo_file
        photo.pack()

        # description
        description_label = Label(self, text=str(DESCRIPTION), font=SMALL_FONT).pack()
        description_label1 = Text(wrap=WORD)

        # date
        Label(self, text="Product will be available: ", font=LARGE_FONT).pack()
        date = Label(self, text=str(PRODUCT_AVAILABLE_DAY) + "/" + str(PRODUCT_AVAILABLE_MONTH) + "/" + str(PRODUCT_AVAILABLE_YEAR), font=LARGE_FONT).pack()
        Label(self, text="Your rent day:", font=LARGE_FONT).pack()
        Label(self, text="Hour:", font=SMALL_FONT).pack()
        hour = Combobox(self).pack()
        Label(self, text="Day:", font=SMALL_FONT).pack()
        day = Combobox(self).pack()
        Label(self, text="Month:", font=SMALL_FONT).pack()
        month = Combobox(self).pack()
        Label(self, text="Year:", font=SMALL_FONT).pack()
        year = Combobox(self).pack()

        # calculated price
        price_label = Label(self, text="Price: " + str(CALCULATED_PRICE) + "£", font=LARGE_FONT).pack(pady=10, padx=10)

        Label(self, text="Delivery:", font=SMALL_FONT).pack()
        delivery = Combobox(self).pack()

        # pay
        pay = Button(self, text="Pay", command=lambda: controller.show_frame(SuccessPage)).pack()


class SuccessPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # green success
        Label(self, text="Success", foreground="green", font=LARGE_FONT).pack(pady=10, padx=10)

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack()

        # test
        back = Button(self, text="test// error", command=lambda: controller.show_frame(ErrorPage)).pack(pady=10, padx=10)


class ErrorPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # red error
        Label(self, text="Error", foreground="red", font=LARGE_FONT).pack(pady=10, padx=10)

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack()

#BACKEND _________________-

#DATABASE
class DataBaseController:
    userdb = ""
    toolsdb = ""
    rentalsdb = ""

    def __init__(self):
        self.userdb = TinyDB("Databases/users.json")
        self.toolsdb = TinyDB("Databases/tools.json")
        self.rentalsdb = TinyDB("Databases/rentals.json")

    def createuser(self, username, password):
        self.userdb.insert({"id": time.time(), 'name': username, 'password': password})

    def getuser(self, action, username, password):
        User = Query()
        if (action == "login"):
            return self.userdb.search(User.name == username and User.password == password)

    def createtool(self, userid, name, price, type):
        self.toolsdb.insert({"id": time.time(), 'userid': userid, 'name': name, 'price': price, 'type': type})

    def gettool(self, searchby, query):
        Tool = Query()
        if (searchby == "typeof"):

            return self.toolsdb.search(Tool.type == query)
        elif (searchby == "name"):
            return self.toolsdb.search(Tool.name == query)
        elif (searchby == "userid"):
            return self.toolsdb.search(Tool.userid == query)

    def checkavaiblity(self, toolid, startdate, enddate):
        Rental = Query()
        return self.rentalsdb.search(
            Rental.toolid == toolid and (
                    Rental.startdate >= startdate or Rental.startdate <= enddate or Rental.enddate >= enddate or Rental.enddate >= startdate))

    def addrental(self, userid, toolid, startdate, enddate):
        self.rentalsdb.insert(
            {"id": time.time(), 'userid': userid, 'toolid': toolid, 'startdate': startdate, 'enddate': enddate})

#LOGIN

class LoginController:
    session = False
    userid = 0

    def __init__(self):
        pass

    def login(self, username, password):
        if (self.session):
            what_to_do = input("You are already login, do you want log in to another account? (Y/N):")
            if (what_to_do == "Y"):
                self.logout()
        else:
            db = DataBaseController()
            login = db.getuser("login", username, password)
            # print(login)
            if (login):
                self.session = True
                self.userid = login[0]["id"]
            else:
                print("Bad password or login")

    def logout(self):
        self.session = False

#RENTALS

class RentalController:

    def check_availability(self, toolid, startdate, enddate):
        db = DataBaseController()
        if db.checkavaiblity(toolid, startdate, enddate):
            return False
        return True

    def add_rental(self, userid, toolid, startdate, enddate):
        db = DataBaseController()
        db.addrental(userid, toolid, startdate, enddate)

#TOOLS

class ToolController():
    tool_list = []
    rental = RentalController();

    def hire(self):
        return

    def list_all(self, userid):
        db = DataBaseController()
        self.tool_list = db.gettool("userid", userid)

        while (self.display_menu()):
            pass

    def search_by_type(self, typeof, userid):
        db = DataBaseController()
        self.tool_list = db.gettool("typeof", typeof)
        while self.display_rental_menu(userid):
            pass

    def search_by_name(self, name, userid):
        db = DataBaseController()
        self.tool_list = db.gettool("name", name)
        while self.display_rental_menu(userid):
            pass

    def add_tool(self, userid, name, price, type):
        db = DataBaseController()
        db.createtool(userid, name, price, type)

    def remove_tool(self):
        return

    def display_menu(self):
        for index, toolitem in enumerate(self.tool_list):
            print(toolitem["name"], "to edit choose: ", index)
        print("to back to main meny choose x")
        where_to_go = input("Your choose:")
        if (where_to_go == "x"):
            return False
        elif (int(where_to_go) in range(0, len(self.tool_list))):
            print("Edit of Tool")

        else:
            print("Not allowed selection")
        return True

    def display_rental_menu(self, userid):
        for index, toolitem in enumerate(self.tool_list):
            print(toolitem["name"], "to choose: ", index)
        print("to back to main meny choose x")
        where_to_go = input("Your choose:")
        if (where_to_go == "x"):

            return False
        elif (int(where_to_go) in range(0, len(self.tool_list))):
            print("Option of Tool")
            print("Now you could check availability of tool")
            start = datetime.strptime(input("Begging date(dd/mm/yyyy):"), "%d/%m/%Y").timetuple()
            beg_date = mktime(start)
            end = datetime.strptime(input("End date(dd/mm/yyyy):"), "%d/%m/%Y").timetuple()
            end_date = mktime(end)
            print(beg_date, "test", end_date)
            if (self.rental.check_availability(int(where_to_go), beg_date, end_date)):

                if(input("Tool is avaible, do you want reserve? (y/n)")=="y"):
                    self.rental.add_rental(userid, int(where_to_go), beg_date, end_date)

        else:
            print("Not allowed selection")
        return True

#USER
class UserController:
    def __init__(self):
        return

    def create_account(self, username, password):
        db = DataBaseController()
        db.createuser(username, password)
        print("Account for " + username + " Created")

#MENU DATA
class MenuController:
    login = LoginController()

    def __init__(self):
        self.data = []
        self.user = UserController()
        self.tool = ToolController()

    def display_menu(self):

        if self.login.session:
            print("Logout: 1")

        else:
            print("Login: 1")

        print("Search Tool: 2")
        if self.login.session:
            print("Add Tool: 3")
            print("My Rentals: 4")
            print("My Tools: 5")
        else:
            print("Create Account: 3")
        print("Exit: 6")
        where_to_go = input("Where do you want to go?")

        if (where_to_go == "1" and self.login.session):
            print("Logout")
            self.logout_menu()
        elif (where_to_go == "1"):
            print("Login")
            self.login_menu()
        elif (where_to_go == "2"):
            print("Search Tool:")
            self.search_tool("typeorname")

        elif (where_to_go == "3" and self.login.session):
            print("Add Tool")
            self.create_tool()
        elif (where_to_go == "3"):
            print("Create Account")
            self.create_account_menu()
        elif (where_to_go == "4"):
            print("My Rentals")
        elif (where_to_go == "5"):
            print("My Tools")
            self.search_tool("userid")
        elif (where_to_go == "6"):
            exit()
        else:
            print("Not allowed selection")

    def login_menu(self):

        username = input("Insert Login:")
        password = getpass()
        # print("username: " + username + "Password: " + password)
        self.login.login(username, password)

    def create_account_menu(self):

        username = input("Insert Login")
        password = 1
        password2 = 2
        while (password != password2):
            password = getpass()
            password2 = getpass()
            if (password != password2):
                print("Passwords doesn't match, try again!")
        self.user.create_account(username, password)

    def logout_menu(self):
        if (self.login.session):
            choose = input("Are you sure? (Y/N):")
            if (choose == "Y"):
                self.login.logout()
                print("You are logout")

    def create_tool(self):

        name = input("Insert toolname: ")
        price = input("Insert price: ")
        type = input("insert type: ")
        self.tool.add_tool(self.login.userid, name, price, type)

    def search(self):
        print("to search by name: 1")
        print("to search by type: 2")
        print("to exit to main menu: x")
        where_to_go = input("How would you like a search")
        if (where_to_go == "x"):
            return False
        elif where_to_go == "1":
            what_do_you_want_find = input("what would you like a search")
            self.tool.search_by_name(what_do_you_want_find, self.login.userid)
            pass
        elif where_to_go == "2":
            what_do_you_want_find = input("what would you like a search")
            self.tool.search_by_type(what_do_you_want_find, self.login.userid)
            pass

        return True

    def search_tool(self, searchby):
        if (searchby == "userid"):
            self.tool.list_all(self.login.userid)
        else:
            while self.search():
                pass


#BACKEND __________________

#main loop
if __name__ == "__main__":
    app = SharedPower()
    app.mainloop()