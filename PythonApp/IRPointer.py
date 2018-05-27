#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @file: IRPointer.py
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

import Pointer
import math
from Point import Point

class IRPointer(Pointer.Pointer):

	def __init__(self, remote_id, params):
		super(IRPointer, self).__init__(params)
		self.remote_id = remote_id
		self.offX = 5
		self.offY = 5

	def update(self, irPoints):
		p1 = irPoints[0]
		p2 = irPoints[1]
		if p1 is None or p2 is None:
			return

		mp = p1.midPoint(p2);
		mp.y = 1-mp.y
		dist = p1.diff(p2);
		angle = p1.angle(p2);

		# Point where the remote is pointing
		fp = Point([0.5, 0.5])
		mprel = mp.diff(fp)
		mprel.rotate(angle)


		# Screen size
		screen = Point([0.4, 0.4])

		# Upper left screen corner in remote perspective
		sp = Point([mprel.x-screen.x/2, mprel.y+screen.y])

		# Where the cursor should be
		up = Point([-sp.x, -sp.y])
		#print("up:",up)
		# Normalize screen
		up.x = up.x/(screen.x)
		up.y = -up.y/(screen.y)

		# Smooth movement
		sm = self.smooth(up)
		#print(sm)

		self._update(sm)

	def smooth(self, new):
		radius = 0.02

		smX = self.posX
		smY = self.posY

		distX = new.x - self.posX
		distY = new.y - self.posY

		if abs(distX) > radius:
			smX = new.x - math.copysign(radius, distX)
		if abs(distY) > radius:
			smY = new.y - math.copysign(radius, distY)

		sm = [smX*0.9+new.x*0.1, smY*0.9+new.y*0.1,]

		return sm


	def _draw(self):
		print(self.params)
		color = self.params["color"]
		if self.params["cursor"] == "circle":
			return self.canvas.create_oval([0, 0], [10, 10], fill=color)
		elif self.params["cursor"] == "square":
			return self.canvas.create_rectangle([0, 0], [10, 10], fill=color)

	def getID(self):
		return self.remote_id


def main():
	import tkinter as Tk
	import PointCanvas
	import ZigBeeReader
	import ZigBeeHandler
	import _thread as thread

	def onClick(event):
		src = event.source.getParams()["name"]
		print("Click from:", src, event.x, event.y)


	root = Tk.Tk()
	root.title("IRPointer Test")
	canvas = PointCanvas.PointCanvas(master=root, width=1024, height=1024, bg='lightblue')
	canvas.pack()

	canvas.addClickCB(onClick)

	handler = ZigBeeHandler.ZigBeeHandler(canvas)

	reader = ZigBeeReader.ZigBeeReader(handler)

	reader.start()

	root.mainloop()

	reader.stop()


if __name__ == "__main__":
	main()
