import arcade
from .constants import *
from arcade.gui import *


class Button(TextButton):
    def __init__(self, view,next_view, x=0, y=0, width=100, height=40, 
                 text="Button",font_size=20,font_name=CHERNOBYL_FONT,
                 font_color=arcade.color.WHITE,face=arcade.color.GRAY, 
                 highlight=arcade.color.WHITE,shadow=arcade.color.BLACK,
                 btn_height=7):
        
        super().__init__(x, y, width, height, text,font_size,CHERNOBYL_FONT,
                         font_color,face,highlight,shadow,btn_height)
        self.view = view
        self.next_view = next_view

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            print("Pressed")
            self.pressed = False
            self.view.window.show_view(self.next_view)
            

class QuitButton(TextButton):
    def __init__(self, view, x=0, y=0, width=100, height=40, 
                 text="Quit",font_size=20,font_name=CHERNOBYL_FONT,
                 font_color=arcade.color.WHITE,face=arcade.color.GRAY, 
                 highlight=arcade.color.WHITE,shadow=arcade.color.BLACK,
                 btn_height=7):
        
        super().__init__(x, y, width, height, text,font_size,CHERNOBYL_FONT,
                         font_color,face,highlight,shadow,btn_height)
        self.view = view

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            arcade.close_window()

class Menu(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.RED_DEVIL)
        self.background = arcade.load_texture(BG_MENU)
        self.set_buttons()

    
    def set_buttons(self):
        self.button_list.append(Button(self, Choose_side(), SCREEN_WIDTH/2,
                                SCREEN_HEIGHT/2 - 50, 110, 50, "Play", highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
        self.button_list.append(QuitButton(self, SCREEN_WIDTH/2,
                                SCREEN_HEIGHT/2 - 150, 110, 50,highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
            
    def on_draw(self):
        arcade.start_render()
        scale = SCREEN_WIDTH / self.background.width
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        super().on_draw()
        #draw background
        
        
class Choose_side(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Choose your side", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        mission = Mission()
        self.window.show_view(mission)
        
        
class Mission(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Mission", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        newspaper = Newspaper()
        self.window.show_view(newspaper)
        
        
class Newspaper(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.GRAY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Newspaper", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        menu = Menu()
        self.window.show_view(menu)