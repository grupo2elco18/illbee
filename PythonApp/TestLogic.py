#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image
import time

WAITING = 0
SUCCESS = 1
FAIL = -1

class TestLogic(object):

	def __init__(self, frame, remotes):
		super(TestLogic, self).__init__()
		self.frame = frame
		self.frame.getPointCanvas().addClickCB(self._onClick)
		self.test = None
		self.question = None
		self.remotes = {}
		self.nAns = 0
		for r in remotes:
			self.remotes[r] = Score()


	def _onClick(self, event):
		print(event)
		score = self.remotes[event.source]
		if score.result != WAITING:
			return

		pos = self.frame.getPointCanvas().getImagePos(event)
		if pos is None:
			return
		if self._checkSuccess(pos):
			score.update(self.test.getSuccess(), SUCCESS)
		else:
			score.update(self.test.getFail(), FAIL)

		self.nAns += 1

		self.printStatus()

		if self.nAns == len(self.remotes):
			time.sleep(5)
			self.next()

	def start(self, test):
		self.test = test
		self.next()

	def next(self):
		self.resetRemotes()
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
		px = self.solution[pos[0], pos[1]]
		print(pos, px)
		return px[0] < 10

	def resetRemotes(self):
		self.nAns = 0
		for r in self.remotes:
			self.remotes[r].reset()

	def printStatus(self):
		print("Current Scores:")
		for r in self.remotes:
			score = self.remotes[r]
			name = r.getParams()["name"]
			print(name + ":", score.score)

class Score(object):
	def __init__(self):
		super(Score, self).__init__()
		self.score = 0
		self.result = WAITING

	def reset(self):
		self.result = WAITING

	def update(self, score, result):
		if self.result != WAITING:
			return
		self.score += score
		self.result = result
