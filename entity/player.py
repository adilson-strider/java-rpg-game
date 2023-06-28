import pygame as pg
from config import *
from entity.entity import Entity


def handle_input():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


class Player(Entity):
    def __init__(self, game):
        super().__init__()
        # print("player created")

        self.game = game

        self.world_x = TILE_SIZE * 23
        self.world_y = TILE_SIZE * 21

        self.screen_x = SCREEN_WIDTH / 2 - (TILE_SIZE / 2)
        self.screen_y = SCREEN_HEIGHT / 2 - (TILE_SIZE / 2)

        self.solid_area = pg.Rect(8, 16, 32, 32)

        self.area_def_x = self.solid_area.x
        self.area_def_y = self.solid_area.y

        self.has_key = 0

        self.speed = 7

        try:
            self.image_up1 = pg.image.load("resources/images/player/boy_up_1.png")
            self.image_up1 = pg.transform.scale(self.image_up1, (TILE_SIZE, TILE_SIZE))
            self.images.append(self.image_up1)

            self.image_up2 = pg.image.load("resources/images/player/boy_up_2.png")
            self.image_up2 = pg.transform.scale(self.image_up2, (TILE_SIZE, TILE_SIZE))
            self.images.append(self.image_up2)

            self.image_down1 = pg.image.load("resources/images/player/boy_down_1.png")
            self.image_down1 = pg.transform.scale(self.image_down1, (TILE_SIZE, TILE_SIZE))
            self.images.append(self.image_down1)

            self.image_down2 = pg.image.load("resources/images/player/boy_down_2.png")
            self.image_down2 = pg.transform.scale(self.image_down2, (TILE_SIZE, TILE_SIZE))
            self.images.append(self.image_down2)

            self.image_left1 = pg.image.load("resources/images/player/boy_left_1.png")
            self.image_left1 = pg.transform.scale(self.image_left1, (TILE_SIZE, TILE_SIZE))
            self.images.append(self.image_left1)

            self.image_left2 = pg.image.load("resources/images/player/boy_left_2.png")
            self.image_left2 = pg.transform.scale(self.image_left2, (TILE_SIZE, TILE_SIZE))
            self.images.append(self.image_left2)

            self.image_right1 = pg.image.load("resources/images/player/boy_right_1.png")
            self.image_right1 = pg.transform.scale(self.image_right1, (TILE_SIZE, TILE_SIZE))
            self.images.append(self.image_right1)

            self.image_right2 = pg.image.load("resources/images/player/boy_right_2.png")
            self.image_right2 = pg.transform.scale(self.image_right2, (TILE_SIZE, TILE_SIZE))
            self.images.append(self.image_right2)

        except:
            print("Erro ao carregar a imagem.")

    def update(self):
        handle_input()
        self.update_position()

    def update_position(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] or keys[pg.K_DOWN] or keys[pg.K_RIGHT] or keys[pg.K_LEFT]:
            if keys[pg.K_UP]:
                self.direction = "up"
            elif keys[pg.K_DOWN]:
                self.direction = "down"
            if keys[pg.K_RIGHT]:
                self.direction = "right"
            elif keys[pg.K_LEFT]:
                self.direction = "left"

            self.collision_on = False
            self.game.col_checker.check_tile(self)

            obj_index = self.game.col_checker.check_object(self, True)
            self.pickup_obj(obj_index)

            if not self.collision_on:
                if self.direction == "up":
                    self.world_y -= self.speed
                elif self.direction == "down":
                    self.world_y += self.speed
                elif self.direction == "right":
                    self.world_x += self.speed
                elif self.direction == "left":
                    self.world_x -= self.speed

            self.sprite_counter += 1
            if self.sprite_counter > 7:
                if self.sprite_num == 1:
                    self.sprite_num = 2
                elif self.sprite_num == 2:
                    self.sprite_num = 1
                self.sprite_counter = 0

    def pickup_obj(self, index):
        if index != 999:
            object_name = self.game.objs[index].name

            match object_name:
                case "Key":
                    self.has_key += 1
                    self.game.objs[index] = None
                    print("Keys: ", self.has_key)
                case "Door":
                    if self.has_key > 0:
                       self.game.objs[index] = None
                       self.has_key -= 1
                case "Chest":
                    pass
                case _:
                    pass

    def render(self, screen):

        temp_image = self.image_down1

        if self.direction == "up":
            if self.sprite_num == 1:
                temp_image = self.image_up1
            if self.sprite_num == 2:
                temp_image = self.image_up2
        elif self.direction == "down":
            if self.sprite_num == 1:
                temp_image = self.image_down1
            if self.sprite_num == 2:
                temp_image = self.image_down2
        elif self.direction == "left":
            if self.sprite_num == 1:
                temp_image = self.image_left1
            if self.sprite_num == 2:
                temp_image = self.image_left2
        elif self.direction == "right":
            if self.sprite_num == 1:
                temp_image = self.image_right1
            if self.sprite_num == 2:
                temp_image = self.image_right2

        screen.blit(temp_image, (self.screen_x, self.screen_y))
