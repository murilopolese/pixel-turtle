import PixelKit as kit

# This calculates the points on a line between the coordinates `x0`, `y0` and
# `x1`, `y1`.
def bresenham(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x1 + x*xx + y*yx, y1 + x*xy + y*yy
        if D > 0:
            y += 1
            D -= dx
        D += dy

def line(x1, y1, x2, y2, color):
    for pixel in bresenham(x1, y1, x2, y2):
        kit.setPixel(pixel[0], pixel[1], color)
    kit.render()

kit.clear()
line(2, 2, 5, 5, [10, 0, 0])
