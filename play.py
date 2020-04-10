import arcade
from app import (Menu, Create_phase ,Choose_side, Mission, Newspaper,
                constants as c)


def main():
    """Main method."""
    window = arcade.Window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT,c.SCREEN_TITLE)
    menu = Menu()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()
    
