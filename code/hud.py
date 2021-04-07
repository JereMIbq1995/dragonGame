import arcade
from code.attacker import Warrior

class HUD():
    def __init__(self,windowWidth,windowHeight,warriorTypes):
        self._spriteSize = 174
        self._windowWidth = windowWidth
        self._windowHeight = windowHeight
        self._blockWidth = self._windowWidth / 20

        self._warriorTypes = warriorTypes
        self._selectionSprites = arcade.SpriteList()
        self._setUpTypes()
        self._lastTypePosition = (self._selectionSprites[-1].center_x, self._selectionSprites[-1].center_y)

        self._lastSelectedPosition = (0,0)


    def _setUpTypes(self):
        index = 0
        for warriorId in self._warriorTypes:
            warriorType = arcade.Sprite(filename = f"images/warriors/{warriorId}/0.png",scale = self._blockWidth / self._spriteSize,image_width = self._spriteSize,image_height = self._spriteSize)
            warriorType.center_x = self._windowWidth / 2 - self._blockWidth / 2 + index * self._blockWidth
            warriorType.center_y = self._windowHeight * 0.05
            self._selectionSprites.append(warriorType)
            index += 1

    def getWarrior(self,mouseX,mouseY):
        i = 0
        for sprite in self._selectionSprites:
            if sprite.collides_with_point((mouseX,mouseY)):
                warrior = Warrior(self._warriorTypes[i],True,self._blockWidth / self._spriteSize)
                warrior.center_x = mouseX
                warrior.center_y = mouseY
                self._lastSelectedPosition = (self._selectionSprites[i].center_x, self._selectionSprites[i].center_y)
                self._selectionSprites.pop(i)
                self._warriorTypes.pop(i)
                return warrior
            i += 1
        return(None)

    def putWarriorInHUD(self, warriorId):
        # self._selectionSprites.append(arcade.Sprite(filename = f"images/warriors/{warriorId}/0.png",scale = self._blockWidth / self._spriteSize,image_width = self._spriteSize,image_height = self._spriteSize))
        self._warriorTypes.append(warriorId)
        warrior = arcade.Sprite(filename = f"images/warriors/{warriorId}/0.png",scale = self._blockWidth / self._spriteSize,image_width = self._spriteSize,image_height = self._spriteSize)
        warrior.center_x = self._lastSelectedPosition[0]
        warrior.center_y = self._lastSelectedPosition[1]
        self._selectionSprites.append(warrior)

    def draw(self,health, numDragonsDead, totalDragons):
        # arcade.draw_rectangle_outline(self._selectionSprites[i].center_x,self._selectionSprites[i].center_y,self._blockWidth,self._blockWidth,(0,0,0),2)
        self._selectionSprites.draw()
        arcade.draw_text(f"Health: {health}",0,0,(0,0,0),30)
        arcade.draw_text(f"Dragons: {numDragonsDead}/{totalDragons}", self._lastTypePosition[0] + 0.1*self._windowWidth, 0, (0,0,0), 30)