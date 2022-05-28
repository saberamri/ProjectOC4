from datetime import datetime
from typing import List
from pydantic import BaseModel, PositiveInt, constr

from round import Round


class Tournament(BaseModel):
    id: PositiveInt
    rounds: List[Round]= []
    number_of_rounds: PositiveInt = 4
    players: List[PositiveInt]
    description: constr(strict=True, min_length=2, max_length=50) = " "
    name: constr(strict=True, min_length=2, max_length=20)
    start_date: datetime = datetime.today()
    end_date: datetime = None
    place: constr(strict=True, min_length=2, max_length=20)
    time_control: str
    
tournament = Tournament(
    id=122,
    player=[2,6,8],
    name="first tournament",
    place="Paris",
    time_control="blitz"
    
    )

print(tournament)