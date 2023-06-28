import pygame
from assets import Assets
from collisionchecker import CollisionChecker
import config
from entity.player import Player
from game_state import GameState
from tile.tilemanager import TileManager

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.player = Player(self)
        self.tile_manager = TileManager(self.player)
        self.col_checker = CollisionChecker(self)
        self.assets = Assets(self)
        self.objs = []
        

    def set_up(self):
        
        self.objects.append(self.player)
        self.game_state = GameState.RUNNING
        self.tile_manager.load_map("resources/maps/world01.txt")
        self.assets.set_object()

    def update(self):
        self.screen.fill(config.BLACK)
        self.handle_events()

        # TILE
        self.tile_manager.render(self.screen)

        # OBJECT
        for obj in self.objs:
            if obj is not None:
                obj.render(self.screen)
                

        # PLAYER
        for object in self.objects:
            object.render(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED

        self.player.update()

