import pygame
from states import *
import images


class Player:

    def __init__(self):

        self.x = 500
        self.y = 500

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
                self.y -= self.running_speed
            else:
                self.y -= self.walking_speed
        if self.moving_right:
            if self.state == PlayerStates.running:
                self.x += self.running_speed
            else:
                self.x += self.walking_speed
        if self.moving_down:
            if self.state == PlayerStates.running:
                self.y += self.running_speed
            else:
                self.y += self.walking_speed
        if self.moving_left:
            if self.state == PlayerStates.running:
                self.x -= self.running_speed
            else:
                self.x -= self.walking_speed

    def set_state(self, state):
        if self.state not in [state,
                              PlayerStates.attacking,
                              PlayerStates.casting,
                              PlayerStates.hit,
                              PlayerStates.death]:
            self.state = state
            self.step_no = 0
            self.steps = get_num_steps_player(state)

    def force_state(self, state):
        self.state = state
        self.step_no = 0
        self.steps = get_num_steps_player(state)

    def can_move(self):
        if self.state not in [PlayerStates.attacking, PlayerStates.casting]:
            return True

    def stop_moving(self):

        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

    def is_moving(self):
        return self.moving_up or self.moving_right or self.moving_down or self.moving_left

    def draw(self, screen):

        self.step_no += 1
        if self.step_no == self.steps:
            if self.state in [PlayerStates.attacking, PlayerStates.casting, PlayerStates.hit, PlayerStates.death]:
                self.force_state(PlayerStates.paused)
            else:
                self.step_no = 0

        screen.blit(images.get_player_image(self.state, self.direction, self.step_no), (self.x, self.y))
