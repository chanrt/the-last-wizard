import images
from states import *


class Spell:

    def __init__(self, state, position):
        self.x = position[0]
        self.y = position[1]
        self.state = state

        self.row_no = -2
        self.col_no = 0

        if self.state == Spells.explosion:
            self.row_limit = 8
            self.col_limit = 8
            self.width = 512
            self.height = 512
        elif self.state == Spells.purple_fire:
            self.row_limit = 5
            self.col_limit = 7
            self.width = 96
            self.height = 192
        elif self.state == Spells.wings:
            self.x -= 5
            self.y -= 20
            self.row_limit = 6
            self.col_limit = 6
            self.width = 384
            self.height = 384

    def move(self, move):
        self.x -= move[0]
        self.y -= move[1]

    def draw(self, screen):
        if 0 <= self.row_no < self.row_limit:
            screen.blit(images.spell_images[self.state],
                        (self.x - self.width / 2, self.y - self.height / 2),
                        (self.col_no * self.width, self.row_no * self.height, self.width, self.height))

        self.col_no += 1
        if self.col_no == self.col_limit:
            self.col_no = 0
            self.row_no += 1
