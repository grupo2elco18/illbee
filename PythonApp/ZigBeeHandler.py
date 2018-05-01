import IRPointer

class ZigBeeHandler(object):

	def __init__(self, canvas):
		super(ZigBeeHandler, self).__init__()
		self.canvas = canvas
		self.remotes = {}


	def data(self, serial, points):
		remote = None
		if serial not in self.remotes:
			remote = self.new_remote(serial)
			if remote is None:
				return
			self.remotes[serial] = remote
		else:
			remote = self.remotes[serial]

		remote.update(points)

	def new_remote(self, serial):
		print("New remote", serial)
		pointer = IRPointer.IRPointer(serial, None)
		self.canvas.addPointer(pointer)
		return pointer
