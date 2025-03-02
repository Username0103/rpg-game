'''home of classes'''
from dataclasses import dataclass
import pickle
from pathlib import Path

#pylint: disable = W1514

class Game:
    '''Game information to save'''
    _instances = []
    _instance_map = {}
    _next_instance_id = 0
    '''Game class is the mother of all classes.'''
    def __init__(self, save_name = 'savegame.sav') -> None:
        self.current_path = Path(__file__).resolve().parent.joinpath('saves', save_name)
        self.instance_id = Game._next_instance_id  # Assign unique ID
        Game._next_instance_id += 1
        Game._instances.append(self)
        Game._instance_map[self.instance_id] = self # Store in the map

    def save(self) -> None:
        '''saves game'''
        with self.current_path.open('wb') as savefile:
            pickle.dump(Game._instances, savefile)

    def load(self) -> None:
        '''loads game'''
        with self.current_path.open('rb') as savefile:
            Game._instances = pickle.load(savefile)
            for current_instance in Game._instances:
                Game._instance_map[current_instance.instance_id] = current_instance
    @classmethod
    def get_object(cls, instance_id):
        '''Retrieves a game instance by its ID'''
        return cls._instance_map.get(instance_id) # Efficient dictionary lookup

@dataclass
class Stats(Game):
    '''stores stats that every creature has'''
    name: str
    leve: int # probably won't get to more than like 50
    stre: int # player will be able to invest points manually in each stat
    agil: int # a good default would be 5, with 5 points total per level.
    inte: int
    endu: int
    def __post_init__(self):
        # derived stats:
        self.mxhl: int = self.endu * 2 + 10
        self.mxap: int = self.agil // 2 + 2
        self.mxmp: int = self.inte // 2 + 2
        # limited by max stats:
        self._hlth: int = self.mxhl
        self._acpt: int = self.mxap
        self._mgpt: int = self.mxmp
        Game.__init__(self)

    def _make_property(self, name, max_name) -> property:
        _name = f'_{name}'
        def getter(self):
            return getattr(self, _name)
        def setter(self, value):
            max_value = self, max_name
            setattr(self, _name, min(value, max_value))
        return property(getter, setter)

    hlth = '...'

class Player(Stats):
    '''to contain player specific data and behavior'''

class NPC(Stats):
    '''to contain monster specific data and behavior'''

# if __name__ == "__main__":
#     #pylint: disable = W0212
#     # Example Usage:

#     # Create some instances
#     game1 = Game()
#     player1 = Player(leve=5, stre=15, agil=10, inte=8, endu=12, name='abc')
#     enemy1 = NPC(leve=5, stre=8, agil=12, inte=6, endu=10, name='dfg')
#     player2 = Player(leve=5, stre=18, agil=12, inte=9, endu=15, name='uhj')
#     game1.save()

#     Game._instances = []
#     Game._instance_map = {}

#     game1.load()

#     retrieved_enemy = Game.get_object(enemy1.instance_id) # Note: enemy1 is from *before* save/load, but IDs are preserved
#     if retrieved_enemy:
#         print(f"Retrieved Enemy by ID: {retrieved_enemy}, Health: {retrieved_enemy.hlth}, Strength: {retrieved_enemy.stre}")
#     else:
#         print("Enemy not found with that ID.")

#     # Verify loaded instances (optional - just for demonstration)
#     for instance in Game._instances:
#         if isinstance(instance, Player):
#             print(f"Loaded Player:, ID: {instance.instance_id}, Health: {instance.hlth}, Strength: {instance.stre}")
#         elif isinstance(instance, NPC):
#             print(f"Loaded Enemy:, ID: {instance.instance_id}, Health: {instance.hlth}, Strength: {instance.stre}")
#         elif isinstance(instance, Game):
#             print(f"Loaded Game Instance: ID: {instance.instance_id}")

if __name__ == "__main__":
    print(dir(Player))