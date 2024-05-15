import RPi.GPIO as GPIO
from lucy import settings
class Indicator:
# Pin configuration
    def __init__(self):
        self.pin=settings.LED_PIN
        GPIO.setmode(GPIO.BCM)  # Use BCM numbering
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.cleanup()
    def turn_on(self):
       GPIO.output(self.pin, GPIO.HIGH)
    def turn_of(self):
       GPIO.output(self.pin, GPIO.LOW)
       GPIO.cleanup()


# Clean up GPIO

