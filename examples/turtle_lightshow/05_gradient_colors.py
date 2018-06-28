# The next lines will make the Pixel Turtle and its heading invisible
# and will clear the screen for light show
hidePixel()
hideHeading()
clear()

# First we move to the top left corner
moveTo(0, 0)

for i in range(0, 8):
    color = [12-i, 0, 8+i]
    setColor(color)
    backward(7)
    move(1, 0)
    forward(7)
    move(1, 0)

# Move back to the center of the screen
moveTo(8, 4)
# Set the Pixel Turtle color back to its original green
setColor(green)
# Make both the Pixel Turtle and its heading visible again
showPixel()
showHeading()
