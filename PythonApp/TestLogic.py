#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image

class TestLogic(object):

	def __init__(self, frame):
		super(TestLogic, self).__init__()
		self.frame = frame
		self.frame.getPointCanvas().addClickCB(self._onClick)
		self.test = None
		self.question = None


	def _onClick(self, event):
		print(event)
		self.next()

	def start(self, test):
		self.test = test
		self.next()

	def next(self):
		self.question = self.test.next()
		if self.question.qtype != "map":
			print("Wrong type of question type")
			return

		self.frame.setText(self.question.title)
		params = self.question.params
		image = Image.open(params["bg"])
		self.frame.setImage(image)
