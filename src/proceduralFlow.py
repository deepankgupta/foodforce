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
#Mohit

import pickle
import pygame
from pygame.locals import *
from sys import exit
import os
from time import *
#from threades import *
#from model import *
import threades
import threading
import gui_buttons
import gui
import game_events
#from gui import *
#from chat import *
import model
import chat
#import texts_spa
#import texts_eng
#from Foodforce2 import Earthquake
import natural_calamities
import level_change
import defaultStyle

load_level_obj = level_change.change_level()

storyboardfile = None
storyboard_file = ''
GAME_END_FLAG = False

# Event Types in case of non-event based conditions

FACILITYNUMBERCONDITION = 1
FACILITYLEVELCONDITION = 2
INDICATORVALUECONDITION = 3
RESOURCEVALUECONDITION = 4
MONEYVALUECONDITION = 5

# Conditions Related Classes

class condition:
    '''Class which defines the behaviour of each single condition
    '''
    Flag = False
    eventBased = True
    eventType = 0
    fac_name = ''
    res_name = ''
    checktype = '=='
    ind_name = ''
    value = 0

    def __init__(self,Flag = False,eventBased = True,eventType = 0,fac_name = '',res_name = '',checktype = '==',ind_name = '',value = 0):

        self.Flag = Flag
        self.eventBased = eventBased
        self.eventType = eventType
        self.fac_name = fac_name
        self.res_name = res_name
        self.checktype = checktype
        self.ind_name = ind_name
        self.value = value

    def checkCondition(self,events = []):
        ''' Checks whether the condition is true or not
        '''

        # Check for event based conditions
        if self.eventBased :
            if self.Flag == False:
                for event in events:
                    if (event.type == self.eventType) and (event.facility_name == self.fac_name) and (event.res_name == self.res_name) :
                        self.Flag = True

        # Check for non event based conditions
        else:
            if self.eventType == FACILITYNUMBERCONDITION:

                for fac in model.facilities_list:
                    if fac.get_name() == self.fac_name:

                        if self.checktype == '==':
                            if fac.get_original_number() == self.value:
                                self.Flag = True
                            else:
                                self.Flag = False

                        if self.checktype == '<=':
                            if fac.get_original_number() <= self.value:
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '>=':
                            if fac.get_original_number() >= self.value:
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '<':
                            if  fac.get_original_number() < self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '>':
                            if  fac.get_original_number() > self.value :
                                self.Flag = True
                            else:
                                self.Flag = False



            if self.eventType == FACILITYLEVELCONDITION:

                for fac in model.facilities_list:
                    if fac.get_name() == self.fac_name:

                        if self.checktype == '==':
                            if fac.get_level() == self.value:
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '<=':
                            if  fac.get_level() <= self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '>=':
                            if fac.get_level() >= self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '<':
                            if fac.get_level() < self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '>':
                            if fac.get_level() > self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


            if self.eventType == INDICATORVALUECONDITION:

                for ind in model.indicators_list:
                    if ind.get_name() == self.ind_name:

                        if self.checktype == '==':
                            if ind.get_value() == self.value:
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '<=':
                            if  ind.get_value() <= self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '>=':
                            if  ind.get_value() >= self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '<':
                            if ind.get_value() < self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '>':
                            if ind.get_value() > self.value :
                                self.Flag = True
                            else:
                                self.Flag = False



            if self.eventType == RESOURCEVALUECONDITION:

                for res in model.resources:
                    if res.get_name() == self.res_name:

                        if self.checktype == '==':
                            if res.get_vquantity() == self.value:
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '<=':
                            if  res.get_vquantity() <= self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '>=':
                            if  res.get_vquantity() >= self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '<':
                            if  res.get_vquantity() > self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


                        if self.checktype == '>':
                            if  res.get_vquantity() > self.value :
                                self.Flag = True
                            else:
                                self.Flag = False


            if self.eventType == MONEYVALUECONDITION:


                if self.checktype == '==':
                    if model.money.get_money() == self.value:
                        self.Flag = True
                    else:
                        self.Flag = False


                if self.checktype == '<=':
                    if  model.money.get_money() <= self.value :
                        self.Flag = True
                    else:
                        self.Flag = False


                if self.checktype == '>=':
                    if  model.money.get_money() >= self.value :
                        self.Flag = True
                    else:
                        self.Flag = False


                if self.checktype == '<':
                    if model.money.get_money() < self.value :
                        self.Flag = True
                    else:
                        self.Flag = False


                if self.checktype == '>':
                    if  model.money.get_money() > self.value :
                        self.Flag = True
                    else:
                        self.Flag = False



        return self.Flag








class checkConditions:
    ''' Class which initializes the conditions and checks their status
    '''
    closure = ''
    timer = -1
    time = 0
    conditionslist = []


    def __init__(self,condn):
        ''' Initializes the variables of the class
        '''
        self.closure = condn[0]
        self.timer = condn[1]   # TODO timer here should be in days
        condnlist = condn[2]
        self.conditionslist = []

        for Conditions in condnlist:
            addcondition = condition(False,Conditions[0],Conditions[1],Conditions[2],Conditions[3],Conditions[4],Conditions[5],Conditions[6])
            self.conditionslist.append(addcondition)

        if not (self.timer == -1):
            self.time = 0
            self.init_days = model.game_controller.get_total_days()
            
    def checkConditions(self,events):
        ''' Returns 0/1/2 depending upon the state of conditions
            0 : The conditions are still being tested and the player has neither failed the mission nor has he passed it
            1 : The player has passed the mission
            2 : The player has failed the mission
        '''

        Flag = True
        if threades.levelStartFacilityBuildFlag > 0 or (not threades.levelStartUpdateFlag):
            return 0

        for conditions in self.conditionslist:
            Flag = conditions.checkCondition(events) and Flag

        if self.closure == 'AND':
            if Flag:
                return 1
            else:
                return 0

        if self.closure == 'NOR':

            if Flag and (not self.getTimerFlag()):
                return 0
            if Flag and self.getTimerFlag():
                return 1
            if (not Flag):
                return 2



    def getTimerFlag(self):
        '''Returns True if time got over else returns False
        '''

        if self.init_days > model.game_controller.get_total_days():
            self.init_days = model.game_controller.get_total_days()
        
        self.currentdays = model.game_controller.get_total_days()
        if self.currentdays >= self.timer + self.init_days:
            return True
        else:
            return False


# Constants For actions

CHATACTION = 1
LOADNEXTLEVELACTION = 2
LOADSAMELEVELACTION = 3
EARTHQUAKEACTION = 4
DELAYACTION = 5
WFPWINDOWACTION = 6
STORYBOARDWINDOWACTION = 7
FAILUREWINDOWACTION = 8
SBINSTRUCTIONMESSAGE = 9
GAMEENDACTION = 10
# Global variable for storyboard level
storyboard_level = 1

# Action Related classes

class actionTemplate:

    ''' The template for the actions which will take place
    '''
    actionType = 0

    def __init__(self,actionType = 0,data = None):
        self.actionType = actionType
        self.data = data


class Actions:
    ''' Class which contains a list of all the events
        which can happen in the game while the sequential flow
    '''

    def __init__(self,action):
        ''' Initialises the action and takes the corresponding action
        '''

        self.curentLevel = 1
        self.time = 0
        self.timer = 0
        #print action.actionType
        if action.actionType == 1:
            self.Chat(action.data)
        if action.actionType == 2:
            self.loadNextLevel()
        if action.actionType == 3:
            self.loadLevelAgain()
        if action.actionType == 4:
            self.callEarthquake()
        if action.actionType == 5:
            self.initDelay(action.data)
        if action.actionType == 6:
            self.showWFPWindow(action.data)
        if action.actionType == 7:
            self.showStoryboardWindow(action.data)
        if action.actionType == 8:
            self.showFailureWindow(action.data)
        if action.actionType == 9:
            self.showInstructionMessage(action.data)
        if action.actionType == 10:
            self.showCredits()
            




    def Chat(self,data):
        '''
            Chat text should be a list with first the name
            of the character and then his dialogue,

        '''
        if gui_buttons.gui_obj.get_child_win_flag():
            gui_buttons.gui_obj.close_child_win()
        if gui_buttons.gui_obj.get_win_flag():
            gui_buttons.gui_obj.close_win()

        text = data[0]
        bckgnd = data[1]
        print 'In pro'
        print bckgnd
        chat.showChat(text,bckgnd)
        event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
        game_events.EventQueue.add(event)

    def initDelay(self,time):
        ''' To be called when initialising the delay
        '''
        self.timerClock = pygame.time.Clock()
        self.timerClock.tick()
        self.time = 0
        self.timer = time

    def checkDelay(self):
        ''' To be called when checking the delay
        '''
        timeElapsed = self.timerClock.tick(30)
        if not (timeElapsed>1000):
            self.time += timeElapsed
        if self.time < self.timer:
            return False
        else:
            event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
            game_events.EventQueue.add(event)
            return True




    def callEarthquake(self):
        natural_calamities.earthquake()
        

    def loadNextLevel(self):

        global storyboard_level   
        data_file = os.path.join('storyboards',str(model.storyboard_file),'data','data'+str(storyboard_level+1)+'.pkl')
               
        model.game_controller.reset_time()
        graphics_file = 'graphics_layout.pkl'
        storyboard_level += 1
        load_level_obj.new_level_stats(data_file,graphics_file)
        event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
        game_events.EventQueue.add(event)


    def loadLevelAgain(self):
        print "Number 2"
        global storyboard_level
        data_file = os.path.join('storyboards',str(model.storyboard_file),'data','data'+str(storyboard_level)+'.pkl')
                
        graphics_file = 'graphics_layout.pkl'
        load_level_obj.new_level_stats(data_file,graphics_file)
        # Seeking in the storyboard to the current level
        model.game_controller.reset_time()
        closeStoryBoardFile()
        openStoryBoardFile()
        lev = 1
        while not lev == storyboard_level:
            obj = pickle.load(storyboardfile)
            if ((obj[0] == 'actionTrue') or (obj[0] == 'action')) and (obj[1][0] == 2):
                lev += 1

        if not storyboard_level == 1:
            run = True
            if obj[0] == 'actionTrue':

                while run :
                    obj = pickle.load(storyboardfile)
                    if obj[1][0] == 3:
                        run = False

        # End of seeking


        event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
        game_events.EventQueue.add(event)


    def showWFPWindow(self,text):


        self.brown_color = (255,214,150)
        self.green_color = (0,250,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(40))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.brown_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = self.brown_color
        win_style['border-width'] = 2

        st_desktop = gui.Desktop()
        clock = pygame.time.Clock()
        clock.tick(30)

        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((150.0,100.0))
        size_win =threades.resize_pos((700.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = st_desktop, text = "    Reward" , style = win_style, shadeable = False, closeable = False,moveable = False)
        #self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        #self.win.surf.set_alpha(140) This seems to be redundant as translucency doesnt seems to work properly

        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 0
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.brown_color
        labelStyleCopy['border-color'] = self.black_color

        self.storyboardwin_run = True
        logo =  pygame.image.load(os.path.join('data', 'WFPLOGO.png')).convert()
        ff_logo = pygame.transform.scale(logo,threades.resize_pos((500,500)))
        position_blit = threades.resize_pos((100,100))
        self.win.surf.blit(ff_logo,position_blit)
        update_rect = pygame.Rect(threades.resize_rect((150,100,700,600)))

        #self.instructions_counter = 0
        label = gui.Label(position = threades.resize_pos((50.0,100.0),(700.0,600.0),self.win.size),size = threades.resize_pos((600.0,440.0),(700.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)

        gl_time = 0

        while self.storyboardwin_run:
            pygame.display.set_caption('FoodForce2')

            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.storyboardwin_run = False

            gl_time += clock.tick(30)
            if gl_time >= 17000:
                self.storyboardwin_run = False

            st_desktop.update()
            st_desktop.draw()
            pygame.display.update([update_rect])
        self.win.close()

        event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
        game_events.EventQueue.add(event)

    def showInstructionMessage(self,text):
        
        thread_instruction = threading.Thread(target = gui_buttons.showMessages.addMessage, args=[text,True]).start()
        event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
        game_events.EventQueue.add(event)
        
        
    def showStoryboardWindow(self,text):

        self.brown_color = (255,214,150)
        self.green_color = (0,250,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(40))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.brown_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = self.brown_color
        win_style['border-width'] = 2

        st_desktop = gui.Desktop()
        clock = pygame.time.Clock()
        clock.tick(30)

        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((150.0,100.0))
        size_win =threades.resize_pos((900.0,500.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = st_desktop, text = "                               FoodForce2" , style = win_style, shadeable = False, closeable = False,moveable = False)
        #self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        #self.win.surf.set_alpha(140) This seems to be redundant as translucency doesnt seems to work properly

        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 0
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.brown_color
        labelStyleCopy['border-color'] = self.black_color

        update_rect = pygame.Rect(threades.resize_rect((150,100,900,500)))

        self.storyboardwin_run = True
        #logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        #ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))

        #self.instructions_counter = 0
        label = gui.Label(position = threades.resize_pos((100.0,100.0),(900.0,500.0),self.win.size),size = threades.resize_pos((700.0,340.0),(900.0,500.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)

        gl_time = 0

        st_desktop.update()
        st_desktop.draw()
        pygame.display.update([update_rect])

        while self.storyboardwin_run:
            pygame.display.set_caption('FoodForce2')

            for e in gui.setEvents(pygame.event.get()):
                if e.type == MOUSEBUTTONDOWN:
                    if e.button == 1:
                        self.storyboardwin_run = False
                    
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.storyboardwin_run = False

            gl_time += clock.tick(30)
            if gl_time >= 17000:
                self.storyboardwin_run = False



        self.win.close()

        event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
        game_events.EventQueue.add(event)


    def showFailureWindow(self,text):

        self.brown_color = (255,214,150)
        self.green_color = (0,250,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(40))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.brown_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = self.brown_color
        win_style['border-width'] = 2

        st_desktop = gui.Desktop()
        clock = pygame.time.Clock()
        clock.tick(30)

        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((150.0,100.0))
        size_win =threades.resize_pos((900.0,500.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = st_desktop, text = " FoodForce2" , style = win_style, shadeable = False, closeable = False,moveable = False)
        #self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        #self.win.surf.set_alpha(140) This seems to be redundant as translucency doesnt seems to work properly

        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 0
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.brown_color
        labelStyleCopy['border-color'] = self.black_color

        self.storyboardwin_run = True
        #logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        #ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))

        #self.instructions_counter = 0
        label = gui.Label(position = threades.resize_pos((100.0,100.0),(900.0,500.0),self.win.size),size = threades.resize_pos((700.0,340.0),(900.0,500.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)

        gl_time = 0

        st_desktop.update()
        st_desktop.draw()
        pygame.display.update()
        
        while self.storyboardwin_run:
            pygame.display.set_caption('FoodForce2')

            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.storyboardwin_run = False
                #if e.type == MOUSEBUTTONDOWN:
                    #if e.button == 1:
                        #self.storyboardwin_run = False
                    
            gl_time += clock.tick(30)
            if gl_time >= 17000:
                self.storyboardwin_run = False




        event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
        game_events.EventQueue.add(event)


    def showCredits(self):
    
        global GAME_END_FLAG
        self.brown_color = (255,214,150)
        self.green_color = (0,250,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(40))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.brown_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = self.brown_color
        win_style['border-width'] = 2

        st_desktop = gui.Desktop()
        clock = pygame.time.Clock()
        clock.tick(30)

        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((150.0,100.0))
        size_win =threades.resize_pos((900.0,500.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = st_desktop, text = "                               Credits" , style = win_style, shadeable = False, closeable = False,moveable = False)
        #self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        #self.win.surf.set_alpha(140) This seems to be redundant as translucency doesnt seems to work properly

        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 0
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.brown_color
        labelStyleCopy['border-color'] = self.black_color

        update_rect = pygame.Rect(threades.resize_rect((150,100,900,500)))

        self.storyboardwin_run = True
        #logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        #ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
        text = model.text_file.credits_text
        #self.instructions_counter = 0
        label = gui.Label(position = threades.resize_pos((100.0,100.0),(900.0,500.0),self.win.size),size = threades.resize_pos((700.0,380.0),(900.0,500.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)

        gl_time = 0

        st_desktop.update()
        st_desktop.draw()
        pygame.display.update([update_rect])

        while self.storyboardwin_run:
            pygame.display.set_caption('FoodForce2')

            for e in gui.setEvents(pygame.event.get()):
                if e.type == MOUSEBUTTONDOWN:
                    if e.button == 1:
                        self.storyboardwin_run = False
                    
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.storyboardwin_run = False

            gl_time += clock.tick(30)
            if gl_time >= 17000:
                self.storyboardwin_run = False



        self.win.close()
        
        GAME_END_FLAG = True

# Storyboard Related Functions

def openStoryBoardFile():

    global storyboardfile
    global storyboard_file_name
    if model.storyboard_file != '':
        storyboardfile = open(os.path.join('storyboards',model.storyboard_file,'storyboard_'+model.select_lang_flag+'.pkl'),'rb')

def closeStoryBoardFile():
    if model.storyboard_file != '':
        storyboardfile.close()


# Functions to handle events and conditions
class storyboardFlow:


    def __init__(self):
        self.runFlag = True
        self.actionRunningFlag = False
        self.conditionTestingFlag = False
        self.prevConditionResult = -1
        self.norConditionFlag = False

    def flow(self):


        events_list = game_events.EventQueue.get_events()

        if self.actionRunningFlag:
            
            if not self.action.timer == 0:
                self.action.checkDelay()
            for event in events_list:
                if event.type == game_events.ACTIONCOMPLETEEVENT:
                    self.actionRunningFlag = False

        elif self.conditionTestingFlag:
            if self.checkConditionsObj.checkConditions(events_list) == 1:
                self.prevConditionResult = 1
                self.conditionTestingFlag = False
            if self.checkConditionsObj.checkConditions(events_list) == 2:
                self.prevConditionResult = 2
                self.conditionTestingFlag = False

        else:
            
            try:
                variable = pickle.load(storyboardfile)
                if variable[0] == 'action':
                    tempAction = actionTemplate(variable[1][0],variable[1][1])
                    if tempAction.actionType == 1:
                        tempAction.data[1] = os.path.join(str(model.storyboard_file),'images','chat images',tempAction.data[1])
                    self.action = Actions(tempAction)
                    self.actionRunningFlag = True
                    self.norConditionFlag = False


                if variable[0] == 'condition':
                    self.checkConditionsObj = checkConditions(variable[1])
                    self.conditionTestingFlag = True
                    if variable[1][0] == 'NOR':
                        self.norConditionFlag = True
                    else:
                        self.norConditionFlag = False

                if self.norConditionFlag:
                    if (variable[0] == 'actionTrue') and (self.prevConditionResult == 1):
                        
                        tempAction = actionTemplate(variable[1][0],variable[1][1])
                        self.action = Actions(tempAction)
                        self.actionRunningFlag = True

                    if (variable[0] == 'actionFalse') and (self.prevConditionResult == 2):
                        
                        tempAction = actionTemplate(variable[1][0],variable[1][1])
                        self.action = Actions(tempAction)
                        self.actionRunningFlag = True


            except EOFError:
                self.action.showCredentials()

