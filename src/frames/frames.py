import sensor, image

class Frames:

    def __init__(self):
        self.img = None

    def top(self):
        if self.img:
            return sensor.snapshot
        else:
            # TODO: write exception
            pass

    img = sensor.snapshot()