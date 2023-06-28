import pygame as pg
import config

class Entity:
    def __init__(self):
        self.world_x = 0
        self.world_y = 0
        self.speed = 0
        self.direction = ""
        self.images = []
        self.sprite_counter = 0
        self.sprite_num = 1
        self.solid_area = None
        self.area_def_x = 0
        self.area_def_y = 0
        self.collision_on = False
