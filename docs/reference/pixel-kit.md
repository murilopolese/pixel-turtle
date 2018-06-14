---
layout: default
---

# Pixel Kit List of Commands

`dialValue`:

Stores the last dial value. This value is always between `0` and `4095`

<hr>

`isPressingUp`:

Stores if the joystick up is being pressed. This value is `False` or `True`

<hr>

`isPressingDown`:

Stores if the joystick down is being pressed. This value is `False` or `True`

<hr>

`isPressingLeft`:

Stores if the joystick left is being pressed. This value is `False` or `True`

<hr>

`isPressingRight`:

Stores if the joystick right is being pressed. This value is `False` or `True`

<hr>

`isPressingClick`:

Stores if the joystick click is being pressed. This value is `False` or `True`

<hr>

`isPressingA`:

Stores if the button A is being pressed. This value is `False` or `True`

<hr>

`isPressingB`:

Stores if the button B is being pressed. This value is `False` or `True`

<hr>

`checkControls()`:

Update all button values and dial value

<hr>

`checkJoystick()`:

Update only joystick buttons values

<hr>

`checkButtons()`:

Update only buttons values

<hr>

`checkDial()`:

Update only dial value

<hr>

`onJoystickUp()`:

Called when joystick up is pressed

<hr>

`onJoystickDown()`:

Called when joystick down is pressed

<hr>

`onJoystickLeft()`:

Called when joystick left is pressed

<hr>

`onJoystickRight()`:

Called when joystick right is pressed

<hr>

`onJoystickClick()`:

Called when joystick click is pressed

<hr>

`onButtonA()`:

Called when button A is pressed

<hr>

`onButtonB()`:

Called when button B is pressed

<hr>

`onDial(dialValue)`:

Called when dial value has changed

<hr>

`setPixel(x, y, color)`:

Set the pixel on `x`, `y` with the `color` in the format `[red, green, blue]` where `red`, `green` and `blue` are the amount of those colors you want in our final color. Values can be between `0` and `100` but after `20` you might need eye protection.

<hr>


`setBackground(color)`:

Set background to `color`

<hr>

`clear()`:

Set background to black (turn off all LEDs)

<hr>

`render()`:

Render the pixels on the screen. Previous drawing methods won't change the LEDs until `render()` is called.
