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

	def update(self, pos):
		self._update(pos)
