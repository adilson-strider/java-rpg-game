from config import *
from tile.tilemanager import *


class CollisionChecker:
    def __init__(self, game):
        self.game = game

    def check_tile(self, entity):
        entity_left_world_x = entity.world_x + entity.solid_area.x
        entity_right_world_x = entity.world_x + entity.solid_area.x + entity.solid_area.width
        entity_top_world_y = entity.world_y + entity.solid_area.y
        entity_bottom_world_y = entity.world_y + entity.solid_area.y + entity.solid_area.height

        entity_left_col = entity_left_world_x // TILE_SIZE
        entity_right_col = entity_right_world_x // TILE_SIZE
        entity_top_row = entity_top_world_y // TILE_SIZE
        entity_bottom_row = entity_bottom_world_y // TILE_SIZE

        tile_num1, tile_num2 = 0, 0

        direction = entity.direction

        if direction == "up":
            entity_top_row = (entity_top_world_y - entity.speed) // TILE_SIZE

            tile_num1 = self.game.tile_manager.map_tile_num[entity_left_col][entity_top_row]
            tile_num2 = self.game.tile_manager.map_tile_num[entity_right_col][entity_top_row]

        elif direction == "down":
            entity_bottom_row = (entity_bottom_world_y + entity.speed) // TILE_SIZE

            tile_num1 = self.game.tile_manager.map_tile_num[entity_left_col][entity_bottom_row]
            tile_num2 = self.game.tile_manager.map_tile_num[entity_right_col][entity_bottom_row]

        elif direction == "left":
            entity_left_col = (entity_left_world_x - entity.speed) // TILE_SIZE

            tile_num1 = self.game.tile_manager.map_tile_num[entity_left_col][entity_top_row]
            tile_num2 = self.game.tile_manager.map_tile_num[entity_left_col][entity_bottom_row]

        elif direction == "right":
            entity_right_col = (entity_right_world_x - entity.speed) // TILE_SIZE

            tile_num1 = self.game.tile_manager.map_tile_num[entity_right_col][entity_top_row]
            tile_num2 = self.game.tile_manager.map_tile_num[entity_right_col][entity_bottom_row]

        if self.game.tile_manager.tiles[tile_num1].collision or self.game.tile_manager.tiles[tile_num2].collision:
            entity.collision_on = True

    def check_object(self, entity, player):

        index = 999

        for i, obj in enumerate(self.game.objs):
            if obj is not None:
                # get entity solid area position
                entity.solid_area.x = entity.world_x + entity.solid_area.x
                entity.solid_area.y = entity.world_y + entity.solid_area.y

                # get entity solid area position
                obj.solid_area.x = obj.world_x + obj.solid_area.x
                obj.solid_area.y = obj.world_y + obj.solid_area.y

                if entity.direction == "up":
                    entity.solid_area.y -= entity.speed
                    if entity.solid_area.colliderect(obj.solid_area):
                        if obj.collision:
                            entity.collision_on = True
                        if player:
                            index = i
                elif entity.direction == "down":
                    entity.solid_area.y += entity.speed
                    if entity.solid_area.colliderect(obj.solid_area):
                        if obj.collision:
                            entity.collision_on = True
                        if player:
                            index = i
                elif entity.direction == "left":
                    entity.solid_area.x -= entity.speed
                    if entity.solid_area.colliderect(obj.solid_area):
                        if obj.collision:
                            entity.collision_on = True
                        if player:
                            index = i
                elif entity.direction == "right":
                    entity.solid_area.x += entity.speed
                    if entity.solid_area.colliderect(obj.solid_area):
                        if obj.collision:
                            entity.collision_on = True
                        if player:
                            index = i

                entity.solid_area.x = entity.area_def_x
                entity.solid_area.y = entity.area_def_y
                obj.solid_area.x = obj.area_def_x          
                obj.solid_area.y = obj.area_def_y 


        return index
