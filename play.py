import arcade
from app import MyGame, constants as c


def main():
    """Main method."""
    game = MyGame(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
