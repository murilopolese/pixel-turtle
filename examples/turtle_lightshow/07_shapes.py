def rectangle(width=1, height=1):
    for i in range(0, 2):
        forward(width-1)
        left(2)
        forward(height-1)
        left(2)

def square(size=1):
    rectangle(size)

def circle(size=1):
    for i in range(0, 8):
        forward(size-1)
        left()

# Make sure heading is not on a diagonal
def triangle(size=1):
    forward(size)
    left(3)
    forward(size)
    left(3)
    forward(size)
    left(2)

# Make sure heading is on a diagonal
def triangle2(size=1):
    forward(size)
    left(3)
    forward(size)
    left(2)
    forward(size)
    left(3)

# Make sure heading is not on a diagonal
def fillRectangle(width=1, height=1):
    for i in range(0, width):
        forward(height-1)
        if i == width-1:
            break
        if i % 2 == 0:
            right(2)
            forward()
            right(2)
        else:
            left(2)
            forward()
            left(2)
