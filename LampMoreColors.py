#Program asks for user input to determine color to shine.

import time, sys
import RPi.GPIO as GPIO
from updateSheets import *
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

redPin = 18  #Set to appropriate GPIO
greenPin = 23 #Should be set in the 
bluePin = 24  #GPIO.BOARD format
button = 16#
onButton = 4
NUMCOLORS = 10

lampOn = True;

GPIO.setup(button,GPIO.IN)
GPIO.setup(onButton,GPIO.IN)
hz = 100
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

red = GPIO.PWM (redPin, hz)
green = GPIO.PWM (greenPin, hz)
blue = GPIO.PWM (bluePin, hz)


def blink(rVal, gVal, bVal):
    GPIO.setmode(GPIO.BCM)
    red.start((rVal/2.55))#
    green.start((gVal/2.55))
    blue.start((bVal/2.55))
    
    
def turnOff():
    GPIO.setmode(GPIO.BCM)
    red.start(0)#
    green.start(0)
    blue.start(0)
    
def redOn():
    blink(255,0,0)

def greenOn():
    blink(0,255,0)

def blueOn():
    blink(0,0,255)
    
def orangeOn():
    blink (255,120,0)
    
def yellowOn():
    blink(255,255,0)

def cyanOn():
    blink(0,255,255)

def magentaOn():
    blink(255,0,255)
    
def purpleOn():
    blink(100,0,255)
    
def pinkOn():
    blink (255,40,150)

def whiteOn():
    blink(255,255,255)

def whiteOff():
    turnOff()
    
        
def checkLightColour(counter):
     sheetColour = getSheetColour()
     if sheetColour != counter:
        print (":)")
        changeLightColour(int(sheetColour))
        return int(sheetColour)
    
def changeLightColour(pos):
    whiteOff()
    if pos == 1:
        redOn()
    elif pos == 2:
        orangeOn()
    elif pos == 3:
        yellowOn()
    elif pos == 4:
        greenOn()
    elif pos == 5:
        cyanOn()
    elif pos == 6:
        blueOn()
    elif pos == 7:
        purpleOn()
    elif pos == 8:
        magentaOn()
    elif pos == 9:
        pinkOn()
    elif pos == 10:
        whiteOn()
  
requestTime = 500000;
def main():
    GPIO.setwarnings(False)
    whiteOff()
    counter = 1;
    timer = 0;
    blink (100,100,0)
    print ("blinked")
    while True:
        timer += 1

        if (GPIO.input(button) == True):
            print ("button pressed")
            whiteOff()
            counter += 1
            if (counter > NUMCOLORS):
                counter = 1
            changeLightColour(counter)
            updateSheetColour(counter)
            print (counter)
            time.sleep(0.5)

        if (timer == requestTime):
            timer = 0
            print("yes")
            counter = checkLightColour(counter)
        
        if (GPIO.input(onButton) == True):
            whiteOff()
            print("light opff")
            time.sleep(0.5)
            while (True):
                if (GPIO.input(onButton) == True):
                    break
            time.sleep(0.5)
            print("light on")
            changeLightColour(counter)
                

            
main()


