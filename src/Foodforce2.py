#! /usr/bin/env python
#

# ***** BEGIN LICENSE BLOCK *****
# Version: CPAL 1.0
#
# The contents of this file are subject to the Common Public Attribution
# License Version 1.0 (CPAL); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://opensource.org/licenses/cpal_1.0
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# ***** END LICENSE BLOCK ****
#

import pygame
from pygame.locals import *
from sys import exit
import os
from time import *
#from threades import *
import threades
import threading
import gui
#from gui import *
import defaultStyle
#from load_images import *
import display_panel
#from gui_buttons import *
import gui_buttons
import chat
import game_events
#from model import *
import texts
import load_images
import model
import level_change
import random
import proceduralFlow
import natural_calamities



    


desktop2 = gui.Desktop()
def message_window():
    ''' Thread to display the messages'''

    font_color = (255,214,150)
    myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))
    # Custom gui.Window Style
    win_style = gui.defaultWindowStyle.copy()
    win_style['font'] = myfont
    win_style['bg-color'] = (0,0,0)
    
    # Calculating position and size of window from the size of the threades.desktop
    position_win =threades.resize_pos((745.0,42.0))
    size_win =threades.resize_pos((450.0,150.0))

    # Creating custom label style for the text to be displayed as a threades.message
    labelStyleCopy = gui.defaultLabelStyle.copy()
    labelStyleCopy['wordwrap'] = True
    labelStyleCopy['autosize'] = False
    labelStyleCopy['font'] = myfont
    #labelStyleCopy['font-color'] = font_color

    while True:
        (text,color) = threades.message.pop_message()
        if text:

            # Creating window
            win_style['font-color'] = color
            labelStyleCopy['font-color'] = color

            win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = "Message " ,style = win_style ,closeable = False ,shadeable = False,moveable = False)
            pygame.draw.rect(win.surf,color,threades.resize_rect((3,3,444,144)),1)            
            #win.surf.set_alpha(160)
            # Creating label
            message_label = gui.Label(position = threades.resize_pos((5,50),(450.0,150.0),win.size),size = threades.resize_pos((440,140),(450.0,150.0),win.size), parent = win, text = text, style = labelStyleCopy)
            sleep(6)
            win.close()
        sleep(2)


def load_sound(name):

    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join(name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:

        raise SystemExit, message
    return sound

def escape():

    win_flag = gui_buttons.gui_obj.get_win_flag()
    child_win_flag = gui_buttons.gui_obj.get_child_win_flag()
    if child_win_flag:
        gui_buttons.gui_obj.close_child_win()
    elif win_flag:
        gui_buttons.gui_obj.close_win()
    else:
        pause_screen(False)

def safe_exit(button = None):
    #print 'in safe_exit'
    #print 'in safe_exit'
    
    proceduralFlow.openStoryBoardFile()
    proceduralFlow.closeStoryBoardFile()
    soundtrack.stop()
    pygame.mixer.quit()
    pygame.quit()
    exit()



clock = pygame.time.Clock()


def event_handling(e):
    
    if e.type == pygame.QUIT:
        safe_exit()
    if e.type == QUIT:
        safe_exit()
    if e.type == KEYDOWN:
        if e.key == 27:  # For escape key
            escape()
        if e.key == K_UP:
            threades.transform_obj.start_move('up')
        if e.key == K_DOWN:
            threades.transform_obj.start_move('down')
        if e.key == K_LEFT:
            threades.transform_obj.start_move('left')
        if e.key == K_RIGHT:
            threades.transform_obj.start_move('right')
        if e.key == K_f or e.key == 61:
            threades.transform_obj.focus()
        if e.key == K_d or e.key == 45:
            threades.transform_obj.defocus()
        if e.key == K_RETURN:
            gui_buttons.gui_obj.press_enter()
        
        win_flag = gui_buttons.gui_obj.get_win_flag()
        if not win_flag:
            if e.key == K_s:
                gui_buttons.gui_obj.setup_obj.setup()
            if e.key == K_u:
                gui_buttons.gui_obj.upgrade_obj.upgrade()
            if e.key == K_b:
                gui_buttons.gui_obj.buysell_obj.buysell()
            
            
    if e.type == KEYUP:
        if e.key == K_UP:
            threades.transform_obj.stop_move('up')
        if e.key == K_DOWN:
            threades.transform_obj.stop_move('down')
        if e.key == K_LEFT:
            threades.transform_obj.stop_move('left')
        if e.key == K_RIGHT:
            threades.transform_obj.stop_move('right')

    x,y = pygame.mouse.get_pos()
    r = pygame.Rect(threades.resize_rect((0,40,930,560)))
    if gui_buttons.gui_obj.buysell_obj.get_win_flag():
        gui_buttons.gui_obj.buysell_obj.drawPriceChart()
    if r.collidepoint(x,y):
        
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1 and gui_buttons.gui_obj.get_child_win_flag():
                gui_buttons.gui_obj.setup_obj.bardisplay.updateChart((x,y))
            if e.button == 1 and gui_buttons.gui_obj.buysell_obj.get_win_flag():
                gui_buttons.gui_obj.buysell_obj.barObject.updateChart((x,y))
            if e.button == 4:
                threades.transform_obj.focus()
            if e.button == 5:
                threades.transform_obj.defocus()

soundtrack = load_sound(os.path.join('data', 'soundtrack.ogg'))

def get_update_region():
    # Function which returns the regions to be updated
    
    list_rects = []
    if threades.total_update_flag:
        threades.screen.blit(surface_top,(0,0))
        pygame.draw.rect(threades.screen,(0,0,0),threades.resize_rect((0,600,1200,300)))
        list_rects.append(pygame.Rect(threades.resize_pos((0,0)),threades.resize_pos((1200,900))))
        return list_rects
    
    list_rects.append(pygame.Rect(threades.resize_pos((0,40)),threades.resize_pos((930,560))))
                      
    if (panel.ind.update_flag or panel.man.update_flag or panel.res.update_flag or threades.panel_update_flag):
        pygame.draw.rect(threades.screen,(0,0,0),threades.resize_rect((0,600,1200,300)))
        list_rects.append(pygame.Rect(threades.resize_pos((0,600)),threades.resize_pos((1200,300))))
    
    if panel.map.update_flag or threades.map_update_flag:
        list_rects.append(pygame.Rect(threades.resize_pos((930,390)),threades.resize_pos((270,210))))
        
    if panel.res.money_flag or threades.top_update_flag:
        threades.screen.blit(surface_top,(0,0))
        list_rects.append(pygame.Rect((0,0),threades.resize_pos((1200,40))))
        
    if panel.fac.update_flag or threades.facilities_update_flag:
        list_rects.append(pygame.Rect(threades.resize_pos((930,40)),threades.resize_pos((270,350))))
        
    return list_rects

    

class starting_intro:
    ''' Display the starting intro_text and menu
    '''

    def main_menu(self,pause_flag = True):
        ''' Display the starting menu
        '''

        logo = pygame.image.load(os.path.join('data', 'logo.png')).convert()
        self.ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
        threades.screen.fill((0,0,0))
        threades.screen.blit(self.ff_logo,threades.resize_pos((40,50)))

        # Font type
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))

        # Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button_green.png')).convert_alpha()
        self.button_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)

        self.pause_flag = pause_flag
        if self.pause_flag:
            self.start_button = gui.Button(position = threades.resize_pos((500,500)), size = threades.resize_pos((200,30)), parent = desktop2, text = "Start New Game",style = self.button_style)
            self.start_button.onClick = self.startup_text
        else:
            self.resume_button = gui.Button(position = threades.resize_pos((500,500)), size = threades.resize_pos((200,30)), parent = desktop2, text = "Resume Game",style = self.button_style)
            self.resume_button.onClick = self.resume

        #self.resume_button = gui.Button(position = threades.resize_pos((500,550)), size = threades.resize_pos((200,30)), parent = threades.desktop, text = "Resume Game",style = self.button_style)
        self.controls_button = gui.Button(position = threades.resize_pos((500,600)), size = threades.resize_pos((200,30)), parent = desktop2, text = "Controls",style = self.button_style)
        self.exit_button = gui.Button(position = threades.resize_pos((500,650)), size = threades.resize_pos((200,30)), parent = desktop2, text = "Exit",style = self.button_style)
        self.instructions_button = gui.Button(position = threades.resize_pos((500,550)), size = threades.resize_pos((200,30)), parent = desktop2, text = "Guide",style = self.button_style)
        self.about_us_button = gui.Button(position = threades.resize_pos((1000,20)), size = threades.resize_pos((150,30)), parent = desktop2, text = "About Us",style = self.button_style)
        
                                      
        #self.resume_button.onClick = self.resume
        self.controls_button.onClick = self.controls
        self.exit_button.onClick = safe_exit
        
        self.instructions_button.onClick = self.instructionsWindow
        self.about_us_button.onClick = self.aboutUsWindow

        self.run = True

    def instructionsWindow(self,button = None):
        ''' Opens a window for Instructions
        '''
        
        self.remove_buttons()
        self.lightgreen_color = (0,100,0)
        self.green_color = (0,150,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(40))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.green_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = (0,150,0)
        
        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((150.0,270.0))
        size_win =threades.resize_pos((900.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = desktop2, text = "     Guide" , style = win_style, shadeable = False, closeable = False,moveable = False)
        self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        #self.win.surf.set_alpha(140) This seems to be redundant as translucency doesnt seems to work properly

        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = (0,200,0)
        labelStyleCopy['border-color'] = self.black_color
        
        self.skip_button = gui.Button(position = threades.resize_pos((500,550),(900.0,600.0),self.win.size), size = threades.resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Skip  ",style = self.button_style)
        self.next_button = gui.Button(position = threades.resize_pos((380,550),(900.0,600.0),self.win.size), size = threades.resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Next > ",style = self.button_style)
        self.prev_button = gui.Button(position = threades.resize_pos((260,550),(900.0,600.0),self.win.size), size = threades.resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = "  < Prev  ",style = self.button_style)

        self.next_button.onClick = self.increaseInstructionsCounter
        self.prev_button.onClick = self.decreaseInstructionsCounter
        self.skip_button.onClick = self.close_win
        self.instructions_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
        
        self.instructions_counter = 0
        label = gui.Label(position = threades.resize_pos((10.0,100.0),(900.0,600.0),self.win.size),size = threades.resize_pos((880.0,440.0),(900.0,600.0),self.win.size), parent = self.win, text = '', style = labelStyleCopy)

        while self.instructions_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,50)))

            label.text = texts.instruction_text[self.instructions_counter]
            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.instructions_run = False
                        self.win.close()
                    if e.key == K_RIGHT:
                        if self.instructions_counter < len(texts.instruction_text)-1:
                            self.instructions_counter += 1
                    if e.key == K_LEFT:
                        if self.instructions_counter > 0 :
                            self.instructions_counter -= 1

            desktop2.update()
            desktop2.draw()
            pygame.display.update()
            
    def increaseInstructionsCounter(self,button = None):
        if self.instructions_counter < len(texts.instruction_text)-1:
            self.instructions_counter +=1
    
    def decreaseInstructionsCounter(self,button = None):
        if self.instructions_counter > 0 :
            self.instructions_counter -=1
        

            

    def aboutUsWindow(self,button = None):
        ''' Displays the credits
        '''
        
        self.remove_buttons()
        self.lightgreen_color = (0,100,0)
        self.green_color = (0,150,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(40))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.green_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = (0,150,0)
        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((150.0,270.0))
        size_win =threades.resize_pos((900.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = desktop2, text = "     About Us " , style = win_style, shadeable = False, closeable = False,moveable = False)
        self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        #self.win.surf.set_alpha(140) This seems to be redundant as translucency doesnt seems to work properly

        self.next_button = gui.Button(position = threades.resize_pos((500,650)), size = threades.resize_pos((200,30)), parent = self.win, text = "Next ",style = self.button_style)
        
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = (0,200,0)
        labelStyleCopy['border-color'] = self.black_color
        
        self.close_button = gui.Button(position = threades.resize_pos((500,550),(900.0,600.0),self.win.size), size = threades.resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Close  ",style = self.button_style)
        
        self.close_button.onClick = self.close_win
        self.about_us_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
        
        #self.instructions_counter = 0
        label = gui.Label(position = threades.resize_pos((10.0,100.0),(900.0,600.0),self.win.size),size = threades.resize_pos((880.0,440.0),(900.0,600.0),self.win.size), parent = self.win, text = '', style = labelStyleCopy)

        while self.about_us_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,50)))

            label.text = texts.about_us_text
            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.about_us_run = False
                        self.win.close()
         
            desktop2.update()
            desktop2.draw()
            pygame.display.update()
    
    def startup_text(self,button = None):
        ''' Displays the startup text
        '''

        self.remove_buttons()
        threades.screen.fill((255,255,255))
        hunger_map = pygame.image.load(os.path.join('data', 'Wfpwork.png')).convert()
        hunger_map =  pygame.transform.scale(hunger_map,threades.new_screen_size)
        threades.screen.blit(hunger_map,threades.resize_pos((0,0)))

        color_brown = (255,214,150)
        # gui.Window custom style
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(28))
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = color_brown
        win_style['bg-color'] = (0,0,0, 180)
        win_style['border-color'] = color_brown
        position_win =threades.resize_pos((200.0,50.0))
        size_win =threades.resize_pos((800.0,600.0))
        win = gui.Window(position = position_win, size = size_win, parent = desktop2, text = " FOODFORCE II : ESCAPING POVERTY  " ,style = win_style,shadeable = False, closeable = False,moveable = False)
        self.startup_text_run = True
        win.surf.set_alpha(100)
        myfont2 = pygame.font.Font("font.ttf",threades.resize_pt(19))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = True
        labelstyle1['autosize'] = False
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = color_brown

        counter = 0
        label = gui.Label(position = threades.resize_pos((10.0,130.0),(800.0,600.0),win.size),size = threades.resize_pos((780.0,460.0),(800.0,600.0),win.size), parent = win, text = '', style = labelstyle1)
        
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.skip_button = gui.Button(position = threades.resize_pos((600,550),(800.0,600.0),win.size), size = threades.resize_pos((150,30),(800.0,600.0),win.size), parent = win, text = "  Skip  ",style = button_style)
        self.skip_button.onClick = self.turnoff_startup_run
        model.global_time = 0
        
        #One time show of the background image
        threades.screen.fill((255,255,255))
        threades.screen.blit(hunger_map,threades.resize_pos((0,0)))
        pygame.display.flip()
        #sleep(5)
        first_display = True
        model.global_time = 0
        while self.startup_text_run:

            label.text =  texts.trailer_text[counter]
            for e in gui.setEvents(pygame.event.get()):
                if e.type == pygame.QUIT:
                    safe_exit()
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.startup_text_run = False
                    if e.key == K_RETURN:
                        counter += 1
            
            if model.global_time >= 5000:
                first_display = False                
                model.global_time = 0
                counter += 1
            if not first_display:
                
                threades.screen.fill((255,255,255))
                threades.screen.blit(hunger_map,threades.resize_pos((0,0)))
                desktop2.update()
                desktop2.draw()
                pygame.display.flip()
                
            if counter == len(texts.trailer_text):
                self.startup_text_run = False
            
            
            
        
            model.iteration_time = clock.tick()
            model.global_time += model.iteration_time
        win.close()

        
        self.run = False

    def turnoff_startup_run(self,button = None):
        
        self.startup_text_run = False
        
    def resume(self,button = None):
        ''' Resumes Game
        '''
        self.remove_buttons()
        self.run = False

    def controls(self,button = None):
        """"show controllers
        """
        self.remove_buttons()
        self.lightgreen_color = (0,100,0)
        self.green_color = (0,150,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(40))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.green_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = (0,150,0)
        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((150.0,270.0))
        size_win =threades.resize_pos((900.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = desktop2, text = "     Controls " , style = win_style, shadeable = False, closeable = False)
        self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        self.win.surf.set_alpha(140)

        control_text = """\n\n  Setup Facility           :       s \n\n  Upgrade Facility       :       u \n\n  Buy/Sell                    :       b \n\n  Scroll threades.screen up       :       up arrow \n\n  Scroll threades.screen down   :       down arrow \n\n  Scroll threades.screen left      :       left arrow \n\n  Scroll threades.screen right    :       right arrow """
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(25))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.lightgreen_color
        labelStyleCopy['border-color'] = self.black_color
        self.message_label = gui.Label(position = threades.resize_pos((80,80),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Setup Facility ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,130),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Upgrade Facility ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,180),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Buy/Sell ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,230),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Scroll Screen up ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,280),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Scroll Screen down", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,330),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Scroll Screen left ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,380),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Scroll Screen right ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,430),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Focus ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,480),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "De Focus ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,80),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,130),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,180),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,230),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,280),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,330),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,380),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,430),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,480),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,80),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "s ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,130),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "u ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,180),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "b ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,230),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "up arrow ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,280),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "down arrow ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,330),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "left arrrow ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,380),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "right arrow ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,430),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "f ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,480),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "d ", style = labelStyleCopy)

        self.win.surf.set_alpha(255)
        self.ok_button = gui.Button(position = threades.resize_pos((480,550),(600.0,600.0),self.win.size), size = threades.resize_pos((80,30),(600.0,600.0),self.win.size), parent = self.win, text = "  OK  ",style = self.button_style)

        self.ok_button.onClick = self.close_win
        self.controls_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
        while self.controls_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,50)))

            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.controls_run = False
                        self.win.close()

            desktop2.update()
            desktop2.draw()
            pygame.display.update()


    def close_win(self,button = None):
        self.win.close()
        self.controls_run = False
        self.instructions_run = False
        self.about_us_run = False

    def remove_buttons(self):
        ''' Removes the buttons from the gui.Desktop
        '''

        win = gui.Window(position = (0,0), size = (100,100), parent = desktop2)
        if self.pause_flag:
            self.start_button._set_parent(win)
        else:
            self.resume_button._set_parent(win)

        self.controls_button._set_parent(win)
        self.exit_button._set_parent(win)
        self.about_us_button._set_parent(win)
        self.instructions_button._set_parent(win)
        win.close()





def pause_screen(pause_flag = True):

    start = starting_intro()

    start.main_menu(pause_flag)
    logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
    ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
    while start.run:
        pygame.display.set_caption('FoodForce2')
        threades.screen.fill((0,0,0))
        threades.screen.blit(ff_logo,threades.resize_pos((40,50)))
        
        for e in gui.setEvents(pygame.event.get()):
            if e.type == pygame.QUIT:
                safe_exit()
            if e.type == QUIT:
                safe_exit()

        desktop2.update()
        desktop2.draw()
        pygame.display.update()
    threades.total_update_flag = True

wfp_logo = pygame.image.load(os.path.join('data', 'top.png')).convert()
surface_top = pygame.transform.scale(wfp_logo,threades.resize_pos((1200,40)))
   
def main():

    global panel
    global chat_screen
    global level_setting
    
    # Displaying the WFP logo
    intro_thread = threading.Thread(target = load_images.load_images, args=[])
    intro_thread.start()
    # Loading and starting the sound play
    soundtrack.play(-1)
    level_setting=level_change.change_level()
    pause_screen()

    intro_thread.join()
    threades.initialize_facilities()

    #surface_middle = pygame.transform.scale(surface3,threades.resize_pos((1200,560)))
    
    # Processing regarding the storyboard
    proceduralFlow.openStoryBoardFile()
    storyboardObj = proceduralFlow.storyboardFlow()
    proceduralFlow.openStoryBoardFile()

    gui_buttons.initialize_gui()

    threades.screen.fill((0,0,0))
    panel = display_panel.display_panel()
    animation_obj = threades.Animation()
    animation_obj.update()
    # Starting of the threads
    update_thread = threading.Thread(target = threades.update_turn, args=[]).start()
    message_thread = threading.Thread(target = message_window, args=[]).start()
    mouse_flag = False
    chat_screen=chat.chat()
        
    
    model.game_controller.reset_time()
    # The main infinite loop
    while True:
        #clock.tick()
        model.game_controller.update_level_time(threades.update_thread_pause)
        

        mouse_flag = False
            
        (x,y) = (0,0)
        x,y = pygame.mouse.get_pos()
        
        if (x > (threades.new_screen_size[0]-60)):
            threades.transform_obj.move_free((-10,0))
            
        if x < threades.resize_pt_x(60) :
            threades.transform_obj.move_free((10,0))
            
        if  y > threades.resize_pt_y(840):
            threades.transform_obj.move_free((0,-10))
            
        if y < threades.resize_pt_y(60):
            threades.transform_obj.move_free((0,10))
            
        if (x > threades.resize_pt_x(0)) and (x < threades.resize_pt_x(600)) and (y > threades.resize_pt_y(845)) and (y < threades.resize_pt_y(900)):
            mouse_flag = True
            
        pygame.display.set_caption('FoodForce2')

        for e in gui.setEvents(pygame.event.get()):
            event_handling(e)

        
        #pygame.draw.rect(threades.screen,(209,169,106),threades.resize_rect((0,40,1200,560)))
        animation_obj.update()


        # Calculate the values of the indicators
        threades.calculate_indicators_starting()
        
        #For middle surface
        #surface_middle = pygame.transform.scale(surface3,threades.resize_pos((1200,560)))
        #threades.screen.blit(surface_middle,threades.resize_pos((0,40)))

        

        
        rects_list = get_update_region()
        panel.update()
        
        if (threades.total_update_flag or threades.map_update_flag or threades.facilities_update_flag or threades.panel_update_flag or panel.res.money_flag):
            threades.desktop.update()
            threades.desktop.draw()
        
        pygame.display.update(rects_list)

        model.iteration_time = clock.tick()
        model.global_time += model.iteration_time
        storyboardObj.flow()

        

if __name__ == '__main__':
    main()



