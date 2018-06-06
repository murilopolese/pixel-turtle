# Pixel Kit API Documentation

## Pixel Turtle Library

- `forward(n)` or `f(n)`: Move forward `n` steps. Steps can be negative numbers.
- `backward(n)` or `b(n)`: Move backwards `n` steps. Steps can be negative numbers.
- `left(n)` or `l(n)`: Turn left `n` steps. Steps can be negative numbers.
- `right(n)` or `r(n)`: Turn right `n` steps. Steps can be negative numbers.
- `penUp()` or `pu()`: Stop leaving a trail when pixel turtle moves
- `penDown()` or `pd()`: Make a trail when pixel turtle moves
- `clear()` or `c()`: Clear the trails on screen
- `setColor(colour)` or `sc(colour)`: Set pixel colour so it leaves a trail on the set colour. Colours are defined by 3 numbers in the format `[red, green, blue]` representing the amount or `red`, `green` and `blue` in your final colour.
- `setHeadingColor(colour)` or `shc(colour)`: Set pixel heading colour. Heading does not leave a trail. Colours are defined by 3 numbers in the format `[red, green, blue]` representing the amount or `red`, `green` and `blue` in your final colour.
- `move(x, y)` or `m(x, y)`: Teleport your pixel turtle `x` steps on the horizontal and `y` steps on the vertical based on your current pixel turtle positon. The steps can be negative numbers.
- `moveTo(x, y)` or `mt(x, y)`: Teleport your pixel turtle to the column `x` and line `y` of your Pixel Kit. The pixel on the top left corner is the row `0` and column `0`. The numbers grow to the right and down (the pixel on bottom right is row `7` and column `15`).
- `getX()` or `gx()`: Tells you what column your pixel turtle is.
- `getY()` or `gy()`: Tells you what row your pixel turtle is.
- `showHeading()` or `sh()`: Show heading.
- `hideHeading()` or `hh()`: Hide heading.
- `showPixel()` or `sp()`: Show pixel turtle.
- `hidePixel()` or `hp()`: Hide Pixel turtle.

### Examples

```python
# Draw 2 lines with different colours and return to initial position
green = [0, 10, 0]
red = [10, 0, 0]
setColor(green)
forward(2)
left(2)
setColor(red)
forward(2)
right(2)
move(2, -2)
```

```python
# Bouncing Turtle
from time import sleep
playing = True
while playing:
    forward()
    if getY() >= 7 or getY() <= 0:
        left(3)
    sleep(0.1)
```

## Pixel Kit Library

- `dialValue`: Stores the last dial value. This value is always between `0` and `4095`
- `isPressingUp`: Stores if the joystick up is being pressed. This value is `False` or `True`
- `isPressingDown`: Stores if the joystick down is being pressed. This value is `False` or `True`
- `isPressingLeft`: Stores if the joystick left is being pressed. This value is `False` or `True`
- `isPressingRight`: Stores if the joystick right is being pressed. This value is `False` or `True`
- `isPressingClick`: Stores if the joystick click is being pressed. This value is `False` or `True`
- `isPressingA`: Stores if the button A is being pressed. This value is `False` or `True`
- `isPressingB`: Stores if the button B is being pressed. This value is `False` or `True`
- `checkControls()`: Update all button flags and dial value
- `checkJoystick()`: Update only joystick buttons flags
- `checkButtons()`: Update only buttons flags
- `checkDial()`: Update only dial value
- `onJoystickUp()`: Called when joystick up is pressed
- `onJoystickDown()`: Called when joystick down is pressed
- `onJoystickLeft()`: Called when joystick left is pressed
- `onJoystickRight()`: Called when joystick right is pressed
- `onJoystickClick()`: Called when joystick click is pressed
- `onButtonA()`: Called when button A is pressed
- `onButtonB()`: Called when button B is pressed
- `onDial(dialValue)`: Called when dial value has changed
- `setPixel(x, y, colour)`: Set the pixel on `x`, `y` with the `colour` in the format `[red, green, blue]` where `red`, `green` and `blue` are the amount of those colours you want in your final colour. Values can be between `0` and `100` but after `20` you might need eye protection.
- `setBackground(colour)`: Set background to `colour`
- `clear()`: Set background to black (turn off all LEDs)
- `render()`: Render the pixels on the screen. Previous drawing methods won't change the LEDs until `render()` is called.

### Examples

```python
# Changing background on button click
import PixelKit as kit
from time import sleep
green = [0, 10, 0]
yellow = [10, 10, 0]
while True:
    kit.checkControls()
    if kit.isPressingClick:
        kit.setBackground(green)
    else:
        kit.setBackground(yellow)
    kit.render()
    sleep(0.2)
```

```python
# Same thing but different
import PixelKit as kit
from time import sleep
green = [0, 10, 0]
yellow = [10, 10, 0]

def handleButtonA():
    kit.setBackground(green)
    kit.render()
def handleButtonB():
    kit.setBackground(yellow)
    kit.render()

kit.onButtonA = handleButtonA
kit.onButtonB = handleButtonB

while True:
    kit.checkControls()
    sleep(0.2)
```
