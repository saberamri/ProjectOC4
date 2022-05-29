from manager import Manager

from models.player import Player


player_manager = Manager(item_type=Player)
print(player_manager.load_from_json(path="Jason\players.json"))