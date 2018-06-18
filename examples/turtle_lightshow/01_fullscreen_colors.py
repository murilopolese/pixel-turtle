# The next lines will make the Pixel Turtle and its heading invisible
# and will clear the screen for light show
hidePixel()
hideHeading()
clear()

# Those are the colors for the light show (you can add new colors)
colors = [yellow, green, cyan, purple, black]

# For each color we will make the Pixel Turtle walk all the screen
for color in colors:
    # First we move to the top left corner
    moveTo(0, 0)
    # Then we set the color
    setColor(color)

    # We will repeat the following lines 8 times
    for i in range(0, 8):
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
