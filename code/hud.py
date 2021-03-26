import arcade

class HUD():
    def __init__(self,windowWidth,windowHight):
        self._score = 0
        self._health = 100

        self._spriteSize = 10
        self._windowWidth = windowWidth
        self._windowHight = windowHight
        self._blockWidth = self._windowWidth / 20
        self._mouseSprite = arcade.Sprite("images/blankTexture.png",scale = self._blockWidth / self._spriteSize,image_width = self._spriteSize,image_height = self._spriteSize)

        with open("resources/warriorTypes.txt","r") as warriorTypesFile:
            size = 0
            for line in warriorTypesFile:
                size += 1
        with open("resources/warriorTypes.txt","r") as warriorTypesFile:
            self._types = arcade.SpriteList()
            i = 0
            for line in warriorTypesFile:
                locationX = self._windowWidth / 2 - size * self._blockWidth / 2 + i * self._blockWidth
                locationY = self._windowHight * 0.05
                self._types.append(arcade.Sprite(filename = f"images/warriors/{line.strip()}/0.png",scale = self._blockWidth / self._spriteSize,image_width = self._spriteSize,image_height = self._spriteSize,center_x = locationX,center_y = locationY))
                self._mouseSprite.textures.append(arcade.load_texture(f"images/warriors/{line.strip()}/0.png"))
                i+=1

    def update(self,mouseX,mouseY,pressed):
        self._mouseSprite.center_x = mouseX
        self._mouseSprite.center_y = mouseY
        i = 1
        moving = False
        for sprite in self._types:
            if sprite.collides_with_point((mouseX,mouseY)) and pressed:
                self._mouseSprite.set_texture(i)
                moving = True
            i += 1
            if not pressed and moving:
                self._mouseSprite.set_texture(0)
                return(i)
        return(0)


    def draw(self):
        for i in range(len(self._types)):
            arcade.draw_rectangle_outline(self._types[i].center_x,self._types[i].center_y,self._blockWidth,self._blockWidth,(0,0,0),2)
        self._types.draw()