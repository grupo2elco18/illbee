import Pointer

class IRPointer(Pointer):

	def __init__(self, remote_id, color):
		super(IRPointer, self).__init__()
		self.remote_id = remote_id
		self.color = color

	def update(self, irPoints):
		pass # TODO Render IR points to cursor screen

	def _draw(self):
		pass # TODO draw figure. png?
