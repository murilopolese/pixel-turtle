# The next lines will make the Pixel Turtle and its heading invisible
# and will clear the screen for light show
hidePixel()
hideHeading()
clear()

# Those are the colors for the light show
colors = [red, yellow, green, cyan, blue, purple, white, black]

# For each color we will make the Pixel Turtle draw a spyral
for color in colors:
    # First we move to the top left corner but one pixel outside the screen
    # just to make the math easier.
    moveTo(-1, 0)
    setColor(color)
    for i in range(0, 4):
        right(2)
        forward(16-(2*i))
        right(2)
        forward(7-(2*i))
        right(2)
        forward(15-(2*i))
        right(2)
        forward(6-(2*i))

# Move back to the center of the screen
moveTo(8, 4)
# Set the Pixel Turtle color back to its original green
setColor(green)
# Make both the Pixel Turtle and its heading visible again
showPixel()
showHeading()
