'''allows the use of items, magic, and abiltites.'''

from classes import Player, NPC
from dataclasses import dataclass

@dataclass
class Item:
    item_name: str
    to_impact: str
    impact_value: int

    def use_item(self):
        ...

def use_item(player: Player, npc: NPC):
    '''modifies player and enemy class based on the used item'''

def use_ability(player: Player, npc: NPC):
    '''modifies player and enemy class based on the used ability'''
