#!/usr/bin/python3

# !/usr/bin/python3
from tkinter import *
root = Tk()
root.title("Title")

l1 = Label(root, text="Enter the sample text below (500 words)", anchor=W)
l1.grid(row=0, column=0, sticky=W)

text1 = Text(root)
text1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
txt1 = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
text1.insert(END,txt1)

l2 = Label(root, text="Dictionary", anchor=W)
l2.grid(row=0, column=1, sticky=W, columnspan=3)

text2 = Text(root)
text2.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
txt2 = "Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English"
text2.insert(END, txt2)

def CheckCallBack(*argv):
	print (v.get())

def btn1CallBack(*argv):
	print (argv)

v = IntVar()
c = Checkbutton(text="Same length words ", variable=v, command=CheckCallBack)
c.grid(row = 2, column = 0, sticky=W)
c.var = v

button = Button(text='words length', command= btn1CallBack)
button.grid(row = 2, column = 1, sticky = W)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)


root.geometry('600x400')
root.mainloop()