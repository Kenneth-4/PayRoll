import tkinter as tk
from tkinter import Label, font
from Main_Window import MainWindow

if __name__ == "__main__":
    main = tk.Tk()
    main.geometry("900x250")
    main.title("BBtrix System")

    Main_Window = MainWindow(main)
    main.mainloop()