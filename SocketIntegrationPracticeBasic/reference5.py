from tkinter import * 
class GUI(object):
	"""docstring for GUI"""
	def __init__(self):
		super().__init__()
		self.geometry("744x377")

	def status(self):
		self.var = StringVar()
		self.var.set("ready")
		sef.statusbar = Label(self,textvar=self.var,relief=SUNKEN,anchor = "w")
		
if __name__ == '__main__':
	window = GUI()
	window.mainloop()