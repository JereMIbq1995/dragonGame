class Attacker(arcade.Sprite):
    def __init__(self), path, scaling:
        self._health = 0.0
        self._atk = 0.0
        self._attackRange = 0.0
        self._isAlive = bool

        super().__init__(f"images/tiles/{typeId}.png", scaling)

#Damage function takes health and applies the damage to it
    def takeDamage(damage):
        self._health = self._health - damage
    

    def attack():
        pass

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health


    def get_atk(self):
        return self._atk

    def set_atk(self, atk):
        self._atk = atk


    def get_attackRange(self):
        return self._attackRange

    def set_attackRange(self, attackRange):
        self.attackRange = attackRange


class Warrior(Attacker):
    def __init__(self, typeId, beingSelected, scaling):
        self._warriorTypeId = int 
        self._beingSelected= bool
        self._PlacedOnBoard= bool
        super().__init__(f"images/tiles/warriors/{typeId}.png", scaling)

    def get_warriorTypeId(self):
        return self._warriorTypeId 

    def set_warriorTypeId(self, typeId):
        self._warriorTypeId = typeId

    def get_beingSelected(self):
        return self._beingSelected 

    def set_beingSelected(self, beingSelected):
        self._beingSelected = beingSelected

    def get_PlacedOnBoard(self):
        return self._PlacedOnBoard
    
    def set_PlacedOnBoard(self, PlacedOnBoard):
        self._PlacedOnBoard = PlacedOnBoard

