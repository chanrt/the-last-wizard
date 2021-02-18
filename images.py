import pygame
from states import *

# Player images
images_bg_color = (105, 74, 46)
player_images = []


def load_player_images():

    for state in player_states:
        temp_2d_array = []
        for direction in directions:
            temp_1d_array = []
            if state in ["attack", "magic spelling", "tipping over"]:
                for step in thirteen_player_steps:
                    surface = pygame.image.load("sprites/player/" + state + " " + direction + step + ".bmp")
                    surface.set_colorkey(images_bg_color)
                    temp_1d_array.append(surface)
            else:
                for step in eight_player_steps:
                    surface = pygame.image.load("sprites/player/" + state + " " + direction + step + ".bmp")
                    surface.set_colorkey(images_bg_color)
                    temp_1d_array.append(surface)
            temp_2d_array.append(temp_1d_array)
        player_images.append(temp_2d_array)


def get_player_image(player_state, player_direction, player_step_no):
    return player_images[player_state][player_direction][player_step_no]
