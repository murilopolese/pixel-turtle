import PixelKit as kit
from time import sleep

black = [0, 0, 0]
red = [10, 0, 0]
green = [0, 10, 0]
blue = [0, 0, 10]
yellow = [10, 10, 0]
cyan = [0, 10, 10]
purple = [10, 0, 10]

colors = [black, red, yellow, green, cyan, blue, purple]
color = 1
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
