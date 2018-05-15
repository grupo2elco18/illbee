#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as Tk
from PointCanvas import PointCanvas
from TestLogic import WAITING, SUCCESS, FAIL

class TestFrame(Tk.Frame):

	def __init__(self, root):
		super(TestFrame, self).__init__(root)
		self.users = {}
		self.labels = {}
		self.createWidgets()

	def createWidgets(self):
		self.rowconfigure(0, weight=None)
		self.columnconfigure(0, weight=3)
		self.rowconfigure(1, weight=1)
		self.columnconfigure(1, weight=1)

		self.label = Tk.Label(self, text="", font=(None, 30), bg='lightblue')
		self.label.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)

		self.score = Tk.Frame(self, bg='lightblue')
		self.score.grid(row=0, column=1, rowspan=2, sticky=Tk.N+Tk.S+Tk.E+Tk.W);


		self.canvas = PointCanvas(master=self, bg='lightblue')
		self.canvas.grid(row=1, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)

	def addUser(self, name, score):
		self.users[name] = score
		label = Tk.Label(self.score, bg='lightblue', font=(None, 15))
		self.labels[name] = label
		self.updateUser(name)
		label.pack()


	def updateUsers(self):
		for u in self.users:
			self.updateUser(u)

	def updateUser(self, name):
		label = self.labels[name]
		score = self.users[name]
		label["text"] = str(score.score) + "\t" + name
		if score.result == WAITING:
			label["fg"] = "black"
		elif score.result == FAIL:
			label["fg"] = "red"
		elif score.result == SUCCESS:
			label["fg"] = "green"

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
