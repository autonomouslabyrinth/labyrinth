import os
from skimage import io

class Board:
	def __init__(self, path, filename):
		image_path = os.path.join(path, filename)
		self.image = io.imread(image_path)

	def detect_circles(self):
		self.circles = []
		c = Circle(4, 4, 3)
		self.circles.append(c)

	def print_circles(self):
		for circle in self.circles:
			print(circle)

class Circle:
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r

	def update_circle(self, x, y, r):
		pass

 
