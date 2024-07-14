from tkinter import *
root = Tk()

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
#can_widget = Canvas(root,width=canvas_width,height=canvas_height)
#can_widget.pack()

#TODO: for line
#can_widget.create_line(0,0,800,200,fill = "red")
#to create a rectangle 
#can_widget.create_rectangle(3,5,700,300,fill="blue")
#create text 
#can_widget.create_text(200,200,text = "python")
#create oval
#can_widget.create_oval(3,5,500,200,fill="green")
#define
def first(event):
	print(f"{event.x},{event.y}")
#events where mouse was 
widget = Button(root,text="click")
widget.pack()
widget.bind('<Button-1>',first)
widget.bind('<Double-1>',quit)
root.mainloop()