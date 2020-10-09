from tkinter import *

root = Tk()
mainColour = "white"
# BUTTON FUNCTIONS
def choice():
    line.config(text="new text")
    b1button.config(text="new choice1")
    b2button.config(text="new choice2")
    b3button.config(text="new choice3")

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
line = Message(root, text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ",width = 800, font = "20", bg = mainColour)
line.pack()
frame = Frame(root)
frame.pack()

#BUTTONS
b1button = Button(frame, text = "Choice 1",height = 3, width = 10, bg = mainColour,activebackground="white", command = choice)
b1button.pack(side = LEFT)
b2button = Button(frame, text ="Choice 2",height = 3, width = 10, bg = mainColour,activebackground="white")
b2button.pack(side = LEFT)
b3button = Button(frame, text="Restart",height = 3, width = 10, bg = mainColour,activebackground="white")
b3button.pack(side = LEFT)

root.config(menu=menubar)
root.mainloop()


