from enum import Enum


class GameResult(Enum):
    """The winner is..."""
    draw = 0
    nought = 1
    cross = 2


if __name__ == "__main__":
    print("\nVALUES |  NAMES")
    for result in GameResult:
        print(result.value, '     | ', result.name)
