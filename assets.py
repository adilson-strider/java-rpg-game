from config import *
from object.superobject import Obj_Chest, Obj_Door, Obj_Key

class Assets:
	def __init__(self, game):
		self.game = game

	def set_object(self):

		key1 = Obj_Key(self.game.player)
		self.game.objs.append(key1)
		self.game.objs[0].world_x = 23 * TILE_SIZE
		self.game.objs[0].world_y = 7 * TILE_SIZE

		key2 = Obj_Key(self.game.player)
		self.game.objs.append(key2)
		self.game.objs[1].world_x = 23 * TILE_SIZE
		self.game.objs[1].world_y = 40 * TILE_SIZE

		key3 = Obj_Key(self.game.player)
		self.game.objs.append(key3)
		self.game.objs[2].world_x = 38 * TILE_SIZE
		self.game.objs[2].world_y = 8 * TILE_SIZE

		door1 = Obj_Door(self.game.player)
		self.game.objs.append(door1)
		self.game.objs[3].world_x =  10 * TILE_SIZE
		self.game.objs[3].world_y =  11 * TILE_SIZE

		door2 = Obj_Door(self.game.player)
		self.game.objs.append(door2)
		self.game.objs[4].world_x =  8 * TILE_SIZE
		self.game.objs[4].world_y =  28 * TILE_SIZE

		door3 = Obj_Door(self.game.player)
		self.game.objs.append(door3)
		self.game.objs[5].world_x = 12 * TILE_SIZE
		self.game.objs[5].world_y = 22 * TILE_SIZE

		door3 = Obj_Chest(self.game.player)
		self.game.objs.append(door3)
		self.game.objs[6].world_x = 10 * TILE_SIZE
		self.game.objs[6].world_y =  7 * TILE_SIZE

		

