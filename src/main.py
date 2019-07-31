from board.board import Board
from frames.frames import Frames
from ball.ball import Ball
from servo.servo import Servos


def run():
    # Initialize objects
    frms = Frames()
    brd = Board(frms.top())
    bal = Ball(frms.top())
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
        bal.update(frms.top())


if __name__ == "__main__":
    run()
