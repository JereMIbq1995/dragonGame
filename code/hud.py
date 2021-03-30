import arcade
from code.warrior import Warrior

class HUD():
    def __init__(self,windowWidth,windowHight,warriorTypes):
        self._spriteSize = 150
        self._windowWidth = windowWidth
        self._windowHight = windowHight
        self._blockWidth = self._windowWidth / 20

        self._warriorTypes = warriorTypes

        self._types = arcade.SpriteList()

        for warriorId in self._warriorTypes:
            self._types.append(arcade.Sprite(filename = f"images/warriors/{warriorId}/0.png",scale = self._blockWidth / self._spriteSize,image_width = self._spriteSize,image_height = self._spriteSize))

    def getWarrior(self,mouseX,mouseY):
        i = 0
        for sprite in self._types:
            if sprite.collides_with_point((mouseX,mouseY)):
                warrior = Warrior(self._warriorTypes[i],True,1)
                self._types.pop(i)
                self._warriorTypes.pop(i)
                return warrior
            i += 1
        return(None)

    def putWarriorInHUD(warriorId):
        self._types.append(arcade.Sprite(filename = f"images/warriors/{warriorId}/0.png",scale = self._blockWidth / self._spriteSize,image_width = self._spriteSize,image_height = self._spriteSize))
        self._warriorTypes.append(warriorId)

    def draw(self,health):
        for i in range(len(self._types)):
            self._types[i].center_x = self._windowWidth / 2 - self._blockWidth / 2 + i * self._blockWidth
            self._types[i].center_y = self._windowHight * 0.05
            arcade.draw_rectangle_outline(self._types[i].center_x,self._types[i].center_y,self._blockWidth,self._blockWidth,(0,0,0),2)
        self._types.draw()
        arcade.draw_text(f"Health: {health}",0,0,(0,0,0),30)