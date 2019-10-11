import RPi.GPIO as GPIO


class Light:
    turned_on = False
    pin_number = None

    def __init__(self, pin_number):
        self.pin_number = pin_number
        GPIO.setup(self.pin_number, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin_number, GPIO.HIGH)
        self.turned_on = True

    def turn_off(self):
        GPIO.output(self.pin_number, GPIO.LOW)
        self.turned_on = False

    def is_turned_on(self):
        return self.turned_on
