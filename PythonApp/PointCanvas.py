#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @file: PointCanvas.py
#
# Copyright (C) 2018 by Alejandro Vicario and the IllBee contributors.
#
# This file is part of the IllBee project.
#
# IllBee is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IllBee is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with IllBee.  If not, see <http://www.gnu.org/licenses/>.

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
