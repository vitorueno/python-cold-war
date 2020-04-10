import arcade
import json
from .constants import *
from arcade.gui import *


class Button(TextButton):
    def __init__(self, view,next_view, x=0, y=0, width=100, height=40, 
                 text='Button',font_size=20,font_name=CHERNOBYL_FONT,
                 font_color=arcade.color.WHITE,face=arcade.color.GRAY, 
                 highlight=arcade.color.DARK_GRAY,shadow=arcade.color.DARK_LIVER,
                 btn_height=7):
        
        super().__init__(x, y, width, height, text,font_size,CHERNOBYL_FONT,
                         font_color,face,highlight,shadow,btn_height)
        self.view = view
        self.next_view = next_view

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            self.view.window.show_view(self.next_view)

class QuitButton(TextButton):
    def __init__(self, view, x=0, y=0, width=100, height=40, 
                 text='Sair',font_size=20,font_name=CHERNOBYL_FONT,
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

class Check_box(TextButton):
    def __init__(self, view,other_checkbox, x=0, y=0, width=100, height=40, 
                 color=arcade.color.WHITE,clicked=arcade.color.BLACK,
                 text='',font_size=20,font_name=CHERNOBYL_FONT,
                 font_color=arcade.color.WHITE):
        
        super().__init__(x, y, width, height,text,font_size,font_name,
                         font_color,color,color,color)
        self.view = view
        self.color = color
        self.clicked = clicked
        self.other_checkbox = other_checkbox

    def on_press(self):
        if not self.other_checkbox.pressed: 
            if self.pressed:
                self.pressed = False
                self.face_color = self.highlight_color = self.shadow_color = self.color
            else:
                self.pressed = True
                
    def on_release(self):
        if not self.other_checkbox.pressed:
            if self.pressed:
                self.face_color = self.highlight_color = self.shadow_color = self.clicked
                
                
class Menu(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.RED_DEVIL)
        self.background = arcade.load_texture(BG_MENU)
        self.set_buttons()

    
    def set_buttons(self):
        self.button_list.append(Button(self, Choose_side(), SCREEN_WIDTH/2,
                                SCREEN_HEIGHT/2 - 20, 150, 50, 'Jogar', 
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
        
        self.button_list.append(Button(self, Create_phase(), SCREEN_WIDTH/2,
                                SCREEN_HEIGHT/2 - 120, 150, 50, 'Criar Fases', 
                                16,highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
        
        self.button_list.append(QuitButton(self, SCREEN_WIDTH/2,
                                SCREEN_HEIGHT/2 - 220, 150, 50,
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
            
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        super().on_draw()


class Create_phase(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN)
        self.background = arcade.load_texture(BG_CREATE_PHASE)
        self.set_buttons()
            
    def set_buttons(self):
        self.button_list.append(Button(self, Menu(), SCREEN_WIDTH/2 - 280,
                                50, 160, 40, 'Voltar ao Menu', 15, 
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
        self.eua_btn = Check_box(self, None,SCREEN_WIDTH/2 - 75, SCREEN_HEIGHT-450, 
                                10, 10, color=arcade.color.WHITE,clicked=arcade.color.BLUE)
        self.urss_btn = Check_box(self,self.eua_btn, SCREEN_WIDTH/2 + 75, SCREEN_HEIGHT-450, 
                                10, 10, color=arcade.color.WHITE,clicked=arcade.color.RED)
        self.eua_btn.other_checkbox = self.urss_btn
        self.button_list.append(self.eua_btn)
        self.button_list.append(self.urss_btn)
        
    
        self.button_list.append(Button(self, None, SCREEN_WIDTH/2,
                            SCREEN_HEIGHT-250, 160, 50, 'Criar Missão',
                            15))
            
        self.button_list.append(Button(self, None, SCREEN_WIDTH/2,
                            SCREEN_HEIGHT-350, 160, 50, 'Criar Jornal',
                            15))
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        arcade.draw_text("Criar Fase", SCREEN_WIDTH/2, SCREEN_HEIGHT/2+220,
                         arcade.color.WHITE,50,align='center', anchor_x='center',
                         anchor_y='center',font_name=CHERNOBYL_FONT)
        arcade.draw_text("EUA", SCREEN_WIDTH/2 - 40, SCREEN_HEIGHT/2-150,
                         arcade.color.WHITE,15,align='center', anchor_x='center',
                         anchor_y='center',font_name=OLD_FONT1)
        arcade.draw_text("URSS", SCREEN_WIDTH/2 + 40, SCREEN_HEIGHT/2-150,
                         arcade.color.WHITE,15,align='center', anchor_x='center',
                         anchor_y='center',font_name=OLD_FONT1)
        
        arcade.draw_text("Selecione um dos lados para criar uma missão/jornal", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-180,
                        arcade.color.WHITE,15,align='center', anchor_x='center',
                        anchor_y='center',font_name=OLD_FONT1)
        super().on_draw()
        
    def on_mouse_press(self, x, y, button, modifiers):
        self.eua_btn.check_mouse_press(x,y)
        self.urss_btn.check_mouse_press(x,y)
        self.button_list[0].check_mouse_press(x,y)
    
        if self.eua_btn.pressed:
            self.button_list[3].next_view = Create_mission("EUA")
            self.button_list[4].next_view = Create_newspaper("EUA")
            self.button_list[3].check_mouse_press(x,y)
            self.button_list[4].check_mouse_press(x,y)
        elif self.urss_btn.pressed:
            self.button_list[3].next_view = Create_mission("URSS")
            self.button_list[4].next_view = Create_newspaper("URSS")
            self.button_list[3].check_mouse_press(x,y)
            self.button_list[4].check_mouse_press(x,y)

        
class Create_mission(arcade.View):
    def __init__(self,side):
        super().__init__()
        self.side = side
        
    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN)
        self.background = arcade.load_texture(BG_CREATE_PHASE)
        self.set_buttons()
        
    def set_buttons(self):
        self.button_list.append(Button(self, Create_phase(), SCREEN_WIDTH/2 - 280,
                                50, 160, 40, 'Voltar', 15, highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        arcade.draw_text("Criar Missão", SCREEN_WIDTH/2, SCREEN_HEIGHT/2+220,
                         arcade.color.WHITE,50,align='center', anchor_x='center',
                         anchor_y='center',font_name=CHERNOBYL_FONT)
        super().on_draw()

class Create_newspaper(arcade.View):
    def __init__(self,side):
        super().__init__()
        self.side = side
        
    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN)
        self.background = arcade.load_texture(BG_CREATE_PHASE)
        self.set_buttons()
        
    def set_buttons(self):
        self.button_list.append(Button(self, Create_phase(), SCREEN_WIDTH/2 - 280,
                                50, 160, 40, 'Voltar', 15, highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        arcade.draw_text("Criar Jornal", SCREEN_WIDTH/2, SCREEN_HEIGHT/2+220,
                         arcade.color.WHITE,50,align='center', anchor_x='center',
                         anchor_y='center',font_name=CHERNOBYL_FONT)
        super().on_draw()
    
    
class Choose_side(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)
        self.background = arcade.load_texture(BG_CHOOSE_SIDE)
        self.side = None
        self.eua = arcade.Sprite(EUA_SIDE,center_x=SCREEN_WIDTH/2 + 2,
                                 center_y=SCREEN_HEIGHT/2 - 46)
        self.urss = arcade.Sprite(URSS_SIDE,center_x=SCREEN_WIDTH/2 - 1,
                                  center_y=SCREEN_HEIGHT/2 - 46)
        self.button_list.append(Button(self, Menu(), SCREEN_WIDTH/2 - 280,
                                30, 160, 40, 'Voltar ao Menu', 15, 
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))

    def set_mission_button(self):
        self.button_list.append(Button(self, Mission('test.json'), SCREEN_WIDTH/2 + 280,
                                30, 160, 40, 'Primeira missão', 15, 
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background,0,255)
        if self.side is not None:
            arcade.draw_text(f'Lado: {self.side}',SCREEN_WIDTH/2 ,20,
                             arcade.color.WHITE,20,anchor_x='center',
                             font_name=OLD_FONT1)
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
    def __init__(self,file_name):
        super().__init__()
        with open(f'{MISSIONS}/{file_name}',encoding='utf-8') as file:
            self.mission = json.load(file)
        
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.top_secret = arcade.load_texture(TOP_SECRET)
        self.set_buttons()
        
    def set_buttons(self):
        if self.mission['destn1'] is not None:
            next_view1 = Mission(self.mission['destn1']) 
        else:
            next_view1 = Newspaper(self.mission['newspaper'])
        if self.mission['destn2'] is not None:
            next_view2 = Mission(self.mission['destn2']) 
        else:
            next_view2 = Newspaper(self.mission['newspaper'])
        
        self.button_list.append(Button(self, next_view1, SCREEN_WIDTH/2 - 280,
                                       40, 160, 40,self.mission['btn_name1'])) 
        
        self.button_list.append(Button(self, next_view2, SCREEN_WIDTH/2 + 280,
                                        40,160,40,self.mission['btn_name2']))
            
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
        super().on_draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        super().on_mouse_press(_x,_y,_button,_modifiers)
        
        
class Newspaper(arcade.View):
    def __init__(self,file_name):
        super().__init__()
        with open(f'{NEWSPAPER}/{file_name}',encoding='utf-8') as file:
            self.newspaper = json.load(file)
            
    def on_show(self):
        arcade.set_background_color(arcade.color.GRAY_BLUE)
        self.background = arcade.load_texture(BG_NEWSPAPER)
        self.astronaut = arcade.Sprite(ASTRONAUT,center_x=616,center_y=224)
        self.button_list.append(Button(self, Menu(), 616,40,
                                160, 40, 'Voltar ao Menu', 15, 
                                highlight=arcade.color.DARK_GRAY,
                                shadow=arcade.color.DARK_LIVER))
        
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
        super().on_draw()
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        super().on_mouse_press(_x, _y, _button, _modifiers)