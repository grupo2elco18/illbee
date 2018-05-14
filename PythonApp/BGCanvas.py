#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as Tk
from PIL import Image, ImageTk

class BGCanvas(Tk.Canvas):
	def __init__(self, **kwargs):
		super(BGCanvas, self).__init__(**kwargs)
		self.bind("<Configure>", self._bg_resize)

	def setBG(self, image):
		self.original = image
		self.image = ImageTk.PhotoImage(self.original)
		self.bg = self.create_image(0,0,image=self.image, anchor=Tk.NW)
		self.tag_lower(self.bg)

	def _bg_resize(self, event):
		width, height = self.original.size
		vscale = event.width/width;
		hscale = event.height/height;

		scale = vscale;
		if hscale < vscale:
			scale = hscale

		size = (int(width*scale), int(height*scale))
		resized = self.original.resize(size,Image.ANTIALIAS)
		self.image = ImageTk.PhotoImage(resized)
		self.delete(self.bg)
		self.bg = self.create_image(0, 0, image=self.image, anchor=Tk.NW)





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
