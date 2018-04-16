#!/usr/bin/python3

import tkinter as Tk

class App(Tk.Frame):

	def __init__(self, master=None):
		super(App, self).__init__(master)
		self.bind("<Configure>", self.on_resize)
		self.createWidgets()

	def createWidgets(self):
		self.rowconfigure(0, weight=1)

		self.button = Tk.Button(self)
		self.button["text"] = "QUIT"
		self.button["fg"] = "red"
		self.button["command"] = self.quit

		self.button.grid(row=0, column=1)
		self.columnconfigure(0, weight=1)

		self.hi_there = Tk.Button(self, text="Hello", command=self.say_hi)
		self.hi_there.grid(row=0, column=0)
		self.columnconfigure(1, weight=1)

		self.canvas = Tk.Canvas(self, bg="blue");
		self.canvas.grid(row=0, column=2, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
		self.columnconfigure(2, weight=1)

	def say_hi(self):
		print("Hello, World!")

	def on_resize(self,event):
		print(self.grid_bbox())


def main():
	root = Tk.Tk()
	root.title("ILLUD Test") # TODO those thing in config file
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)
	app = App(root)
	app.grid(sticky=Tk.N+Tk.S+Tk.E+Tk.W)
	root.mainloop()
	root.destroy()

if __name__ == "__main__":
	# execute only if run as a script
	main()
