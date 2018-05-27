#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @file: CursorPointer.py
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

import Pointer


class CursorPointer(Pointer.Pointer):

	def __init__(self):
		super(CursorPointer, self).__init__()
		self.posX = 0
		self.posY = 0
		self.offX = 10
		self.offY = 10
		self.radius = 10

	def _draw(self):
		up_left = [self.posX-self.radius, self.posY-self.radius]
		lower_right = [self.posX+self.radius, self.posY+self.radius]
		return self.canvas.create_oval(up_left, lower_right, fill='orange')

	def update(self, pos):
		self._update(pos)
