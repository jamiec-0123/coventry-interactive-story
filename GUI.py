from tkinter import *
root = Tk()
#MAIN STUFF
root.geometry("900x200")
root.title("INTERACTIVE STORY")
#TEXT
w = Label(root, text ='FLY ON DORITOS', font = "20")
w.pack()
w = Message(root, text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ",width = 800, font = "20")
w.pack()
frame = Frame(root)
frame.pack()
#BUTTONS
b1_button = Button(frame, text = "Choice 1",height = 3, width = 10)
b1_button.pack(side = LEFT)
b2_button = Button(frame, text ="Choice 2",height = 3, width = 10)
b2_button.pack(side = LEFT)
b3_button = Button(frame, text="Restart",height = 3, width = 10)
b3_button.pack(side = LEFT)

root.mainloop()


