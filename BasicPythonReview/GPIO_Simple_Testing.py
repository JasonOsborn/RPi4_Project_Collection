from gpiozero import LED, Button, Buzzer
from time import sleep
import sys

button1 = Button(2)
ledGreen = LED(25)
buzzer = Buzzer(15)
# mark gpio 25 as an LED named ledgreen

RESET = 0 # Debug
if(RESET):
    ledGreen.off()
    sys.exit()

while True:
    button1.wait_for_press()
    ledGreen.on()
    buzzer.on()
    sleep(1)
    ledGreen.off()
    buzzer.off()

