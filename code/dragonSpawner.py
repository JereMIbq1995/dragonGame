import arcade
from code.attacker import Dragon
class DragonSpawner:
    def __init__(self, spawnList, dragonPaths, stage, spawnLocation):
        self._spawnList = spawnList
        self._dragonPaths = dragonPaths
        self._spawnLocationX = spawnLocation[0]
        self._spawnLocationY = spawnLocation[1]
        self._stage = stage
        self._timer = 0
    
    def startSpawning(self):
        self._timer = 0
        arcade.schedule(self._spawnDragon, 0.1)
    
    def _spawnDragon(self, delta_time: float):
        self._timer += delta_time
        if (len(self._spawnList) > 0 and self._timer >= self._spawnList[0]["timeSpawn"]):
            typeId = self._spawnList[0]["type"]
            absoluteVelocity = self._spawnList[0]["absoluteVelocity"]
            movingPath = self._dragonPaths[self._spawnList[0]["path"]]
            currentDestTile = self._stage.getTileSprites()[movingPath[0]]

            newDragon = Dragon(typeId, absoluteVelocity, movingPath, 0.4)
            newDragon.center_x = self._spawnLocationX
            newDragon.center_y = self._spawnLocationY
            newDragon.setVelocityByDestTile(currentDestTile)
            
            self._stage.addDragon(newDragon)
            self._spawnList.pop(0)