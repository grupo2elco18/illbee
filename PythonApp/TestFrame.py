#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as Tk
from PointCanvas import PointCanvas

class TestFrame(Tk.Frame):

	def __init__(self, root):
		super(TestFrame, self).__init__(root)
		self.createWidgets()

	def createWidgets(self):
		self.rowconfigure(0, weight=None)
		self.columnconfigure(0, weight=3)
		self.rowconfigure(1, weight=1)
		self.columnconfigure(1, weight=1)

		self.label = Tk.Label(self, text="", font=(None, 30), bg='lightblue')
		self.label.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
		self.button2 = Tk.Button(self, text="button", bg='lightblue')
		self.button2.grid(row=0, column=1, rowspan=2, sticky=Tk.N+Tk.S+Tk.E+Tk.W);

		self.canvas = PointCanvas(master=self, bg='lightblue')
		self.canvas.grid(row=1, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)

	def setImage(self, image):
		self.canvas.setBG(image)

	def getPointCanvas(self):
		return self.canvas

	def setText(self, text):
		self.label["text"] = text




def main():
	root = Tk.Tk()
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)
	app = TestFrame(root)
	app.grid(sticky=Tk.N+Tk.S+Tk.E+Tk.W)

	app.setImage(image)
	root.mainloop()

if __name__ == "__main__":
	main()
