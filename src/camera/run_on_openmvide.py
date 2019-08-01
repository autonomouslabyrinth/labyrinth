import sensor, image, time
from pyb import USB_VCP


# Pink
thresholds = [(20, 85, 25, 100, -45, 40)]

# Sensor Initialization
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking

# USB Initialization
usb = USB_VCP()

# Send X,Y
while(True):
    img = sensor.snapshot()
    for blob in img.find_blobs(thresholds, pixels_threshold=25, area_threshold=25, merge=True):

        # Filter non-circle blobs
        if blob.roundness() > 0.6:
            buf = str(blob.cx()) + ' ' + str(blob.cy())
            usb.send(buf)

            # Draw red circle around ball
            # radius = 9
            # img.draw_circle(x, y, radius, color = (255, 0, 0), thickness = 4, fill = False)

    #print(clock.fps())
