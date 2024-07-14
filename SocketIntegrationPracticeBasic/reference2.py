from tkinter import *
root = Tk()
root.geometry("600x800")
root.title("reference project 2")

#text for form
Label(root,text="yoyooy",font= "timesnewroman 13 bold").grid(row=0,column=3)
name = Label(root,text = "name").grid(row = 1,column = 2)
phone= Label(root,text = "phone").grid(row = 2,column = 2)
gender = Label(root,text = "gender").grid(row = 3,column = 2)
extra = Label(root,text = "extra").grid(row = 4,column = 2)
#variables for storing
namevalue = StringVar()
phonevalue = IntVar()
gendervalue = StringVar()
extravalue = StringVar()
#For storing entries 
nameentry = Entry(root, textvariable=namevalue).grid(row = 1,column=3)
phoneentry = Entry(root, textvariable=phonevalue).grid(row =2 ,column=3)
extraentry = Entry(root, textvariable=extravalue).grid(row = 4,column=3)
genderentry = Checkbutton(text = "hhth",variable = gendervalue).grid(row=3,column=3)
#defining getvals
def getval():
	print("ok")
	print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),extravalue.get()}")

	with open("records.txt","w") as f:
		f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),extravalue.get()}")	
#button
Button(text="ajsjasjk",command=getval).grid(row=7,column=3)
#radio button 
var = StringVar()
var.set("Radio")
radio = Radiobutton(root,text="haj",variable=var,value=1).grid()
#list box
def add():
	global i
	lbx.insert(ACTIVE,f"{i}")
	i = i+1
def upload():
	statusvar.set("snjjj")
	sbar.update()
	import time
	time.sleep(2)
	statusvar.set("Ready jjj")
lbx = Listbox(root)
lbx.grid()
lbx.insert(END,"haaiioop")
Button(root,text="add",command=add).grid()
#for connecting scrollbar to a widget
scrollbar = Scrollbar(root)
scrollbar.grid()
listbox= Listbox(root,yscrollcommand=scrollbar.set)
listbox.grid()
for i in range(344):
	listbox.insert(END,f"Item {i}")
listbox.grid()
scrollbar.config(command=listbox.yview)
#status bar 
statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root,textvariable=statusvar,relief=SUNKEN)
sbar.grid(sticky="ew")
Button(root,text="test",command=upload).grid()
root.mainloop()