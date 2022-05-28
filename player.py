from datetime import date
from enum import Enum
from pydantic import BaseModel, PositiveInt


class Gender(Enum):
    """
    Gender is a class that inherits from the Enum class.
    
    Args:
        Enum (class): Enum is a basic python module integrated 
        into the language. it will enumerate the values of the
        gender variable.
    """
    Mal = "M"
    Female = "F"


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
    gender: Gender
    

player1 = Player(
    id=123, 
    rank=102, 
    last_name="Amri", 
    first_name="Saber", 
    birth_date= "1979-04-23", 
    gender= "M")

print(player1)