#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @file: Point.py
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

import math

class Point(object):
	def __init__(self, pos):
		super(Point, self).__init__()
		self.x = pos[0]
		self.y = pos[1]

	def getPos(self):
		return [self.x, self.y]

	def midPoint(self, point):
		mx = self.x + point.x
		my = self.y + point.y
		return Point([mx/2, my/2])

	def dist(self, point):
		dx = self.x - point.x
		dy = self.y - point.y
		return math.sqrt(dx*dx + dy*dy)

	def diff(self, point):
		dx = self.x - point.x
		dy = self.y - point.y
		return Point([dx, dy])

	def angle(self, point):
		diff = self.diff(point)
		return math.atan(diff.y/diff.x)

	def rotate(self, angle):
		newX = self.x*math.cos(angle)-self.y*math.sin(angle)
		newY = self.y*math.cos(angle)+self.x*math.sin(angle)
		self.x = newX
		self.y = newY

	def __str__(self):
		return "<Point: " + str(self.x) + ", " + str(self.y) + ">"
