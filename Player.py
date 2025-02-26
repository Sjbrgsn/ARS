from car import *

ACCELERATION = 0.005
ANGULAR_SPEED = 5.0

RADIAL_ACCELERATION = 0.05

MOVE_SPEED = 3

class Player(Car):
    def __init__(self, ang, rad):
        Car.__init__(self, ang, rad)
        self.speed = 0.5
        self.turnVel = 0
        
        self.score = 0

        self.shakeSound = pygame.mixer.Sound("media/Screenshake.ogg")
        self.shakeSound.set_volume(0.3)
        self.shaking = False

    def update(self, inputManager):
        if(inputManager.moveLeft):
            self.turnVel += RADIAL_ACCELERATION
        elif(inputManager.moveRight):
            self.turnVel -= RADIAL_ACCELERATION
        else:
            self.turnVel -= self.turnVel * 0.05

        if(self.rad < MIN_SHAKE_RAD or self.rad > MIN_RAD + MAX_SHAKE_RAD):
            screenshaker.shake()

            if self.shaking == False:
                self.shakeSound.play(-1)
                self.shaking = True
        else:
            self.shakeSound.stop()
            self.shaking = False
        
        self.rad += self.turnVel


        if(inputManager.accelerate == True):
            if not self.speed > 1:
                self.speed += ACCELERATION
        
        if inputManager.decelerate == True:
            if not self.speed < 0.25:
                self.speed -= ACCELERATION
                
                self.breaking = True
        else:
            self.breaking = False

        #Calculating the angle change based on the radius
        angleChange = ANGULAR_SPEED / self.rad * self.speed
        self.ang += angleChange
        Car.update(self);

    def loadImage(self):
        self.imgTemplate = pygame.image.load("media/carPlayer.png")

    def addScore(self):
        self.score += 1000

    def resetCar(self):
        self.ang = 0
        self.rad = getRandomRadius()
        self.turnVel = 0
        self.speed = 0.5

    def onMinRadius(self):
        self.turnVel = 0
    
    def onMaxRadius(self):
        self.turnVel = 0

