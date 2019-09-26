class GameMove:
    """GameMove class stores information about each move
        object of GameMove class contains:
        * field in [0,..,9] describing place at the board
        * side in [0,1] respectively [nought, cross]"""

    def __init__(self, field, side):
        """This class stores info about move: nought/cross and board coordinates"""
        assert 0 <= field <= 9, "field should be from 0 to 9"
        assert side in [0, 1], "side should be 0 or 1"

        self.side = side
        self.field = field

    def get_side(self):
        """Says which opponent moved"""
        # return GameSide(self.side).name
        return self.side

    def get_field(self):
        """Returns place of given move"""
        return self.field


if __name__ == "__main__":
    move = GameMove(1, 'mr')
    print("Side: ", move.get_side())
    print("Field: ", move.get_field())