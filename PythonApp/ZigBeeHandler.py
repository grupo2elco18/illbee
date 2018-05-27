#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @file: ZigBeeHandler.py
#
# Copyright (C) 2018 by Alejandro Vicario and the IllBee contributors.
#
# This file is part of the IllBee project.
#
# IllBee is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IllBee is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with IllBee.  If not, see <http://www.gnu.org/licenses/>.

import IRPointer
from Point import Point
import xml.etree.ElementTree as ET

remotes_file = "res/remotes.xml" # TODO config

class ZigBeeHandler(object):

	def __init__(self, canvas):
		super(ZigBeeHandler, self).__init__()
		self.canvas = canvas
		self.remotes = {}
		self.xml_remotes = []
		self.load()

	def load(self):
		xml = ET.parse(remotes_file).getroot()
		for r in xml.findall("remote"):
			params = {}
			serial = r.attrib["serial"]
			params["serial"] = serial
			params["name"] = r.find("name").text
			params["color"] = r.find("color").text
			params["cursor"] = r.find("cursor").text
			pointer = IRPointer.IRPointer(serial, params)
			self.xml_remotes.append(pointer)

	def data(self, serial, data):
		#print(data)

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
			if 	r.getID() == serial:
				self.canvas.addPointer(r)
				return r

		print("Unknown remote")
		return None

	def get_remotes(self):
		return self.xml_remotes

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
