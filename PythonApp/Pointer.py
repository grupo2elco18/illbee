# -*- coding: utf-8 -*-
from Event import Event

class Pointer(object):

	def __init__(self, params):
		super(Pointer, self).__init__()
		self.canvas = None
		self.poxX = 0
		self.posY = 0
		self.offX = 0
		self.offY = 0
		self.moved = False
		self.params = params

	def getParams(self):
		return self.params

	def onClick(self):
		if(self.canvas == None):
			return
		event = Event()
		event.x = self.posX
		event.y = self.posY
		event.source = self
		self.canvas.onClick(event)


	def _update(self, pos):
		self.posX = pos[0]
		self.posY = pos[1]
		self.moved = True

	def move(self):
		if(self.canvas == None):
			return
		if(self.params == None):
			return
		if(not self.moved):
			return

		sizeX = self.canvas.winfo_width()
		sizeY = self.canvas.winfo_height()
		posX = self.posX*sizeX
		posY = self.posY*sizeY

		x0 = posX - self.offX
		y0 = posY - self.offY
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
