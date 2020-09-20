import arcade
import json
import requests
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
        # self.ui_manager.purge_ui_elements()        
        # self.setup()
        btn_already_exist = self.ui_manager.find_by_id('missao')
        if btn_already_exist:
            btn_already_exist.next_view = Choose_Chapter(self.side) # updating destination
            
        else: # we must create it for the first time
            mission_button = Button(self, Choose_Chapter(self.side), self.ui_manager,
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

class Choose_Chapter(arcade.View):
    def __init__(self, side='EUA'):
        super().__init__()
        self.ui_manager = UIManager()
        self.side = side
        
    def on_show_view(self):
        arcade.set_background_color(arcade.color.CYAN)
        self.background = arcade.load_texture(BG_CHOOSE_CHAPTER)
        self.setup()
    
    def setup(self):
        go_back_button = Button(self, Choose_side(), self.ui_manager,'side', 
                            SCREEN_WIDTH//2-280, 30, 160,40,
                            'Voltar', font_size=15)
        self.ui_manager.add_ui_element(go_back_button)
        
        request = requests.get(f'{BASE_URL}/chapters?side={self.side}')
        chapters = request.json()
        
        for i in range(len(chapters)):
            mission_id = ''
            chapter_id = chapters[i]['id']
            r_chapter_missions = requests.get(f'{BASE_URL}/missions?chapterId={chapter_id}')
            chapter_missions = r_chapter_missions.json()
            for mission in chapter_missions:
                if mission['first_mission'] == 1:
                    mission_id = mission['id']
                
            button = Button(self, Mission(mission_id), self.ui_manager,
                            chapters[i]['id'], SCREEN_WIDTH//2,
                            SCREEN_HEIGHT - (i * 40) - 100 , 200, 30,
                            chapters[i]['name'], font_size=15) 
            self.ui_manager.add_ui_element(button)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        arcade.draw_text(f'Escolha de capítulo: {self.side}',SCREEN_WIDTH//2, 
                        SCREEN_HEIGHT-50,arcade.color.WHITE,25, align='center',
                        anchor_x='center', font_name=CHERNOBYL_FONT)
        
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
        
class Mission(arcade.View):
    def __init__(self, id):
        super().__init__()
        self.ui_manager = UIManager()
        request = requests.get(f'{BASE_URL}/missions/{id}')
        self.mission = request.json()
        
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.top_secret = arcade.load_texture(TOP_SECRET)
        self.setup()
        
    def setup(self):
        next_view = None
        href_btn_1 = self.mission['href_button_1']
        href_btn_2 = self.mission['href_button_2']
        

        #button 1
        if 'm' in href_btn_1:
            next_view = Mission(href_btn_1[2:])
        elif 'n' in href_btn_1:
            next_view = Newspaper(href_btn_1[2:])
        # elif 'r' in href_btn_1:
        #     next_view = Report(href_btn_1[2:])
        
        #button 2
        if 'm' in href_btn_2:
            next_view = Mission(href_btn_2[2:])
        elif 'n' in href_btn_2:
            next_view = Newspaper(href_btn_2[2:])
        # elif 'r' in href_btn_2:
        #     next_view = Report(href_btn_2[2:])
        
        txt_btn_1 = self.mission['text_button_1']
        button_1 = Button(self, next_view, self.ui_manager, 'btn_1',
                        SCREEN_WIDTH//2 - 280, 40, 160, 40, txt_btn_1, font_size=15)
        self.ui_manager.add_ui_element(button_1)
        
        txt_btn_2 = self.mission['text_button_2']
        button_2 = Button(self, next_view, self.ui_manager, 'btn_2',
                        SCREEN_WIDTH//2 + 280, 40, 160, 40, txt_btn_2, font_size=15)
        self.ui_manager.add_ui_element(button_2)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.mission['title'], 520, 510,
                         arcade.color.BLACK, font_size=40,
                         anchor_x='center',font_name=OLD_FONT2)
        
        text = self.mission['description']
        parsed_text = self.break_lines(text)
        
        arcade.draw_text(parsed_text, SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 20,
                         arcade.color.BLACK, 25, align='center', anchor_x='center', 
                         anchor_y='center', font_name=OLD_FONT2)
        arcade.draw_lrwh_rectangle_textured(14, 475,247, 116, self.top_secret,0,255)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
        
    def break_lines(self, text, max_length=35):
        chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
        parsed_text = ''
        for chunk in chunks:
            parsed_text += chunk + '\n' 
        return parsed_text

class Newspaper(arcade.View):
    def __init__(self, id):
        super().__init__()
        self.ui_manager = UIManager()
        request = requests.get(f'{BASE_URL}/newspapers/{id}')
        self.newspaper = request.json()
            
    def on_show(self):
        arcade.set_background_color(arcade.color.GRAY_BLUE)
        self.background = arcade.load_texture(BG_NEWSPAPER)
        self.astronaut = arcade.Sprite(ASTRONAUT,center_x=616,center_y=224)
        self.setup()
        
    def setup(self):
        menu_button = Button(self, Menu(), self.ui_manager, 'menu_end_game',
                              616, 40, 160, 40, 'Voltar ao Menu', font_size=15)
        self.ui_manager.add_ui_element(menu_button)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        arcade.draw_text(self.newspaper['headline'], 400, 419, arcade.color.BLACK,
                        font_size=45, anchor_x='center',font_name=OLD_FONT1)
        arcade.draw_text(self.newspaper['subtitle'], 220 , 337,arcade.color.BLACK,
                        font_size=20, anchor_x='center',font_name=OLD_FONT1)
        
        text = self.newspaper['text']
        parsed_text = self.break_lines(LOREM, 35)
        arcade.draw_text(parsed_text, 235, 273,arcade.color.GRAY,
                        font_size=14, anchor_x='center',anchor_y='top',
                        font_name=OLD_FONT2)
        self.astronaut.draw()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
        
    def break_lines(self, text, max_length=35):
        chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
        parsed_text = ''
        for chunk in chunks:
            parsed_text += chunk + '\n' 
        return parsed_text
