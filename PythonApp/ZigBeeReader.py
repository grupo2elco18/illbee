import serial
import xbee

class ZigBeeReader(object):

	def __init__(self, handler):
		super(ZigBeeReader, self).__init__()
		self.handler = handler
		self.ser = serial.Serial('/dev/ttyACM0', # TODO config
			baudrate=115200,
			bytesize=serial.EIGHTBITS,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
		)
		self.xbee = None
		self.data = {}

	def start(self):
		self.xbee = xbee.XBee(self.ser, callback=self.recv_data)

	def stop(self):
		self.xbee.halt()
		self.ser.close()

	def recv_data(self, data):

		serial = bytes2hex(data["source_addr_long"])
		data = data["rf_data"].decode("utf-8")

		if serial not in self.data:
			self.data[serial] = ""

		for c in data:
			if c == '\r':
				line = self.data[serial]
				self.data[serial] = ""
				self.handler.data(serial, line)
			else:
				self.data[serial] += c


def bytes2hex(bytes):
	h = "";
	for b in bytes:
		h += "{0:02X}".format(b)
	return h



def main():

	class HandlerTest(object):
		def __init__(self):
			super(HandlerTest, self).__init__()
			self.p = 0;

		def data(self, serial, data):
			print(serial, data)

	handler = HandlerTest()
	reader = ZigBeeReader(handler)

	reader.start()

	input("Press Enter to continue...")

	reader.stop()

if __name__ == '__main__':
	main();
