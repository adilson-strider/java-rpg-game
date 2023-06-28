import pygame as pg
from config import *
from tile.tile import Tile


class TileManager:
    def __init__(self, player) -> None:
        self.tiles = []
        self.player = player

        # como criar array bidimensional (valeu chatgpt! ;))
        self.map_tile_num = [[0] * MAX_WORLD_ROW for _ in range(MAX_WORLD_COL)]

        self.setup("grass00", False)
        self.setup("wall", True)
        self.setup("water01", True)
        self.setup("earth", False)
        self.setup("tree", True)
        self.setup("road00", False)

    def setup(self, image_name, collision):
        try:
            tile = Tile()
            tile.image = pg.image.load("resources/images/tiles/" + image_name + ".png")
            tile.image = pg.transform.scale(tile.image, (TILE_SIZE, TILE_SIZE))
            tile.collision = collision
            self.tiles.append(tile)
        except Exception as e:
            print("Algum problema ao carregar as imagens!")

    def load_map(self, map_path):
        try:
            with open(map_path, "r") as file:
                lines = file.readlines()
                for row, line in enumerate(lines):
                    numbers = line.strip().split(" ")
                    for column, number in enumerate(numbers):
                        self.map_tile_num[column][row] = int(number)
        except Exception as e:
            print(e)

    def render(self, screen):
        world_col = 0
        world_row = 0

        while world_col < MAX_WORLD_COL and world_row < MAX_WORLD_ROW:

            tile_number = self.map_tile_num[world_col][world_row]

            # implamenta a câmera usando coordenadas de tela e de mapa
            world_x = world_col * TILE_SIZE
            world_y = world_row * TILE_SIZE
            screen_x = world_x - self.player.world_x + self.player.screen_x
            screen_y = world_y - self.player.world_y + self.player.screen_y

            # renderiza apenas o tile que pode ser visto
            if world_x + TILE_SIZE > self.player.world_x - self.player.screen_x and \
                    world_x - + TILE_SIZE < self.player.world_x + self.player.screen_x and \
                    world_y + TILE_SIZE > self.player.world_y - self.player.screen_y and \
                    world_y - TILE_SIZE < self.player.world_y + self.player.screen_y:
                screen.blit(self.tiles[tile_number].image, (screen_x, screen_y))

            world_col += 1

            if world_col == MAX_WORLD_COL:
                world_col = 0
                world_row += 1
