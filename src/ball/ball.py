import sensor
from board.board import Lines


class Ball:

	def __init__(self, img):
		# Pink
		self.thresholds = [(20, 85, 25, 100, -45, 40)]
		self.x = 0
		self.y = 0

		# Tracking using the OpenMV Cam.
		sensor.reset()
		sensor.set_pixformat(sensor.RGB565)
		sensor.set_framesize(sensor.QVGA)
		sensor.skip_frames(time=2000)
		sensor.set_auto_gain(False)  # must be turned off for color tracking
		sensor.set_auto_whitebal(False)  # must be turned off for color tracking
		self.update(img)

	def update(self, img):
		for blob in img.find_blobs(self.thresholds, pixels_threshold=25, area_threshold=25, merge=True):
			# Filter non-circle blobs
			if blob.roundness() > 0.6:
				self.x = blob.cx()
				self.y = blob.cy()
				# Draw red circle around ball
				# radius = 9
				# img.draw_circle(x, y, radius, color=(255, 0, 0), thickness=4, fill=False)

	def online(self, lines):
		# Returns True or False
		pass

	def finished(self):
		# Returns True or False
		pass
