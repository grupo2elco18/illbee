import Pointer

class IRPointer(Pointer.Pointer):

	def __init__(self, remote_id, color):
		super(IRPointer, self).__init__()
		self.remote_id = remote_id
		self.color = color
		self.offX = 5
		self.offY = 5

	def update(self, irPoints):
		print(irPoints)
		mx = (irPoints[0][0]+irPoints[1][0])/2
		my = (irPoints[0][1]+irPoints[1][1])/2
		posX = mx
		posY = 1024 - my
		self._update([posX, posY])

	def _draw(self):
		return self.canvas.create_oval([0, 0], [10, 10], fill='orange')

def read_serial(pointer, zb):
	while True:
		pointer.update(zb.read_points())


def main():
	import tkinter as Tk
	import PointCanvas
	import ZigBeeReader
	import _thread as thread


	root = Tk.Tk()
	root.title("IRPointer Test")
	canvas = PointCanvas.PointCanvas(master=root, width=1024, height=1024, bg='lightblue')
	canvas.pack()

	pointer = IRPointer(None, None)
	canvas.addPointer(pointer)

	zb = ZigBeeReader.ZigBeeReader()

	thread.start_new_thread( read_serial, (pointer, zb, ) )

	root.mainloop()


if __name__ == "__main__":
	main()
