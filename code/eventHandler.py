class EventHandler:
    def __init__(self):
        self._warriorSelected = None
    
    def handleWarriorSelection(self, hud, mouse_x, mouse_y, stage):
        self._warriorSelected = hud.getWarrior(mouse_x, mouse_y)
        if (not self._warriorSelected == None):
            stage.addWarrior(self._warriorSelected)

    def handleWarriorPlacement(self, tiles, hud, mouse_x, mouse_y):
        if (not self._warriorSelected == None):
            for tile in tiles:
                if tile.collides_with_point((mouse_x, mouse_y)):
                    self._warriorSelected.center_x = mouse_x
                    self._warriorSelected.center_y = mouse_y
                    tile.setOccupied(True)
                    break
            self._warriorSelected = None
                

    def handleHighlightingSprites(self):
        pass

    def handleStickingWarriorToMouse(self, mouse_x, mouse_y):
        if (not self._warriorSelected == None):
            self._warriorSelected.center_x = mouse_x
            self._warriorSelected.center_y = mouse_y