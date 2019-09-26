from game.game_functions import menu, game, scoreboard
import graphics.ConsoleView as ConsoleView

import pygame
import sys

if __name__ == "__main__":

    pygame.init()
    creen = pygame.display.set_mode([500, 500])

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # sys.exit()
                running = False

        # display menu
        menu()

        # run game
        game()

        # print scores
        scoreboard()

        # play again
        if not ConsoleView.play_again():
            break
