from game.GameBoard import GameBoard
from game.GameSide import GameSide
from random import randint


class Game:

    def __init__(self):

        """Initiate game"""

        # static values
        self.game_side = 0
        self.game_board = GameBoard()
        self.dct = None

        # dynamic values
        self._randomize_side()

    def _randomize_side(self):
        self.game_side = randint(0, 1)

    def toggle_side(self):
        game_side = 0 if self.game_side == 1 else 1
        self.game_side = game_side

    def add_move(self, field):
        self.game_board.add_move(field, self.game_side)

    def get_moves_dict(self):
        return self.game_board.get_moves_dict()

    def get_current_side_as_str(self):
        side = GameSide(self.game_side).name
        return side

    def is_move_allowed(self, key):

        dct = self.get_moves_dict()

        if key in dct:
            value = dct.get(key)
            if value is None:
                error_code = None
                move_allowed = True
            else:
                error_code = 0
                move_allowed = False
        else:
            error_code = 1
            move_allowed = False

        return move_allowed, error_code

    def is_game_finished(self):

        # winning case
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        dct = self.get_moves_dict()

        game_finished = False
        result = None

        for lst in list_of_lists:
            if self._check_fields(dct, lst):
                game_finished = True
                result = dct.get(lst[0])

        # draw case
        values = []
        for value in dct:
            values.append(dct.get(value))

        draw = True
        if None in values:
            draw = False

        if draw:
            result = 2
            game_finished = True

        return game_finished, result

    @staticmethod
    def _check_fields(dct, lst):

        values = []

        for key in lst:
            values.append(dct.get(key))

        same = True
        for i in range(len(values) - 1):
            if values[i] != values[i + 1] or values[i] is None:
                 same = False

        return same


if __name__ == "__main__":
    game = Game()
