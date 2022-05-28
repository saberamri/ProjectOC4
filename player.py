from datetime import date, timedelta
from enum import Enum
from pydantic import BaseModel, PositiveInt, validator, constr


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
    rank: PositiveInt
    last_name: constr(strict=True, min_length=2, max_length=20)
    first_name: constr(strict=True, min_length=2, max_length=20)
    birth_date: date
    gender: Gender
    
    @validator("birth_date")
    def check_age(cls, v):
        """verify that participants are at least 18 years old.
            Args:
                v (date): date of birth of participants.
            Raises:
                ValueError: the age of the participants is under 18.
            Returns:
                v: birth date of participant.
        """
        age = (date.today() - v) // timedelta(days=365.2425)
        if age < 18:
            raise ValueError('age must be > 18')
        return v
    

player1 = Player(
    id=123, 
    rank=102, 
    last_name="Amri", 
    first_name="Saber", 
    birth_date= "2015-04-23", 
    gender= "M")

print(player1)