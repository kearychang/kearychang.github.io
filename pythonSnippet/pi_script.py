import sys # module for handling command-line arguments
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

led = 21
interval = float(sys.argv[1])
interval2 = float(sys.argv[2])
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(led, GPIO.OUT)

def callback_f(led,interval):
  GPIO.output(led, GPIO.HIGH)
  sleep(interval)
  GPIO.output(led, GPIO.LOW)
  sleep(interval2)

while True: # Run forever
  callback_f(led,interval)
