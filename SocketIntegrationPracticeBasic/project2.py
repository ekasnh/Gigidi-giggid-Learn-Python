from tkinter import *
sample_root = Tk()
#for resizing GUI window
canvas_width = 800
canvas_height = 400
sample_root.geometry(f"{canvas_height}x{canvas_width}")
sample_root.minsize(300,300)
sample_root.maxsize(1200,980)
sample_root.title("reference project")
#label and pack function
labelone = Label(text='''kjsjkkja''',bg = "red",fg = "white",padx = 23,pady= 10,font=("comicsans",19,"bold"),borderwidth = 3,relief=SUNKEN)
labelone.pack(side = BOTTOM,anchor = "nw",fill = X)
#important attributes 
#text,bd,fg,font,padx,pady,relief-border styling sunken,raised,ridge,groove

#for showing images 

photo = PhotoImage(file = "")
labeltwo = Label(image=photo)
labeltwo.pack()

#frames

f1 = Frame(sample_root,bg= "grey")
f1.pack(side=LEFT)
frame = Frame(sample_root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=RIGHT,anchor="nw")
#commands 
def hello():
	print("hello")
#button 
b1 = Button(frame,fg="red",text = "Print now",command= hello)
b1.pack()
#grid
user = Label(sample_root,text = "username")
pswd = Label(sample_root,text = "pswd")
user.pack()#only two functions can be there rows and attribute
pswd.pack()
#variables in tkinter 
uservalue = StringVar()
passvalue = StringVar()
#for text box
userentry =  Entry(sample_root,textvariable = uservalue)

passentry = Entry(sample_root,textvariable=passvalue)
userentry.pack()
passentry.pack()
sample_root.mainloop()