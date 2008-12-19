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

from sys import exit
import os
from time import *
from threades import *
import threades
import threading

import gui
from gui import *


class chat:
    
    ''' Class which is used to show chats for the storyline
    '''
    
        
    def __init__():
        
        ''' Constructor
        '''
        
        self.chatWinFlag = False
        
    def chatWindow(windowtext = None):
        
        ''' Opens a new chat window
        '''
        
        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the desktop        
        position_win =resize_pos((0.0,0.0))
        size_win =new_screen_size

        # Creating window
        self.chatWin = Window(position = position_win, size = size_win, parent = desktop, text = '' ,style = win_style,closeable = False,shadeable = False,moveable = False)
        self.chatWin.surf.set_alpha(140)
        
        self.chatWinFlag = True
        
    def addChat(playerName = None,message = ''):
        
        ''' Adds Chat to the chat window
        '''
        
        #TODO: Make a list of all the characters and make their pics
        #and load them in a dictionary with their names as keys
        
        srf = pygame.surface.Surface(resize_pos(
        