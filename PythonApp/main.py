#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as Tk
from PIL import Image
from TestFrame import TestFrame
from ZigBeeReader import ZigBeeReader
from ZigBeeHandler import ZigBeeHandler


def main():
	root = Tk.Tk()
	root.title("ILLBEE Test") # TODO config file
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)
	app = TestFrame(root)
	app.grid(sticky=Tk.N+Tk.S+Tk.E+Tk.W)

	image = Image.open("tests/res/spain.png")
	app.setImage(image)

	handler = ZigBeeHandler(app.getPointCanvas())
	reader = ZigBeeReader(handler)

	reader.start()

	root.mainloop()

	reader.stop()


if __name__ == "__main__":
	# execute only if run as a script
	main()
