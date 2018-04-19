# -*- coding: utf-8 -*-

class Pointer(object):

	def __init__(self):
		super(Pointer, self).__init__()
		self.canvas = None
		self.poxX = 0
		self.posY = 0
		self.offX = 0
		self.offY = 0
		self.moved = False

	def onClick(self, event=None):
		if(self.canvas == None):
			return

	def update(self, pos):
		self.posX = pos[0]
		self.posY = pos[1]
		self.moved = True

	def move(self):
		if(self.canvas == None):
			return
		if(self.id == None):
			return
		if(not self.moved):
			return
		x0 = self.posX - self.offX
		y0 = self.posY - self.offY
		pos = self.canvas.coords(self.id)
		inc_x0 = x0 - pos[0]
		inc_y0 = y0 - pos[1]

		self.canvas.move(self.id, inc_x0, inc_y0);
		self.moved = False

	def draw(self, canvas):
		if(canvas == None):
			return
		self.canvas = canvas
		self.id = self._draw();

	def _draw(self):
		pass

# TODO change checks for exceptions
