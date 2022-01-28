from tkinter import Frame, Label
import tkinter

class BaseFrame(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		top_label = Label(master, text="Hello World!")
		top_label.place(x=0, y=0, height=50, width=200)
		bottom_name = Label(master, text="Quit")
		bottom_name.place(x=0, y=200, height=50, width=200)


if __name__ == '__main__':
	root = tkinter.Tk()
	root.title("Hello there!")
	root.geometry('200x400')
	app = BaseFrame(root)
	app.mainloop()