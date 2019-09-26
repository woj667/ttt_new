from graphics.GameResult import GameResult
from graphics.GameSide import GameSide


def get_field():
    key = str(input("Enter field: "))

    dict_of_moves = {
        'q': 1,
        'w': 2,
        'e': 3,
        'a': 4,
        's': 5,
        'd': 6,
        'z': 7,
        'x': 8,
        'c': 9
    }

    if key in dict_of_moves:
        value = dict_of_moves[key]
    else:
        value = 999

    return value


def play_again():
    key = str(input("Play again? y/n: "))

    if key in ['y', 'Y']:
        return True
    else:
        return False


def render_board():
    print("Choose field:")
    print("{0:^3}|{1:^3}|{2:^3}".format('q', 'w', 'e'))
    print("-----------")
    print("{0:^3}|{1:^3}|{2:^3}".format('a', 's', 'd'))
    print("-----------")
    print("{0:^3}|{1:^3}|{2:^3}".format('z', 'x', 'c'))
    print("\n")


def update_layout(move_dict):

    list_of_moves = []

    for key in move_dict:
        value = move_dict.get(key)

        if value == 0:
            move = 'O'
        elif value == 1:
            move = 'X'
        else:
            move = ' '

        list_of_moves.append(move)

    print("{0:^3}|{1:^3}|{2:^3}".format(list_of_moves[0], list_of_moves[1], list_of_moves[2]))
    print("-----------")
    print("{0:^3}|{1:^3}|{2:^3}".format(list_of_moves[3], list_of_moves[4], list_of_moves[5]))
    print("-----------")
    print("{0:^3}|{1:^3}|{2:^3}".format(list_of_moves[6], list_of_moves[7], list_of_moves[8]))


def display_result(result):
    assert result in [0, 1, 2]

    if result in [0, 1]:
        result_str = GameResult(result).name
        print(result_str, 'won!')
    else:
        print('draw!')


def display_error_msg(error_code):

    error_list = ["Move not allowed - field occupied",
                  "Move not allowed - wrong key"]

    assert error_code in range(len(error_list))

    print(error_list[error_code])


def display_game_side(side):
    side_str = GameSide(side).name
    print("Turn:", side_str)


if __name__ == "__main__":
    render_board()
    print('\n')
