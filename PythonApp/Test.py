#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @file: Test.py
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


class Test(object):
	def __init__(self, name, desc):
		super(Test, self).__init__()
		self.name = name
		self.desc = desc
		self.questions = []
		self.finised = []
		self.score = 0
		self.fail = 0

	def addQuestion(self, question):
		self.questions.append(question)

	def next(self):
		if len(self.questions) == 0:
			return None

		q = self.questions.pop(0)
		self.finised.append(q)

		self.score = q.score
		self.fail = q.fail
		return q

	def getSuccess(self):
		if self.score == 1:
			return 1

		score = self.score
		self.score = score - 1
		return score

	def getFail(self):
		return self.fail


	def reset(self):
		self.questions = self.finised
		self.finised = []


	def __str__(self):
		s = "<Test: "
		s += self.name
		s += "\n["
		for q in self.questions:
			s+= "\n" + str(q)

		return s + "\n" + "]>"


class Question(object):
	def __init__(self, title, qtype, params):
		super(Question, self).__init__()
		self.title = title
		self.qtype = qtype
		self.params = params
		self.score = 0
		self.fail = 0

	def setScore(self, success, fail):
		self.score = success
		self.fail = fail


	def __str__(self):
		s = "<Question: "
		s += self.title + " ["
		s += str(self.score) + ", "
		s += str(self.fail) + "]>"
		return s
