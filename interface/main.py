from tkinter import *
import tkinter
from turtle import color


class Basebutom(Frame):
	def __ini(self, master):
		Frame.__init__(self, master)
		my_but = tkinter.Button()
		my_but.pack(padx=10, pady=10)

class BaseFrame(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		main = Text(master)
		main.grid(padx=(10,50), pady=(10,0), )
		self.grid()

if __name__ == '__main__':
	root = tkinter.Tk()
	root.title("Hello there!")
	root.geometry('600x800')
	root.resizable(width=FALSE, height=FALSE)
	app = BaseFrame(root)
	app.mainloop()



	
		# top_label = Label(master, text="Hello World!")
		# top_label.place(x=0, y=0, height=50, width=200)

		# body = Label(master, text="BODY!", background='blue')
		# body.place(x=0, y=55, height=200, width=200)


		# bottom_name = Label(master, text="Quit", background='red')
		# bottom_name.place(x=0, y=205, height=50, width=200)

		# my_butt =  Label(bottom_name, text='Label in quit button', background='green')
		# my_butt.place(x=50, y=30, width=150, height=20)
		# my_butto =  Entry(bottom_name, textvariable='Label in quit button', background='white')
		# my_butto.pack()
		