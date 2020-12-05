#Program asks for user input to determine color to shine.

import time, sys
import RPi.GPIO as GPIO
from updateSheets import *

redPin = 12  #Set to appropriate GPIO
greenPin = 16 #Should be set in the 
bluePin = 18  #GPIO.BOARD format
button = 22#
NUMCOLORS = 7
GPIO.setmode(GPIO.BOARD)

GPIO.setup(button,GPIO.IN)


def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
    
def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def redOn():
    blink(redPin)

def redOff():
    turnOff(redPin)

def greenOn():
    blink(greenPin)

def greenOff():
    turnOff(greenPin)

def blueOn():
    blink(bluePin)

def blueOff():
    turnOff(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOn():
    blink(greenPin)
    blink(bluePin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOn():
    blink(redPin)
    blink(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)
    
        
def checkLightColour(counter):
     sheetColour = getSheetColour()
     if sheetColour != counter:
        print ":)"
        changeLightColour(int(sheetColour))
        return int(sheetColour)
    
def changeLightColour(pos):
    whiteOff()
    if pos == 1:
        redOn()
    elif pos == 2:
        yellowOn()
    elif pos == 3:
        greenOn()
    elif pos == 4:
        cyanOn()
    elif pos == 5:
        blueOn()
    elif pos == 6:
        magentaOn()
    elif pos == 7:
        whiteOn()
  

def main():
    GPIO.setwarnings(False)
    whiteOff()
    counter = 1;
    timer = 0;
    changeLightColour(counter)
    while True:
        timer += 1

        if (GPIO.input(button) == GPIO.HIGH):
            print (counter)
            whiteOff()
            counter += 1
            if (counter >= 8):
                counter = 1
            changeLightColour(counter)
            updateSheetColour(counter)
            print (counter)
            time.sleep(0.25)

        if (timer == 500000):
            timer = 0
            print "yes"
            counter = checkLightColour(counter)

            
main()


