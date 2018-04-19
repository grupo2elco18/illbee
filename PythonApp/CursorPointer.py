#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Pointer


class CursorPointer(Pointer.Pointer):

	def __init__(self):
		super(CursorPointer, self).__init__()
		self.posX = 0
		self.posY = 0
		self.offX = 10
		self.offY = 10
		self.radius = 10

	def _draw(self):
		up_left = [self.posX-self.radius, self.posY-self.radius]
		lower_right = [self.posX+self.radius, self.posY+self.radius]
		return self.canvas.create_oval(up_left, lower_right, fill='orange')



def main():
	import tkinter as Tk
	import PointCanvas
	import _thread as thread
	import time


	root = Tk.Tk()
	root.title("CursorPointer")
	canvas = PointCanvas.PointCanvas(master=root, width=400, height=400, bg='lightblue')
	canvas.pack()

	pointer = CursorPointer()
	canvas.addPointer(pointer)

	def motion(event):
		pos = event.x, event.y

		pointer.update(pos)

	canvas.bind('<Motion>', motion)

	root.mainloop()


if __name__ == "__main__":
	main()
