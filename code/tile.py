import arcade
class Tile(arcade.Sprite):
    def __init__(self, imagePath = "images/tiles/normalTile.png", scaling = 1.0):
        self._occupied = False
        self._warriorOccupied = ""
        super().__init__(imagePath, scaling)

    def getOccupied(self):
        return self._occupied

    def getWarriorOccupied(self):
        return self._warriorOccupied

    def setOccupied(self, occupied):
        self._occupied = occupied

    def setWarrior(self, warriorOccupied):
        self._warriorOccupied = warriorOccupied
    
    def highlightedMode(self):
        super().set_texture(1)
    
    def normalMode(self):
        super().set_texture(0)