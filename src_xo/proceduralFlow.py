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

class checkFlow :
    
    ''' Class which maintains a sequential flow of the game
        The class maintains the flow by keeping an account of 
        indicators/facilities/resources or money.
    '''
    
    def __init__(self):
        ''' Constructor of checkflow.
        '''
        
        self.indicator = None
        self.facilities = None 
        self.resources = None 
        self.money = None 
        self.time = None
    
    def clearConditions(self):
        ''' Re-initialises the condition on the gameflow.
        '''
        
        self.indicator = None
        self.facilities = None 
        self.resources = None 
        self.money = None 
        
    def initializeConditions(self,indicator = None,facilities = None,resource = None,money = None):
        ''' Initializes the conditions/boundations 
            on the sequential flow of the game.
        '''
        
        self.indicator = indicator
        self.facilities = facilities
        self.resources = resource
        self.money = money
        
    def checkConditions(self):
        ''' Checks the boundations/conditions on the variables 
            returns True if the conditions have been fulfilled,
            that means the aim of the stage has been achieved, 
            else return False
        '''
        
        flag = True
        
        if self.indicator:
            for key in self.indicator.keys():
                for ind in indicators_list:
                    if ind.name == key :
                        if self.indicator[key] > ind.get_value():
                            flag = False
                    
        if self.facilities:
            for key in self.facilities.keys():
                for fac in facilities_list:
                    if fac._name == key :
                        if self.facilities[key] > fac.get_number():
                            flag = False
                    
        if self.resources:
            for key in self.resources.keys():
                for res in resources:
                    if res._name == key :
                        if self.resources[key] > res.get_vquantity():
                            flag = False
                    
        if self.money:
            if self.money > money.get_money():
                flag = False
        
        return flag
       

class events:
    ''' Class which contains a list of all the events
        which can happen in the game while the sequential flow
    '''
    
    def __init__(self):
        pass
    
    def Chat(self,text):
        ''' Chat text should be a list with first the name
            of the character and then his dialogue,
        '''
        showChat(text)
        
    def 