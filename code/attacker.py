import arcade
import random
import math
from code import constants
class Attacker(arcade.Sprite):
    def __init__(self, path, scaling):
        self._maxHealth = 5
        self._health = 5
        self._atk = 1.0
        self._attackRange = 100
        self._isAlive = bool
        self._cooldown = 0.25
        self._currentCooldown = 0.0
        self._speed = 3

        super().__init__(path, scaling)

#Damage function takes health and applies the damage to it
    def takeDamage(self,damage):
        self._health = self._health - damage

    def attack(self, attackList):
        if attackList != []:
            index = random.randint(0,len(attackList) - 1)
            index = 0
            self.radians = math.pi / 2 - math.atan((attackList[index].center_x - self.center_x) / (attackList[index].center_y - self.center_y))
            if attackList[index].center_y < self.center_y:
                print(f"Before: {self.radians}")
                self.radians = (math.pi / 2 - self.radians + math.pi / 2) * -1
                print(f"After: {self.radians}")
            
            print(self.radians)
            if self._currentCooldown <= 0:
                projectile = arcade.Sprite("images/projectile.png",1)
                projectile.angle = self.angle
                projectile.center_x = self.center_x
                projectile.center_y = self.center_y
                projectile.change_x = math.cos(self.radians) * self._speed
                projectile.change_y = math.sin(self.radians) * self._speed
                self._currentCooldown = self._cooldown
                return projectile
            else:
                self._currentCooldown -= 0.0166666
                return None
        return None

    def setCooldown(self, amount):
        self._cooldown = amount

    def getHealth(self):
        return self._health

    def setHealth(self, health):
        self._health = health

    def getAtk(self):
        return self._atk

    def setAtk(self, atk):
        self._atk = atk

    def getAttackRange(self):
        return self._attackRange

    def setAttackRange(self, attackRange):
        self.attackRange = attackRange

    def setLocation(self, x, y):
        super()._set_center_x(x)
        super()._set_center_y(y)
    
    def setVelocity(self, x, y):
        super()._set_change_x(x)
        super()._set_change_y(y)
    
    def die(self):
        super().remove_from_sprite_lists()

class Warrior(Attacker):
    def __init__(self, typeId, beingSelected, scaling):
        self._warriorTypeId = typeId
        self._beingSelected = beingSelected
        self._placedOnBoard = False
        super().__init__(f"images/warriors/{typeId}/0.png", scaling)

    def getWarriorTypeId(self):
        return self._warriorTypeId 

    def setWarriorTypeId(self, typeId):
        self._warriorTypeId = typeId

    def getBeingSelected(self):
        return self._beingSelected 

    def setBeingSelected(self, beingSelected):
        self._beingSelected = beingSelected

    def getPlacedOnBoard(self):
        return self._placedOnBoard
    
    def setPlacedOnBoard(self, placedOnBoard):
        self._placedOnBoard = placedOnBoard
    
    def draw_health_bar(self):
        if self._health > 0:
            width = (self._health / self._maxHealth) * super().width
            arcade.draw_rectangle_filled(super().center_x, super().bottom - 3, width, constants.HEALTH_BAR_HEIGHT, arcade.color.GREEN)

"""
    Test dragon class for the Dragon Spawner
    (More functions and attributes need to be added to complete this class)
"""
class Dragon(Attacker):
    def __init__(self, typeId, absoluteVelocity, movingPath, scaling = 0.5):
        self._dragonTypeId = typeId
        self._movingPath = movingPath
        self._currentPathIndex = 0
        self._absoluteVelocity = absoluteVelocity
        super().__init__(f"images/dragons/{typeId}/0.png", scaling)

    def getDragonTypeId(self):
        return self._dragonTypeId

    def setDragonTypeId(self, typeId):
        self._dragonTypeId = typeId

    def getPath(self):
        return self._movingPath
    
    def setPath(self, movingPath):
        self._movingPath = movingPath
    
    def getAbsoluteVelocity(self):
        return self._absoluteVelocity
    
    def setAbsoluteVelocity(self, absoluteVelocity):
        self._absoluteVelocity = absoluteVelocity

    def getCurrentDestTileIndex(self):
        return self._movingPath[self._currentPathIndex]

    def popCurrentDestTileIndex(self):
        if (self._currentPathIndex < len(self._movingPath) - 1):
            self._currentPathIndex += 1

    def setVelocityByDestTile(self, tile):
        distanceToLocation = arcade.get_distance_between_sprites(self, tile)
        scaler = self._absoluteVelocity / distanceToLocation
        change_x = scaler * ( tile.center_x - self.center_x )
        change_y = scaler * ( tile.center_y - self.center_y )
        super().setVelocity(change_x, change_y)

    def draw_health_bar(self):
        if self._health > 0:
            width = (self._health / self._maxHealth) * super().width
            arcade.draw_rectangle_filled(super().center_x, super().bottom - 3, width, constants.HEALTH_BAR_HEIGHT, arcade.color.RED)