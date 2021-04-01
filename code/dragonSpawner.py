import arcade
from code.attacker import Dragon
class DragonSpawner:
    def __init__(self, spawnList, stage, spawnLocation):
        self._spawnList = spawnList
        self._spawnLocationX = spawnLocation[0]
        self._spawnLocationY = spawnLocation[1]
        self._stage = stage
        self._timer = 0
    
    def startSpawning(self):
        self._timer = 0
        arcade.schedule(self._spawnDragon, 0.1)
    
    def _spawnDragon(self):
        self._timer += 0.1
        if (self._timer >= self._spawnList[0]["timeSpawn"]):
            newDragon = Dragon(self._spawnList[0]["type"], 0.5)
            newDragon.center_x = self._spawnLocationX
            newDragon.center_y = self._spawnLocationY
            stage.addDragon(newDragon)
            self._spawnList.pop(0)