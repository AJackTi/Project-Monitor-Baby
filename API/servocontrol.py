import RPi.GPIO as GPIO
import time


def main(minutes, pin_number):
    timeout = time.time() + 60*int(minutes)
    frequency_hertz = 50
    pwm = GPIO.PWM(pin_number, frequency_hertz)
    left_position = 0.40
    right_position = 2.5
    middle_position = (right_position - left_position) / 2 + left_position
    positionList = [left_position, middle_position,
                    right_position, middle_position]
    ms_per_cycle = 1000 / frequency_hertz
    while True:
        test = 0
        for i in range(3):
            for position in positionList:
                duty_cycle_percentage = position * 100 / ms_per_cycle
                pwm.start(duty_cycle_percentage)
                time.sleep(.5)
                if time.time() > timeout:
                    break
                test = test - 1
    

if __name__ == '__main__':
    main(10)
