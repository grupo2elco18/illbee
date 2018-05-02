import IRPointer
import xml.etree.ElementTree as ET

remotes_file = "res/remotes.xml" # TODO config

class ZigBeeHandler(object):

	def __init__(self, canvas):
		super(ZigBeeHandler, self).__init__()
		self.canvas = canvas
		self.remotes = {}
		xml = ET.parse(remotes_file).getroot()
		self.xml_remotes = xml.findall("remote")


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
