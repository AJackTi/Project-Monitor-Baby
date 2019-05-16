#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    if GPIO.input(channel):
        print "Sound Detected!"
        return True


# let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel, callback)

def main():
    # infinite loop
    while True:
            try:
                time.sleep(1)
                GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
                if callback(channel):
                        print "ABCXYZ"
                GPIO.remove_event_callback(channel)
                time.sleep(1)
            except:
                pass
    GPIO.cleanup()

if __name__ == '__main__':
        main()