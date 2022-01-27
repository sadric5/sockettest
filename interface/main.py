from tkinter import Frame, Label

class BaseFrame(Frame):
	def __init__(self, master):
		self.__init__(master)
		self.grid()
		top_label = Label(master, tex="Hello world!")