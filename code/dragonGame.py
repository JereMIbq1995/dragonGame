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
        self._stage = Stage("stages/stage1.json")
        self._hud = HUD(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self._stage.getWarriorTypes())
        self._eventHandler = EventHandler()
        self._stage.startSpawningDragon()

    def handleMouseMotion(self, mouse_x, mouse_y, dx, dy):
        self._eventHandler.handleHighlightingSprites(self._stage.getTileSprites(), mouse_x, mouse_y)
        self._eventHandler.handleStickingWarriorToMouse(mouse_x, mouse_y)
        self._eventHandler.handleShowingWarriorRange(self._stage.getWarriorSprites(), mouse_x, mouse_y)
    
    def handleMousePress(self, mouse_x, mouse_y, button, modifiers):
        selectingMode = self._eventHandler.getSelectingMode()
        if (selectingMode):
            self._eventHandler.handleWarriorSelection(self._hud, mouse_x, mouse_y, self._stage)
        else:
            self._eventHandler.handleWarriorPlacement(self._stage.getTileSprites(), self._hud, mouse_x, mouse_y)

    def handleMouseRelease(self, mouse_x, mouse_y, button, modifiers):
        self._mousePress = False

    def update(self):
        self._stage.getAllSprites().update()
        self._eventHandler.handleDragonsMovement(self._stage)
        self._eventHandler.handleDragonReachesCastle(self._stage)
        self._eventHandler.handleWarriorAttack(self._stage)
        self._eventHandler.handleDamageToDragons(self._stage)

    def draw(self):
        self._stage.getAllSprites().draw()

        for dragon in self._stage.getDragonSprites():
            dragon.drawHealthBar()

        for warrior in self._stage.getWarriorSprites():
            warrior.drawHealthBar()
            warrior.drawRange()

        self._hud.draw(self._stage.getCastleHealth(), self._stage.getNumDragonsDead(), self._stage.getNumDragons())
