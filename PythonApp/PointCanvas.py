#!/usr/bin/python3
#!/# -*- coding: utf-8 -*-
import tkinter as Tk


class PointCanvas(Tk.Canvas):
	def __init__(self, **kwargs):
		super(PointCanvas, self).__init__(**kwargs)
		self.pointers = []
		self._update()

	def addPointer(self, pointer):
		self.pointers.append(pointer)
		pointer.draw(self)

	def _update(self):
		for p in self.pointers:
			p.move()

		self.after(20, self._update)

def main():
	import _thread as thread
	import time

	CANVAS_WIDTH = 400
	CANVAS_HEIGHT = 400

	# circle starting center coordinates and radius
	CIRCLE_X = 50
	CIRCLE_Y = 50
	CIRCLE_RADIUS = 20

	# fix animation rate, time in milliseconds
	STEP_TIME = 25
	STEP_X = 1
	STEP_Y = 1

	def move_circle():
		''' recursive function '''

		while True:
			canvas.move("orange_circles", STEP_X, STEP_Y)
			x0, y0, x1, y1 = canvas.bbox("orange_circles")
			if x1 > CANVAS_WIDTH:
				break
			time.sleep(1/STEP_TIME)

		#canvas.after(STEP_TIME, move_circle)

	def circle(x, y, r):
		# form a bounding square using center (x,y) and radius r
		# upper left corner (ulc) and lower right corner (lrc) coordinates of square
		ulc = x-r, y-r
		lrc = x+r, y+r
		# give the circle a tag name for reference
		canvas.create_oval(ulc, lrc, tag="orange_circles", fill='orange')
	root = Tk.Tk()
	root.title("Animated Circle")
	# ulc position of rootwindow
	root.geometry("+{}+{}".format(150, 80))
	# create a canvas to draw on
	canvas = Tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='lightblue')
	canvas.pack()

	circle(CIRCLE_X, CIRCLE_Y, CIRCLE_RADIUS)
	#circle(CIRCLE_X, CIRCLE_Y-55, CIRCLE_RADIUS/2)

	#move_circle()
	thread.start_new_thread(move_circle, ( ) )

	root.mainloop()



if __name__ == "__main__":
	main()
