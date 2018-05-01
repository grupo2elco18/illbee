import Pointer

class IRPointer(Pointer.Pointer):

	def __init__(self, remote_id, color):
		super(IRPointer, self).__init__()
		self.remote_id = remote_id
		self.color = color
		self.offX = 5
		self.offY = 5

	def update(self, irPoints):
		mx = (irPoints[0].x+irPoints[1].x)/2
		my = (irPoints[0].y+irPoints[1].y)/2
		posX = mx
		posY = 1024 - my
		self._update([posX/1024, posY/1024])

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
