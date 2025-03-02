"""simulates battle in rpg game"""

from time import sleep
import random as rand
from classes import Player, NPC
from misc_functions import cls, getch

# pylint: disable = C0116


def battle(global_player: Player, global_enemy: NPC):
    player = global_player
    enemy = global_enemy
    while True:
        print(f"You have entered into a battle with {enemy.name}")
        print("Press a number key to input a value")
        inp = get_input()
        cls()
        do_action(inp, player, enemy)


# test claude coder please do something


def attack(player, enemy):
    base_damage = rand.randint(1, 2)
    dmg_randomness = rand.uniform(1.0, 1.3)
    strength_multiplier = 1 + (player.stre / 10)
    level_multiplier = 1 + (player.leve / 5)
    dmg = base_damage + strength_multiplier * level_multiplier * dmg_randomness
    enemy.hlth -= dmg


def ability():
    pass


def do_action(action: str, player, enemy):
    if action == "1":
        attack(player, enemy)
    if action == "2":
        pass
    if action == "3":
        pass
    if action == "4":
        pass
    if action == "5":
        pass

    raise SyntaxError(
        "got to end of control flow in" f"{do_action.__name__}. action was {action}"
    )


def print_actions():
    print("1. Attack")
    print("2. Abilities")
    print("3. Magic")
    print("4. Items")
    print("5. Flee")
    print("6. Exit")


def print_fail():
    print("Invalid input. Input must be")
    print("a number between 1 and 5.")


def get_input() -> str:
    while True:
        print_actions()
        inp = getch()

        if inp.isdigit():
            inp = int(inp)
        if inp in [str(num) for num in range(1, 7)]:
            return inp

        print_fail()
        sleep(1)
        cls()


if __name__ == "__main__":
    player1 = Player(mxhl=100, leve=5, stre=15, agil=10, inte=8, endu=12, name="abc")
    enemy1 = NPC(mxhl=50, leve=5, stre=8, agil=12, inte=6, endu=10, name="dfg")
    battle(player1, enemy1)
