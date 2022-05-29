import json
from typing import Any


class Manager:
    """
    manager: it is a layer between the database and the model:
    data access layer which is used to serialize and deserialize
    the data and to:
    - Create item as player
    - modify an element as a player
    - save this element in a database

    """

    def __init__(self, item_type: Any):
        """
        main constructors which initializes:
        - item_type (Any): instance of a class
        """
        self.item_type = item_type
        self.items = {}

    def load_from_json(self, path: str):
        """
        load the jason data of a Player() or Tournament() from a path and
        store this data in the -items- dictionary of the Player() or
        Tournament() instance key

        Args:
            path (str): path of data
        """
        with open(path) as json_data:
            data_dict = json.load(json_data)
            for item_data in data_dict:
                item = self.item_type(**item_data)
                self.items[item.id] = item
            return self.items
    
    def all(self):
        """convert data dict in data list and retrieve values from a dictionary
        Returns:
            items.values() (list): data list
        """
        return self.items.values()