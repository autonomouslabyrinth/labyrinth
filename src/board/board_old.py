import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from skimage.feature import canny
from skimage.util import img_as_ubyte
from skimage.color import rgb2gray
from skimage.transform import hough_circle, hough_circle_peaks

class Board:
	def __init__(self, path, filename):
		image_path = os.path.join(path, filename)
		color_image = io.imread(image_path)
		gray_image = rgb2gray(color_image)
		self.image = img_as_ubyte(gray_image)

	def detect_circles(self):
		self.circles = []
		c = Circle(0, 0, 0)
		
		# hough circles
		edges = canny(self.image)  # TODO: thresholds might need to be changed for video feed hysteris
		radii = np.arange(1000, 1100)
		hough_circles = hough_circle(edges, radii)
		
		# count
		count = 0
		for twodim in hough_circles:
			for row in twodim:
				for elem in row:
					if elem != 0:
						count += 1
		print("COUNT = " + str(count))

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

 
