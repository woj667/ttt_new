from game.GameMove import GameMove


class GameBoard():
    """GameBoard class stores information about each move. You can:
    * add move (object) to the list of moves
    * get dictionary with {key}:{value} respectively {field}:{side}"""

    def __init__(self):
        """Initialize game board"""

        # empty the board
        self.list_of_moves = []

        # create dictionary of moves
        self.dict_of_moves = dict()
        for i in range(9):
            self.dict_of_moves[i+1] = None

    def add_move(self, field, side):
        """Adds move (object) to the list of objects"""
        # create object
        move = GameMove(field, side)

        # append moves
        self.list_of_moves.append(move)

    def get_moves_dict(self):
        """Returns dictionary of all moves as {field: side}"""
        for move in self.list_of_moves:
            self.dict_of_moves[move.get_field()] = move.get_side()
        return self.dict_of_moves

    # todo
    def get_moves_list(self):
        pass

if __name__ == "__main__":

    game_board = GameBoard()
    print('empty dict: ', game_board.get_moves_dict())

    game_board.add_move(1, 1)
    game_board.add_move(2, 0)
    game_board.add_move(3, 0)
    game_board.add_move(4, 0)

    print('mod dict: ', game_board.get_moves_dict())


