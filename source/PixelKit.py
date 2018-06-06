from machine import Pin, ADC
from neopixel import NeoPixel

# Hardware information:
# Pin numbers for each hardware connected to the PixelKit ESP32
NEOPIXEL_PIN = 4
SIZE = 128 # Amount of leds
WIDTH = 16 # Number of columns
HEIGHT = 8 # Number of lines
DIAL_PIN = 36
JOYSTICK_UP_PIN = 35
JOYSTICK_DOWN_PIN = 34
JOYSTICK_LEFT_PIN = 26
JOYSTICK_RIGHT_PIN = 25
JOYSTICK_CLICK_PIN = 27
BUTTON_B_PIN = 18
BUTTON_A_PIN = 23
BUTTON_NONE_PIN = 5 # dunno what is this

# Hardware instances
# Objects representing the available hardware on the PixelKit
neopixel_pin = Pin(NEOPIXEL_PIN, Pin.OUT)
np = NeoPixel(neopixel_pin, SIZE)
np.timing = 1 # This will set the neopixel frequency correctly
joystickUp = Pin(JOYSTICK_UP_PIN, Pin.IN)
joystickDown = Pin(JOYSTICK_DOWN_PIN, Pin.IN)
joystickLeft = Pin(JOYSTICK_LEFT_PIN, Pin.IN)
joystickRight = Pin(JOYSTICK_RIGHT_PIN, Pin.IN)
joystickClick = Pin(JOYSTICK_CLICK_PIN, Pin.IN)
buttonA = Pin(BUTTON_A_PIN, Pin.IN)
buttonB = Pin(BUTTON_B_PIN, Pin.IN)
buttonNone = Pin(BUTTON_NONE_PIN, Pin.IN)
dial = ADC(Pin(DIAL_PIN))
dial.atten(ADC.ATTN_11DB)

# Hardware values
# Values based on the available hardware
dialValue = dial.read()
isPressingUp = False
isPressingDown = False
isPressingLeft = False
isPressingRight = False
isPressingClick = False
isPressingA = False
isPressingB = False

# Group all the other functions to check the hardware
def checkControls():
    checkJoystick()
    checkButtons()
    checkDial()

# Checks the joystick, "debounce" the presses and calls the
# function related to which joystick button was pressed
def checkJoystick():
    global isPressingUp
    global isPressingDown
    global isPressingLeft
    global isPressingRight
    global isPressingClick
    if joystickUp.value() == 0 and not isPressingUp:
        isPressingUp = True
        onJoystickUp()
    if joystickUp.value() != 0 and isPressingUp:
        isPressingUp = False

    if joystickDown.value() == 0 and not isPressingDown:
        isPressingDown = True
        onJoystickDown()
    if joystickDown.value() != 0 and isPressingDown:
        isPressingDown = False

    if joystickLeft.value() == 0 and not isPressingLeft:
        isPressingLeft = True
        onJoystickLeft()
    if joystickLeft.value() != 0 and isPressingLeft:
        isPressingLeft = False

    if joystickRight.value() == 0 and not isPressingRight:
        isPressingRight = True
        onJoystickRight()
    if joystickRight.value() != 0 and isPressingRight:
        isPressingRight = False

    if joystickClick.value() == 0 and not isPressingClick:
        isPressingClick = True
        onJoystickClick()
    if joystickClick.value() != 0 and isPressingClick:
        isPressingClick = False

# Checks the buttons, "debounce" the presses and calls the
# function related to which button was pressed
def checkButtons():
    global isPressingA
    global isPressingB
    if buttonA.value() == 0 and not isPressingA:
        isPressingA = True
        onButtonA()
    if buttonA.value() != 0 and isPressingA:
        isPressingA = False
    if buttonB.value() == 0 and not isPressingB:
        isPressingB = True
        onButtonB()
    if buttonB.value() != 0 and isPressingB:
        isPressingB = False

# Checks the dial value and only set the hardware value and call the
# function related with the dial if the new value is different from the previous
def checkDial():
    global dialValue
    newValue = dial.read()
    if newValue != dialValue:
        dialValue = dial.read()
        onDial(dialValue)

# Called when those hardware change values
def onJoystickUp():
    return False
def onJoystickDown():
    return False
def onJoystickLeft():
    return False
def onJoystickRight():
    return False
def onJoystickClick():
    return False
def onButtonA():
    return False
def onButtonB():
    return False
def onDial(dialValue):
    return False

# NeoPixel values are stored in a unidimensional array so to get `x` and `y`
# coordinates it's needed some math to break the values into rows
def getIndexFromCoordinate(x, y):
    return ((y) * WIDTH) + (x)

# Set a pixel `color` on coordinates `x` and `y`. This will only set the value
# on the "buffer" (`np`) and won't light any LED by itself. This operation is
# as fast as setting a value to an array
def setPixel(x, y, color=[0, 10, 0]):
    index = getIndexFromCoordinate(x, y)
    np[index] = color

# Set the entire screen to a given color. This will only set the value on the
# "buffer" (`np`) and won't light any LED by itself. This operation is as fast
# as setting a value to an array
def setBackground(color=[10,10,0]):
    np.fill(color)

# `setBackground` to black color (turn all the LED off)
def clear():
    setBackground([0, 0, 0])

# Send the "buffer" (`np`) values to the hardware. This operation is slower
# since it requires to send the information to the actual hardware and should be
# called as little as possible.
def render():
    np.write()
