import arcade

class Warrior(arcade.Sprite):
    def __init__(self, filePath = "images/warriors/bob.png", scale = 1.0):
        super().__init__(filePath, scale)
