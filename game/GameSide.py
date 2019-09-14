from enum import Enum


class GameSide(Enum):
    """Noughts and crosses"""
    nought = 1
    cross = 2


if __name__ == "__main__":
    print("\nVALUES |  SIDES")
    for result in GameSide:
        print(result.value, '     | ', result.name)

    random_side = 1
    side = GameSide(random_side).name
    print("\nSide: ", side)
