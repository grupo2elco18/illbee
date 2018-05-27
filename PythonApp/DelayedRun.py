#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @file: DelayedRun.py
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

import time
import threading

class DelayedRun(threading.Thread):
	def __init__(self, target, time):
		super(DelayedRun, self).__init__()
		self.target = target
		self.time = time

	def run(self):
		time.sleep(self.time)
		self.target()
