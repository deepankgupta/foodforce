#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
#   Date : 9/06/2008
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

import pygame
from pygame.locals import *
from pygame.display import *
from pygame.mouse import *
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

if model.FLAG_XO:
    import game_sharing
    import olpcgames.mesh as mesh



desktop2 = gui.Desktop()
set_icon(pygame.image.load(os.path.join('data', 'WFPLOGO.png')).convert_alpha())

update_thread = None
message_thread = None
level_obj = level_change.change_level()
storyboardObj = proceduralFlow.storyboardFlow()
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

        if threades.GAME_EXIT_FLAG:
            return
        sleep(1)
        if threades.GAME_EXIT_FLAG:
            return
        sleep(1)
        if threades.GAME_EXIT_FLAG:
            return
        


def load_sound(name):

    if not pygame.mixer:
        return None
    fullname = os.path.join(name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:

        return None
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
    """
        Maintains safe exit from the game
    """
    #print 'in safe_exit'
    #print 'in safe_exit'
    threades.GAME_EXIT_FLAG = True
    
    if message_thread:
        message_thread.join()
    sleep(1)
    proceduralFlow.openStoryBoardFile()
    proceduralFlow.closeStoryBoardFile()
    if soundtrack:
        soundtrack.stop()
    pygame.mixer.quit()
    pygame.quit()
    exit()



clock = pygame.time.Clock()


def event_handling(e):
    """
       Handles all the event of the game and takes corresponding action
    """
    
    #For the safe exit of the game
    if e.type == pygame.QUIT:
        safe_exit()
    if e.type == QUIT:
        safe_exit()
        
         #Updates the region
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
        
            #Tackles the cases of setting up a facility,upgrading a facility,buying and selling of resources
        win_flag = gui_buttons.gui_obj.get_win_flag()
        if not win_flag:
            if e.key == K_s and gui_buttons.gui_obj.setup_button.enabled:
                gui_buttons.gui_obj.setup_obj.setup()
            if e.key == K_u and gui_buttons.gui_obj.upgrade_button.enabled:
                gui_buttons.gui_obj.upgrade_obj.upgrade()
            if e.key == K_b and gui_buttons.gui_obj.buysell_button.enabled:
                gui_buttons.gui_obj.buysell_obj.buysell()
            
                #Resetting the game
    if proceduralFlow.GAME_END_FLAG:
        threades.PLACING_LIST_TEMP = []
        proceduralFlow.GAME_END_FLAG = False
        proceduralFlow.closeStoryBoardFile()
        proceduralFlow.openStoryBoardFile()
        threades.delete_saved_game()
        proceduralFlow.storyboard_level = 1
        proceduralFlow.load_level_obj.new_level_stats('data.pkl','graphics_layout.pkl')
        event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
        game_events.EventQueue.add(event)
        model.game_controller.reset_time()
        pause_screen()
        #print proceduralFlow.storyboard_level
        
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
    if model.FLAG_XO:
        
        if e.type==mesh.CONNECT :
            game_sharing.sharing_handler(e.type,None,'')
        #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,None,'']).start()
        elif e.type==mesh.PARTICIPANT_ADD or e.type==mesh.PARTICIPANT_REMOVE :
            game_sharing.sharing_handler(e.type,e.handle,'')
        #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,'']).start()
        elif e.type==mesh.MESSAGE_MULTI or e.type==mesh.MESSAGE_UNI :
            game_sharing.sharing_handler(e.type,e.handle,e.content)
        #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,e.content]).start()



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

    

def load_resume_game():
   
    actiontemp = proceduralFlow.actionTemplate()
    actiontemp.actionType = 3
    proceduralFlow.openStoryBoardFile()
    action_obj = proceduralFlow.Actions(actiontemp)
    
    #threades.game_save_flag = False

    
class starting_intro:
    ''' Display the starting intro_text and menu
    '''

    def main_menu(self,pause_flag = True, game_save_flag = False):
        ''' Display the starting menu
        '''
        self.init_game_save_flag = game_save_flag
        self.game_save_flag = False
        logo = pygame.image.load(os.path.join('data', 'logo.png')).convert()
        self.ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
        threades.screen.fill((0,0,0))
        threades.screen.blit(self.ff_logo,threades.resize_pos((40,50)))

        # Font type
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))

        # Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button_green.png')).convert_alpha()
        buttonsurf = pygame.transform.scale(buttonsurf, (36, threades.resize_pt_y(40)))
        self.button_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)
        

        self.pause_flag = pause_flag
        if self.pause_flag:
            self.start_button = gui.Button(position = threades.resize_pos((475,500)), size = threades.resize_pos((250,50)), parent = desktop2, text = "Start New Game",style = self.button_style) 
            self.start_button.onClick = self.storyboardWindow
            
            #Resume saved level button if a game is saved
            if self.init_game_save_flag == True:
                self.resume_saved_level_button = gui.Button(position = threades.resize_pos((475,430)),size = threades.resize_pos((250,50)), parent = desktop2, text = "Resume Saved Game",style =self.button_style)
                self.resume_saved_level_button.onClick = self.resume_saved_level

            
        else:
            self.resume_button = gui.Button(position = threades.resize_pos((475,430)), size = threades.resize_pos((250,50)), parent = desktop2, text = "Resume Game",style = self.button_style)
            self.resume_button.onClick = self.resume
            
            self.start_game_again_button = gui.Button(position = threades.resize_pos((475,500)), size = threades.resize_pos((250,50)), parent = desktop2, text = "Start Game Again",style = self.button_style) 
            self.start_game_again_button.onClick = self.start_game_again
            
            #Save Game Button
            if proceduralFlow.storyboard_level != 1:
                self.save_button = gui.Button(position = threades.resize_pos((475,430)), size = threades.resize_pos((250,50)), parent = desktop2, text = "Save Current Level",style = self.button_style)
                self.save_button.onClick = self.save_current_level

        
        self.controls_button = gui.Button(position = threades.resize_pos((475,640)), size = threades.resize_pos((250,50)), parent = desktop2, text = "Controls",style = self.button_style)
        self.exit_button = gui.Button(position = threades.resize_pos((475,710)), size = threades.resize_pos((250,50)), parent = desktop2, text = "Exit",style = self.button_style)
        self.instructions_button = gui.Button(position = threades.resize_pos((475,570)), size = threades.resize_pos((250,50)), parent = desktop2, text = "Guide",style = self.button_style)
        self.about_us_button = gui.Button(position = threades.resize_pos((1000,20)), size = threades.resize_pos((150,40)), parent = desktop2, text = "About Us",style = self.button_style)
        
                                      

        self.controls_button.onClick = self.controls
        self.exit_button.onClick = safe_exit
        
        self.instructions_button.onClick = self.instructionsWindow
        self.about_us_button.onClick = self.aboutUsWindow

        self.run = True
     
    def start_game_again(self,button=None):
        

        
        #stopping the soundtrack
        if soundtrack:
            soundtrack.stop()
            
        #reinitialising the flags    
        storyboardObj.conditionTestingFlag = False
        storyboardObj.runFlag = True
        storyboardObj.actionRunningFlag = False
        storyboardObj.prevConditionResult = -1
        storyboardObj.norConditionFlag = False

        
    
        #closing the storyboard
        proceduralFlow.closeStoryBoardFile()
        
        #selecting the storyboard
        self.storyboardWindow()
        
        #opening the storyboard again
        proceduralFlow.openStoryBoardFile()
        
        #erasing the facilities and deciding the data file
        for item in os.listdir(os.path.join("storyboards")):            
            if model.storyboard_file == str(item)+'/storyboard.pkl':    
                data_file = 'storyboards/'+str(item)+'/data/data1.pkl'
        
            
            
        graphics_file = 'graphics_layout.pkl'
        level_obj.new_level_stats(data_file,graphics_file) 
         
        
        model.game_controller.reset_time() 
        
        gui_buttons.instruction_off_flag = True
        #print gui_buttons.instruction_off_flag
        
            
    def storyboardWindow(self,button=None):
        self.remove_buttons()
        self.lightgreen_color = (0,100,0)
        self.green_color = (0,150,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font('font.ttf',threades.resize_pt(50))
        
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.lightgreen_color
        win_style['bg-color'] = self.black_color
        win_style['border-color'] =self.black_color
        
        position_win = threades.resize_pos((150.0,270.0))
        size_win = threades.resize_pos((900.0,650.0))
        
        myfont2 = pygame.font.Font('font.ttf',threades.resize_pt(20))
        labelstylecopy = gui.defaultLabelStyle.copy()
        labelstylecopy['font'] = myfont2
        labelstylecopy['font-color'] = self.lightgreen_color
        labelstylecopy['border-width'] = 1
        labelstylecopy['border-color'] = (0,0,0)
        labelstylecopy['autosize']=True
        labelstylecopy['wordwrap']=False
        
        
        op_style = gui.defaultOptionBoxStyle
        op_style['font'] = myfont2
        op_style['font-color'] = self.lightgreen_color
        op_style['normal'] = True
        op_style['autosize'] = True
        op_style['word wrap'] = False
        self.op_style = op_style
        
        
        
        
        self.win = gui.Window(position = position_win,size = size_win,parent = desktop2,style = win_style,text = "    Choose Storyboard", closeable = False,shadeable = False,moveable = False )
        self.win.onClose = self.main_menu(self.pause_flag)
        
        vertical_dist = 200.0     #for the position of optionboxes
        for item in os.listdir(os.path.join("storyboards")):
            self.item = gui.OptionBox(position = threades.resize_pos((150.0,vertical_dist),(900.0,600.0),self.win.size),parent = self.win,style = op_style,text = str(item))
            self.item.onValueChanged = self.select_storyboard
            vertical_dist = vertical_dist + 40
        
        self.skip_button = gui.Button(position = threades.resize_pos((100,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Skip  ",style = self.button_style)
        self.skip_button.onClick = self.close_win
        self.play_button = gui.Button(position = threades.resize_pos((500,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Play  ",style = self.button_style)
        self.play_button.onClick = self.startup_text
        
        
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
        self.storyboard_menu_run = True
        while self.storyboard_menu_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,50)))
            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.storyboard_menu_run = False
                        self.win.close()
                    
                if model.FLAG_XO:
                    if e.type==mesh.CONNECT :
                        game_sharing.sharing_handler(e.type,None,'')
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,None,'']).start()
                    elif e.type==mesh.PARTICIPANT_ADD or e.type==mesh.PARTICIPANT_REMOVE :
                        game_sharing.sharing_handler(e.type,e.handle,'')
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,'']).start()
                    elif e.type==mesh.MESSAGE_MULTI or e.type==mesh.MESSAGE_UNI :
                        game_sharing.sharing_handler(e.type,e.handle,e.content)
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,e.content]).start()


            desktop2.update()
            desktop2.draw()
            pygame.display.update()
            
            
    def select_storyboard(self,button = None):
        for item in os.listdir(os.path.join("storyboards")):
            if button.text == str(item):
                model.storyboard_file = str(item)+'/storyboard.pkl'
                break
        

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
        win_style['border-color'] = (0,0,0)
        
        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((150.0,310.0))
        size_win =threades.resize_pos((900.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = desktop2, text = "    Guide" , style = win_style, shadeable = False, closeable = False,moveable = False)
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
        
        self.skip_button = gui.Button(position = threades.resize_pos((500,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Skip  ",style = self.button_style)
        self.next_button = gui.Button(position = threades.resize_pos((380,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Next > ",style = self.button_style)
        self.prev_button = gui.Button(position = threades.resize_pos((260,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = "  < Prev  ",style = self.button_style)

        self.next_button.onClick = self.increaseInstructionsCounter
        self.prev_button.onClick = self.decreaseInstructionsCounter
        self.prev_button.enabled = False
        self.skip_button.onClick = self.close_win
        self.instructions_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
        
        self.instructions_counter = 0
        label = gui.Label(position = threades.resize_pos((10.0,100.0),(900.0,600.0),self.win.size),size = threades.resize_pos((880.0,440.0),(900.0,600.0),self.win.size), parent = self.win, text = '', style = labelStyleCopy)
        
        #The loop which pauses the game
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
                if model.FLAG_XO:
                    if e.type==mesh.CONNECT :
                        game_sharing.sharing_handler(e.type,None,'')
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,None,'']).start()
                    elif e.type==mesh.PARTICIPANT_ADD or e.type==mesh.PARTICIPANT_REMOVE :
                        game_sharing.sharing_handler(e.type,e.handle,'')
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,'']).start()
                    elif e.type==mesh.MESSAGE_MULTI or e.type==mesh.MESSAGE_UNI :
                        game_sharing.sharing_handler(e.type,e.handle,e.content)
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,e.content]).start()


            desktop2.update()
            desktop2.draw()
            pygame.display.update()
            
    def increaseInstructionsCounter(self,button = None):
        self.prev_button.enabled = True
        if self.instructions_counter < len(texts.instruction_text)-1:
            self.instructions_counter +=1
        if self.instructions_counter == len(texts.instruction_text)-1:
            self.next_button.enabled = False
    
    def decreaseInstructionsCounter(self,button = None):
        self.next_button.enabled = True
        if self.instructions_counter > 0 :
            self.instructions_counter -=1
        if self.instructions_counter == 0:
            self.prev_button.enabled = False
        

            

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
        win_style['border-color'] = (0,0,0)
        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((150.0,280.0))
        size_win =threades.resize_pos((900.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = desktop2, text = "     About Us " , style = win_style, shadeable = False, closeable = False,moveable = False)
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
        
        self.close_button = gui.Button(position = threades.resize_pos((400,550),(900.0,600.0),self.win.size), size = threades.resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Close  ",style = self.button_style)
        
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
                if model.FLAG_XO:
                    if e.type==mesh.CONNECT :
                        game_sharing.sharing_handler(e.type,None,'')
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,None,'']).start()
                    elif e.type==mesh.PARTICIPANT_ADD or e.type==mesh.PARTICIPANT_REMOVE :
                        game_sharing.sharing_handler(e.type,e.handle,'')
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,'']).start()
                    elif e.type==mesh.MESSAGE_MULTI or e.type==mesh.MESSAGE_UNI :
                        game_sharing.sharing_handler(e.type,e.handle,e.content)
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,e.content]).start()

         
            desktop2.update()
            desktop2.draw()
            pygame.display.update()
    
    def startup_text(self,button = None):
        ''' Displays the startup text
        '''
        
        threades.current_level = 1
        self.remove_buttons()
        if soundtrack:
            soundtrack.play(-1)
            
        self.storyboard_menu_run = False       
        self.run = False
        self.win.close()
    
        
        
    def turnoff_startup_run(self,button = None):
        
        self.startup_text_run = False
    
    def resume_saved_level(self,button = None):
        '''Resumes saved level'''
        
        threades.resume_game()
        self.remove_buttons()
        self.run = False
        
    def save_current_level(self,button = None):
        '''Saves the current level'''
        threades.current_level = proceduralFlow.storyboard_level
        threades.save_game()
        self.remove_buttons()
        self.run = False
        
        
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

        control_text = """\n\n  Build           :       s \n\n  Upgrade       :       u \n\n  Market                    :       b \n\n  Scroll threades.screen up       :       up arrow \n\n  Scroll threades.screen down   :       down arrow \n\n  Scroll threades.screen left      :       left arrow \n\n  Scroll threades.screen right    :       right arrow """
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(25))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.green_color
        labelStyleCopy['border-color'] = self.black_color
        
        #Creating labels for text to be written
        self.message_label = gui.Label(position = threades.resize_pos((80,80),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Build ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,130),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Upgrade ", style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,180),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Market ", style = labelStyleCopy)
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
        
      #The loop which pauses the game unless an action is taken by the user 
        while self.controls_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,50)))

            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.controls_run = False
                        self.win.close()
                if model.FLAG_XO:
                    if e.type==mesh.CONNECT :
                        game_sharing.sharing_handler(e.type,None,'')
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,None,'']).start()
                    elif e.type==mesh.PARTICIPANT_ADD or e.type==mesh.PARTICIPANT_REMOVE :
                        game_sharing.sharing_handler(e.type,e.handle,'')
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,'']).start()
                    elif e.type==mesh.MESSAGE_MULTI or e.type==mesh.MESSAGE_UNI :
                        game_sharing.sharing_handler(e.type,e.handle,e.content)
                    #sharing_thread = threading.Thread(target = game_sharing.sharing_handler, args=[e.type,e.handle,e.content]).start()

                
            desktop2.update()
            desktop2.draw()
            pygame.display.update()


    def close_win(self,button = None):
        self.win.close()
        self.controls_run = False
        self.instructions_run = False
        self.about_us_run = False
        self.storyboard_menu_run = False

    def remove_buttons(self):
        ''' Removes the buttons from the gui.Desktop
        '''

        win = gui.Window(position = (0,0), size = (100,100), parent = desktop2)
        if self.pause_flag:
            self.start_button._set_parent(win)
            if self.init_game_save_flag:
                self.resume_saved_level_button._set_parent(win)
                self.init_game_save_flag = False    
        else:
            self.start_game_again_button._set_parent(win)
            self.resume_button._set_parent(win)
            if proceduralFlow.storyboard_level !=1:
                self.save_button._set_parent(win)
            
        
        self.controls_button._set_parent(win)
        self.exit_button._set_parent(win)
        self.about_us_button._set_parent(win)
        self.instructions_button._set_parent(win)
        win.close()





def pause_screen(pause_flag = True):

    start = starting_intro()

    start.main_menu(pause_flag,threades.game_save_flag)
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

def facility_placement():
    (x,y) = (0,0)
    x,y = pygame.mouse.get_pos()
    gui_buttons.gui_obj.setup_button.enabled = False
    facility_name = threades.buildFacilityPlacementFlag
    
    for i in range(len(model.Facility_Size)):
        if model.Facility_Size[i][0] == facility_name:
            height = model.Facility_Size[i][1]
            width = model.Facility_Size[i][2]
            
            height_temp = threades.resize_pt_y((model.Facility_Size[i][1])*threades.transform_obj.ratio)
            width_temp = threades.resize_pt_x((model.Facility_Size[i][2])*threades.transform_obj.ratio)
            
    
    if x > threades.resize_pt_x(930):    
        pygame.mouse.set_pos(threades.resize_pt_x(930),y)
    if y > threades.resize_pt_y(600):
        pygame.mouse.set_pos(x,threades.resize_pt_y(600))
    
    x -= width_temp/2
    y -= height_temp/2
    rect = (x,y,width,height)
    rect_temp = (x,y,width_temp,height_temp)
    rect_obj = pygame.Rect(rect)
    rect_obj_temp = pygame.Rect(rect_temp)
     
    collide_check = threades.place_facility_collide_check(rect_obj)
    if collide_check:
        color = (205,0,0)
    else:
        color = (205,200,100)
    pygame.draw.rect(threades.screen,color,rect_obj_temp,5)
    
    l,m,r = pygame.mouse.get_pressed()
    if l == 1 and collide_check == False:
        (a,b) = threades.transform_obj.inverse_trans_cordinate((x,y))
        rect_obj_send = pygame.Rect((a,b,width_temp,height_temp))
        PLACING_DATA_LIST = [threades.buildFacilityPlacementFlag,rect_obj_send] 
        threades.build_placed_facility(threades.buildFacilityPlacementFlag,False,PLACING_DATA_LIST)
        threades.set_build_facility_placement_flag()
        gui_buttons.gui_obj.setup_button.enabled = True
    if r == 1:
        threades.set_build_facility_placement_flag()
        gui_buttons.gui_obj.setup_button.enabled = True
            
message_thread = None
def main():

    global panel
    global chat_screen
    global level_setting
    global message_thread
    
    cursor = pygame.cursors.load_xbm(os.path.join('art', 'ff2_cursor.xbm'),os.path.join('art', 'ff2_cursor-mask.xbm'))
    #print cursor
    pygame.mouse.set_cursor(cursor[0],cursor[1],cursor[2],cursor[3])
    # Displaying the WFP logo
    intro_thread = threading.Thread(target = load_images.load_images, args=[])
    intro_thread.start()
    # Loading and starting the sound play
    #level_setting=level_change.change_level()
    threades.current_level = threades.check_saved_game_level()
    
    
    
    model.game_controller.reset_time()
    
    pause_screen()
    intro_thread.join()
    
    
        
    
    proceduralFlow.storyboard_level = threades.current_level
    if threades.current_level != 1:
        load_resume_game()
    else:
        threades.initialize_facilities(True)
        proceduralFlow.openStoryBoardFile()

     
    # loading the correct data file
    for item in os.listdir(os.path.join("storyboards")):
        if model.storyboard_file == str(item)+'/storyboard.pkl':            
            data_file = 'storyboards/'+str(item)+'/data/data1.pkl'
            break
        
    model.init_cons(data_file)
    model.init_obj()

    gui_buttons.initialize_gui()

    threades.screen.fill((0,0,0))
    panel = display_panel.display_panel()
    animation_obj = threades.Animation()
    animation_obj.update()
    # Starting of the threads
    #print update_thread
    message_thread = threading.Thread(target = message_window, args=[])
    message_thread.start()
    mouse_flag = False
    chat_screen=chat.chat()
        
    clock = pygame.time.Clock()
    # The main infinite loop
    while True:
        time_passed = clock.tick()
        model.game_controller.update_level_time(threades.update_thread_pause)
        threades.update_turn(time_passed)
        animation_obj.update()


        mouse_flag = False
            
        (x,y) = (0,0)
        x,y = pygame.mouse.get_pos()
        
        if not gui_buttons.gui_obj.get_win_flag():
            if len(threades.buildFacilityPlacementFlag):
                facility_placement()               
            if (x > (threades.resize_pt_x(890)) and x < threades.resize_pt_x(930)) and y< threades.resize_pt_y(600):
                threades.transform_obj.move_free((-10,0))
                
            if x < threades.resize_pt_x(60) and y< threades.resize_pt_y(600):
                threades.transform_obj.move_free((10,0))
                
            if  y > threades.resize_pt_y(560) and y< threades.resize_pt_y(600) and x < threades.resize_pt_x(930):
                threades.transform_obj.move_free((0,-10))
                
            if y < threades.resize_pt_y(60) and x < threades.resize_pt_x(930) and x < threades.resize_pt_x(930):
                threades.transform_obj.move_free((0,10))
                
            if (x > threades.resize_pt_x(0)) and (x < threades.resize_pt_x(600)) and (y > threades.resize_pt_y(845)) and (y < threades.resize_pt_y(900)):
                mouse_flag = True
                
        pygame.display.set_caption('FoodForce2')

        for e in gui.setEvents(pygame.event.get()):
            event_handling(e)

        
        

        # Calculate the values of the indicators
        threades.calculate_indicators_starting()
        
               

        
        rects_list = get_update_region()
        panel.update()
        
        if (threades.total_update_flag or threades.map_update_flag or threades.facilities_update_flag or threades.panel_update_flag or panel.res.money_flag):
            threades.desktop.update()
            threades.desktop.draw()
        
        pygame.display.update(rects_list)

        model.iteration_time = time_passed
        model.global_time += model.iteration_time
        storyboardObj.flow()
        gui_buttons.instruction_off_flag = False

if __name__ == '__main__':
    main()



