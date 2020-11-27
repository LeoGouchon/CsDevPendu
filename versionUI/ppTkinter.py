import tkinter as tk

window = tk.Tk()
window.title('PENDU | CS-DEV')
window.geometry('600x600')
labelHello = tk.Label(window, text = 'hello world', fg = "green")
labelHello.pack()

buttonQuitt = tk.Button(window, text = "EXIT", fg = "red", command = window.destroy)
buttonQuitt.pack()

window.mainloop()