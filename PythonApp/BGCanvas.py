#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as Tk
from PIL import Image, ImageTk
import math

class BGCanvas(Tk.Canvas):
	def __init__(self, **kwargs):
		super(BGCanvas, self).__init__(**kwargs)
		self.bg = None
		self.bind("<Configure>", self._bg_resize)

	def setBG(self, image):
		self.original = image
		if self.original is None:
			if self.bg is not None:
				self.delete(self.bg)
			return

		self._bg_resize()

	def _bg_resize(self, event=None):
		if self.original is None:
			return

		width, height = self.original.size

		sizeX = self.winfo_width()
		sizeY = self.winfo_height()

		vscale = sizeX/width;
		hscale = sizeY/height;

		scale = vscale;
		if hscale < vscale:
			scale = hscale

		self.size = (math.ceil(width*scale), math.ceil(height*scale+0.5))

		resized = self.original.resize(self.size,Image.ANTIALIAS)
		self.image = ImageTk.PhotoImage(resized)
		if self.bg is not None:
			self.delete(self.bg)
		self.bg = self.create_image(0, 0, image=self.image, anchor=Tk.NW)
		self.tag_lower(self.bg)

	def getImagePos(self, event):
		sizeX = self.winfo_width()
		sizeY = self.winfo_height()
		relImageX = self.size[0]/sizeX
		relImageY = self.size[0]/sizeY

		relCursorX = event.x/relImageX
		relCursorY = event.y/relImageY

		if relCursorX > 1 or relCursorX > 1:
			return None

		width, height = self.original.size

		return [relCursorX*width, relCursorY*height]





def main():
	root = Tk.Tk()
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)
	app = BGCanvas(master=root)

	image = Image.open("tests/res/spain.png")
	app.setBG(image)

	app.grid(sticky=Tk.N+Tk.S+Tk.E+Tk.W)
	root.mainloop()

if __name__ == "__main__":
	main()
