# The next lines will make the Pixel Turtle and its heading invisible
# and will clear the screen for light show
hidePixel()
hideHeading()
clear()

# Those are the colors for the light show
colors = [white, red, yellow, green, cyan, blue, purple, white]

# First we move to the top left corner
moveTo(0, 0)

# For each color we will make the Pixel Turtle make a stripe of that color
for color in colors:
    setColor(color)

    # Walk 7 steps backward (since Pixel Turtle is facing up)
    backward(7)
    # Side step to the right
    move(1, 0)
    # Walk 7 steps forward
    forward(7)
    # Side step to the right
    move(1, 0)

# Move back to the center of the screen
moveTo(8, 4)
# Set the Pixel Turtle color back to its original green
setColor(green)
# Make both the Pixel Turtle and its heading visible again
showPixel()
showHeading()
