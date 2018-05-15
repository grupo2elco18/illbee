#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as Tk
from PIL import Image
from TestFrame import TestFrame
from ZigBeeReader import ZigBeeReader
from ZigBeeHandler import ZigBeeHandler
from TestLogic import TestLogic
from TestLoader import TestLoader
import sys



def main():
	if len(sys.argv) != 3:
		print("Arguments Error")

	# TODO: check if arguments are correct
	serial = sys.argv[1]
	test = sys.argv[2]

	root = Tk.Tk()
	root.title("ILLBEE Test") # TODO config file
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)
	app = TestFrame(root)
	app.grid(sticky=Tk.N+Tk.S+Tk.E+Tk.W)

	handler = ZigBeeHandler(app.getPointCanvas())
	reader = ZigBeeReader(handler, serial)
	logic = TestLogic(app, handler.get_remotes)
	loader = TestLoader(logic)

	loader.load(test)



	reader.start()

	root.mainloop()

	reader.stop()


if __name__ == "__main__":
	# execute only if run as a script
	main()
