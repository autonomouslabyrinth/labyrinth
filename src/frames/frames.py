import sensor, image

class Frames:

    def __init__(self):
        self.img = None

    def top(self):
        self.img = sensor.snapshot()
        return self.img
