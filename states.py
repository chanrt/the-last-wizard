class PlayerStates:
    paused = 0
    walking = 1
    running = 2
    attacking = 3
    casting = 4
    hit = 5
    death = 6


class Directions:
    n = 0
    ne = 1
    e = 2
    se = 3
    s = 4
    sw = 5
    w = 6
    nw = 7


class Projectiles:
    flame = 0
    frost = 1


class Spells:
    explosion = 0
    purple_fire = 1
    wings = 2


class Objects:
    large_rock = 0
    road = 1


def get_num_steps_player(state):

    if state in [PlayerStates.paused, PlayerStates.walking, PlayerStates.running, PlayerStates.hit]:
        return 8
    elif state in [PlayerStates.attacking, PlayerStates.casting, PlayerStates.death]:
        return 13


player_states = ["paused", "walking", "running", "attack", "magic spelling", "been hit", "tipping over"]
directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
spell_names = ["explosion", "purple_fire", "wings"]
projectile_names = ["flame", "frost"]
object_names = ["large_rock", "road"]
eight_player_steps = ["0000", "0001", "0002", "0003", "0004", "0005", "0006", "0007"]

thirteen_player_steps = eight_player_steps[:]
thirteen_player_steps.append("0008")
thirteen_player_steps.append("0009")
thirteen_player_steps.append("0010")
thirteen_player_steps.append("0011")
thirteen_player_steps.append("0012")
