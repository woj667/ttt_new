from game.GameBoard import GameBoard


class Game:

    def __init__(self):
        """Initiate game"""
        self.board = GameBoard()
        self.finished = False
        self.result = None

    def is_move_allowed(self):
        pass

    def add_move(self, move):
        pass

    def get_game_result(self):

        if self.board.number_of_moves() == 9:
            self.finished = True

        # todo code winning moves

    def is_game_finished(self):
        # todo finishing condition
        return self.finished


if __name__ == "__main__":
    game = Game()
    print("result: ", game.result)
