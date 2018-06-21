import PixelKit as kit
from time import sleep

colors = [black, red, yellow, green, cyan, blue, purple]
color = 3
setColor(colors[color])

def changeColor():
    global color
    color = (color + 1) % len(colors)
    setColor(colors[color])

kit.onJoystickUp = forward
kit.onJoystickDown = backward
kit.onJoystickLeft = left
kit.onJoystickRight = right
kit.onJoystickClick = changeColor
kit.onButtonA = penDown
kit.onButtonB = penUp

while True:
    kit.checkControls()
    sleep(0.2)
