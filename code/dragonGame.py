import arcade
import json
from code import constants
from code.tile import Tile
from code.stage import Stage
# from code.attacker import Warrior, Dragon
# from code.hud import HUD

class DragonGame:
    def __init__(self):
        # self._hud = HUD()
        self._warriorSelected = False
        self._selectedWarrior = None
        self._stage = Stage("stages/stage1.json")
    
    def handleMouseMotion(self, mouse_x, mouse_y, dx, dy):
        for tile in self._stage.getTiles():
            if tile.collides_with_point((mouse_x, mouse_y)):
                tile.highlightedMode()
            if not tile.collides_with_point((mouse_x, mouse_y)):
                tile.normalMode()
        
        if (self._warriorSelected):
            self._selectedWarrior.center_x = mouse_x
            self._selectedWarrior.center_y = mouse_y
    
    def handleMousePress(self, mouse_x, mouse_y, button, modifiers):
        if (not self._warriorSelected):
            for warrior in self._stage.getWarriors():
                if warrior.collides_with_point((mouse_x, mouse_y)):
                    self._warriorSelected = True
                    self._selectedWarrior = warrior
                    break
        else:
            self._warriorSelected = False
            self._selectedWarrior = None

    def handleMouseRelease(self, mouse_x, mouse_y, button, modifiers):
        pass

    def update(self):
        self._stage.getAllSprites().update()

    def draw(self):
        self._stage.getAllSprites().draw()
        # self._hud.draw()