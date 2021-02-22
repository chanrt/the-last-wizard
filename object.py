import images
from states import *


class Object:
    def __init__(self, x, y, state):
        self.width = 512
        self.height = 512

        self.x = x * self.width
        self.y = y * self.height
        self.state = state

    def move(self, move):
        self.x -= move[0]
        self.y -= move[1]

    def draw(self, screen):
        screen.blit(images.object_images[self.state], (self.x, self.y))
