from tkinter import *
def donothing():
root = Tk()
colour = 'white'
menubar = Menu(root)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="DARK MODE", command=donothing)
helpmenu.add_command(label="LIGHT MODE", command=donothing)
menubar.add_cascade(label="UI MODE", menu=helpmenu)

mainColour = colour
#MAIN STUFF
root.configure(bg = mainColour)
root.geometry("900x200")
root.title("INTERACTIVE STORY")
def refreshBg():
    root.configure(bg = 'white')
#TEXT
w = Label(root, text ='FLY ON DORITOS', font = "20", bg = mainColour)
w.pack()
w = Message(root, text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ",width = 800, font = "20", bg = mainColour)
w.pack()
frame = Frame(root)
frame.pack()
#BUTTONS
b1_button = Button(frame, text = "Choice 1",height = 3, width = 10, bg = mainColour)
b1_button.pack(side = LEFT)
b2_button = Button(frame, text ="Choice 2",height = 3, width = 10, bg = mainColour)
b2_button.pack(side = LEFT)
b3_button = Button(frame, text="Restart",height = 3, width = 10, bg = mainColour)
b3_button.pack(side = LEFT)
root.config(menu=menubar)
root.mainloop()


