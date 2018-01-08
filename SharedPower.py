import tkinter as tk
import tkinter.ttk as tkk

LARGE_FONT = ("Helvetica", 12)
SMALL_FONT = ("Helvetica", 8)

DESCRIPTION_TEXT = "description"
class SharedPower(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Shared Power")
        self.iconbitmap("res/favicon.ico")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (
        StartPage, ConnectPage, SignInPage, SearchPage, ServerDownPage, ResultPage, AddPage, MyToolsPage, ProductPage,
        SuccessPage, ErrorPage):
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
        photoimage = tk.PhotoImage(file="res/tools_128.png")
        label1 = tk.Label(self, image=photoimage)
        label1.image = photoimage
        label1.pack()
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign up", command=lambda: controller.show_frame(SignInPage))
        button1.pack()
        login = tk.Entry(self)
        login.pack()
        password = tk.Entry(self, show="*")
        password.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class SignInPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sign up", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        label1 = tk.Label(self, text="Login:", font=SMALL_FONT)
        label1.pack()
        login = tk.Entry(self)
        login.pack()
        label2 = tk.Label(self, text="Password:", font=SMALL_FONT)
        label2.pack()
        password = tk.Entry(self, show="*")
        password.pack()
        label3 = tk.Label(self, text="Password again:", font=SMALL_FONT)
        label3.pack()
        password1 = tk.Entry(self, show="*")
        password1.pack()
        button2 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(StartPage))
        button2.pack()
class ConnectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Connecting", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.progressbar = tkk.Progressbar(self)
        self.progressbar.config(maximum=10)
        self.progressbar.pack()

        def on_start_button_clicked(self):
            self.progressbar.start(1000)

        def on_stop_button_clicked(self):
            self.progressbar.stop()
        on_start_button_clicked(self)
        button = tk.Button(self, text="Next", command=lambda: controller.show_frame(SearchPage))
        button.pack()
        button1 = tk.Button(self, text="Failed", command=lambda: controller.show_frame(ServerDownPage))
        button1.pack()




class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        photoimage = tk.PhotoImage(file="res/user_64.png")

        label2 = tk.Label(self, image=photoimage)

        label2.image = photoimage
        label2.pack()
        username = tk.Label(self, text="Luke Logan", font=SMALL_FONT).pack()
        button = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage))
        button.pack()
        button1 = tk.Button(self, text="My tools", command=lambda: controller.show_frame(MyToolsPage))
        button1.pack()
        button = tk.Button(self, text="Add tool", command=lambda: controller.show_frame(AddPage))
        button.pack()
        search = tk.Entry(self)
        search.pack()
        button2 = tk.Button(self, text="Search", command=lambda: controller.show_frame(ResultPage))
        button2.pack()

class ServerDownPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Server Down", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)
        photoimage = tk.PhotoImage(file="res/x_128.png")
        label2 = tk.Label(self, image=photoimage)
        label2.image = photoimage
        label2.pack()
        button = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button.pack()
class ResultPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Back", command=lambda: controller.show_frame(SearchPage))
        button2.pack()
        search = tk.Entry(self)
        search.pack()
        button2 = tk.Button(self, text="Search", command=lambda: controller.show_frame(ResultPage))
        button2.pack()
        scrollbar = tkk.Scrollbar(self)
        scrollbar.pack()

        mylist = tk.Listbox(self, yscrollcommand=scrollbar.set)
        for line in range(100):
            mylist.insert(tk.END, "This is line number " + str(line))

        mylist.pack(fill=tk.BOTH)
        scrollbar.config(command=mylist.yview)

        #self.yScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        #self.listbox = tk.Listbox(self, yscrollcommad=self.yScroll.set)
        #self.listbox.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        #self.yScroll['command'] = self.listbox.yview

class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Back", command=lambda: controller.show_frame(SearchPage))
        button2.pack()
        label = tk.Label(self, text="Add tool", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label1 = tk.Label(self, text="Name:", font=LARGE_FONT).pack()
        Name = tk.Entry(self)
        Name.pack()
        label2 = tk.Label(self, text="Type:", font=LARGE_FONT).pack()
        Type = tkk.Combobox(self)
        Type.pack()
        label3 = tk.Label(self, text="Condition:", font=LARGE_FONT).pack()
        condition = tkk.Combobox(self)
        condition.pack()
        #login = tk.Entry(self)
        #login.pack()
        label35 = tk.Label(self, text="Photo:", font=LARGE_FONT).pack()
        test = tk.PhotoImage(file="res/image_128.png")
        product_image = tk.Label(self, image=test)
        product_image.image = test
        product_image.pack()
        label4 = tk.Label(self, text="Describe product:", font=LARGE_FONT).pack()
        description = tk.Entry(self, textvariable=DESCRIPTION_TEXT)
        description.pack()
        label5 = tk.Label(self, text="Choose last day of rent:", font=LARGE_FONT).pack()
        label6 = tk.Label(self, text="Day:", font=SMALL_FONT).pack()
        day = tkk.Combobox(self).pack()
        label7 = tk.Label(self, text="Month:", font=SMALL_FONT).pack()
        month = tkk.Combobox(self).pack()
        label8 = tk.Label(self, text="Year:", font=SMALL_FONT).pack()
        year = tkk.Combobox(self).pack()
        label9 = tk.Label(self, text="Price in £", font=LARGE_FONT).pack()
        label10 = tk.Label(self, text="Per day:", font=SMALL_FONT).pack()
        price_hour = tk.Entry(self, textvariable=DESCRIPTION_TEXT).pack()
        label11 = tk.Label(self, text="Per month:", font=SMALL_FONT).pack()
        price_day = tk.Entry(self, textvariable=DESCRIPTION_TEXT).pack()
        button3 = tk.Button(self, text="Add this tool", command=lambda: controller.show_frame(SearchPage))
        button3.pack(pady=10, padx=10)

class MyToolsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="My Tools", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()

        #ScrollTest
        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)
        #ScrollTest


class ProductPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class SuccessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
class ErrorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to SharedPower", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Sign in", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button1.pack()
        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(ConnectPage))
        button2.pack()
if __name__ == "__main__":
    #ScrollTest
    class SampleApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)


            self.frame = tk.SharedPower(root)
            self.frame.pack()
            self.label = tk.Label(text="Shrink the window to activate the scrollbar.")
            self.label.pack()
            buttons = []
            for i in range(10):
                buttons.append(tk.Button(self.frame.interior, text="Button " + str(i)))
                buttons[-1].pack()
    #ScrollTest
    app = SharedPower()
    app.mainloop()
