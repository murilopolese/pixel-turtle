# The next lines will make the Pixel Turtle and its heading invisible
# and will clear the screen for light show
hidePixel()
hideHeading()
clear()

# First we move to the top left corner
moveTo(0, 0)
right(2)

for i in range(0, 8):
    for j in range(0, 15):
        if j % 2 == 0:
            setColor(red)
        else:
            setColor(cyan)
        forward()
    if i % 2 == 0:
        right(2)
        forward()
        right(2)
    else:
        left(2)
        forward()
        left(2)

# Move back to the center of the screen
moveTo(8, 4)
# Set the Pixel Turtle color back to its original green
setColor(green)
# Make both the Pixel Turtle and its heading visible again
showPixel()
showHeading()
