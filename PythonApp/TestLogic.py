#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @file: TestLogic.py
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


from PIL import Image
from DelayedRun import DelayedRun

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
			score = Score()
			self.remotes[r] = score
			self.frame.addUser(r.getParams()["name"], score)


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
		name = event.source.getParams()["name"]
		self.frame.updateUser(name)

		if self.nAns == len(self.remotes):
			self.waitNext()

	def waitNext(self):
		self.frame.setText("Siguiente pregunta:...")
		task = DelayedRun(self.next, 5)
		task.start()

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
		self.frame.updateUsers()

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
