import sys, serial, struct

class Camera:

    def __init__(self):
        self.port = '/dev/ttypACM0'
        self.sp = Serial(port, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                         xonxoff=False, rtscts=False, stopbits=serial.STOPBITS_ONE, timeout=None, dsrdtr=True)

    def data(self):
        # Receive
        size = 3
        return self.sp.read(size)
