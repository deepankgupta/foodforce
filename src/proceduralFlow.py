#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
#   Date : 9/12/2008 
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

from sys import exit
import os
from time import *
from threades import *
from model import *
import threades
import threading
import gui_buttons
import gui
from gui import *
from chat import *




# Event Types in case of non-event based conditions

FACILITYNUMBERCONDITION = 1
FACILITYLEVELCONDITION = 2
INDICATORVALUECONDITION = 3
RESOURCEVALUECONDITION = 4
MONEYVALUECONDITION = 5


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
        if self.eventBased:
            
            for event in events:
                if (event.type == self.eventType) and (event.facility_name == self.fac_name) and (event.res_name == self.res_name) :
                    self.Flag = True
                    
        # Check for non event based conditions
        else:
            if self.type == FACILITYNUMBERCONDITION:
                
                for fac in facilities_list:                
                    if fac.get_name() == self.fac_name:
                        
                        if self.checktype == '==':
                            if fac.get_original_number() == self.value:
                                self.Flag = True
                    
                        if self.checktype == '<=':
                            if self.value <= fac.get_original_number():
                                self.Flag = True
                        
                        if self.checktype == '>=':
                            if self.value >= fac.get_original_number():
                                self.Flag = True

                        if self.checktype == '<':
                            if self.value < fac.get_original_number():
                                self.Flag = True
                        
                        if self.checktype == '>':
                            if self.value > fac.get_original_number():
                                self.Flag = True


            if self.type == FACILITYLEVELCONDITION:
                
                for fac in facilities_list:                
                    if fac.get_name() == self.fac_name:
                        
                        if self.checktype == '==':
                            if fac.get_level() == self.value:
                                self.Flag = True
                    
                        if self.checktype == '<=':
                            if self.value <= fac.get_level():
                                self.Flag = True
                        
                        if self.checktype == '>=':
                            if self.value >= fac.get_level():
                                self.Flag = True

                        if self.checktype == '<':
                            if self.value < fac.get_level():
                                self.Flag = True
                        
                        if self.checktype == '>':
                            if self.value > fac.get_level():
                                self.Flag = True

            if self.type == INDICATORVALUECONDITION:
                
                for ind in indicators_list:                
                    if ind.get_name() == self.ind_name:
                        
                        if self.checktype == '==':
                            if ind.get_value() == self.value:
                                self.Flag = True
                    
                        if self.checktype == '<=':
                            if self.value <= ind.get_value():
                                self.Flag = True
                        
                        if self.checktype == '>=':
                            if self.value >= ind.get_value():
                                self.Flag = True

                        if self.checktype == '<':
                            if self.value < ind.get_value():
                                self.Flag = True
                        
                        if self.checktype == '>':
                            if self.value > ind.get_value():
                                self.Flag = True

    
            if self.type == RESOURCEVALUECONDITION:
                
                for res in resources:                
                    if res.get_name() == self.res_name:
                        
                        if self.checktype == '==':
                            if res.get_vquantity() == self.value:
                                self.Flag = True
                    
                        if self.checktype == '<=':
                            if self.value <= res.get_vquantity():
                                self.Flag = True
                        
                        if self.checktype == '>=':
                            if self.value >= res.get_vquantity():
                                self.Flag = True

                        if self.checktype == '<':
                            if self.value < res.get_vquantity():
                                self.Flag = True
                        
                        if self.checktype == '>':
                            if self.value > res.get_vquantity():
                                self.Flag = True

            if self.type == MONEYVALUECONDITION:
                
                
                if self.checktype == '==':
                    if money.get_money() == self.value:
                        self.Flag = True
            
                if self.checktype == '<=':
                    if self.value <= money.get_money():
                        self.Flag = True
                
                if self.checktype == '>=':
                    if self.value >= money.get_money():
                        self.Flag = True

                if self.checktype == '<':
                    if self.value < money.get_money():
                        self.Flag = True
                
                if self.checktype == '>':
                    if self.value > money.get_money():
                        self.Flag = True

                             
        return Flag
                                

                        





class checkConditions:
    ''' Class which initializes the conditions and checks their status
    '''
    closure = ''
    timer = -1
    time = 0
    conditionslist = []
    
    
    def initConditions(self,condn):
        ''' Initializes the variables of the class
        '''
        self.closure = condn[0]
        self.timer = condn[1]
        condnlist = condn[2]
        
        for Conditions in condnlist:
            addcondition = condition(False,condn[2][0],condn[2][1],condn[2][2],condn[2][3],condn[2][4],condn[2][5],condn[2][6])
            self.conditionslist.append(addcondition)
            
        if not (self.timer == -1):
            self.time = 0
            self.timerClock = pygame.time.Clock()
            self.timerClock.tick()
            
    def checkConditions(self):
        ''' Returns 0/1/2 depending upon the state of conditions
            0 : The conditions are still being tested and the player has neither failed the mission nor has he passed it
            1 : The player has passed the mission
            2 : The player has failed the mission
        '''
        
        Flag = True
        
        for conditions in self.conditionslist:
            Flag = Flag and conditions.checkCondition()
            
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
        time_click = self.timerClock.click()
        if time_click < 1000:
            self.time += time_click
            
        if self.time >= self.timer:
            return True
        else:
            return False
        
                        

class Actions:
    ''' Class which contains a list of all the events
        which can happen in the game while the sequential flow
    '''
    
    def __init__(self):
        pass
    
    def Chat(self,text,bckgnd=None):
        ''' 
            Chat text should be a list with first the name
            of the character and then his dialogue,
            
        '''
        surf_bckgnd = pygame.image.load(os.path.join('data',bckgnd)).convert()
        surf_bckgnd = pygame.transform.scale(surf_bckgnd,resize_pos((1200,900)))
        screen.blit(surf_bckgnd,(0,0))
        showChat(text)
        
        
    def delay(self,time):
        ''' Need to figure out how to implement this
        '''
        #if 