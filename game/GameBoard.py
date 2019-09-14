class GameBoard():

    def __init__(self):
        """Initialize game board"""

        # board empty
        self.moves_all = []
        self.moves_nought = []
        self.moves_cross = []

    def add_nought(self, move):
        self.moves_nought.append(move)
        self.moves_all.append(move)

    def add_cross(self, move):
        self.moves_cross.append(move)
        self.moves_all.append(move)

    def is_occupied(self, move):
        return True if move in self.moves_all else False

    def number_of_moves(self):
        return len(self.moves_all)

    def list_all_moves(self):
        return self.moves_all

    def clear(self):
        # board empty
        self.moves_all = []
        self.moves_nought = []
        self.moves_cross = []


if __name__ == "__main__":
    game_board = GameBoard()
    game_board.add_cross('c1')
    game_board.add_nought('n1')
    game_board.add_nought('n2')
    print("all moves: ", game_board.list_all_moves())
    print("number of moves: ", game_board.number_of_moves())
    print("occupied") if game_board.is_occupied('n3') else print('Free')

