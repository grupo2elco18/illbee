import serial

class ZigBeeReader(object):

	def __init__(self):
		super(ZigBeeReader, self).__init__()
		self.ser = serial.Serial('/dev/ttyACM0',
			baudrate=115200,
			bytesize=serial.EIGHTBITS,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE
		)

	def read_points(self):
		point1 = []
		point2 = []
		while True:
			c = self.ser.read(1).decode("utf-8")
			if c is '{':
				point1.append(self.read_number());
				point1.append(self.read_number());
				point2.append(self.read_number());
				point2.append(self.read_number());
				break
		return [point1 , point2];


	def read_number(self):
		number = []
		while True:
			c = self.ser.read(1).decode("utf-8")
			if c is ',':
				break
			number.append(c)

		return int(''.join(number))


def main():
	reader = ZigBeeReader()
	while True:
		print(reader.read_points())

if __name__ == '__main__':
	main();
