#!/usr/bin/env python
import RPi.GPIO as GPIO
import pygame
import random
import time
import os
import urllib2, base64

os.system("amixer set PCM 100%")

def makeAuthorizedRequest(url, username, password):
	request = urllib2.Request(url)
	base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)
	result = urllib2.urlopen(request)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

username = "admin"
password = "admin"
apiAddress = 'http://10.0.0.1/'
urlon1 = '{0}api/callAction?deviceID=33&name=startProgram&arg1=5'.format(apiAddress)
urlon2 = '{0}api/callAction?deviceID=82&name=startProgram&arg1=5'.format(apiAddress)
urlon3 = '{0}api/callAction?deviceID=5&name=startProgram&arg1=5'.format(apiAddress)
urloff1 = '{0}api/callAction?deviceID=33&name=setColor&arg1=255&arg2=0&arg3=0&arg4=255'.format(apiAddress)
urloff2= '{0}api/callAction?deviceID=82&name=setColor&arg1=0&arg2=0&arg3=255&arg4=0'.format(apiAddress)
urloff3= '{0}api/callAction?deviceID=5&name=setColor&arg1=255&arg2=255&arg3=255&arg4=0'.format(apiAddress)
values = { 'username': username,'password': password }

music_files = []
music_files = [file for file in os.listdir('./sounds/') if os.path.isfile(file) and file.endswith(('.mp3', '.aif', '.wav'))]

pygame.mixer.init()
#preload first sound
pygame.mixer.music.load(music_files[random.randint(0, len(music_files)-1)])

while True:
	try:
		input_state = GPIO.input(18)
		time.sleep(0.001)

		if input_state == False:
			pygame.mixer.music.play()

			print('Button Pressed')

			makeAuthorizedRequest(urlon1, username, password)
			makeAuthorizedRequest(urlon2, username, password)
			makeAuthorizedRequest(urlon3, username, password)

			time.sleep(3)

			makeAuthorizedRequest(urloff1, username, password)
			makeAuthorizedRequest(urloff2, username, password)
			makeAuthorizedRequest(urloff3, username, password)

			#load sound for next button press to avoid lag after clicking button
			pygame.mixer.music.load(music_files[random.randint(0, len(music_files)-1)])
	except Exception:
		pass