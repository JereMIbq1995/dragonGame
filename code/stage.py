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
        self._projectiles = arcade.SpriteList()
        self._allSprites = arcade.SpriteList()

        self._warriorTypes = []
        self._dragonTypes = []

        self._stageData = json.load(open(jsonPath))

        self._setUp()
    
    def getTileSprites(self):
        return self._tiles
    
    def getDragonSprites(self):
        return self._enemies
    
    def getWarriorSprites(self):
        return self._warriors

    def getProjectileSprites(self):
        return self._projectiles
    
    def getAllSprites(self):
        return self._allSprites

    def getWarriorTypes(self):
        return self._warriorTypes

    def addWarrior(self,warrior):
        self._warriors.append(warrior)
        self._allSprites.append(warrior)

    def removeWarrior(self,warrior):
        warrior.remove_from_sprite_lists()

    def addDragon(self,dragon):
        self._enemies.append(dragon)
        self._allSprites.append(dragon)

    def removeDragon(self,dragon):
        dragon.remove_from_sprite_lists()

    def addProjectile(self, projectile):
        self._projectiles.append(projectile)
        self._allSprites.append(projectile)

    def removeProjectile(self, projectile):
        projectile.remove_from_sprite_lists()

    def getCastleHealth(self):
        return self._stageData["castleHealth"]
    
    def _setUp(self):
        self._setUpTiles(100, constants.SCREEN_HEIGHT - 100)
        self._setUpWarriors()
        self._setUpDragons()

    def _setUpDragons(self):
        self._dragonTypes = self._stageData["enemyList"]
    
    def _setUpWarriors(self):
        self._warriorTypes = self._stageData["warriors"]

    def _setUpTiles(self, init_x, init_y):
        next_x = init_x
        next_y = init_y
        index = 0
        for tileNum in self._stageData["boardArray"]:
            tile = Tile(tileNum,scaling = constants.SCREEN_WIDTH / 20 / 120)

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