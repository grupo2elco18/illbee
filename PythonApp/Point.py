import math

class Point(object):
	def __init__(self, pos):
		super(Point, self).__init__()
		self.x = pos[0]
		self.y = pos[1]

	def getPos(self):
		return [self.x, self.y]

	def midPoint(self, point):
		mx = self.x + point.x
		my = self.y + point.y
		return Point([mx/2, my/2])

	def dist(self, point):
		dx = self.x - point.x
		dy = self.y - point.y
		return math.sqrt(dx*dx + dy*dy)

	def diff(self, point):
		dx = self.x - point.x
		dy = self.y - point.y
		return Point([dx, dy])

	def angle(self, point):
		diff = self.diff(point)
		return math.atan(diff.y/diff.x)

	def rotate(self, angle):
		newX = self.x*math.cos(angle)-self.y*math.sin(angle)
		newY = self.y*math.cos(angle)+self.x*math.sin(angle)
		self.x = newX
		self.y = newY

	def __str__(self):
		return "<Point: " + str(self.x) + ", " + str(self.y) + ">"
