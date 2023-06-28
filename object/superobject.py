import pygame as pg
from config import *

class SuperObject:
    def __init__(self, player):
        self.image = None
        self.name = ""
        self.player = player
        self.collision = False
        self.world_x = 0
        self.world_y = 0
        self.area_def_x = 0
        self.area_def_y = 0
        self.solid_area = pg.Rect(0, 0, 48, 48)


    def render(self, screen):
        screen_x = self.world_x - self.player.world_x + self.player.screen_x
        screen_y = self.world_y - self.player.world_y + self.player.screen_y

        # renderiza apenas o tile que pode ser visto
        if self.world_x + TILE_SIZE > self.player.world_x - self.player.screen_x and \
                self.world_x - + TILE_SIZE < self.player.world_x + self.player.screen_x and \
                self.world_y + TILE_SIZE > self.player.world_y - self.player.screen_y and \
                self.world_y - TILE_SIZE < self.player.world_y + self.player.screen_y:
            screen.blit(self.image, (screen_x, screen_y))

class Obj_Key(SuperObject):
    def __init__(self, player):
        super().__init__(player)

        self.name = "Key"
        try:
            self.image = pg.image.load("resources/images/objects/key.png")
            self.image = pg.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        except:
            print("Erro ao carregar a imagem.")
        
    def render(self, screen):
        return super().render(screen)
    
class Obj_Door(SuperObject):
    def __init__(self, player):
        super().__init__(player)

        self.name = "Door"
        try:
            self.image = pg.image.load("resources/images/objects/door.png")
            self.image = pg.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        except:
            print("Erro ao carregar a imagem.")
        self.collision = True
    
class Obj_Chest(SuperObject):
    def __init__(self, player):
        super().__init__(player)

        self.name = "Chest"
        try:
            self.image = pg.image.load("resources/images/objects/chest.png")
            self.image = pg.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        except:
            print("Erro ao carregar a imagem.")