import arcade
class Attacker(arcade.Sprite):
    def __init__(self, path, scaling):
        self._health = 0.0
        self._atk = 0.0
        self._attackRange = 0.0
        self._isAlive = bool

        super().__init__(path, scaling)

#Damage function takes health and applies the damage to it
    def takeDamage(damage):
        self._health = self._health - damage
    
    def attack():
        pass

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

"""
    Test dragon class for the Dragon Spawner
    (More functions and attributes need to be added to complete this class)
"""
class Dragon(Attacker):
    def __init__(self, typeId, scaling):
        self._dragonTypeId = typeId
        super().__init__(f"images/dragons/{typeId}/0.png", scaling)

    def getDragonTypeId(self):
        return self._dragonTypeId

    def setDragonTypeId(self, typeId):
        self._dragonTypeId = typeId