import PixelKit as kit
from random import randint as random
from time import sleep

t = 0
colors = [
    [0, 0, 2],
    [10, 10, 10],
    [10, 0, 0],
    [10, 10, 0],
    [10, 0, 10]
]

class Bullet():
    def __init__(self, position=[4, 4], vector=[-1,1]):
        self.position = position
        self.vector = vector
        self.life = 0

    def getX(self):
        return self.position[0]

    def getY(self):
        return self.position[1]

    def move(self):
        self.position[0] += self.vector[0]
        self.position[1] += self.vector[1]
        self.position[0] %= 16
        self.position[1] %= 8
        self.life += 1

class Ship():
    vectors = [
        [0,-1],
        [1,-1],
        [1,0],
        [1,1],
        [0,1],
        [-1,1],
        [-1,0],
        [-1,-1]
    ]
    sprites = [
        [
            [0, 1, 0],
            [0, 1, 0],
            [2, 3, 2]
        ],
        [
            [0, 0, 1],
            [2, 1, 0],
            [3, 2, 0]
        ],
        [
            [2, 0, 0],
            [3, 1, 1],
            [2, 0, 0]
        ],
        [
            [3, 2, 0],
            [2, 1, 0],
            [0, 0, 1]
        ],
        [
            [2, 3, 2],
            [0, 1, 0],
            [0, 1, 0]
        ],
        [
            [0, 2, 3],
            [0, 1, 2],
            [1, 0, 0]
        ],
        [
            [0, 0, 2],
            [1, 1, 3],
            [0, 0, 2]
        ],
        [
            [1, 0, 0],
            [0, 1, 2],
            [0, 2, 3]
        ]
    ]

    def __init__(self, position=[4, 4], direction=0):
        self.direction = direction
        self.position = position
        self.bullets = []

    def getX(self):
        return self.position[0]

    def getY(self):
        return self.position[1]

    def getSprite(self):
        return self.sprites[self.direction]

    def turnLeft(self):
        self.direction = (self.direction-1)%len(self.sprites)

    def turnRight(self):
        self.direction = (self.direction+1)%len(self.sprites)

    def getVector(self):
        return self.vectors[self.direction]

    def moveForward(self):
        vector = self.getVector()
        self.position[0] += vector[0]
        self.position[1] += vector[1]
        self.position[0] %= 16
        self.position[1] %= 8

    def fire(self):
        if len(self.bullets) < 3:
            self.bullets.append(Bullet(list(self.position), self.getVector()))


enemies = [Ship([random(0,15),random(0,7)], random(0, 8))]
mainShip = Ship()
kit.onJoystickLeft = mainShip.turnLeft
kit.onJoystickRight = mainShip.turnRight
kit.onJoystickUp = mainShip.moveForward
kit.onButtonA = mainShip.moveForward
kit.onJoystickClick = mainShip.fire
kit.onButtonB = mainShip.fire

def renderMainShip():
    for y, row in enumerate(mainShip.getSprite()):
        for x, c in enumerate(row):
            kit.setPixel((mainShip.getX()+x-1)%16, (mainShip.getY()+y-1)%8, colors[c])

def renderEnemies():
    for enemy in enemies:
        if t % 96 == 0:
            enemy.turnRight()
        elif t % 48 == 0:
            enemy.turnLeft()
        if t % 24 == 0:
            enemy.moveForward()
        for y, row in enumerate(enemy.getSprite()):
            for x, c in enumerate(row):
                if c != 0:
                    kit.setPixel((enemy.getX()+x-1)%16, (enemy.getY()+y-1)%8, colors[(c+2)%len(colors)])

def renderMainShipBullets():
    for i, bullet in enumerate(mainShip.bullets):
        if t % 2 == 0:
            bullet.move()
            if bullet.life > 20:
                del mainShip.bullets[i]
            else:
                for j, enemy in enumerate(enemies):
                    if enemy.getX() == bullet.getX() and enemy.getY() == bullet.getY():
                        del enemies[j]
                        del mainShip.bullets[i]
        kit.setPixel(bullet.getX(), bullet.getY(), colors[4])

def loop():
    kit.setBackground(colors[0])
    renderMainShipBullets()
    if t % 200 == 0:
        enemies.append(Ship([random(0,15),random(0,7)], random(0, 8)))
    renderMainShip()
    renderEnemies()

def start():
    global t
    while True:
        t += 1
        kit.checkControls()
        loop()
        kit.render()
        sleep(0.001)
