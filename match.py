from pydantic import BaseModel, PositiveInt


class Match(BaseModel):
    """
    The Match() class inherits from the BaseModel() class:it contains the elements of Match

    Args:
        BaseModel (class): This class contains the attributes and methods of match
    """
    player1_id: PositiveInt
    player2_id: PositiveInt
    score_player1: float = None

    @property
    def score_player2(self):
        return 1.0 - self.score_player1
    
    @score_player2.setter
    def score_player2(self, value):
        self.score_player1 = 1.0 - value