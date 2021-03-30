import arcade
import json
from code import constants
from code.tile import Tile
from code.stage import Stage
# from code.attacker import Warrior, Dragon
from code.hud import HUD
from code.eventHandler import EventHandler

class DragonGame:
    def __init__(self):
        self._eventHandler = EventHandler()
        self._hud = HUD(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self._stage = Stage("stages/stage1.json")
    
    def handleMouseMotion(self, mouse_x, mouse_y, dx, dy):
        self._eventHandler.handleHighlightingSprites(self._stage.getTiles(), mouse_x, mouse_y)
        self._eventHandler.handleStickingWarriorToMouse(mouse_x, mouse_y)
    
    def handleMousePress(self, mouse_x, mouse_y, button, modifiers):
        self._eventHandler.handleWarriorSelection(self._hud, mouse_x, mouse_y, self._stage)
        self._eventHandler.handleWarriorPlacement(self._stage.getTiles(), self._hud, mouse_x, mouse_y)

    def handleMouseRelease(self, mouse_x, mouse_y, button, modifiers):
        self._mousePress = False

    def update(self):
        self._stage.getAllSprites().update()
        self._hud.update(self._mouseX, self._mouseY, self._mousePress)

    def draw(self):
        self._stage.getAllSprites().draw()
        self._hud.draw(self._stage.getHealth())
