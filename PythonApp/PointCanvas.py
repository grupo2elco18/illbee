#!/usr/bin/python3
#!/# -*- coding: utf-8 -*-
import tkinter as Tk


class PointCanvas(Tk.Canvas):
	def __init__(self, **kwargs):
		super(PointCanvas, self).__init__(**kwargs)
		self.pointers = []
		self._update()

	def addPointer(self, pointer):
		self.pointers.append(pointer)
		pointer.draw(self)

	def _update(self):
		for p in self.pointers:
			p.move()

		self.after(20, self._update)

def main():
	import tkinter as Tk
	import CursorPointer


	root = Tk.Tk()
	root.title("PointCanvas Test")
	canvas = PointCanvas(master=root, width=400, height=400, bg='lightblue')
	canvas.pack()

	pointer = CursorPointer.CursorPointer()
	canvas.addPointer(pointer)

	def motion(event):
		pos = event.x, event.y
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
