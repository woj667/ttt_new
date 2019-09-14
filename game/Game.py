from game.GameBoard import GameBoard


class Game:

    def __init__(self):
        """Initiate game"""
        self.Board = GameBoard()
        self.finished = 0
        self.result = None


    def is_move_allowed(self):
        pass

    def add_move(self, move):
        pass

    def is_move_winning(self):

        if self.Board.number_of_moves() == 9:
            self.finished = True

        # todo code winning moves


if __name__ == "__main__":
    game = Game()
    print("result: ", game.result)
