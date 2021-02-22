import pygame
from states import *
import images
import utility


class Player:

    def __init__(self, position):

        self.x = position[0] / 2
        self.y = position[1] / 2

        self.move_x = 0
        self.move_y = 0

        self.walking_speed = 2
        self.running_speed = 4

        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

        self.state = PlayerStates.paused
        self.direction = Directions.e

        self.step_no = 0
        self.steps = get_num_steps_player(self.state)

    def get_position(self):
        return tuple([self.x, self.y])

    def move(self, keys):

        # Reset states
        self.stop_moving()

        # Up and down
        if keys[pygame.K_w]:
            self.moving_up = True
        if keys[pygame.K_s]:
            self.moving_down = True
        if self.moving_up and self.moving_down:
            self.moving_up = False
            self.moving_down = False

        # Left and right
        if keys[pygame.K_a]:
            self.moving_left = True
        if keys[pygame.K_d]:
            self.moving_right = True
        if self.moving_right and self.moving_left:
            self.moving_right = False
            self.moving_left = False

        # Determine state
        if self.is_moving():
            if keys[pygame.K_LSHIFT]:
                self.set_state(PlayerStates.running)
            else:
                self.set_state(PlayerStates.walking)
        else:
            self.set_state(PlayerStates.paused)

        # Determining direction
        if self.moving_down and self.moving_right:
            self.direction = Directions.se
        elif self.moving_down and self.moving_left:
            self.direction = Directions.sw
        elif self.moving_down:
            self.direction = Directions.s
        elif self.moving_up and self.moving_right:
            self.direction = Directions.ne
        elif self.moving_up and self.moving_left:
            self.direction = Directions.nw
        elif self.moving_up:
            self.direction = Directions.n
        elif self.moving_right:
            self.direction = Directions.e
        elif self.moving_left:
            self.direction = Directions.w

        # Determining position
        if self.moving_up:
            if self.state == PlayerStates.running:
                self.move_y -= self.running_speed
            else:
                self.move_y -= self.walking_speed
        if self.moving_right:
            if self.state == PlayerStates.running:
                self.move_x += self.running_speed
            else:
                self.move_x += self.walking_speed
        if self.moving_down:
            if self.state == PlayerStates.running:
                self.move_y += self.running_speed
            else:
                self.move_y += self.walking_speed
        if self.moving_left:
            if self.state == PlayerStates.running:
                self.move_x -= self.running_speed
            else:
                self.move_x -= self.walking_speed

    def set_state(self, state, mouse_pos=None):
        if self.state not in [state,
                              PlayerStates.attacking,
                              PlayerStates.casting,
                              PlayerStates.hit,
                              PlayerStates.death]:
            self.state = state
            self.step_no = 0
            self.steps = get_num_steps_player(state)

            if state in [PlayerStates.attacking, PlayerStates.casting]:
                self.change_direction(utility.get_angle(self.x, self.y, mouse_pos[0], mouse_pos[1]))
                self.move_x = 0
                self.move_y = 0

    def force_state(self, state):
        self.state = state
        self.step_no = 0
        self.steps = get_num_steps_player(state)

    def can_move(self):
        if self.state not in [PlayerStates.attacking, PlayerStates.casting]:
            return True

    def get_move(self):
        return tuple([self.move_x, self.move_y])

    def stop_moving(self):

        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False
        self.move_x = 0
        self.move_y = 0

    def is_moving(self):
        return self.moving_up or self.moving_right or self.moving_down or self.moving_left

    def change_direction(self, angle):
        if 338 <= angle < 23:
            self.direction = Directions.e
        elif 23 <= angle < 68:
            self.direction = Directions.ne
        elif 68 <= angle < 113:
            self.direction = Directions.n
        elif 113 <= angle < 158:
            self.direction = Directions.nw
        elif 158 <= angle < 203:
            self.direction = Directions.w
        elif 203 <= angle < 248:
            self.direction = Directions.sw
        elif 248 <= angle < 293:
            self.direction = Directions.s
        elif 293 <= angle < 338:
            self.direction = Directions.se
        else:
            self.direction = Directions.e

    def draw(self, screen):

        self.step_no += 1
        if self.step_no == self.steps:
            if self.state in [PlayerStates.attacking, PlayerStates.casting, PlayerStates.hit, PlayerStates.death]:
                self.force_state(PlayerStates.paused)
            else:
                self.step_no = 0

        screen.blit(images.get_player_image(self.state, self.direction, self.step_no), (self.x - 56, self.y - 56))
