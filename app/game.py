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
        
class Button_Create_chapter(Button):
    def __init__(self, view, next_view, ui_manager, id, x=0, y=0, width=100,
                height=40, text='Button', align='center', font_size=20):
        super().__init__(view, next_view, ui_manager, id, x, y, width, height, text, align,
                         font_size)
        self.payload = None
        
    def set_payload(self, chapter_text, side):
        self.payload = {"name": chapter_text, "country": side}
        
    def on_click(self):
        if self.payload is not None:
            try:    
                requests.post(f'{BASE_URL}/chapters', json = self.payload)
            except:
                self.view.window.show_view(Menu())
            else:
                self.view.window.show_view(self.next_view)
        else:
            self.view.window.show_view(Menu())
            
            
class Button_Create_Mission(Button):
    def __init__(self, view, next_view, ui_manager, id, x=0, y=0, width=100,
                height=40, text='Button', align='center', font_size=20):
        super().__init__(view, next_view, ui_manager, id, x, y, width, height, text, align,
                         font_size)
        self.payload = None
        
    def set_payload(self, title, description, text_btn_1, text_btn_2, first_mission, id_chapter):
        self.payload = {"title": title,
                        "description": description,
                        "text_button_1":text_btn_1,
                        "text_button_2":text_btn_2,
                        "href_button_1": None,
                        "href_button_2": None,
                        "first_mission": first_mission,
                        "id_chapter": id_chapter,
                        }
        
    def on_click(self):
        if self.payload is not None:
            try:    
                requests.post(f'{BASE_URL}/missions', json = self.payload)
            except:
                self.view.window.show_view(Menu())
            else:
                self.view.window.show_view(self.next_view)
        else:
            self.view.window.show_view(Menu())

class Button_Link_Mission(Button):
    def __init__(self, view, next_view, ui_manager, id, x=0, y=0, width=100,
                height=40, text='Button', align='center', font_size=20):
        super().__init__(view, next_view, ui_manager, id, x, y, width, height, text, align,
                         font_size)
        self.payload = None
        self.mission_id = None
        
    def set_payload(self, href_btn_1, href_btn_2, mission_id):
        self.payload = {"href_button_1": href_btn_1, "href_button_2": href_btn_2}
        self.mission_id = mission_id
        
    def on_click(self):
        if self.payload is not None:
            try:    
                requests.put(f'{BASE_URL}/missions/{self.mission_id}', json=self.payload)
            except:
                self.view.window.show_view(Menu())
            else:
                self.view.window.show_view(self.next_view)
        else:
            self.view.window.show_view(Menu())

class Button_Create_Newspaper(Button): 
    def __init__(self, view, next_view, ui_manager, id, x=0, y=0, width=100,
                height=40, text='Button', align='center', font_size=20):
        super().__init__(view, next_view, ui_manager, id, x, y, width, height, text, align,
                         font_size)
        self.payload = None
        
    def set_payload(self, headline, subtitle, text, image_path, id_chapter):
        self.payload = {"headline": headline,
                        "subtitle": subtitle,
                        "text":text,
                        "image_path":image_path, 
                        "id_chapter":id_chapter 
                        }
        
    def on_click(self):
        if self.payload is not None:
            try:    
                requests.post(f'{BASE_URL}/newspapers', json = self.payload)
            except:
                self.view.window.show_view(Menu())
            else:
                self.view.window.show_view(self.next_view)
        else:
            self.view.window.show_view(Menu())

class Check_box(UIFlatButton):
    def __init__(self, 
                id,
                ui_manager,
                x=0,
                y=0,
                width=100,
                height=40,
                text='',
                align='center',
                bg_color=arcade.color.WHITE,  
                bg_color_hover = arcade.color.GRAY,
                bg_color_press = arcade.color.BLUE, 
                border_color=arcade.color.BLACK,
                border_color_hover=arcade.color.BLACK, 
                border_color_press=arcade.color.BLACK):
        
        super().__init__(text, x, y, width, height, align, id)

        self.style.set_class_attrs(
            id,
            bg_color=bg_color,
            bg_color_hover=bg_color_hover,
            bg_color_press=bg_color_press,
            border_color=border_color,
            border_color_hover=border_color_hover,
            border_color_press=border_color_press
        )

        self.pressed = False
        self.checkbox_list = None
        self.title = None
        self.ui_manager = ui_manager

    def set_checkbox_list(self, checkbox_list):
        self.checkbox_list = checkbox_list
    
    def set_title(self, title):
        self.title = title
    
    def set_father_id(self, id):
        self.father_id = id 
    
    def on_click(self):
        if self.checkbox_list is not None:
            for c in self.checkbox_list:
                checkbox = self.ui_manager.find_by_id(c.id)
                checkbox.pressed = False
                
        if not self.pressed:
            self.pressed = True
        else:
            self.pressed = False
        
    # def on_press(self):
    #     if not self.other_checkbox.pressed: 
    #         if self.pressed:
    #             self.pressed = False
    #             self.face_color = self.highlight_color = self.shadow_color = self.color
    #         else:
    #             self.pressed = True
                
    # def on_release(self):
    #     if not self.other_checkbox.pressed:
    #         if self.pressed:
    #             self.face_color = self.highlight_color = self.shadow_color = self.clicked

class Input(arcade.gui.UIInputBox):
    def __init__(self, id, x=0, y=0, width=100, height=40, text='', 
                font_name=OLD_FONT1,
                font_size=12,
                font_color=arcade.color.BLACK,
                font_color_hover=arcade.color.BLACK,
                font_color_focus=arcade.color.BLACK,
                border_width= 3,
                border_color= arcade.color.BLACK,
                border_color_hover= arcade.color.GRAY,
                border_color_focus=arcade.color.BLACK,
                bg_color=arcade.color.WHITE,
                bg_color_hover=arcade.color.WHITE,
                bg_color_focus=arcade.color.WHITE,
                vmargin=10,
                margin_left=15):
    
        super().__init__(x, y, width, height, text, id)
        
        self.style.set_class_attrs(
            id,
            font_name=font_name,
            font_size=font_size,
            font_color=font_color,
            font_color_hover=font_color_hover,
            font_color_focus=font_color_focus,
            border_width= border_width,
            border_color= border_color,
            border_color_hover= border_color_hover,
            border_color_focus=border_color_focus,
            bg_color=bg_color,
            bg_color_hover=bg_color_hover,
            bg_color_focus=bg_color_focus,
            vmargin=vmargin,
            margin_left=margin_left
        )


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
                            SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50, 110,
                            50, 'Jogar')
        self.ui_manager.add_ui_element(play_button)
        
        create_btn = Button(self, Create(), self.ui_manager, 'create_btn',
                            SCREEN_WIDTH/2, SCREEN_HEIGHT//2 - 120, 110,
                            50, 'Criar')
        self.ui_manager.add_ui_element(create_btn)
        
        quit_button = QuitButton('sair',SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 190, 
                                110, 50, 'Sair')
        
        self.ui_manager.add_ui_element(quit_button)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    
class Choose_side(arcade.View):
    def __init__(self, creating=None):
        super().__init__()
        self.ui_manager = UIManager()
        self.creating = creating
    
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
        if self.creating is None:
            menu_button = Button(self, Menu(), self.ui_manager,'menu', 
                                SCREEN_WIDTH//2-280, 30, 160,40,
                                'Voltar ao Menu', font_size=15)
            
            self.ui_manager.add_ui_element(menu_button)
        else:
            go_back_button = Button(self, Create(), self.ui_manager,'go_back_btn', 
                                SCREEN_WIDTH//2-280, 30, 160,40,
                                'Voltar', font_size=15)
            self.ui_manager.add_ui_element(go_back_button)
            
    def set_mission_button(self):
        # self.ui_manager.purge_ui_elements()        
        # self.setup()
        btn_already_exist = self.ui_manager.find_by_id('missao')
        if btn_already_exist:
            btn_already_exist.next_view = Choose_Chapter(self.side, self.creating) # updating destination
            
        else: # we must create it for the first time
            
            btn_text = 'Primeira missão'
            if self.creating is not None:
                btn_text = 'Prosseguir Criação'
                
            mission_button = Button(self, Choose_Chapter(self.side, self.creating),
                                self.ui_manager, 'missao', SCREEN_WIDTH//2 + 280,
                                30, 200, 40, btn_text, font_size=15)
            
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
    def __init__(self, side='EUA', creating=None):
        super().__init__()
        self.ui_manager = UIManager()
        self.side = side
        self.creating = creating
        
    def on_show_view(self):
        arcade.set_background_color(arcade.color.CYAN)
        self.background = arcade.load_texture(BG_CHOOSE_CHAPTER)
        self.setup()
    
    def setup(self):
        go_back_button = Button(self, Choose_side(self.creating), self.ui_manager, 
                            'side', SCREEN_WIDTH//2-280, 30, 160,40, 'Voltar', 
                            font_size=15)
        
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
            
            next_view = Mission(mission_id)
            if self.creating is not None:
                next_view = self.creating
                
                if type(self.creating) == Create_Mission:
                    self.creating.set_side(self.side)
                    self.creating.set_chapter(chapters[i]['id'])
                    
                elif type(self.creating) == Link_mission:
                    next_view = Choose_Mission(side=self.side,chapter=chapters[i]['id'], creating=self.creating)
                
                elif type(self.creating) == Create_Newspaper:
                    self.creating.set_side(self.side)
                    self.creating.set_chapter(chapters[i]['id'])
                
            button = Button(self, next_view, self.ui_manager,
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

class Choose_Mission(arcade.View):
    def __init__(self, side='EUA', chapter=None, creating=None):
        super().__init__()
        self.ui_manager = UIManager()
        self.side = side
        self.chapter = chapter
        self.creating = creating
        
        
    def set_side(self,side):
        self.side = side 

    def set_chapter(self,chapter):
        self.chapter = chapter 
    
    def on_show_view(self):
        arcade.set_background_color((146,116,82))
        # self.background = arcade.load_texture(BG_CHOOSE_CHAPTER)
        self.setup()
    
    def setup(self):
        go_back_button = Button(self, Choose_Chapter(self.side, Link_mission()), self.ui_manager, 
                            'side', SCREEN_WIDTH//2-280, 30, 160,40, 'Voltar', 
                            font_size=15)
        
        self.ui_manager.add_ui_element(go_back_button)
        
        request = requests.get(f'{BASE_URL}/missions?chapterId={self.chapter}')
        missions = request.json()
        
        spacing_y = 60
        for i in range(len(missions)):
            next_view = Link_mission(chapter=self.chapter, side=self.side)
            next_view.set_mission(mission_id=missions[i]['id'])
            button = Button(self, next_view, self.ui_manager, 'M' + str(missions[i]['id']),
                            SCREEN_WIDTH//2, SCREEN_HEIGHT - 100 - (i * spacing_y), 200, 30,
                            missions[i]['title'], font_size=15)
            
            self.ui_manager.add_ui_element(button)
            
    def on_draw(self):
        arcade.start_render()
        # arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
        #                                     self.background,0,255)
        arcade.draw_text(f'Escolha de Missão:', SCREEN_WIDTH//2, 
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
        next_view_1 = None
        next_view_2 = None
        href_btn_1 = self.mission['href_button_1']
        href_btn_2 = self.mission['href_button_2']
        
        #button 1
        if 'M' in href_btn_1.upper():
            next_view_1 = Mission(id=href_btn_1[2:])
        elif 'N' in href_btn_1.upper():
            next_view_1 = Newspaper(id=href_btn_1[2:])
        # elif 'r' in href_btn_1:
        #     next_view = Report(href_btn_1[2:])
        
        #button 2
        if 'M' in href_btn_2.upper():
            next_view_2 = Mission(href_btn_2[2:])
        elif 'N' in href_btn_2.upper():
            next_view_2 = Newspaper(href_btn_2[2:])
        # elif 'r' in href_btn_2:
        #     next_view = Report(href_btn_2[2:])
        
        txt_btn_1 = self.mission['text_button_1']
        button_1 = Button(self, next_view_1, self.ui_manager, 'btn_1',
                        SCREEN_WIDTH//2 - 280, 40, 160, 40, txt_btn_1, font_size=15)
        
        self.ui_manager.add_ui_element(button_1)
        
        txt_btn_2 = self.mission['text_button_2']
        button_2 = Button(self, next_view_2, self.ui_manager, 'btn_2',
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
        parsed_text = self.break_lines(text, 35)
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


class Create(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        
    def on_show_view(self):
        arcade.set_background_color(arcade.color.PINK_LACE)
        self.background = arcade.load_texture(BG_CHOOSE_CHAPTER)
        self.setup()
    
    def setup(self):
        create_chapter_btn = Button(self, Create_chapter(), self.ui_manager, 
                            'create_chapter_btn', SCREEN_WIDTH//2,
                            SCREEN_HEIGHT//2 + 80, 250, 50, 'Criar Capítulo')
        
        self.ui_manager.add_ui_element(create_chapter_btn)
        
        create_mission_btn = Button(self, Choose_side(Create_Mission()), self.ui_manager, 
                            'create_mission_btn', SCREEN_WIDTH//2,
                            SCREEN_HEIGHT//2 + 20, 250, 50, 'Criar Missão')
        
        self.ui_manager.add_ui_element(create_mission_btn)
        
        link_mission_btn = Button(self, Choose_side(Link_mission()), self.ui_manager, 
                            'link_mission_btn', SCREEN_WIDTH//2,
                            SCREEN_HEIGHT//2 - 40, 250, 50, 'Ligar missões')

        self.ui_manager.add_ui_element(link_mission_btn)
        
        create_newspaper_btn = Button(self, Choose_side(Create_Newspaper()), self.ui_manager, 
                            'create_newspaper_btn', SCREEN_WIDTH//2,
                            SCREEN_HEIGHT//2 - 100, 250, 50, 'Criar Jornal')

        self.ui_manager.add_ui_element(create_newspaper_btn)

        menu_btn = Button(self, Menu(), self.ui_manager, 'menu_btn', 
                          SCREEN_WIDTH//2 - 280, 40, 200, 40, 
                          'Voltar ao Menu', font_size=15)
        
        self.ui_manager.add_ui_element(menu_btn)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        arcade.draw_text('Criação', SCREEN_WIDTH//2, SCREEN_HEIGHT-80,
                        arcade.color.WHITE, 40 , align='center', 
                        anchor_x='center', font_name=CHERNOBYL_FONT)
        
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
        

class Create_chapter(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        
    def on_show_view(self):
        arcade.set_background_color(arcade.color.GREEN_YELLOW)
        self.background = arcade.load_texture(BG_CHOOSE_CHAPTER)
        self.setup()
    
    def setup(self):
        go_back_button = Button(self, Create(), self.ui_manager, 'go_back_button', 
                          SCREEN_WIDTH//2 - 280, 40, 200, 40, 
                          'Voltar', font_size=15)
        
        self.ui_manager.add_ui_element(go_back_button)
        
        chapter_name_inpt = Input('chapter_name_inpt',SCREEN_WIDTH//2, 
                                  SCREEN_HEIGHT//2 + 80, 250, 50, '')
        self.ui_manager.add_ui_element(chapter_name_inpt)
        
        eua_check_box = Check_box('eua_checkbox', self.ui_manager, SCREEN_WIDTH//2-50, 
                                SCREEN_HEIGHT//2 - 50, 20, 20)
        
        urss_check_box = Check_box('urss_checkbox', self.ui_manager, SCREEN_WIDTH//2+50, 
                                SCREEN_HEIGHT//2 - 50, 20, 20,
                                bg_color_press=arcade.color.RED)
        
        checkbox_list = [eua_check_box, urss_check_box]
        eua_check_box.set_checkbox_list(checkbox_list)
        urss_check_box.set_checkbox_list(checkbox_list)
        
        self.ui_manager.add_ui_element(eua_check_box)
        self.ui_manager.add_ui_element(urss_check_box)
        
        confirm_btn = Button_Create_chapter(self, Create(), self.ui_manager,
                                            'create_chapter_btn', SCREEN_WIDTH//2,
                                            SCREEN_HEIGHT//2 - 125, 200, 40,
                                            'Criar Capítulo', font_size=15)
        self.ui_manager.add_ui_element(confirm_btn)
    
    def on_update(self, delta_time):
        input = self.ui_manager.find_by_id('chapter_name_inpt')
        text = input.text
        
        eua_checkbox = self.ui_manager.find_by_id('eua_checkbox')
        urss_checkbox = self.ui_manager.find_by_id('urss_checkbox')
        
        side = ''
        if eua_checkbox.pressed:
            side = 'EUA'
        elif urss_checkbox.pressed:
            side = 'URSS'    
    
        button = self.ui_manager.find_by_id('create_chapter_btn')
        
        if len(text) > 0 and len(side) > 0: 
            button.set_payload(text, side)
            
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        arcade.draw_text('Criar Capítulo', SCREEN_WIDTH//2, SCREEN_HEIGHT-80,
                        arcade.color.WHITE, 40, align='center', 
                        anchor_x='center', font_name=CHERNOBYL_FONT)
        
        arcade.draw_text('Informe o Nome do Capítulo', SCREEN_WIDTH//2, SCREEN_HEIGHT//2+110,
                        arcade.color.WHITE, 16, align='center', 
                        anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Selecione o País Da Missão', SCREEN_WIDTH//2, SCREEN_HEIGHT//2,
                        arcade.color.WHITE, 16, align='center', 
                        anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('EUA', SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2- 35,
                        arcade.color.WHITE, 12, align='center', 
                        anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('URSS', SCREEN_WIDTH//2 + 50, SCREEN_HEIGHT//2 - 35,
                        arcade.color.WHITE, 12, align='center', 
                        anchor_x='center', font_name=OLD_FONT1)
        
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
        
        
class Create_Mission(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.side = None
        self.chapter = None
        
        # self.screen_top = SCREEN_HEIGHT
        # self.screen_right = SCREEN_WIDTH
        # self.screen_bottom = 0
        # self.screen_left = 0
        
        # self.left_missions_list = []
        # self.right_missions_list = []
        # self.spacing_y = 60

    def set_side(self, side):
        self.side = side
                
    def set_chapter(self, chapter):
        self.chapter = chapter
    
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BRONZE)
        self.background = arcade.load_texture(BG_CHOOSE_CHAPTER)
        self.setup()
    
    def setup(self):
        name_inpt = Input('name_inpt',SCREEN_WIDTH//2, 
                        SCREEN_HEIGHT//2 + 160, 250, 50, '')
        self.ui_manager.add_ui_element(name_inpt)
        
        description_inpt_1 = Input('description_inpt_1',SCREEN_WIDTH//2, 
                                SCREEN_HEIGHT//2 + 70, 500, 50, '')
        description_inpt_2 = Input('description_inpt_2',SCREEN_WIDTH//2, 
                                SCREEN_HEIGHT//2 + 20, 500, 50, '')
        description_inpt_3 = Input('description_inpt_3',SCREEN_WIDTH//2, 
                                SCREEN_HEIGHT//2 - 30, 500, 50, '')
        
        self.ui_manager.add_ui_element(description_inpt_1)
        self.ui_manager.add_ui_element(description_inpt_2)
        self.ui_manager.add_ui_element(description_inpt_3)
        
        txt_btn_1_inpt = Input('txt_btn_1_inpt',SCREEN_WIDTH//2 - 150, 
                                SCREEN_HEIGHT//2 - 125, 170, 50, '')
        self.ui_manager.add_ui_element(txt_btn_1_inpt)
        
        txt_btn_2_inpt = Input('txt_btn_2_inpt',SCREEN_WIDTH//2 + 150, 
                                SCREEN_HEIGHT//2 - 125, 170, 50, '')
        
        self.ui_manager.add_ui_element(txt_btn_2_inpt)
        
        go_back_button = Button(self, Choose_Chapter(self.side, Create_Mission()),
                        self.ui_manager, 'go_back_button', SCREEN_WIDTH//2 - 280,
                        40, 200, 40, 'Voltar', font_size=15)
        self.ui_manager.add_ui_element(go_back_button)
        
        confirm_btn = Button_Create_Mission(self, Create(), self.ui_manager,
                                            'create_mission_btn', SCREEN_WIDTH//2 + 280,
                                            40, 200, 40, 'Criar Missão', font_size=15)
        self.ui_manager.add_ui_element(confirm_btn)
        
        is_first_checkbox = Check_box('is_first_checkbox', self.ui_manager, SCREEN_WIDTH//2,
                                     SCREEN_HEIGHT//2 - 195, 20, 20) 
        self.ui_manager.add_ui_element(is_first_checkbox)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        
        arcade.draw_text(f'Criar Missão: {self.side} - Cap. {self.chapter}', 
                        SCREEN_WIDTH//2, SCREEN_HEIGHT-80,
                        arcade.color.WHITE, 40, align='center', 
                        anchor_x='center', font_name=CHERNOBYL_FONT)
        
        arcade.draw_text('Informe o Nome da Missão', SCREEN_WIDTH//2,
                        SCREEN_HEIGHT//2+190, arcade.color.WHITE, 16,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Informe a Descrição da Missão', SCREEN_WIDTH//2,
                        SCREEN_HEIGHT//2+100, arcade.color.WHITE, 16,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Texto do Botão 1', SCREEN_WIDTH//2 - 150,
                        SCREEN_HEIGHT//2 - 95, arcade.color.WHITE, 14,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Texto do Botão 2', SCREEN_WIDTH//2 + 150,
                        SCREEN_HEIGHT//2 - 95, arcade.color.WHITE, 14,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('É a Primeira Missão do Capítulo?', SCREEN_WIDTH//2,
                        SCREEN_HEIGHT//2 - 180, arcade.color.WHITE, 14,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
    
    def on_update(self, delta_time):
        title_inpt = self.ui_manager.find_by_id('name_inpt')
        title = title_inpt.text 
        
        description_inpt_1 = self.ui_manager.find_by_id('description_inpt_1')
        description_inpt_2 = self.ui_manager.find_by_id('description_inpt_2')
        description_inpt_3 = self.ui_manager.find_by_id('description_inpt_3')
        text = description_inpt_1.text + ' ' + description_inpt_2.text + ' ' + description_inpt_3.text
        
        txt_btn_1_inpt = self.ui_manager.find_by_id('txt_btn_1_inpt')
        txt_1 = txt_btn_1_inpt.text
        
        
        txt_btn_2_inpt = self.ui_manager.find_by_id('txt_btn_2_inpt')        
        txt_2 = txt_btn_2_inpt.text
        
        btn_confirm = self.ui_manager.find_by_id('create_mission_btn')     
        
        is_first_checkbox = self.ui_manager.find_by_id('is_first_checkbox')
        first = is_first_checkbox.pressed
        
        #txt_btn_2_inpt is optionally, so it doesn't need to be filled
        fields_filled = len(title) > 0 and len(text) > 0 and len(txt_1) > 0 
            
        if fields_filled:
            btn_confirm.set_payload(title, text, txt_1, txt_2, first, self.chapter)

    
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
        
        
class Create_Newspaper(arcade.View):
    def __init__(self, side=None, chapter=None):
        super().__init__()
        self.ui_manager = UIManager()
        self.side = side 
        self.chapter = chapter
    
    def set_side(self, side):
        self.side = side 
        
    def set_chapter(self, chapter):
        self.chapter = chapter             
        
    def on_show_view(self):
        arcade.set_background_color(arcade.color.PINK_LACE)
        self.background = arcade.load_texture(BG_CHOOSE_CHAPTER)
        self.setup()
    
    def setup(self):
        go_back_button = Button(self, Create(), self.ui_manager, 'go_back_button', 
                          SCREEN_WIDTH//2 - 280, 40, 200, 40, 
                          'Voltar', font_size=15)
        
        self.ui_manager.add_ui_element(go_back_button)
        
        headline_inpt = Input('headline_inpt',SCREEN_WIDTH//2, 
                            SCREEN_HEIGHT//2 + 150, 250, 50, '')
        self.ui_manager.add_ui_element(headline_inpt)
        
        subtitle_inpt = Input('subtitle_inpt',SCREEN_WIDTH//2, 
                            SCREEN_HEIGHT//2 + 60, 250, 50, '')
        self.ui_manager.add_ui_element(subtitle_inpt)
        
        text_inpt_1 = Input('text_inpt_1',SCREEN_WIDTH//2, 
                            SCREEN_HEIGHT//2 - 30, 500, 50, '')
        self.ui_manager.add_ui_element(text_inpt_1)
        
        text_inpt_2 = Input('text_inpt_2',SCREEN_WIDTH//2, 
                            SCREEN_HEIGHT//2- 80, 500, 50, '')
        self.ui_manager.add_ui_element(text_inpt_2)
        
        text_inpt_3 = Input('text_inpt_3',SCREEN_WIDTH//2, 
                            SCREEN_HEIGHT//2- 130, 500, 50, '')
        self.ui_manager.add_ui_element(text_inpt_3)
        
        confirm_btn = Button_Create_Newspaper(self, Create(), self.ui_manager,
                                            'create_newspaper_btn', SCREEN_WIDTH//2 + 280,
                                            40, 200, 40, 'Criar Jornal', font_size=15)
        self.ui_manager.add_ui_element(confirm_btn)
    
    def on_update(self, delta_time):
        headline_inpt = self.ui_manager.find_by_id('headline_inpt')
        headline_txt = headline_inpt.text 
        
        subtitle_inpt = self.ui_manager.find_by_id('subtitle_inpt')
        subtitle_txt = subtitle_inpt.text 
        
        text_inpt_1 = self.ui_manager.find_by_id('text_inpt_1')
        text_inpt_2 = self.ui_manager.find_by_id('text_inpt_2')
        text_inpt_3 = self.ui_manager.find_by_id('text_inpt_3')
        text = text_inpt_1.text + ' ' + text_inpt_2.text + ' ' + text_inpt_3.text
        
        confirm_btn = self.ui_manager.find_by_id('create_newspaper_btn')
        
        fields_filled = len(headline_txt) > 0 and len(subtitle_txt) > 0 and len(text) > 0
        if fields_filled:
            image = f'app/img/background/{self.side}_flag.png'
            confirm_btn.set_payload(headline_txt, subtitle_txt, text, image, self.chapter)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)

        arcade.draw_text(f'Criar Jornal: {self.side} - Cap. {self.chapter}', 
                        SCREEN_WIDTH//2, SCREEN_HEIGHT-80,
                        arcade.color.WHITE, 40, align='center', 
                        anchor_x='center', font_name=CHERNOBYL_FONT)

        arcade.draw_text('Informe a Manchete da Notícia:', SCREEN_WIDTH//2, 
                        SCREEN_HEIGHT//2+180, arcade.color.WHITE, 16,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Informe o subtítulo da Notícia:', SCREEN_WIDTH//2, 
                        SCREEN_HEIGHT//2+90, arcade.color.WHITE, 16,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Informe o Texto da Notícia:', SCREEN_WIDTH//2, 
                        SCREEN_HEIGHT//2, arcade.color.WHITE, 16,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
        
        
class Link_mission(arcade.View):
    def __init__(self, chapter=None, side=None):
        super().__init__()
        self.ui_manager = UIManager()
        self.chapter = chapter
        self.side = side
        
        self.screen_top = SCREEN_HEIGHT
        self.screen_right = SCREEN_WIDTH
        self.screen_bottom = 0
        self.screen_left = 0
        
        self.left_missions_list = []
        self.right_missions_list = []
        
        self.left_newspapers_list = []
        self.right_newspapers_list = []
        
        self.left_checkbox = []
        self.right_checkbox = []
        
        self.spacing_y = 60
    
    def set_mission(self, mission_id):
        m = requests.get(f'{BASE_URL}/missions/{mission_id}') 
        self.mission = m.json()
        
    def on_show_view(self):
        arcade.set_background_color((146,116,82))
        # self.background = arcade.load_texture(BG_CHOOSE_CHAPTER)
        self.setup()
    
    def setup(self):
        go_back_button = Button(self, Choose_Mission(self.side, self.chapter, Link_mission()),
                        self.ui_manager, 'go_back_button', SCREEN_WIDTH//2 - 340,
                        SCREEN_HEIGHT-30, 100, 40, 'Voltar', font_size=15)
        self.ui_manager.add_ui_element(go_back_button)
        
        m = requests.get(f'{BASE_URL}/missions?chapterId={self.chapter}')
        missions = m.json()
        
        for i in range(len(missions)):
            left_checkbox = Check_box('lM_' + str(missions[i]['id']), self.ui_manager,
                                    SCREEN_WIDTH//2 - 250, 
                                    SCREEN_HEIGHT//2 + 30 - (self.spacing_y * i), 20, 20)
            left_checkbox.set_title(missions[i]['title'])
            
            right_checkbox = Check_box('rM_' + str(missions[i]['id']), self.ui_manager, 
                                    SCREEN_WIDTH//2 + 250, 
                                    SCREEN_HEIGHT//2 + 30 - (self.spacing_y * i), 20, 20,
                                    bg_color_press=arcade.color.RED)
            
            right_checkbox.set_title(missions[i]['title'])
            # right_checkbox.set_father_id(missions[i]['id'])
            
            self.left_missions_list.append(left_checkbox)
            self.right_missions_list.append(right_checkbox)
            
            self.left_checkbox.append(left_checkbox)
            self.right_checkbox.append(right_checkbox)
        
        for checkbox in self.left_missions_list:
            checkbox.set_checkbox_list(self.left_checkbox)
            self.ui_manager.add_ui_element(checkbox) 
        
        for checkbox in self.right_missions_list:
            checkbox.set_checkbox_list(self.right_checkbox)
            self.ui_manager.add_ui_element(checkbox)
        
        n = requests.get(f'{BASE_URL}/newspapers?chapterId={self.chapter}')
        newspapers = n.json()
        
        for i in range(len(newspapers)):
            left_checkbox = Check_box('lN_' + str(newspapers[i]['id']), self.ui_manager,
                                    SCREEN_WIDTH//2 - 100, 
                                    SCREEN_HEIGHT//2 + 30 - (self.spacing_y * i), 20, 20)
            left_checkbox.set_title(newspapers[i]['headline'])
            
            right_checkbox = Check_box('rN_' + str(newspapers[i]['id']), self.ui_manager, 
                                    SCREEN_WIDTH//2 + 100, 
                                    SCREEN_HEIGHT//2 + 30 - (self.spacing_y * i), 20, 20,
                                    bg_color_press=arcade.color.RED)
            right_checkbox.set_title(newspapers[i]['headline'])
            
            self.left_newspapers_list.append(left_checkbox)
            self.right_newspapers_list.append(right_checkbox)
            
            self.left_checkbox.append(left_checkbox)
            self.right_checkbox.append(right_checkbox)
        
        for checkbox in self.left_newspapers_list:
            checkbox.set_checkbox_list(self.left_checkbox)
            self.ui_manager.add_ui_element(checkbox) 
        
        for checkbox in self.right_newspapers_list:
            checkbox.set_checkbox_list(self.right_checkbox)
            self.ui_manager.add_ui_element(checkbox)
        
        confirm_btn = Button_Link_Mission(self, Create(), self.ui_manager,
                                            'button_link_mission', SCREEN_WIDTH//2 + 340,
                                            SCREEN_HEIGHT-30, 100, 40, 'Confirmar', font_size=15)
        self.ui_manager.add_ui_element(confirm_btn)
    
    def on_update(self, delta_time):
        left_checked = None
        for checkbox in self.left_checkbox:
            if checkbox.pressed:
                left_checked = checkbox.id
        
        right_checked = None
        for checkbox in self.right_checkbox:
            if checkbox.pressed:
                right_checked = checkbox.id 
        
        button_link_mission = self.ui_manager.find_by_id('button_link_mission')
        
        if left_checked is not None:
            # lM_1[1:] => M_1
            href_button_1 = left_checked[1:]
            
            if right_checked is not None: 
                href_button_2 = right_checked[1:]
            else:
                href_button_2 = None
            
            button_link_mission.set_payload(href_button_1, href_button_2, self.mission['id'])
            
    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_text(f'Ligar Missão: {self.side} - Cap. {self.chapter}', SCREEN_WIDTH//2, SCREEN_HEIGHT-50,
                        arcade.color.WHITE, 25, align='center', 
                        anchor_x='center', font_name=CHERNOBYL_FONT)
        
        arcade.draw_text(f"Título Missão: {self.mission['title']}", SCREEN_WIDTH//2,
                        SCREEN_HEIGHT//2+200, arcade.color.WHITE, 14,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text(f"descrição: {self.mission['description']}", SCREEN_WIDTH//2,
                        SCREEN_HEIGHT//2+170, arcade.color.WHITE, 14,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text(f"Texto Botão 1: {self.mission['text_button_1']}", SCREEN_WIDTH//2 - 150,
                        SCREEN_HEIGHT//2+140, arcade.color.WHITE, 14,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text(f"Texto Botão 2: {self.mission['text_button_2']}", SCREEN_WIDTH//2 + 150,
                        SCREEN_HEIGHT//2+140, arcade.color.WHITE, 14,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Destino do Botão 1', SCREEN_WIDTH//2 - 150,
                        SCREEN_HEIGHT//2+ 100, arcade.color.WHITE, 14,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Destino do Botão 2', SCREEN_WIDTH//2 + 150,
                        SCREEN_HEIGHT//2+100, arcade.color.WHITE, 14,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Missões', SCREEN_WIDTH//2 - 250,
                        SCREEN_HEIGHT//2+ 70, arcade.color.WHITE, 13,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Missões', SCREEN_WIDTH//2 + 250,
                        SCREEN_HEIGHT//2+ 70, arcade.color.WHITE, 13,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Jornais', SCREEN_WIDTH//2 - 100,
                        SCREEN_HEIGHT//2+ 70, arcade.color.WHITE, 13,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        arcade.draw_text('Jornais', SCREEN_WIDTH//2 + 100,
                        SCREEN_HEIGHT//2+ 70, arcade.color.WHITE, 13,
                        align='center', anchor_x='center', font_name=OLD_FONT1)
        
        for i in range(len(self.left_missions_list)):
            arcade.draw_text(self.left_missions_list[i].title, SCREEN_WIDTH//2 - 250,
                        SCREEN_HEIGHT//2 + 40 - (self.spacing_y * i),
                        arcade.color.WHITE, 12, align='center', 
                        anchor_x='center', font_name=OLD_FONT1)

        for i in range(len(self.right_missions_list)):
            arcade.draw_text(self.right_missions_list[i].title, SCREEN_WIDTH//2 + 250,
                        SCREEN_HEIGHT//2 + 40 - (self.spacing_y * i),
                        arcade.color.WHITE, 12, align='center', 
                        anchor_x='center', font_name=OLD_FONT1)
            
        for i in range(len(self.left_newspapers_list)):
            arcade.draw_text(self.left_newspapers_list[i].title, SCREEN_WIDTH//2 - 100,
                        SCREEN_HEIGHT//2 + 40 - (self.spacing_y * i),
                        arcade.color.WHITE, 12, align='center', 
                        anchor_x='center', font_name=OLD_FONT1)

        for i in range(len(self.right_newspapers_list)):
            arcade.draw_text(self.right_newspapers_list[i].title, SCREEN_WIDTH//2 + 100,
                        SCREEN_HEIGHT//2 + 40 - (self.spacing_y * i),
                        arcade.color.WHITE, 12, align='center', 
                        anchor_x='center', font_name=OLD_FONT1)
    
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        scroll_multiplier = 50
        
        self.screen_top += scroll_y * scroll_multiplier
        self.screen_bottom += scroll_y * scroll_multiplier
        
        if self.screen_top > SCREEN_HEIGHT:
            self.screen_top = SCREEN_HEIGHT
        if self.screen_bottom > 0:
            self.screen_bottom = 0
            
        arcade.set_viewport(self.screen_left, self.screen_right,
                            self.screen_bottom, self.screen_top)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    