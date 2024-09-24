from machine import Pin, Timer
from picozero import Speaker

import time
speaker = Speaker(17)
buttonC = Pin(15, Pin.IN, Pin.PULL_DOWN)
buttonD = Pin(14, Pin.IN, Pin.PULL_DOWN)
buttonE = Pin(13, Pin.IN, Pin.PULL_DOWN)

while(True):
    if(buttonC.value()):
        speaker.play('c4', 0.5)
    if(buttonD.value()):
        speaker.play('d4', 0.5)
    if(buttonE.value()):
        speaker.play('e4', 0.5)

