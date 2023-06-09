import pygame
import config
from game_state import GameState

from game import Game

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("The Adventures of PyBoy")

clock = pygame.time.Clock()

game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
    clock.tick(60)
    game.update()
    pygame.display.flip()
