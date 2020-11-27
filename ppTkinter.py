import tkinter as tk

window = tk.Tk()
labelHello = tk.Label(window, text = 'hello world', fg = "green")
labelHello.pack()

buttonQuitt = tk.Button(window, text = "EXIT", fg = "red", command = window.destroy