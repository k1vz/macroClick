from tkinter import *
import pyautogui

# Creating GUI #
gui = Tk()
gui.title("Full test")
gui.geometry("208x212")
gui.configure(background="black")

# Creating labels #
txtX = Label(gui, text="Coord X:").place(relx=0.025, rely=0.03)
txtY = Label(gui, text="Coord Y:").place(relx=0.025, rely=0.175)
txtLag = Label(gui, text="Delay: ").place(relx=0.025, rely=0.32)

'''
def asa():
    return pyautogui.moveTo(200, 500, 2)


b_macro = Button(gui, text=' 9 ', fg='black', bg='red', command=asa, height=1, width=7).pack()

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        b_hi = Button(self, text = "Hello World\n(click me)", command = self.say_hi).pack()


        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")


        b_quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        b_quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


app = Application(master=gui)
app.mainloop()

app = master = gui
app.mainloop()
'''


class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Entry - X #
        self.entrythingyX = Entry()
        self.entrythingyX.place(relx=0.3, rely=0.035)

        self.contentsX = StringVar()
        self.contentsX.set("")
        self.entrythingyX["textvariable"] = self.contentsX
        self.entrythingyX["width"] = 12

        b_enter = Button(gui, text=' Go ', fg='black', bg='red', height=1,
                         command=self.print_contentsx, width=7).place(relx=0.7, rely=0.02)

        self.entrythingyX.bind('<Key-Return>', self.print_contentsx)

        # Entry - Y #
        self.entrythingyY = Entry()
        self.entrythingyY.place(relx=0.3, rely=0.18)

        self.contentsY = StringVar()
        self.contentsY.set("")
        self.entrythingyY["textvariable"] = self.contentsY
        self.entrythingyY["width"] = 12

        b_enter = Button(gui, text=' Go ', fg='black', bg='red', command=self.print_contentsy,
                         height=1, width=7).place(relx=0.7, rely=0.17)

        self.entrythingyY.bind('<Key-Return>', self.print_contentsy)

        # Entry - Lag #
        self.entrythingyLag = Entry()
        self.entrythingyLag.place(relx=0.247, rely=0.325)

        self.contentsLag = StringVar()
        self.contentsLag.set("")
        self.entrythingyLag["textvariable"] = self.contentsLag
        self.entrythingyLag["width"] = 14

        b_enter = Button(gui, text=' Go ', fg='black', bg='red', command=self.print_contentslag,
                         height=1, width=7).place(relx=0.7, rely=0.32)

        self.entrythingyLag.bind('<Key-Return>', self.print_contentslag)

    def print_contentsx(self, event=''):
        print("X: ", self.contentsX.get())

    def print_contentsy(self, event=''):
        print("Y: ", self.contentsY.get())

    def print_contentslag(self, event=''):
        print("Lag: ", self.contentsLag.get())


# Runing GUI #
gui = App(master=gui).mainloop()
