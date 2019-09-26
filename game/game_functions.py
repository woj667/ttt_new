from game.Game import Game
from graphics import ConsoleView

def menu():
    pass


def game():
    # show layout
    ConsoleView.render_board()

    # run game logic
    game_logic = Game()

    while True:

        # toggle side
        game_logic.toggle_side()

        # display who's turn is
        side = game_logic.get_current_side()
        ConsoleView.display_game_side(side)

        # ask for input
        field = ConsoleView.get_field()

        # main game loop
        while True:
            # check if value is proper & field is not occupied
            move_allowed, error = game_logic.is_move_allowed(field)
            if move_allowed:
                break
            else:
                ConsoleView.display_error_msg(error)

            # ask for input
            field = ConsoleView.get_field()

        # add move
        game_logic.add_move(field)

        # check if game finished
        game_finished, result = game_logic.is_game_finished()

        # display game board
        move_dict = game_logic.get_moves_dict()
        ConsoleView.update_layout(move_dict)

        if game_finished:
            ConsoleView.display_result(result)
            break

    print("ENDGAME")


def scoreboard():
    pass