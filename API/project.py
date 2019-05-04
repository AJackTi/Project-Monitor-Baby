#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from db import *
import servocontrol
from threading import Thread
import playmusic
import datetime
import motiontrack

# region Init
camera = Camera()
music = Music()
deviceRas = DeviceRas()
sensorMotion = SensorMotion()
channelSoundSensor = 11  # Assign pin 17 to sound sensor
channelMotionSensor = 8  # Assign pin 8 to PIR (motion sensor)
channelLed = 10  # Assign pin 10 to LED
countSound = 0
# countCamera = 0
# endregion

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # Set GPIO to pin numbering
GPIO.setup(channelSoundSensor, GPIO.IN)
GPIO.setup(channelMotionSensor, GPIO.IN)  # Setup GPIO pin PIR as input
GPIO.setup(channelLed, GPIO.OUT)  # Setup GPIO pin for LED as output

time.sleep(4)  # Give sensor time to startup


def callback(channelSoundSensor):
    if GPIO.input(channelSoundSensor):
        #print "Sound Detected!"
        global countSound
        countSound += 1
        return True


# let us know when the pin goes HIGH or LOW
#GPIO.add_event_detect(channelSoundSensor, GPIO.BOTH, bouncetime=1000)
# assign function to GPIO PIN, Run function on change
#GPIO.add_event_callback(channelSoundSensor, callback)


def SavingData(countSound, countMotion, countCamera, minutes):
    print 'Saving Data To DB ' + '*'*50
    SensorMotion().insertSpecificDataSensorMotion(None, str(datetime.datetime.now() - datetime.timedelta(minutes=minutes)), str(datetime.datetime.now()), countMotion)
    SensorSound().insertSpecificSensorSound(None, str(datetime.datetime.now() - datetime.timedelta(minutes=minutes)), str(datetime.datetime.now()), countSound)
    Camera().insertSpecificDataCamera(None, str(datetime.datetime.now() - datetime.timedelta(minutes=minutes)), str(datetime.datetime.now()), '_', countCamera)


def Process(minutes=1):
    timeout = time.time() + 60*minutes
    countMotion = 0
    global countSound
    tmp_thread = Thread(target=motiontrack.main, args=[])
    tmp_thread.start()
    countLoop = 1
    try:
        while True:
            if GPIO.input(channelMotionSensor) == True:
                countMotion += 1

            try:
                time.sleep(1)
                GPIO.add_event_detect(channelSoundSensor, GPIO.BOTH, bouncetime=300)
                # GPIO.remove_event_callback(channelSoundSensor)
                GPIO.add_event_callback(channelSoundSensor, callback)
            except:
                pass

            print 'countMotion: ' + str(countMotion)
            print 'countSound: ' + str(countSound)
            print 'countCamera: ' + str(motiontrack.countCamera)
            # subCountSound = countSound
            # Reset after turn on music
            # if :
            #     countSound = 0
            # print timeout
            # print time.time()
            if (time.time() > timeout and time.time() < timeout*(minutes+1)):
                timeout = time.time() + 60*minutes
                if countMotion == 0 and countSound == 0:
                    continue

                elif ((countMotion >= 50 and countMotion <= 100) or (countSound <= 80 and countSound >= 40)) or (motiontrack.countCamera <= 120 and motiontrack.countCamera >= 80):
                    Thread(target=playMusic, args=[minutes]).start()
                    Thread(target=servoControl, args=[minutes]).start()
                    SavingData(countSound, countMotion, motiontrack.countCamera, minutes)
                    countMotion = 0
                    countSound = 0
                    motiontrack.countCamera = 0

                elif ((countMotion >= 100 and countMotion <= 150) or (countSound <= 120 and countSound >= 80)) or (motiontrack.countCamera <= 150 and motiontrack.countCamera >= 120):
                    minutes = 2
                    Thread(target=playMusic, args=[minutes]).start()
                    Thread(target=servoControl, args=[minutes]).start()
                    SavingData(countSound, countMotion, motiontrack.countCamera, minutes)
                    countMotion = 0
                    countSound = 0
                    motiontrack.countCamera = 0

                else:
                    minutes = 3
                    # Alert to parent
                    Thread(target=playMusic, args=[3]).start()
                    Thread(target=servoControl, args=[3]).start()
                    SavingData(countSound, countMotion, motiontrack.countCamera, minutes, minutes)
                    countMotion = 0
                    countSound = 0
                    motiontrack.countCamera = 0
                
            time.sleep(1)

    except KeyboardInterrupt:  # Ctrl+c
        camera.dispose()
        music.dispose()
        deviceRas.dispose()
        sensorMotion.dispose()
        pass  # Do nothing, continue to finally

    # finally:
        # GPIO.cleanup()  # reset all GPIO


def playMusic(minutes):
    playmusic.main("1.mp3", minutes)


def servoControl(minutes):
    servocontrol.main(minutes)


if __name__ == '__main__':
    minutes = 2
    main = Thread(target=Process, args=[minutes])
    main.start()
