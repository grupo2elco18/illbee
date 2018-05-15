#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image

class TestLogic(object):

	def __init__(self, frame, remotes):
		super(TestLogic, self).__init__()
		self.frame = frame
		self.frame.getPointCanvas().addClickCB(self._onClick)
		self.remotes = remotes
		self.test = None
		self.question = None


	def _onClick(self, event):
		print(event)
		pos = self.frame.getPointCanvas().getImagePos(event)
		self._checkSuccess(pos)
		#self.next()

	def start(self, test):
		self.test = test
		self.next()

	def next(self):
		self.question = self.test.next()
		if self.question is None:
			self.frame.setText("END")
			self.frame.setImage(None)
			return

		if self.question.qtype != "map":
			print("Wrong type of question type")
			return

		self.frame.setText(self.question.title)
		params = self.question.params
		image = Image.open(params["bg"])
		self.solution = Image.open(params["answer"]).load()
		self.frame.setImage(image)

	def _checkSuccess(self, pos):
		print(self.solution[pos[0], pos[1]])
