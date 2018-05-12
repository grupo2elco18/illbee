import IRPointer
from Point import Point
import xml.etree.ElementTree as ET

remotes_file = "res/remotes.xml" # TODO config

class ZigBeeHandler(object):

	def __init__(self, canvas):
		super(ZigBeeHandler, self).__init__()
		self.canvas = canvas
		self.remotes = {}
		xml = ET.parse(remotes_file).getroot()
		self.xml_remotes = xml.findall("remote")


	def data(self, serial, data):

		remote = None
		if serial not in self.remotes:
			remote = self.new_remote(serial)
			if remote is None:
				return
			self.remotes[serial] = remote
		else:
			remote = self.remotes[serial]

		line = self._checkLine(data)
		if line is None:
			return
		elif line == "button":
			remote.onClick();
		else:
			numbers = self._numbers(line)
			if numbers is None:
				return
			points = self._points(numbers)
			if points is None:
				return
			remote.update(points)

	def _checkLine(self, line):
		if line.count('{') is not 1:
			return None
		if line.count('}') is not 1:
			return None


		s_pos = line.find('{') + 1
		e_pos = line.find('}', s_pos)
		if e_pos is -1:
			return None

		return line[s_pos:e_pos]

	def _numbers(self, line):
		numbers_list = line.split(',')
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

	def new_remote(self, serial):
		print("New remote", serial)

		for r in self.xml_remotes:
			if 	r.attrib["serial"] == serial:
				name = r.find("name").text
				color = r.find("color").text
				pointer = IRPointer.IRPointer(serial, color)
				self.canvas.addPointer(pointer)
				return pointer

		print("Unknown remote")
		return None

def main():
	tree = ET.parse(remotes_file)

	root = tree.getroot()
	print(root.attrib)
	print(root.tag)
	print(root.findall('remote'))

	for child in root:
		print(child.tag)
		print(child.attrib)
		for c in child:
			print(c.tag)
			print(c.text)

		print(child.find("name").text)







if __name__ == '__main__':
	main()
