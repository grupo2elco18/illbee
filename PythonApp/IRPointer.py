import Pointer
from Point import Point

class IRPointer(Pointer.Pointer):

	def __init__(self, remote_id, color):
		super(IRPointer, self).__init__()
		self.remote_id = remote_id
		self.color = color
		self.offX = 5
		self.offY = 5

	def update(self, irPoints):
		p1 = irPoints[0]
		p2 = irPoints[1]
		if p1 is None or p2 is None:
			return

		mp = p1.midPoint(p2);
		dist = p1.diff(p2);

		# Point where the remote is pointing
		fp = Point([0.5, 1])

		# Screen size
		screen = Point([0.5-abs(dist.x/2), 1-abs(dist.y/2)])

		# Lower left screen corner in remote perspective
		sp = Point([mp.x-screen.x, mp.y])

		# Where the cursor should be
		up = fp.diff(sp)
		up.x = up.x/(screen.x*2) # Normalize screen y dimension

		# TODO allow rotation: extract angle from ir points and
		# rotate screen corner from mp
		self._update(up.getPos())

	def _draw(self):
		return self.canvas.create_oval([0, 0], [10, 10], fill='orange')


def main():
	import tkinter as Tk
	import PointCanvas
	import ZigBeeReader
	import ZigBeeHandler
	import _thread as thread


	root = Tk.Tk()
	root.title("IRPointer Test")
	canvas = PointCanvas.PointCanvas(master=root, width=1024, height=1024, bg='lightblue')
	canvas.pack()

	handler = ZigBeeHandler.ZigBeeHandler(canvas)

	reader = ZigBeeReader.ZigBeeReader(handler)

	reader.start()

	root.mainloop()

	reader.stop()


if __name__ == "__main__":
	main()
