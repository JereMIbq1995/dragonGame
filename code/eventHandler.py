from code.attacker import Warrior
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