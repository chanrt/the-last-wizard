import pygame
from player import Player
from projectile import Projectile
from states import *
import images


def game_loop():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    bg_color = pygame.Color("black")

    projectiles = []

    player = Player()
    images.load_player_images()
    images.load_projectile_images()

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1:
                    player.set_state(PlayerStates.attacking, mouse_pos)
                    projectile = Projectile(Projectiles.flame, player.get_position(), mouse_pos)
                    projectiles.append(projectile)

                elif event.button == 3:
                    player.set_state(PlayerStates.casting, mouse_pos)

        if player.can_move():
            player.move(keys_pressed)
        player.draw(screen)

        for projectile in projectiles:
            projectile.move()
            projectile.draw(screen)
            if projectile.step_no == 40:
                projectiles.remove(projectile)

        pygame.display.flip()


def quit_game():
    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop()
