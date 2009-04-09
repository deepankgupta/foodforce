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
import threades
import threading
import gui_buttons
import gui
from gui import *


class chat:
    
    ''' Class which is used to show chats for the storyline
    '''
    
        
    def __init__(self):
        
        ''' Constructor
        '''
        
        self.chatWinFlag = False
        self.position = (15,10)
        self.initial_position = (15,10)
        self.final_position = (15,600)
        self.imageBox = pygame.image.load(os.path.join('art', 'imageBox.png')).convert_alpha()
        self.chatBox = pygame.image.load(os.path.join('art', 'chatBox.png')).convert_alpha()
        self.characterImage={}
        self.characterImage['KAMAT']=pygame.image.load(os.path.join('art', 'kamat.png')).convert_alpha()
        self.characterImage['SON']=pygame.image.load(os.path.join('art', 'son.png')).convert_alpha()
        self.characterImage['AJMAL']=pygame.image.load(os.path.join('art', 'ajmal.png')).convert_alpha()
        
        
        
    def chatWindow(self,windowtext = None):
        
        ''' Opens a new chat window
        '''
        
        # Disable other gui
        gui_buttons.gui_obj.disable_buttons()   
        
        # Stopping the updation thread
        pause_update_thread()

        
        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the desktop        
        position_win =resize_pos((150.0,75.0))
        size_win = resize_pos((900,750))

        # Creating window
        self.chatWin = Window(position = position_win, size = size_win, parent = desktop, text = '' ,style = win_style,closeable = False,shadeable = False,moveable = False)
        self.chatWin.surf.set_alpha(140)
        
        self.chatWinFlag = True
        
        
    def closeChatWindow(self):
        
        # Enable the gui
        gui_buttons.gui_obj.enable_buttons()
        self.chatWin.close()
        self.chatWinFlag=False
        resume_update_thread()
        
    def addChat(self,playerName = None,message = ''):
        
        ''' Adds Chat to the chat window
            playerName tells the name of the character whose image to be used
            and message sends his mesage.
        '''
        
        #TODO: Make a list of all the characters and make their pics
        # and load them in a dictionary with their names as keys
        # Assuming the dictionary to be playerCharactersImages
        
        self.myfont = pygame.font.Font("font.ttf",20)
        textColor = (0,0,0)
        textSurface = renderText(message,self.myfont,True,textColor,(635,500),False,True)    #here 500(y-coordinate) doesn't make any difference , not used in renderText
        #my_rect=pygame.Rect((0,0,500,500))
        #textSurface=render_textrect(message,self.myfont, my_rect, textColor, None, justification=0)
        tempsize = textSurface.get_size()
        print tempsize[0],tempsize[1]
        tempsize2=tempsize[1]+50
        if tempsize2>120:
            tempSurface = pygame.transform.scale(self.chatBox,(720,tempsize[1]+50))
        else:
            tempSurface = pygame.transform.scale(self.chatBox,(720,120))
        print 'color key is ',tempSurface.get_colorkey()
        tempSurface.blit(textSurface,(50,25))
        tempsize2=tempSurface.get_size()
        print (tempSurface.get_size())[0],(tempSurface.get_size())[1]
        
        dim_y = 0
        if tempsize2[1]>120 :
            dim_y = tempsize2[1]
        else:
            dim_y = 120
            
        finalSurface = pygame.surface.Surface((870,dim_y+30)).convert()
        #pos_of_image_on_finalsurface=(((dim_y)/2)-60)+15
        finalSurface.blit(self.imageBox,(15,15))
        finalSurface.blit(tempSurface,(135,15))
        #finalSurface.blit(playerCharactersImages[playerName],(24,24))
        finalSurface.blit(self.characterImage[str.upper(playerName)],(24,15+9))
        
        finalSurface = pygame.transform.scale(finalSurface,resize_pos(finalSurface.get_size()))
        tempsize = finalSurface.get_size()
        dim_y = tempsize[1]
        
        if (self.position[1]+ dim_y) > self.final_position[1]:
            self.closeChatWindow()
            self.chatWindow()
            self.position = self.initial_position
            self.chatWin.surf.blit(finalSurface,self.position)
            self.position=(self.position[0],self.position[1]+dim_y)
        else:
            self.chatWin.surf.blit(finalSurface,self.position)
           # self.position[1] += dim_y
            self.position=(self.position[0],self.position[1]+dim_y)
            
        
            
            
def showChat(chatText):
    
    ''' Chat text should be a list with first the name
        of the character and then his dialogue,
    '''
    chatObject = chat()
    chatObject.chatWindow()
    clock = pygame.time.Clock()
    i = 0   
    i_incrementor =False
    run = True
    while run:
        if len(chatText)==0:
            break
        
        for e in gui.setEvents(pygame.event.get()):
                if e.type == pygame.QUIT:
                    pygame.mixer.quit()
                    pygame.quit()
                    exit()
                
               
        if threades.global_time >= 5000:
                if  i_incrementor==True:
                    i+=2
                threades.global_time = 0
                
                
                chatObject.addChat(chatText[i],chatText[i+1])
                i_incrementor=True
               
        
        desktop.update()
        desktop.draw()
        pygame.display.flip()
        max_iterations=(len(chatText)-2)
        if i == max_iterations:
            while threades.global_time<5000:
                threades.iteration_time = clock.tick()
                threades.global_time += threades.iteration_time
            run = False
                     
        
        threades.iteration_time = clock.tick()
        threades.global_time += threades.iteration_time  
        
        
    chatObject.closeChatWindow()
    
        
