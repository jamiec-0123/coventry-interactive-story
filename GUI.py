from tkinter import *
import sys

root = Tk()
mainColour = "white"
# BUTTON FUNCTIONS
def choice():
    line.config(text="new text")
    b1button.config(text="new choice1")
    b2button.config(text="new choice2")
    b3button.config(text="new choice3")
    b4button.config(text="return", command = choice)

def exit1():
    root.destroy()

# FUNCTIONS THAT CHANGES APP TO DARK/LIGHT
def lightMode():
    b1button.config(bg="white", activebackground="white",fg = "black")
    b2button.config(bg="white", activebackground="white",fg = "black")
    b3button.config(bg="white", activebackground="white",fg = "black")
    root.config(bg="white")
    line.config(bg="white",fg = "black")
    appName.config(bg="white",fg = "black")
    menubar.config(activebackground="white",fg = "black")
def darkMode():
    b1button.config(bg="#2B2B2B", activebackground="#2B2B2B",fg = "white")
    b2button.config(bg="#2B2B2B", activebackground="#2B2B2B",fg = "white")
    b3button.config(bg="#2B2B2B", activebackground="#2B2B2B",fg = "white")
    root.config(bg="#2B2B2B")
    line.config(bg="#2B2B2B",fg = "white")
    appName.config(bg="#2B2B2B",fg = "white")
    menubar.config(activebackground="#2B2B2B", fg = "white")

# DARK/LIGHT MENU
menubar = Menu(root)
dlmenu = Menu(menubar, tearoff=0)
dlmenu.add_command(label="DARK MODE", command = darkMode)
dlmenu.add_command(label="LIGHT MODE", command = lightMode)
menubar.add_cascade(label="UI MODE", menu=dlmenu)



#MAIN APP SETTINGS
root.geometry("900x200")
root.title("INTERACTIVE STORY")
root.config(bg = "white")

#TEXT
appName = Label(root, text ='FLY ON DORITOS', font = "20", bg = mainColour)
appName.pack()
line = Message(root, text="His fingers were aching terribly from all those online job applications he has been filling out non-stop for the past 3 hours. Even though it was the year 2077, jobs were scarce. Vincent's dull eyes popped open when he saw a job interview invitation from Doritos, Dominoes, B&M on his email.",width = 800, font = "20", bg = mainColour)
line.pack()
frame = Frame(root)
frame.pack()

#BUTTONS
b1button = Button(frame, text = "Doritos",height = 3, width = 10, bg = mainColour,activebackground="white", command = choice)
b1button.pack(side = LEFT)
b2button = Button(frame, text ="Dominoes",height = 3, width = 10, bg = mainColour,activebackground="white", command = choice)
b2button.pack(side = LEFT)
b3button = Button(frame, text="B&M",height = 3, width = 10, bg = mainColour,activebackground="white",command = choice)
b3button.pack(side = LEFT)
b4button = Button(frame, text = "exit",height = 3, width = 10, bg = mainColour,activebackground="white", command = exit1)
b4button.pack(side = LEFT)

root.config(menu=menubar)
root.mainloop()


