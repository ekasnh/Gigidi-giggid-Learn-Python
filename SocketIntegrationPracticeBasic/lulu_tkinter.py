import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('GUI')
#for center
#ttk.Label(win,text='enter ').pack()
#for variable location 
ttk.Label(win,text='enter ').grid(row = 0,column = 0)
age_label = ttk.Label(win,text = '')
win.mainloop()