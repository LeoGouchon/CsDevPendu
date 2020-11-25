from tkinter import Tk, Label, Button

mw = Tk()
labelHello = Label(mw, text="hello world !", fg='blue')
labelHello.pack()
buttonQuitt=Button(mw, text="QUITTER", fg="red", command=mw.destroy)
buttonQuitt.pack()
mw.mainloop()