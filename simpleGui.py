#!/usr/bin/python3

from tkinter import *
root = Tk()
root.title("Title")

img = PhotoImage(file='py.png')
root.tk.call('wm', 'iconphoto', root._w, img)

l1 = Label(root, text="Enter the sample text below (500 words)", anchor=W)
l1.grid(row=0, column=0, sticky=W, padx=10, pady=10)

text1 = Text(root, borderwidth=4, relief="groove")
text1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10, columnspan=2)
txt1 = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
text1.insert(END,txt1)

# scrollb1 = Scrollbar(root, orient="vertical", command=text1.yview)
# scrollb1.grid(row=1, column=1, sticky='ns')
# text1['yscrollcommand'] = scrollb1.set

l2 = Label(root, text="Dictionary", anchor=W)
l2.grid(row=0, column=2, sticky=W, padx=10, pady=10)

text2 = Text(root, borderwidth=4, relief="groove")
text2.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
txt2 = "Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English"
text2.insert(END, txt2)

def CheckCallBack(*argv):
	state = v.get()
	print ("state changed ", state)

	if not state:
		text1.config(state=DISABLED)
	else:
		text1.config(state=NORMAL)

def btnCallBack(*argv):
	print ("btn Clicked", "Entry value is ", length_text.get())

v = IntVar()
c = Checkbutton(text="Same length words ", variable=v, command=CheckCallBack)
c.grid(row = 2, column = 0, sticky=W, padx=10, pady=10)
c.var = v

length_text = Entry(root)
length_text.grid(row = 2, column = 1, sticky = W, padx=10, pady=10)

btn = Button(root, text = "Spell check", command=btnCallBack)
btn.grid(row = 2, column = 2, sticky = E, padx=10, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


# root.geometry('600x400')
root.mainloop()