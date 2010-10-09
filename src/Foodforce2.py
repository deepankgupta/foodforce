#! /usr/bin/env python
# -*- coding: ISO-8859-1 -*-
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
import locale
import pickle
import model
from texts_spa import *
from texts_eng import *
import pygame
from pygame.locals import *
from pygame.display import *
from pygame.mouse import *
from sys import exit
import os
from time import *
import threades
import threading
import gui
import defaultStyle
import display_panel
import gui_buttons
import chat
import game_events
import texts_spa
import texts_eng
import load_images
import level_change
import random
import proceduralFlow
import natural_calamities

if model.FLAG_XO:
    import game_sharing
    import olpcgames.mesh as mesh


select_lang_flag = 1
desktop2 = gui.Desktop()
set_icon(pygame.image.load(os.path.join('data', 'WFPLOGO.png')).convert_alpha())
select_flag  = 1                #Used to determine the button clicked in the main menu..Start new game or Resume Saved Level
update_thread = None
message_thread = None
level_obj = level_change.change_level()
storyboardObj = proceduralFlow.storyboardFlow()
load_images.load_images()
panel = display_panel.display_panel()


def message_window():
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

            win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = model.text_file.message_window_text[0] ,style = win_style ,closeable = False ,shadeable = False,moveable = False)
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
    threades.GAME_EXIT_FLAG = True
    
    if message_thread:
        message_thread.join()
    sleep(1)
    proceduralFlow.openStoryBoardFile()
    proceduralFlow.closeStoryBoardFile()
    threades.audio.stop_soundtrack()
    pygame.mixer.quit()
    pygame.quit()
    exit()



clock = pygame.time.Clock()


def event_handling(e):    
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
        elif e.type==mesh.PARTICIPANT_ADD or e.type==mesh.PARTICIPANT_REMOVE :
            game_sharing.sharing_handler(e.type,e.handle,'')
        elif e.type==mesh.MESSAGE_MULTI or e.type==mesh.MESSAGE_UNI :
            game_sharing.sharing_handler(e.type,e.handle,e.content)

def get_update_region():    
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


    
class starting_intro:
    

    def main_menu(self,pause_flag = True, game_save_flag = False):
        self.init_game_save_flag = game_save_flag
        self.game_save_flag = False
        if threades.game_save_flag:
            self.init_game_save_flag = True
        logo = pygame.image.load(os.path.join('data', 'logo.png')).convert()
        self.ff_logo = pygame.transform.scale(logo,threades.resize_pos((1128,171)))
        threades.screen.fill((0,0,0))
        threades.screen.blit(self.ff_logo,threades.resize_pos((40,90)))

        # Font type
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))

        # Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button_green.png')).convert_alpha()
        buttonsurf = pygame.transform.scale(buttonsurf, (36, threades.resize_pt_y(40)))
        self.button_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)
        self.pause_flag = pause_flag
        if self.pause_flag:
            self.start_button = gui.Button(position = threades.resize_pos((475,500)), size = threades.resize_pos((250,50)), parent = desktop2, text = model.text_file.start_new_game[0],style = self.button_style) 
            self.start_button.onClick = self.select_save_or_new_game
            #Resume saved level button if a game is saved
            if self.init_game_save_flag == True:
                self.resume_saved_level_button = gui.Button(position = threades.resize_pos((475,430)),size = threades.resize_pos((250,50)), parent = desktop2, text = model.text_file.resume_saved_game[0],style =self.button_style)
                self.resume_saved_level_button.onClick = self.select_save_or_new_game

            
        else:
            self.resume_button = gui.Button(position = threades.resize_pos((475,430)), size = threades.resize_pos((250,50)), parent = desktop2, text = model.text_file.resume_game[0],style = self.button_style)
            self.resume_button.onClick = self.resume
            
            self.start_game_again_button = gui.Button(position = threades.resize_pos((475,500)), size = threades.resize_pos((250,50)), parent = desktop2, text = model.text_file.start_game_again[0],style = self.button_style) 
	    self.start_game_again_button.onClick = self.select_lang
            
            #Save Game Button
            if proceduralFlow.storyboard_level != 1:
                self.save_button = gui.Button(position = threades.resize_pos((475,360)), size = threades.resize_pos((250,50)), parent = desktop2, text = model.text_file.save_current_level[0],style = self.button_style)
                self.save_button.onClick = self.save_current_level
            



        self.controls_button = gui.Button(position = threades.resize_pos((475,640)), size = threades.resize_pos((250,50)), parent = desktop2, text = model.text_file.control_button_text[0],style = self.button_style)
        self.exit_button = gui.Button(position = threades.resize_pos((475,710)), size = threades.resize_pos((250,50)), parent = desktop2, text = model.text_file.exit_button_text[0],style = self.button_style)
        self.instructions_button = gui.Button(position = threades.resize_pos((475,570)), size = threades.resize_pos((250,50)), parent = desktop2, text = model.text_file.instructions_window_text[0],style = self.button_style)
        self.about_us_button = gui.Button(position = threades.resize_pos((1000,20)), size = threades.resize_pos((150,40)), parent = desktop2, text = model.text_file.about_button_text[0],style = self.button_style)
        
                                      
        self.controls_button.onClick = self.controls
        self.exit_button.onClick = safe_exit
        
        self.instructions_button.onClick = self.instructionsWindow
        self.about_us_button.onClick = self.aboutUsWindow

        self.run = True
     
    def start_game_again(self,button=None):
        global select_flag
	global panel
        #stopping the soundtrack
        threades.audio.stop_soundtrack()
        threades.audio.play_music(False,'soundtrack')
            
        #reinitialising the flags    
        storyboardObj.conditionTestingFlag = False
        storyboardObj.runFlag = True
        storyboardObj.actionRunningFlag = False
        storyboardObj.prevConditionResult = -1
        storyboardObj.norConditionFlag = False
	self.close_win()
        if select_flag == False:
            self.resume_saved_level()
        else:
            self.startup_text()
        select_flag = True
	self.storyboard_menu_run = False
	self.run = False
	self.language_menu_run = False
        #erasing the facilities and deciding the data file
        gui_buttons.instruction_off_flag = True
	threades.total_update_flag = True
	panel.change_labels()
	gui_buttons.gui_obj.change_label_names()
        
    def select_save_or_new_game(self,button=None):
        global select_flag
        if button.text == model.text_file.start_new_game[0]:
            select_flag = True
        else:
            select_flag = False
        self.select_lang()
	
    def chooseLanguage(self,button = None):
        self.remove_buttons()
        self.lightgreen_color = (0,80,0)
        self.green_color = (0,150,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font('font.ttf',threades.resize_pt(50))
        
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.green_color
        win_style['bg-color'] = self.black_color
        win_style['border-color'] =self.black_color
        
        position_win = threades.resize_pos((150.0,270.0))
        size_win = threades.resize_pos((900.0,650.0))

        myfont2 = pygame.font.Font('font.ttf',threades.resize_pt(20))
        labelstylecopy = gui.defaultLabelStyle.copy()
        labelstylecopy['font'] = myfont2
        labelstylecopy['font-color'] = self.green_color
        labelstylecopy['border-width'] = 1
        labelstylecopy['border-color'] = (0,0,0)
        labelstylecopy['autosize']=True
        labelstylecopy['wordwrap']=False
        
        op_image = pygame.image.load(os.path.join("art","optionbox_green.png")).convert_alpha()
        op_style = gui.createOptionBoxStyle(gui.defaultFont, op_image, 12, (255,255,255),(100,100,100), autosize = True)
       
        op_style['font'] = myfont2
        op_style['font-color'] = self.green_color
        op_style['normal'] = True
        op_style['autosize'] = True
        op_style['word wrap'] = False
        self.op_style = op_style
        
        self.win = gui.Window(position = position_win,size = size_win,parent = desktop2,style = win_style,text = model.text_file.language_window_text[0], closeable = False,shadeable = False,moveable = False )
        self.win.onClose = self.main_menu
        
	self.lang1 = gui.OptionBox(position = threades.resize_pos((150.0,200.0),(900.0,600.0),self.win.size),parent = self.win,style = op_style,text = model.text_file.Language[0])
	self.lang1.onValueChanged = self.select_lang
	
	self.lang2 = gui.OptionBox(position = threades.resize_pos((150.0,240.0),(900.0,600.0),self.win.size),parent = self.win ,style = op_style,text = model.text_file.Language[1])
	self.lang2.onValueChanged = self.select_lang
    
        
        self.skip_button = gui.Button(position = threades.resize_pos((100,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = model.text_file.skip_text[0],style = self.button_style)
        self.skip_button.onClick = self.close_win
        self.play_button = gui.Button(position = threades.resize_pos((500,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = model.text_file.play_text[0],style = self.button_style)
        self.play_button.onClick = self.storyboardWindow

        self.play_button.enabled = False
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1128,171)))
        self.language_menu_run = True
        while self.language_menu_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,90)))
            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.language_menu_run = False
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
	    
	
    def storyboardWindow(self,button = None):
        global select_flag

	self.remove_buttons()
        
        self.lightgreen_color = (0,80,0)
        self.green_color = (0,150,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font('font.ttf',threades.resize_pt(50))
        
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.green_color
        win_style['bg-color'] = self.black_color
        win_style['border-color'] =self.black_color
        
        position_win = threades.resize_pos((150.0,270.0))
        size_win = threades.resize_pos((900.0,650.0))
        
        myfont2 = pygame.font.Font('font.ttf',threades.resize_pt(20))
        labelstylecopy = gui.defaultLabelStyle.copy()
        labelstylecopy['font'] = myfont2
        labelstylecopy['font-color'] = self.green_color
        labelstylecopy['border-width'] = 1
        labelstylecopy['border-color'] = (0,0,0)
        labelstylecopy['autosize']=True
        labelstylecopy['wordwrap']=False
        
        op_image = pygame.image.load(os.path.join("art","optionbox_green.png")).convert_alpha()
        op_style = gui.createOptionBoxStyle(gui.defaultFont, op_image, 12, (255,255,255),(100,100,100), autosize = True)
       
        op_style['font'] = myfont2
        op_style['font-color'] = self.green_color
        op_style['normal'] = True
        op_style['autosize'] = True
        op_style['word wrap'] = False
        self.op_style = op_style
        
        
        
        self.win = gui.Window(position = position_win,size = size_win,parent = desktop2,style = win_style,text = model.text_file.storyboard_window_text[0], closeable = False,shadeable = False,moveable = False )
	self.win.onClose = self.main_menu
        
        vertical_dist = 200.0     #for the position of optionboxes
        
        storyboard_list_file = open('storyboard_list.pkl')
        for i in range(pickle.load(storyboard_list_file)):
            storyboard_name = pickle.load(storyboard_list_file)
            if select_flag == True:
                self.item = gui.OptionBox(position = threades.resize_pos((150.0,vertical_dist),(900.0,600.0),self.win.size),parent = self.win,style = op_style,text = str(storyboard_name[1]))
                self.item.onValueChanged = self.select_storyboard
                vertical_dist = vertical_dist + 40
            else:
                if os.path.exists(os.path.join('storyboards',str(storyboard_name[1]),'save_game.pkl')):
                    self.item = gui.OptionBox(position = threades.resize_pos((150.0,vertical_dist),(900.0,600.0),self.win.size),parent = self.win,style = op_style,text = str(storyboard_name[1]))
                    self.item.onValueChanged = self.select_storyboard
                    vertical_dist = vertical_dist + 40
        
        self.skip_button = gui.Button(position = threades.resize_pos((100,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = model.text_file.skip_text[0],style = self.button_style)
        self.skip_button.onClick = self.close_win
        self.play_button = gui.Button(position = threades.resize_pos((500,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = model.text_file.play_text[0],style = self.button_style)
        self.play_button.onClick = self.start_game_again

	
        self.play_button.enabled = False
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1128,171)))
        self.storyboard_menu_run = True
        while self.storyboard_menu_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,90)))
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
	
        self.play_button.enabled = True
        model.storyboard_file = button.text
	if model.select_lang_flag == 'eng':
	    model.text_file = texts_eng
	elif model.select_lang_flag == 'spa':
	    model.text_file = texts_spa
        
    def select_lang(self,button = None):
	
	language = locale.getdefaultlocale()
	if language[0] == 'en_US':
	    model.select_lang_flag = 'eng'
	elif language[0] == 'es_MX':
	    model.select_lang_flag = 'spa'
	self.storyboardWindow()

	#print model.select_lang_flag
	    
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
        self.win = gui.Window(position = position_win, size = size_win, parent = desktop2, text = model.text_file.instructions_window_text[0], style = win_style, shadeable = False, closeable = False,moveable = False)
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
        
        self.skip_button = gui.Button(position = threades.resize_pos((500,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = model.text_file.skip_text[0],style = self.button_style)
        self.next_button = gui.Button(position = threades.resize_pos((380,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = model.text_file.instructions_next_text[0],style = self.button_style)
        self.prev_button = gui.Button(position = threades.resize_pos((260,490),(900.0,600.0),self.win.size), size = threades.resize_pos((110,30),(900.0,600.0),self.win.size), parent = self.win, text = model.text_file.instructions_pre_text[0],style = self.button_style)

        self.next_button.onClick = self.increaseInstructionsCounter
        self.prev_button.onClick = self.decreaseInstructionsCounter
        self.prev_button.enabled = False
        self.skip_button.onClick = self.close_win
        self.instructions_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1128,171)))
        
        self.instructions_counter = 0
        label = gui.Label(position = threades.resize_pos((10.0,100.0),(900.0,600.0),self.win.size),size = threades.resize_pos((880.0,440.0),(900.0,600.0),self.win.size), parent = self.win, text = '', style = labelStyleCopy)
        
        #The loop which pauses the game
        while self.instructions_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,90)))

            label.text = model.text_file.instruction_text[self.instructions_counter]
            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.instructions_run = False
                        self.win.close()
                    if e.key == K_RIGHT:
                        if self.instructions_counter < len(model.text_file.instruction_text)-1:
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
        if self.instructions_counter < len(model.text_file.instruction_text)-1:
            self.instructions_counter +=1
        if self.instructions_counter == len(model.text_file.instruction_text)-1:
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
        self.win = gui.Window(position = position_win, size = size_win, parent = desktop2, text = model.text_file.about_button_text[0], style = win_style, shadeable = False, closeable = False,moveable = False)
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
        
        self.close_button = gui.Button(position = threades.resize_pos((400,550),(900.0,600.0),self.win.size), size = threades.resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = model.text_file.close_widnow_text[0],style = self.button_style)
        
        self.close_button.onClick = self.close_win
        self.about_us_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1128,171)))
        
        #self.instructions_counter = 0
        label = gui.Label(position = threades.resize_pos((10.0,100.0),(900.0,600.0),self.win.size),size = threades.resize_pos((880.0,440.0),(900.0,600.0),self.win.size), parent = self.win, text = '', style = labelStyleCopy)

        while self.about_us_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,90)))

            label.text = model.text_file.about_us_text
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
        threades.audio.play_music(True,'soundtrack')
        threades.current_level = 1
        self.remove_buttons()
        if proceduralFlow.storyboardfile:
            #closing the storyboard
            proceduralFlow.closeStoryBoardFile()
            #opening the storyboard again
        proceduralFlow.openStoryBoardFile()
	
        data_file = os.path.join('storyboards',str(model.storyboard_file),'data','data1.pkl')            
        graphics_file = 'graphics_layout.pkl'
        level_obj.new_level_stats(data_file,graphics_file) 
        model.game_controller.reset_time() 
        self.run = False
	threades.load_initial_facilities()
	#threades.initialize_facilities()
	#level_obj.new_level_stats(data_file,graphics_file) 

        
    def turnoff_startup_run(self,button = None):
        
        self.startup_text_run = False
    
    def resume_saved_level(self,button = None):
        '''Resumes saved level'''
        threades.audio.play_music(True,'soundtrack')
        threades.resume_game()
        self.remove_buttons()
        self.run = False
        self.storyboard_menu_run = False
        #self.win.close()

        
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
        #threades.total_update_flag = True

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
        self.win = gui.Window(position = position_win, size = size_win, parent = desktop2, text = model.text_file.control_button_text[0], style = win_style, shadeable = False, closeable = False)
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
        self.message_label = gui.Label(position = threades.resize_pos((80,80),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[0], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,130),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[1], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,180),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[2], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,230),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[3], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,280),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[4], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,330),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[5], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,380),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[6], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,430),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[7], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((80,480),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[8], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,80),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[9], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,130),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[9], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,180),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[9], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,230),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[9], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,280),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[9], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,330),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[9], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,380),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[9], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,430),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[9], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((330,480),(600.0,600.0),self.win.size),size = threades.resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[9], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,80),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[10], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,130),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[11], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,180),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[12], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,230),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[13], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,280),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[14], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,330),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[15], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,380),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[16], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,430),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[17], style = labelStyleCopy)
        self.message_label = gui.Label(position = threades.resize_pos((350,480),(600.0,600.0),self.win.size),size = threades.resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[18], style = labelStyleCopy)

        self.win.surf.set_alpha(255)
        self.ok_button = gui.Button(position = threades.resize_pos((480,550),(600.0,600.0),self.win.size), size = threades.resize_pos((80,30),(600.0,600.0),self.win.size), parent = self.win, text = model.text_file.controls_text[19],style = self.button_style)

        self.ok_button.onClick = self.close_win
        self.controls_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((1128,171)))
        
      #The loop which pauses the game unless an action is taken by the user 
        while self.controls_run:
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(ff_logo,threades.resize_pos((40,90)))

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
	self.language_menu_run = False

    def remove_buttons(self):
        ''' Removes the buttons from the gui.Desktop
        '''

        win = gui.Window(position = (0,0), size = (100,100), parent = desktop2)
        if self.pause_flag:
            self.start_button._set_parent(win)
            if self.init_game_save_flag:
                self.resume_saved_level_button._set_parent(win)
                #self.init_game_save_flag = False    
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
    ff_logo = pygame.transform.scale(logo,threades.resize_pos((1128,171)))
    while start.run:
        pygame.display.set_caption('FoodForce2')
        threades.screen.fill((0,0,0))
        threades.screen.blit(ff_logo,threades.resize_pos((40,90)))
        
        for e in gui.setEvents(pygame.event.get()):
            if e.type == pygame.QUIT:
                safe_exit()
            if e.type == QUIT:
                safe_exit()
	#print 'in pause screen'
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
    threades.audio.play_music(False,'soundtrack')
    
    threades.check_saved_game_level()
    model.game_controller.reset_time()
    gui_buttons.initialize_gui()
    pause_screen()
    intro_thread.join()
    
    proceduralFlow.storyboard_level = threades.current_level
    if threades.current_level != 1:
        load_resume_game()
    else:
	threades.load_initial_facilities()
        data_file = os.path.join('storyboards',str(model.storyboard_file),'data','data1.pkl')
        model.init_cons(data_file)
        model.init_obj()
        threades.initialize_facilities(True)
        proceduralFlow.openStoryBoardFile() 

     
    # loading the correct data file

    #gui_buttons.initialize_gui()

    threades.screen.fill((0,0,0))
    #panel = display_panel.display_panel()
    panel.change_labels()
    animation_obj = threades.Animation()
    animation_obj.update()
    # Starting of the threads
    #print update_thread
    message_thread = threading.Thread(target = message_window, args=[])
    message_thread.start()
    mouse_flag = False
    chat_screen=chat.chat()
    #print 'i was here'
    clock = pygame.time.Clock()
    threades.total_update_flag = True
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
