from enum import Enum


class GameResult(Enum):
    """The winner is..."""
    cross = 1
    draw = 2
    nought = 0


if __name__ == "__main__":
    print("\nVALUES |  NAMES")
    for result in GameResult:
        print(result.value, '     | ', result.name)
