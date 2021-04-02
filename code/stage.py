import arcade
import json
from code import constants
from code.tile import Tile
from code.attacker import Warrior
from code.dragonSpawner import DragonSpawner

class Stage:
    def __init__(self, jsonPath):
        self._jsonPath = jsonPath
        self._stageData = json.load(open(jsonPath))

        # castle health:
        self._castleHealth = self._stageData["castleHealth"]

        # tiles related:
        self._tiles = arcade.SpriteList()
        self._dragonLairIndex = self._stageData["lairIndex"]
        self._castleIndex = self._stageData["castleIndex"]

        # dragons related:
        self._enemies = arcade.SpriteList()

        # warriors related:
        self._warriors = arcade.SpriteList()

        # projectiles:
        self._projectiles = arcade.SpriteList()

        # All sprites:
        self._allSprites = arcade.SpriteList()

        self._warriorTypes = []
        self._dragonsList = []

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
        return self._castleHealth
    
    def damageCastle(self, damage):
        self._castleHealth -= damage
    
    def getDragonLairTile(self):
        return self._tiles[self._dragonLairIndex]
    
    def getCastleTile(self):
        return self._tiles[self._castleIndex]
    
    def _setUp(self):
        self._setUpTiles(100, constants.SCREEN_HEIGHT - 100)
        self._setUpWarriors()
        self._setUpDragons()
        spawnLocation = (self._tiles[self._dragonLairIndex].center_x, self._tiles[self._dragonLairIndex].center_y)
        dragonPaths = self._stageData["paths"]

        self._dragonSpawner = DragonSpawner(self._dragonsList, dragonPaths, self, spawnLocation)

    def startSpawningDragon(self):
        self._dragonSpawner.startSpawning()

    def _setUpDragons(self):
        self._dragonsList = self._stageData["dragonsList"]
    
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