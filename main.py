import pygame
from player import Player
from projectile import Projectile
from spell import Spell
from toggle import Toggle
from states import *
import images
import world


def game_loop():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    bg_color = pygame.Color("black")

    projectiles = []
    spells = []
    objects = []
    world.load(objects)

    toggle = Toggle()

    player = Player(pygame.display.get_surface().get_size())
    images.load_player_images()
    images.load_projectile_images()
    images.load_spell_images()
    images.load_object_images()

    running = True
    while running:
        clock.tick(24)
        screen.fill(bg_color)

        keys_pressed = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()
                if event.key == pygame.K_q:
                    toggle.toggle_projectile()
                if event.key == pygame.K_e:
                    toggle.toggle_spells()
                if event.key == pygame.K_h:
                    player.set_state(PlayerStates.casting, mouse_pos)
                    player_position = player.get_position()
                    spell = Spell(Spells.wings, player_position)
                    spells.append(spell)

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    if player.state not in [PlayerStates.casting, PlayerStates.attacking]:
                        player.set_state(PlayerStates.attacking, mouse_pos)
                        projectile = Projectile(toggle.current_projectile, player.get_position(), mouse_pos)
                        projectiles.append(projectile)

                elif event.button == 3:
                    if player.state not in [PlayerStates.casting, PlayerStates.attacking]:
                        player.set_state(PlayerStates.casting, mouse_pos)
                        spell = Spell(toggle.current_spell, mouse_pos)
                        spells.append(spell)

        if player.can_move():
            player.move(keys_pressed)
        player_move = player.get_move()

        for object in objects:
            object.move(player_move)
            object.draw(screen)

        for projectile in projectiles:
            projectile.move(player_move)
            projectile.draw(screen)
            if projectile.step_no == projectile.steps:
                projectiles.remove(projectile)

        for spell in spells:
            spell.move(player_move)
            spell.draw(screen)
            if spell.row_no == spell.row_limit:
                spells.remove(spell)

        player.draw(screen)

        pygame.display.flip()


def quit_game():
    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop()
