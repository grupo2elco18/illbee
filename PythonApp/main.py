#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @file: main.py
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
	logic = TestLogic(app, handler.get_remotes())
	loader = TestLoader(logic)

	loader.load(test)



	reader.start()

	root.mainloop()

	reader.stop()


if __name__ == "__main__":
	# execute only if run as a script
	main()
