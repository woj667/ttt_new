from game.Game import Game


def run():

    # run game logic
    game_logic = Game()

    # check if game is finished
    game_finished = game_logic.is_game_finished()

    while(not game_finished):

        # ask for input
        print("q | w | e")
        print("---------")
        print("a | s | d")
        print("---------")
        print("z | x | c")
        move = input("\nEnter field: ")

        # transfer parameters to the game
        game_logic.add_move(move)

        #

        # display game board



if __name__ == "__main__":
    run()