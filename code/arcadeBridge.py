from code import constants
from code.dragonGame import DragonGame
import arcade

class ArcadeBridge(arcade.Window):

    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)
        #Declare the game:
        self._dragonGame = DragonGame()

    def on_key_press(self):
        pass

    def on_key_release(self):
        pass

    def on_mouse_press(self):
        pass

    def on_mouse_move(self):
        pass

    def on_mouse_release(self):
        pass

    def on_update(self, delta_time):
        self._dragonGame.update()

    def on_draw(self):
        arcade.start_render()
        # Draw stuff here
        self._dragonGame.draw()