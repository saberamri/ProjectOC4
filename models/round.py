from datetime import datetime
from typing import List
from pydantic import BaseModel, constr

from match import Match


class Round(BaseModel):
    """
    The Round() class inherits from the BaseModel() class:it contains the elements of Round

    Args:
        BaseModel (class): This class contains the attributes and methods of round
    """
    name: constr()
    start_date: datetime = datetime.today()
    end_date: datetime = None
    matchs = []