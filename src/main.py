from board.board import Board
from camera.camera import Camera
from ball.ball import Ball
from servo.servo import Servos


def run():
    # Initialize objects
    cam = Camera()
    print(cam.data())
"""
    bal = Ball(cam.data())
    brd = Board(cam.data())
    srvs = Servos()      # TODO: pass in param to initializer

    # Loop until finished
    while not bal.finished():

        # Determine waypoint
        if bal.online(brd.lines()):
            pnt = brd.nearest_corner()
        else:
            pnt = brd.nearest_point() # Snap to line

        # Move servos
        srvs.move(bal, pnt)

        # Update
        bal.update(cam.data())
"""

if __name__ == "__main__":
    run()
