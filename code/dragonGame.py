import arcade
import json
from code.tile import Tile
# from code.attacker import Warrior, Dragon
# from code.hud import HUD

class DragonGame:
    def __init__(self):
        self._tiles = arcade.SpriteList()
        self._enemies = arcade.SpriteList()
        self._warriors = arcade.SpriteList()
        # self._hud = HUD()
        self._allSprites = arcade.SpriteList()
        self._setUp()
    
    def _setUp(self):
        self._setUpTiles(50, 500)

    def _setUpTiles(self, init_x, init_y):
        pass
        stageFile = open("stages/stage1.json")
        stage = json.load(stageFile)
        self._boardWidth = stage["width"]
        self._boardHeight = stage["height"]

        next_x = init_x
        next_y = init_y
        index = 0
        for tileNum in stage["boardArray"]:
            tile = 0
            if tileNum == 0:
                tile = Tile("images/normalTile.png", 0.3)
            elif tileNum == 1:
                tile = Tile("images/dragonLairTile.png", 0.3)
            elif tileNum == 2:
                tile = Tile("images/pathTile.png", 0.3)
            elif tileNum == 3:
                tile = Tile("images/castleTile.png", 0.3)

            tile.center_x = next_x
            tile.center_y = next_y
            self._allSprites.append(tile)

            next_x += tile.width
            
            if (index == self._boardWidth - 1):
                next_x = init_x
                next_y -= tile.height
                index = 0
            else:
                index += 1

    
    def update(self):
        self._allSprites.update()
        pass

    def draw(self):
        self._allSprites.draw()
        pass