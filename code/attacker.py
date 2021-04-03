import random
from code.projectile import Projectile

class Attacker(arcade.Sprite):
    def __init__(self, path, scaling):
        self._health = 0.0
        self._atk = 0.0
        self._attackRange = 0.0
        self._isAlive = bool
        self._cooldown = 0.0
        self._currentCooldown = 0.0

        super().__init__(path, scaling)

#Damage function takes health and applies the damage to it
    def takeDamage(damage):
        self._health = self._health - damage
    
    def attack(self, attackList):
        if self._currentCooldown <= 0 and attackList != []:
            index = random.randint(0,len(attackList))
            super().angle = math.sin(attackList[index].center_x - self.center_x / attackList[index].center_y - self.center_y)
            projectile = Projectile("images/projectile.png",1)
            projectile.angle = angle
            projectile.change_x(math.cos(angle) * speed)
            projectile.change_y(math.sin(angle) * speed)
            self._currentCooldown = self._cooldown
            return projectile
        else:
            self._currentCooldown -= 0.0166666
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
    