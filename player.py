from datetime import date
from pydantic import BaseModel, PositiveInt

class Player(BaseModel):
    """
    The Player() class inherits from the BaseModel() class
    This class contains the attributes and methods of the player user.

    Args:
        BaseModel (class): class BaseModel
    """
    id: PositiveInt
    rank: int
    last_name: str
    first_name: str
    birth_date: date
    gender: str
    

player1 = Player(
    id=123, 
    rank=102, 
    last_name="Amri", 
    first_name="Saber", 
    birth_date= "1979-04-23", 
    gender= "M")

print(player1)