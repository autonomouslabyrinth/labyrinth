# Single Color RGB565 Blob Tracking Example
#
# This example shows off single color RGB565 tracking using the OpenMV Cam.

import sensor, image, time, math

threshold_index = 0 # 0 for red, 1 for green, 2 for blue

# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
# The below thresholds track in general red/green/blue things. You may wish to tune them...
thresholds =  [(20, 85, 25, 100, -45, 40)] #[(-20, 20, -20, 20, -20, 20)] # [(30, 100, 15, 127, 15, 127), # generic_red_thresholds
              #(30, 100, -64, -8, -32, 32), # generic_green_thresholds
             #(0, 30, 0, 64, -128, 0)] # generic_blue_thresholds

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

# Only blobs that with more pixels than "pixel_threshold" and more area than "area_threshold" are
# returned by "find_blobs" below. Change "pixels_threshold" and "area_threshold" if you change the
# camera resolution. "merge=True" merges all overlapping blobs in the image.

while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs([thresholds[threshold_index]], pixels_threshold=25, area_threshold=25, merge=True):

        # Filter non-circle blobs
        if blob.roundness() > 0.6:

            # Draw red circle around ball
            x = blob.cx()
            y = blob.cy()
            radius = 9
            img.draw_circle(x, y, radius, color = (255, 0, 0), thickness = 4, fill = False)

    print(clock.fps())



# Circle Drawing
#
# This example shows off drawing circles on the OpenMV Cam.

while(True):
    clock.tick()

    img = sensor.snapshot()

    for i in range(10):
        x = (pyb.rng() % (2*img.width())) - (img.width()//2)
        y = (pyb.rng() % (2*img.height())) - (img.height()//2)
        radius = pyb.rng() % (max(img.height(), img.width())//2)

        r = (pyb.rng() % 127) + 128
        g = (pyb.rng() % 127) + 128
        b = (pyb.rng() % 127) + 128

        # If the first argument is a scaler then this method expects
        # to see x, y, and radius. Otherwise, it expects a (x,y,radius) tuple.
        img.draw_circle(x, y, radius, color = (r, g, b), thickness = 2, fill = False)

    print(clock.fps())
