from states import *
import images


class Toggle:
    def __init__(self):
        self.current_projectile = 0
        self.current_spell = 0

        self.num_projectiles = len(projectile_names)
        self.num_spells = len(spell_names)

    def toggle_projectile(self):
        self.current_projectile += 1
        if self.current_projectile == self.num_projectiles:
            self.current_projectile = 0

    def toggle_spells(self):
        self.current_spell += 1
        if self.current_spell == self.num_spells:
            self.current_spell = 0
        if self.current_spell == Spells.wings:
            self.toggle_spells()