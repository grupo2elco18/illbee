import serial
import serial.threaded
import _thread as thread
import time
import math

class ZigBeeReader(serial.threaded.LineReader):
	def __init__(self, handler):
		super(ZigBeeReader, self).__init__()
		self.handler = handler
		self.on = False
		self.ser = serial.Serial('/dev/ttyACM0',
			baudrate=115200,
			bytesize=serial.EIGHTBITS,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			timeout=1
		)
		self.p = 0
		self.q = 0

	def start(self):
		self.on = True
		thread.start_new_thread( self._run, ( ) )


	def stop(self):
		self.on = False

	def _run(self):
		with serial.threaded.ReaderThread(self.ser, ReadLines) as protocol:
			protocol.setCB(self._newline)
			while self.on:
				time.sleep(1)
				print(self.p, self.p-self.q)

	def _newline(self, line):
		#print(line)
		self.p = self.p + 1
		serial = self._serial(line)
		if serial is None:
			return
		numbers = self._numbers(line)
		if numbers is None:
			return
		if len(numbers) is not 4 and len(numbers) is not 8:
			return
		points = self._points(numbers)#

		self.q = self.q + 1
		self.handler.data(serial, points)

	def _serial(self, line):
		serial = line[:16]
		hexC = [
			'0', '1', '2', '3', '4', '5', '6', '7',
			'8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
		]
		for c in serial:
			if c not in hexC:
				return None

		return serial

	def _numbers(self, line):
		if line.count('{') is not 1:
			return None
		if line.count('}') is not 1:
			return None

		s_pos = line.find('{') + 1
		e_pos = line.find('}', s_pos)
		if e_pos is -1:
			return None

		numbers_str = line[s_pos:e_pos]
		numbers_list = numbers_str.split(',')
		numbers = []
		for n in numbers_list:
			try:
				numbers.append(int(n))
			except ValueError as e:
				print(e)
				return None

		return numbers

	def _points(self, numbers):
		points = []
		px = numbers[::2]
		py = numbers[1::2]
		for x,y in zip(px,py):
			if x == 1023 or y == 1023:
				points.append(None)
			else:
				points.append(Point([1-x/1024,y/760]))
		return points


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

	def __str__(self):
		return "<Point: " + str(self.x) + ", " + str(self.y) + ">"



class ReadLines(serial.threaded.LineReader):
	TERMINATOR = b'\r'
	def __init__(self):
		super(ReadLines, self).__init__()
		self.cb = None

	def setCB(self, cb):
		self.cb = cb

	def handle_line(self, data):
		if(self.cb is not None):
			self.cb(data);


def main():

	class HandlerTest(object):
		def __init__(self):
			super(HandlerTest, self).__init__()
			self.p = 0;

		def data(self, serial, points):
			print(self.p, serial)
			self.p = self.p + 1
			for p in points:
				print(p.x, p.y)

	handler = HandlerTest()
	reader = ZigBeeReader(handler)

	reader.start()

	input("Press Enter to continue...")

	reader.stop()

if __name__ == '__main__':
	main();
