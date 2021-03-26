import arcade
import json
from code import constants
from code.tile import Tile
from code.warrior import Warrior

class Stage:
    def __init__(self, jsonPath):
        self._jsonPath = jsonPath

        self._tiles = arcade.SpriteList()
        self._enemies = arcade.SpriteList()
        self._warriors = arcade.SpriteList()
        self._allSprites = arcade.SpriteList()

        self._stageData = json.load(open(jsonPath))

        self._setUp()
    
    def getTiles(self):
        return self._tiles
    
    def getEnemies(self):
        return self._enemies
    
    def getWarriors(self):
        return self._warriors
    
    def getAllSprites(self):
        return self._allSprites
    
    def _setUp(self):
        self._setUpTiles(100, constants.SCREEN_HEIGHT - 100)
        self._setUpWarriors()
    
    def _setUpWarriors(self):
        warrior = Warrior("images/warriors/1/0.png", 0.5)
        warrior.center_x = 800
        warrior.center_y = 100
        self._warriors.append(warrior)
        self._allSprites.append(warrior)
        # for warriorNum in self._stageData["warriors"]:
        #     warrior = 0
        #     if warriorNum == 1:
        #         warrior = Warrior("images/warriors/1/0.png")
        #     elif warriorNum == 2:
        #         warrior = Warrior("images/warriors/2/0.png")
        #     elif warriorNum == 3:
        #         warrior = Warrior("images/warriors/3/0.png")

        #     warrior.center_x = 800
            

        #     self._warriors.append(warrior)

    def _setUpTiles(self, init_x, init_y):
        next_x = init_x
        next_y = init_y
        index = 0
        for tileNum in self._stageData["boardArray"]:
            tile = 0
            if tileNum == 0:
                tile = Tile("images/tiles/normalTile.png", constants.SCALING)
                tile.textures.append(arcade.load_texture("images/tiles/normalTile_h.png"))
            elif tileNum == 1:
                tile = Tile("images/tiles/dragonLairTile.png", constants.SCALING)
                tile.textures.append(arcade.load_texture("images/tiles/dragonLairTile_h.png"))
            elif tileNum == 2:
                tile = Tile("images/tiles/pathTile.png", constants.SCALING)
                tile.textures.append(arcade.load_texture("images/tiles/pathTile_h.png"))
            elif tileNum == 3:
                tile = Tile("images/tiles/castleTile.png", constants.SCALING)
                tile.textures.append(arcade.load_texture("images/tiles/castleTile_h.png"))

            tile.center_x = next_x
            tile.center_y = next_y
            
            self._tiles.append(tile)
            self._allSprites.append(tile)

            next_x += tile.width
            
            if (index == self._stageData["width"] - 1):
                next_x = init_x
                next_y -= tile.height
                index = 0
            else:
                index += 1