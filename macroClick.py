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

        Button(gui, text=' Print ', fg='black', bg='red', height=1,
               command=self.print_contentsx, width=7).place(relx=0.7, rely=0.02)

        self.entrythingyX.bind('<Key-Return>', self.print_contentsx)

        # Entry - Y #
        self.entrythingyY = Entry()
        self.entrythingyY.place(relx=0.3, rely=0.18)

        self.contentsY = StringVar()
        self.contentsY.set("")
        self.entrythingyY["textvariable"] = self.contentsY
        self.entrythingyY["width"] = 12

        Button(gui, text=' Print ', fg='black', bg='red', command=self.print_contentsy,
               height=1, width=7).place(relx=0.7, rely=0.17)

        self.entrythingyY.bind('<Key-Return>', self.print_contentsy)

        # Entry - Lag #
        self.entrythingyLag = Entry()
        self.entrythingyLag.place(relx=0.247, rely=0.325)

        self.contentsLag = StringVar()
        self.contentsLag.set("")
        self.entrythingyLag["textvariable"] = self.contentsLag
        self.entrythingyLag["width"] = 14

        Button(gui, text=' Print ', fg='black', bg='red', command=self.print_contentslag,
               height=1, width=7).place(relx=0.7, rely=0.315)

        self.entrythingyLag.bind('<Key-Return>', self.print_contentslag)

        Button(gui, text=' Play ', fg='black', bg='red', command=lambda:
            click(self.contentsX.get(), self.contentsY.get(), self.contentsLag.get()), height=1, width=7) \
            .place(relx=0.35, rely=0.45)

    def print_contentsx(self):
        print("X: ", self.contentsX.get())

    def print_contentsy(self):
        print("Y: ", self.contentsY.get())

    def print_contentslag(self):
        print("Lag: ", self.contentsLag.get())


def click(x, y, lag):
    pyautogui.moveTo(int(x), int(y), int(lag))


# Runing GUI #
gui = App(master=gui).mainloop()
