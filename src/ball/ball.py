class Ball:
	""" 
	X and Y origin defined as bottom left.
	X velocity follows x-axis.
	Y velocity follows y-axis.	
	Velocity can be negative.
	"""
	def __init__(self):
		self.x = 0
		self.y = 0 
		self.x_velocity = 0 
		self.y_velocity = 0
