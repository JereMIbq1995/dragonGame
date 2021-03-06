import arcade
class Tile(arcade.Sprite):
    def __init__(self, typeId, scaling = 0.4):
        self._occupied = False
        self._warriorOccupied = ""
        self._typeId = typeId
        super().__init__(f"images/tiles/{typeId}.png", scaling)
        super().append_texture(arcade.load_texture(f"images/tiles/{typeId}_h.png"))

    def getOccupied(self):
        return self._occupied

    def getWarriorOccupied(self):
        return self._warriorOccupied

    def setOccupied(self, occupied):
        self._occupied = occupied

    def setWarrior(self, warriorOccupied):
        self._warriorOccupied = warriorOccupied
    
    def getTypeId(self):
        return self._typeId

    def setTypeId(self, typeId):
        self._typeId = typeId 
    
    def highlightedMode(self):
        super().set_texture(1)
    
    def normalMode(self):
        super().set_texture(0)