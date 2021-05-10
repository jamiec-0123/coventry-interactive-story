from tkinter import *
from tkinter import messagebox
import threading
from backend import getValue

root = Tk()

root.geometry("250x500")
T = Text(root, height=33, width=250)
T.pack()
def startProgram():
        threading.Timer(60, startProgram).start()
        if getValue() > 20:
            messagebox.showwarning(title="Over", message=str(getValue()))
            T.insert(END, str(getValue()) + '\n')
            T.see(END)
        if getValue() < 10:
            messagebox.showwarning(title="Below", message=str(getValue()))
            T.insert(END, str(getValue()) + '\n')
            T.see(END)
        else:
            T.insert(END,str(getValue()) + '\n')
            T.see(END)
startProgram()
root.mainloop()
