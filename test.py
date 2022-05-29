from manager import Manager

from models.player import Player
from models.tournament import Tournament


# player_manager = Manager(item_type=Player)
# print(player_manager.load_from_json(path="./Jason/players.json"))

tournament_manager = Manager(item_type=Tournament)
print(tournament_manager.load_from_json(path="./Jason/tournaments.json"))