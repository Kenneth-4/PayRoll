import tkinter as tk
from tkinter import Label, font

main = tk.Tk()

main.geometry("900x250")
main.title("PayRoll")

welcome = tk.Label(main, text='WELCOME')
welcome.pack(pady=20)

main.mainloop()
