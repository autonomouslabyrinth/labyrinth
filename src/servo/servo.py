import wiringpi
from ball.ball import Ball
from board.board import Point

class Servo:
	FREQUENCY = 192
	RANGE = 2000
	DELAY_PERIOD = 0.01
	FORWARD = 100
	BACKWARD = 200
	STOP = 0

	def __init__(self, pin):
		self.pin = pin
		self.wiring = wiringpi

		self.wiring.wiringPiSetupGpio()
		self.wiring.pinMode(pin, self.wiring.GPIO.PWM_OUTPUT)
		self.wiring.pwmSetMode(self.wiring.GPIO.PWM_MODE_MS)
		self.wiring.pwmSetClock(FREQUENCY)
		self.wiring.pwmSetRange(RANGE)

	def move_forward(self, msecs):
		for count in range(msecs):	
			self.wiring.pwmWrite(self.pin, FORWARD) 

		# TODO: try replacing loop with a self.wiring.pwmWrite(self.pin, FORWARD, msecs) call
		# TODO: check if time.sleep(delay_period) needed in loop
		# TODO: make the same changed to move_backward()

	def move_backward(self, msecs):
		for count in range(msecs):				 
			self.wiring.pwmWrite(self.pin, BACKWARD)


class Servos:

	def __init(self):
		# Initialize horizontal and vertical servo
		self.horizontal = Servo(12)
		self.vertical = Servo(13)
		pass

	def move(self, ball, point):
		# Adjust servos given ball and point
		pass
