import pygame
from player import Player
from states import *
import images


def game_loop():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    bg_color = pygame.Color("black")

    player = Player()
    images.load_player_images()

    running = True
    while running:
        clock.tick(24)
        screen.fill(bg_color)

        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()
                if event.key == pygame.K_h:
                    player.set_state(PlayerStates.hit)
                if event.key == pygame.K_i:
                    player.set_state(PlayerStates.death)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    player.set_state(PlayerStates.attacking)
                elif event.button == 3:
                    player.set_state(PlayerStates.casting)

        if player.can_move():
            player.move(keys_pressed)
        player.draw(screen)

        pygame.display.flip()


def quit_game():
    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop()
