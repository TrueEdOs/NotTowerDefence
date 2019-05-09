import config.settings as c
import config.colors as color

from models.TextObject import TextObject


class Button():
    def __init__(self, x, y, width, height, caption, bg_color, on_clicked=lambda x : None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = TextObject(caption, c.font, c.menu_button_text_size, color.blue)

    def draw(self, surface):
        self.text.draw(surface, self.x, self.y)
