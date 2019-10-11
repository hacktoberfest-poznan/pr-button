#!/usr/bin/env python3.5
import RPi.GPIO as GPIO
import time

from counter import Counter
from player import Player
from light import Light

LIGHT_PIN = 9
BUTTON_PIN = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = Counter("/home/pi/counter.txt")
player = Player()
light = Light(LIGHT_PIN)
light.turn_off()

prev_input = 0

try:
    while True:
        input = GPIO.input(BUTTON_PIN)
        if ((not prev_input) and input):
            counter.increment()
            light.turn_on()
            player.play_random()
            light.turn_off()
        prev_input = input
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
GPIO.cleanup()
