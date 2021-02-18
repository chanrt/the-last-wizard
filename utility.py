import pygame
import math


def rotate_blit(screen, image, top_left, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)

    screen.blit(rotated_image, new_rect.topleft)


def get_angle(start_x, start_y, end_x, end_y):
    base = end_x - start_x
    perp = end_y - start_y

    if base > 0:
        if -perp > 0:
            angle = math.degrees(math.atan(-perp / base))
        else:
            angle = 360 + math.degrees(math.atan(-perp / base))
    elif base < 0:
        if -perp > 0:
            angle = 180 + math.degrees(math.atan(-perp / base))
        else:
            angle = 180 + math.degrees(math.atan(-perp / base))
    else:
        if -perp > 0:
            angle = 90
        else:
            angle = 270

    return angle
