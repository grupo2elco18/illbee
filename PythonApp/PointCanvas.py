#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as Tk
from BGCanvas import BGCanvas


class PointCanvas(BGCanvas):
	def __init__(self, **kwargs):
		super(PointCanvas, self).__init__(**kwargs)
		self.pointers = []
		self._update()
		self.clickCB = []

	def addPointer(self, pointer):
		self.pointers.append(pointer)
		pointer.draw(self)

	def _update(self):
		for p in self.pointers:
			p.move()

		self.after(20, self._update)

	def addClickCB(self, cb):
		self.clickCB.append(cb)

	def onClick(self, event):
		for cb in self.clickCB:
			cb(event)


def main():
	import tkinter as Tk
	import CursorPointer


	root = Tk.Tk()
	root.title("PointCanvas Test")
	canvas = PointCanvas(master=root, bg='lightblue')
	canvas.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)

	pointer = CursorPointer.CursorPointer()
	canvas.addPointer(pointer)

	def motion(event):
		sizeX = canvas.winfo_width()
		sizeY = canvas.winfo_height()
		pos = event.x/sizeX, event.y/sizeY
		pointer.update(pos)

	canvas.bind('<Motion>', motion)

	def onClickCB(event, pointer):
		print("onClickCB: ", pointer.posX, pointer.posY)

	pointer.setClickCb(onClickCB)

	def onClick(event):
		pointer.onClick(event)

	canvas.bind("<Button-1>", onClick)

	root.mainloop()


if __name__ == "__main__":
	main()
