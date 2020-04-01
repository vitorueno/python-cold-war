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
                 text="Sair",font_size=20,font_name=CHERNOBYL_FONT,
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
                                SCREEN_HEIGHT/2 - 50, 110, 50, "Jogar", 
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
        
        self.button_list.append(QuitButton(self, SCREEN_WIDTH/2,
                                SCREEN_HEIGHT/2 - 150, 110, 50,
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
            
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        super().on_draw()
        
        
class Choose_side(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)
        self.background = arcade.load_texture(BG_CHOOSE_SIDE)
        self.side = None
        self.eua = arcade.Sprite(EUA_SIDE,center_x=SCREEN_WIDTH/2 + 2,center_y=SCREEN_HEIGHT/2 - 46)
        self.urss = arcade.Sprite(URSS_SIDE,center_x=SCREEN_WIDTH/2 - 1,center_y=SCREEN_HEIGHT/2 - 46)
        self.button_list.append(Button(self, Menu(), SCREEN_WIDTH/2 - 280,
                                30, 160, 40, "Voltar ao Menu", 15, 
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))

    def set_mission_button(self):
        self.button_list.append(Button(self, Mission(), SCREEN_WIDTH/2 + 280,
                                30, 160, 40, "Primeira missão", 15, 
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        if self.side is not None:
            arcade.draw_text(f'Lado: {self.side}',SCREEN_WIDTH/2 ,20,arcade.color.WHITE,20,
                             anchor_x="center",font_name=OLD_FONT1)
            if self.side == 'EUA':
                self.eua.draw()
            else:
                self.urss.draw()
        super().on_draw()
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        point = (_x,_y)
        if _button == arcade.MOUSE_BUTTON_LEFT:
            if self.urss.collides_with_point(point) and not \
                self.eua.collides_with_point(point):
                self.side = 'EUA'
                self.set_mission_button()
            elif not self.urss.collides_with_point(point) and \
                self.eua.collides_with_point(point) :
                self.side = 'URSS'
                self.set_mission_button()
        super().on_mouse_press(_x,_y,_button,_modifiers)
    
        
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