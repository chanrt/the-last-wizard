from states import *
import utility
import images
import math


class Projectile:

    def __init__(self, state, start, end):
        self.state = state
        if state == Projectiles.flame:
            self.speed = 20
        elif state == Projectiles.frost:
            self.speed = 15

        self.width = 128
        self.height = 96
        self.x = start[0]
        self.y = start[1]

        self.angle = utility.get_angle(self.x, self.y, end[0], end[1])
        self.speed_x = self.speed * math.cos(math.radians(self.angle))
        self.speed_y = self.speed * math.sin(math.radians(self.angle))

        self.step_no = -10
        self.steps = 40

    def move(self):
        self.x += self.speed_x
        self.y -= self.speed_y

    def draw(self, screen):
        self.step_no += 1
        if 0 <= self.step_no < self.steps:
            utility.rotate_blit(screen, images.projectile_images[self.state][self.step_no],
                                (self.x - self.width / 2, self.y - self.height / 2), self.angle)
            # screen.blit(images.projectile_images[self.state][self.step_no],
            #             (self.x - self.width / 2, self.y - self.height / 2))
