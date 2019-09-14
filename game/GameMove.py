from game.GameSide import GameSide


class GameMove:
    """stores each move in new instance"""

    def __init__(self, side, field):
        """This class stores info about move: nought/cross and board coordinates"""
        self.side = side
        self.field = field

    def get_side(self):
        """Says which opponent moved"""
        return GameSide(self.side).name

    def get_field(self):
        """Returns place of given move"""
        return self.field


if __name__ == "__main__":
    move = GameMove(2, 'mr')
    print("Side: ", move.get_side())
    print("Field: ", move.get_field())