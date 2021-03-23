import arcade

class DragonGame(arcade.Window):

    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.SCREEN_TITLE = "Dragon Game"

        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        # Draw stuff here