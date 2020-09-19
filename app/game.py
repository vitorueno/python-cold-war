import arcade
import json
from .constants import *

import arcade.gui
from arcade.gui import UIFlatButton, UIManager
from arcade.gui.ui_style import UIStyle
        
        
class Button(arcade.gui.UIFlatButton):
    def __init__(self, view, next_view, ui_manager, id,
                x=0,
                y=0,
                width=100,
                height=40,
                text='Button',
                align='center',
                font_size=20, 
                font_name=CHERNOBYL_FONT, 
                font_color=arcade.color.WHITE, 
                font_color_hover=arcade.color.WHITE,
                font_color_press=arcade.color.WHITE,
                bg_color=arcade.color.GRAY,  
                bg_color_hover = arcade.color.GRAY,
                bg_color_press = arcade.color.GRAY, 
                border_color=arcade.color.DARK_GRAY,
                border_color_hover=arcade.color.DARK_GRAY, 
                border_color_press=arcade.color.WHITE):
        
        super().__init__(text, x, y, width, height, align, id)
        
        self.style.set_class_attrs(
            id,
            font_color=font_color,
            font_color_hover=font_color_hover,
            font_color_press=font_color_press,
            font_name=font_name,
            font_size=font_size,
            bg_color=bg_color,
            bg_color_hover=bg_color_hover,
            bg_color_press=bg_color_press,
            border_color=border_color,
            border_color_hover=border_color_hover,
            border_color_press=border_color_press
        )
        
        self.view = view
        self.next_view = next_view
        self.ui_manager = ui_manager


    def on_click(self):
        self.view.window.show_view(self.next_view)
            

class QuitButton(arcade.gui.UIFlatButton):
    def __init__(self, id, 
                x=0, 
                y=0, 
                width=100, 
                height=40,
                text='Button', 
                align='center',
                font_size=20,
                font_name=CHERNOBYL_FONT, 
                font_color=arcade.color.WHITE,
                font_color_hover=arcade.color.WHITE, 
                font_color_press=arcade.color.WHITE,
                bg_color=arcade.color.GRAY,  
                bg_color_hover = arcade.color.GRAY,
                bg_color_press = arcade.color.GRAY, 
                border_color=arcade.color.DARK_GRAY,
                border_color_hover=arcade.color.DARK_GRAY,
                border_color_press=arcade.color.WHITE):
        
        super().__init__(text, x, y, width, height,align,id)
        self.style.set_class_attrs(
            id,
            font_color=font_color,
            font_color_hover=font_color_hover,
            font_color_press=font_color_press,
            font_size=font_size,
            font_name=font_name,
            bg_color=bg_color,
            bg_color_hover=bg_color_hover,
            bg_color_press=bg_color_press,
            border_color=border_color,
            border_color_hover=border_color_hover,
            border_color_press=border_color_press
        )
        
    def on_click(self):
        arcade.close_window()
        

class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        
    def on_show_view(self):
        arcade.set_background_color(arcade.color.RED_DEVIL)
        self.background = arcade.load_texture(BG_MENU)
        self.setup()
    
    def setup(self):
        play_button = Button(self, Choose_side(), self.ui_manager, 'jogar',
                            SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50, 110,
                            50, 'Jogar')
        self.ui_manager.add_ui_element(play_button)
        
        quit_button = QuitButton('sair',SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 150, 
                                110, 50, 'Sair')
        self.ui_manager.add_ui_element(quit_button)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    
class Choose_side(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
    
    def on_show(self):
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)
        self.background = arcade.load_texture(BG_CHOOSE_SIDE)
        self.side = None
        self.eua = arcade.Sprite(EUA_SIDE,center_x=SCREEN_WIDTH/2 + 2,
                                 center_y=SCREEN_HEIGHT/2 - 46)
        self.urss = arcade.Sprite(URSS_SIDE,center_x=SCREEN_WIDTH/2 - 1,
                                  center_y=SCREEN_HEIGHT/2 - 46)
        self.setup()
        
        
    def setup(self):
        menu_button = Button(self, Menu(), self.ui_manager,'menu', 
                            SCREEN_WIDTH//2-280, 30, 160,40,
                            'Voltar ao Menu', font_size=15)
        
        self.ui_manager.add_ui_element(menu_button)

    def set_mission_button(self):
        self.ui_manager.purge_ui_elements()        
        self.setup()
        mission_button = Button(self, Mission('test.json'), self.ui_manager,
                            'missao', SCREEN_WIDTH//2 + 280, 30, 160, 40,
                            'Primeira missão', font_size=15)
        self.ui_manager.add_ui_element(mission_button)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        if self.side is not None:
            arcade.draw_text(f'Lado: {self.side}', SCREEN_WIDTH/2 ,20,
                             arcade.color.WHITE,20,anchor_x='center',
                             font_name=OLD_FONT1)
            if self.side == 'EUA':
                self.eua.draw()
            else:
                self.urss.draw()
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        point = (_x,_y)
        if _button == arcade.MOUSE_BUTTON_LEFT:
            if self.urss.collides_with_point(point) and not \
                self.eua.collides_with_point(point):
                self.side = 'EUA'
                self.set_mission_button()
            elif not self.urss.collides_with_point(point) and \
                self.eua.collides_with_point(point):
                self.side = 'URSS'
                self.set_mission_button()
        super().on_mouse_press(_x,_y,_button,_modifiers)
    
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
        
        
class Mission(arcade.View):
    def __init__(self,file_name):
        super().__init__()
        self.ui_manager = UIManager()
        with open(f'{MISSIONS}/{file_name}', encoding='utf-8') as file:
            self.mission = json.load(file)
        
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.top_secret = arcade.load_texture(TOP_SECRET)
        self.setup()
        
    def setup(self):
        if self.mission['destn1'] is not None:
            next_view1 = Mission(self.mission['destn1']) 
        else:
            next_view1 = Newspaper(self.mission['newspaper'])
        if self.mission['destn2'] is not None:
            next_view2 = Mission(self.mission['destn2']) 
        else:
            next_view2 = Newspaper(self.mission['newspaper'])
        
        choose_button_1 = Button(self, next_view1, self.ui_manager, 'choose_1', 
                                 SCREEN_WIDTH//2 - 280, 40, 160, 40, 
                                 self.mission['btn_name1'])
        self.ui_manager.add_ui_element(choose_button_1)
        
        choose_button_2 = Button(self, next_view2, self.ui_manager, 'choose_2',
                                  SCREEN_WIDTH//2 + 280, 40, 160, 40, 
                                  self.mission['btn_name2'])
        self.ui_manager.add_ui_element(choose_button_2)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.mission['title'], 520, 510,
                         arcade.color.BLACK, font_size=40,
                         anchor_x='center',font_name=OLD_FONT2)
        arcade.draw_text(self.mission['text'], SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150,
                         arcade.color.BLACK, 25,align='center', anchor_x='center',
                         font_name=OLD_FONT2)
        arcade.draw_lrwh_rectangle_textured(14, 475,247, 116,
                                            self.top_secret,0,255)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
        
            
class Newspaper(arcade.View):
    def __init__(self,file_name):
        super().__init__()
        self.ui_manager = UIManager()
        with open(f'{NEWSPAPER}/{file_name}',encoding='utf-8') as file:
            self.newspaper = json.load(file)
            
    def on_show(self):
        arcade.set_background_color(arcade.color.GRAY_BLUE)
        self.background = arcade.load_texture(BG_NEWSPAPER)
        self.astronaut = arcade.Sprite(ASTRONAUT,center_x=616,center_y=224)
        self.setup()
        
    def setup(self):
        menu_button = Button(self, Menu(), self.ui_manager, 'menu_end_game',
                              616,40, 160, 40, 'Voltar ao Menu', font_size=15)
        self.ui_manager.add_ui_element(menu_button)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        arcade.draw_text(self.newspaper['news_title'], 400, 419, arcade.color.BLACK,
                        font_size=45, anchor_x='center',font_name=OLD_FONT1)
        arcade.draw_text(self.newspaper['news_subtitle'], 220 , 337,arcade.color.BLACK,
                        font_size=20, anchor_x='center',font_name=OLD_FONT1)
        arcade.draw_text(self.newspaper['news_text'], 235, 273,arcade.color.GRAY,
                        font_size=14, anchor_x='center',anchor_y='top',
                        font_name=OLD_FONT2)
        self.astronaut.draw()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()