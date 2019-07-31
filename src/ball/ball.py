import sensor


class Ball:

	def __init__(self):
		# Pink
		self.thresholds = [(20, 85, 25, 100, -45, 40)]
		self.x = 0
		self.y = 0

	def update(self, img):
		# Tracking using the OpenMV Cam.
		sensor.reset()
		sensor.set_pixformat(sensor.RGB565)
		sensor.set_framesize(sensor.QVGA)
		sensor.skip_frames(time=2000)
		sensor.set_auto_gain(False)  # must be turned off for color tracking
		sensor.set_auto_whitebal(False)  # must be turned off for color tracking

		for blob in img.find_blobs(self.thresholds, pixels_threshold=25, area_threshold=25, merge=True):

			# Filter non-circle blobs
			if blob.roundness() > 0.6:
				# Draw red circle around ball
				x = blob.cx()
				y = blob.cy()
				radius = 9
				img.draw_circle(x, y, radius, color=(255, 0, 0), thickness=4, fill=False)
