from tkinter import * 
import tkinter.messagebox as tmsg
root = Tk()
root.title("reference 4")
def myfunc():
	print("ekkwejkejk")
def helop():
	print("saksjkas")
	value = tmsg.askquestion("wuhuw","ajkskj")
	if value == "yes":
		msg = "hjajhhja"
	tmsg.showinfo("yoyo",msg)
def dollar():
	tmsg.showinfo("info",f"you get {myslider2.get()} or {myslider.get()}")


# mymenu = Menu(root)
# mymenu.add_command(label = "File",command=myfunc)
# mymenu.add_command(label = "Exit",command=quit)
# root.config(menu=mymenu)

#list of menu 
yourmenubar = Menu(root)
m1 = Menu(yourmenubar,tearoff = 0)
m1.add_command(label = "one",command=myfunc)
m1.add_command(label = "two",command=helop)
m1.add_separator()
m1.add_command(label = "three",command=myfunc)
m1.add_command(label = "four",command=quit)
yourmenubar.add_cascade(label="cascade",menu=m1)
root.config(menu=yourmenubar)
# for slider 
#vertical
myslider = Scale(root,from_=0,to=100,tickinterval=50)
myslider.pack()
Label(root,text="jasksakj").pack()
#horizontal
myslider2 = Scale(root,from_=0,to=100,orient=HORIZONTAL)
myslider2.set(32)
myslider2.pack()
Button(root,text="press",command=dollar).pack()
root.mainloop()