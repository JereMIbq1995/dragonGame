from code.attacker import Warrior
from code import constants
import arcade
import math
class EventHandler:
    def __init__(self):
        self._warriorSelected = None
        self._selectingMode = True    # True: selecting; False: placing
    
    def handleWarriorSelection(self, hud, mouse_x, mouse_y, stage):
        if (self._warriorSelected == None):
            self._warriorSelected = hud.getWarrior(mouse_x, mouse_y)
            if (not self._warriorSelected == None):
                self._warriorSelected.setBeingSelected(True)
                stage.addWarrior(self._warriorSelected)
                self._selectingMode = False
            else:
                self._selectingMode = True


    def handleWarriorPlacement(self, tiles, hud, mouse_x, mouse_y):
        if (not self._warriorSelected == None):
            warriorSet = False
            for tile in tiles:
                if tile.collides_with_point((mouse_x, mouse_y)) and not tile.getOccupied():
                    self._warriorSelected.center_x = tile.center_x
                    self._warriorSelected.center_y = tile.center_y
                    tile.setOccupied(True)
                    self._warriorSelected.setBeingSelected(False)
                    warriorSet = True
                    break
            if (not warriorSet):
                hud.putWarriorInHUD(self._warriorSelected.getWarriorTypeId())
                self._warriorSelected.remove_from_sprite_lists()
            self._warriorSelected = None
            self._selectingMode = True
                

    def handleHighlightingSprites(self, allSprites, mouse_x, mouse_y):
        for sprite in allSprites:
            if sprite.collides_with_point((mouse_x, mouse_y)):
                sprite.highlightedMode()
            else:
                sprite.normalMode()

    def handleStickingWarriorToMouse(self, mouse_x, mouse_y):
        if (not self._warriorSelected == None):
            self._warriorSelected.center_x = mouse_x
            self._warriorSelected.center_y = mouse_y
    
    def getSelectingMode(self):
        return self._selectingMode

    def handleWarriorAttack(self, stage):
        for warrior in stage.getWarriorSprites():
            attackList = []
            for dragon in stage.getDragonSprites():
                if math.sqrt(abs(warrior.center_x - dragon.center_x) * abs(warrior.center_x - dragon.center_x) + abs(warrior.center_y - dragon.center_y) * abs(warrior.center_y - dragon.center_y)) < warrior.get_attackRange():
                    attackList.append(dragon)
            projectile = warrior.attack(attackList)
            if projectile != None:
                stage.addProjectile(projectile)

    def handleDamageToDragons(self, stage):
        for projectile in stage.getProjectileSprites():
            for dragon in stage.getProjectileSprites():
                if projectile.collides_with(dragon):
                    dragon.takeDamage(1)
                    stage.removeProjectile(projectile)
                    pass

    def handleDragonsMovement(self, stage): #dragonSprites, tileSprites):
        dragonSprites = stage.getDragonSprites()
        tileSprites = stage.getTileSprites()
        for dragon in dragonSprites:
                currentDestTile = tileSprites[dragon.getCurrentDestTileIndex()]
                if (arcade.get_distance_between_sprites(dragon, currentDestTile) < constants.REACH_THRESHOLD):
                    dragon.popCurrentDestTileIndex()
                    currentDestTile = tileSprites[dragon.getCurrentDestTileIndex()]
                    dragon.setVelocityByDestTile(currentDestTile)
    
    def handleDragonReachesCastle(self, stage):
        dragonSprites = stage.getDragonSprites()
        castleTile = stage.getCastleTile()
        for dragon in dragonSprites:
            distance = arcade.get_distance_between_sprites(dragon, castleTile)
            if (distance < constants.REACH_THRESHOLD):

                stage.damageCastle(dragon.getAtk())
                stage.removeDragon(dragon)
