# File Name: ludwig_grant_AS05.py
# File Path: /home/ludwigg/Python/PyRpi_AS5/ludwig_grant_AS05.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS5/ludwig_grant_AS05.py

# Grant Ludwig
# 10/14/2019
# AS.05
# Intro to For Loops

# Import Libraries
import RPi.GPIO as GPIO # Raspberry Pi GPIO library
import time # Time library

lightOn = False
#hzList = [0, 0.5, 1, 5, 10]
waitTime = [0, 2, 1, 0.2, 0.1]
waitIndex = 0

# Setup GPIO
GPIO.setwarnings(False) # Ignore warnings
GPIO.setmode(GPIO.BCM) # Use BCM Pin numbering
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW) # Set Pin 4 to be an output pin and set initial value to low (off)
GPIO.setup(16, GPIO.IN)
GPIO.setup(13, GPIO.IN)

# Define Callback Functions
def buttonOne_callback(channel): 
	global lightOn
	global waitIndex
	print ("Button One Falling Edge") # debugging
	lightOn = not lightOn
	if not lightOn:
		waitIndex = 0

def buttonTwo_callback(channel):
	global lightOn
	global waitIndex
	print ("Button Two Falling Edge") # debugging
	if lightOn:
		waitIndex += 1
		if waitIndex >= len(waitTime):
			waitIndex = 0
		
# Add event detectors
GPIO.add_event_detect(16, GPIO.FALLING, callback=buttonOne_callback, bouncetime=300)
GPIO.add_event_detect(13, GPIO.FALLING, callback=buttonTwo_callback, bouncetime=300)

try:
# Setup infinite loop
	while(1): 
		if lightOn:
			GPIO.output(4, GPIO.HIGH)
			if waitTime[waitIndex] != 0:
				time.sleep(waitTime[waitIndex])
				GPIO.output(4, GPIO.LOW)
				time.sleep(waitTime[waitIndex])
		else:
			GPIO.output(4, GPIO.LOW)

except KeyboardInterrupt: 
    # This code runs on a Keyboard Interrupt <CNTRL>+C
	print('\n\n' + 'Program exited on a Keyboard Interrupt' + '\n') 

except: 
    # This code runs on any error
	print('\n' + 'Errors occurred causing your program to exit' + '\n')

finally: 
    # This code runs on every exit and sets any used GPIO pins to input mode.
	GPIO.cleanup()