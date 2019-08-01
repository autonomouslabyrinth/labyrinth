from board.board import Lines


class Ball:

	def __init__(self, cam_data):
		# Pink
		self.x = 0
		self.y = 0
		self.update(cam_data)

	def update(self, cam_data):
		self.x = cam_data.x
		self.y = cam_data.y

	def online(self, lines):
		# Returns True or False
		pass

	def finished(self):
		# Returns True or False
		pass
