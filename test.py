from manager import Manager
from menu import Menu

from models.player import Player
from models.tournament import Tournament
from table import Table
from view import View


player_manager = Manager(item_type=Player)
print(player_manager.load_from_json(path="./Jason/players.json"))

# tournament_manager = Manager(item_type=Tournament)
# print(tournament_manager.load_from_json(path="./Jason/tournaments.json"))

# menu = Menu(
#     title="Gérer les joueurs",
#     options=["Créer un joueur", "éditer le classement d'un joueur"])
# print(menu.show())

# view = View(
#     title="Bienvenu sur class Manager",
#     content= "Gérer les joueurs")
# print(view.show())

table = Table(
    title="Ajouter des joueurs",
    cols=[
        ("nom", "last_name"), 
        ("prénom", "first_name"),
        ("sexe", "gender")],
    items=player_manager.all()).show()

print(table)