#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from Test import Test, Question

class TestLoader(object):

	def __init__(self, logic):
		super(TestLoader, self).__init__()
		self.logic = logic


	def load(self, testfile):
		tree = ET.parse(testfile)
		root = tree.getroot()

		name = root.find("name").text
		desc = root.find("description").text

		test = Test(name, desc)

		for el in root.findall('question'):
			params = {}
			for c in el:
				params[c.tag] = c.text

			title = params["title"]
			del params["title"]
			qtype = params["type"]
			del params["type"]
			score = params["success"]
			del params["success"]
			fail = params["fail"]
			del params["fail"]

			q = Question(title, qtype, params)
			q.setScore(int(score), int(fail))
			test.addQuestion(q)

		self.logic.start(test)



def main():
	class Logic(object):
		def start(self, test):
			print(test)

	loader = TestLoader(Logic())
	test = loader.load("tests/spain.xml")


if __name__ == '__main__':
	main()
