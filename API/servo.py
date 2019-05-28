import RPi.GPIO as GPIO
import time

frequency_hertz = 50
GPIO.setmode(GPIO.BOARD)  # Set GPIO to pin numbering
GPIO.setup(3, GPIO.OUT)
pwm = GPIO.PWM(3, frequency_hertz)
left_position = 0.40
right_position = 2.5
middle_position = (right_position - left_position) / 2 + left_position
positionList = [left_position, middle_position, right_position, middle_position]
ms_per_cycle = 1000 / frequency_hertz
while True:
    for i in range(3):
        for position in positionList:
            duty_cycle_percentage = position * 100 / ms_per_cycle
            pwm.start(duty_cycle_percentage)
            time.sleep(.5)