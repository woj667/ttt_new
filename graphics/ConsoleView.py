def get_key():
    key = int(input("Enter field: "))
    return key


def render_board():
    print("Choose field:")
    print("{0:^3}|{1:^3}|{2:^3}".format(1, 2, 3))
    print("-----------")
    print("{0:^3}|{1:^3}|{2:^3}".format(4, 5, 6))
    print("-----------")
    print("{0:^3}|{1:^3}|{2:^3}".format(7, 8, 9))
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
    print(result)


def display_error_msg(error_code):

    error_list = ["Move not allowed - field occupied",
                  "Move not allowed - wrong key"]

    assert error_code in range(len(error_list))

    print(error_list[error_code])

def display_game_side(side):
    print("Turn:", side)

if __name__ == "__main__":
    render_board()
    print('\n')
    update_layout(['a', 'b', 'c','x','y','z','i','j','k'])
