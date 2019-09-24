from enum import Enum


class GameSide(Enum):
    """Noughts and crosses"""
    nought = 0
    cross = 1
    empty = 2


if __name__ == "__main__":
    print("\nVALUES |  SIDES")
    for result in GameSide:
        print(result.value, '     | ', result.name)

    random_side = 0
    side = GameSide(random_side).name
    print("\nSide: ", side)
