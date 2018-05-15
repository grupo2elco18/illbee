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
