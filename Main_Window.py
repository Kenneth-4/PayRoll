import tkinter
from tkinter import messagebox, Entry, Button, font, Toplevel, Label, Tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.widgets()

    def widgets(self):

        self.welcomeLabel = Label(self.master, text='WELCOME', font=font.Font(size=35, weight="bold"), width=30, height=2)
        self.welcomeLabel.grid(row=0, column=1, columnspan=3, sticky='nsew')

        self.employee_button = Button(self.master, text='Admin Window', )  #command=
        self.employee_button.grid(row=1, column=1, sticky='nsew')

        self.admin_button = Button(self.master, text='Employee Window', )  #command=
        self.admin_button.grid(row=1, column=3, sticky='nsew')

        self.master.columnconfigure((1, 3), weight=7)
        self.master.columnconfigure((0, 4), weight=3)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure((0, 1), weight=1)
        self.master.rowconfigure(2, weight=1)

        def close_window():
            confirmed = messagebox.askyesno("Exit", "Are you sure you want to close the application?")
            if confirmed:
                self.master.destroy()
                

        self.master.protocol("WM_DELETE_WINDOW", close_window)
