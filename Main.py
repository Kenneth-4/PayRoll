from tkinter import tk

if __name__ == "__main__":
    main = tk.Tk()
    main.geometry("900x250")
    main.title("PayRoll")
    welcome = tk.Label(main, text='WELCOME')
    welcome.pack(pady=20)
    main.mainloop()