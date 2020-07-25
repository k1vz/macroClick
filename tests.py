from tkinter import *
import pyautogui

gui = Tk()
gui.title("Full test")
gui.geometry("208x212")
gui.configure(background="black")
ds = 2


def asa():
    return pyautogui.moveTo(200, 500, 2)


#botao_macro = Button(gui, text=' 9 ', fg='black', bg='red', command=asa, height=1, width=7).pack()

'''
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = Button(self, text="QUIT", fg="red",
                           command=self.master.destroy)
        self.quit.pack(side="bottom")

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

        self.entrythingy = Entry()
        self.entrythingy.place(relx = 0.05, rely = 0.035)

        self.contents = StringVar()
        self.contents.set("this is a variable")
        self.entrythingy["textvariable"] = self.contents

        buttom_enter = Button(gui, text=' 9 ', fg='black', bg='red', command=self.print_contents,
                       height=1, width=7)
        buttom_enter.place(relx = 0.7, rely = 0.02)

        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event = ''):
        print("Var: ", self.contents.get())


app = App(master=gui)
app.mainloop()

app = master = gui
app.mainloop()

gui.mainloop()
