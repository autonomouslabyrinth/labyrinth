import time
import wiringpi

#use GPIO naming
wiringpi.wiringPiSetupGpio()

# set 18 to be PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set PWM mode to ms type
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

FORWARD = 100
BACKWARD = 200
STOP = 2000

for i in range(1,2):
    for count in range(100):
        wiringpi.pwmWrite(18, FORWARD) 
        time.sleep(delay_period)
    for count in range(100):
        wiringpi.pwmWrite(18, BACKWARD) 
        time.sleep(delay_period)
wiringpi.pwmWrite(18, STOP)
