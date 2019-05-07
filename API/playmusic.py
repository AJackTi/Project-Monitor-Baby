import pygame
import time


def main(soundName, minutes):
    timeout = time.time() + 60*minutes
    while True:
        test = 0
        pygame.mixer.init()
        pygame.mixer.music.load(soundName)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            if time.time() > timeout:
                break
            test = test - 1
            continue


if __name__ == "__main__":
    main("1.mp3")
