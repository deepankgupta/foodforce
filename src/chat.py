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
#from threades import *
import threades
import threading
import gui_buttons
import gui
import pygame
import model
from pygame.locals import *


desktopChat = gui.Desktop()
run=False
chatObject=None
clock=None
show_whole_chat_flag=False
move_to_next_chatwin_flag=False
background_image=None

class chat:
    
    ''' Class which is used to show chats for the storyline
    '''
    font_color = (255,214,150) 
        
    def __init__(self):
        
        ''' Constructor
        '''
        global background_image
        self.chatWinFlag = False
        self.position = threades.resize_pos((15,10))
        self.initial_position = threades.resize_pos((15,10))
        self.final_position = threades.resize_pos((15,750))
        self.update_win_pos=pygame.Rect(threades.resize_pos((150.0,50.0)),threades.resize_pos((900,800)))
        self.imageBox = pygame.image.load(os.path.join('art', 'imageBox.png')).convert_alpha()
        self.chatBox = pygame.image.load(os.path.join('art', 'chatBox.png')).convert_alpha()
        self.characterImage={}
        self.characterImage['KAMAT']=pygame.image.load(os.path.join('art', 'kamat.png')).convert_alpha()
        self.characterImage['SON']=pygame.image.load(os.path.join('art', 'son.png')).convert_alpha()
        self.characterImage['AJMAL']=pygame.image.load(os.path.join('art', 'ajmal.png')).convert_alpha()
        self.characterImage['PANCH']=pygame.image.load(os.path.join('art', 'panch.png')).convert_alpha()
        self.characterImage['PRIEST']=pygame.image.load(os.path.join('art', 'priest.png')).convert_alpha()
        self.characterImage['SUKHDEV']=pygame.image.load(os.path.join('art', 'sukhdev.png')).convert_alpha() 
        self.characterImage['FARMER']=pygame.image.load(os.path.join('art', 'villager.png')).convert_alpha() 
        #  changes made while adding skip buttons etc
        self.size_win =threades.resize_pos((900.0,800.0))
        self.myfont = pygame.font.Font("font.ttf", threades.resize_pt(16))
        self.button_style=gui.defaultButtonStyle.copy()
        self.button_style['font']=self.myfont
        
        #crating label textsurface
        #myfont = pygame.font.Font("font.ttf",10)
        #textColor = (0,0,0)
        #self.label_text='     ENTER : To show whole chat at once              ESC : To skip chat           '
        #self.label_textsurface=gui.renderText(self.label_text,myfont,True,textColor,(700,20),False,True)
        #self.label_tempSurface = pygame.transform.scale(self.chatBox,(800,30))
        
        self.label_text='     ENTER : To show whole chat              ESC : To skip chat           '
        self.myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))
        self.labelStyleCopy = gui.defaultLabelStyle.copy()
        self.labelStyleCopy['border-width'] = 1
        self.labelStyleCopy['wordwrap'] = True
        self.labelStyleCopy['autosize'] = False
        self.labelStyleCopy['font'] = self.myfont2
        self.labelStyleCopy['font-color'] = (255,214,150) 
        self.labelStyleCopy['border-color'] = (255,214,150) 
        
   
    def chatWindow(self,windowtext = None):
        
        ''' Opens a new chat window
        '''
        global desktopChat
        global move_to_next_chatwin_flag
        
        move_to_next_chatwin_flag=False     #so that the next window waits for the user to press enter
        # Disable other gui
        gui_buttons.gui_obj.disable_buttons()   
        
        # Stopping the updation thread
        threades.pause_update_thread()

        
        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the desktop        
        position_win =threades.resize_pos((150.0,50.0))
        size_win = threades.resize_pos((900,800))
        #print 'size win is',size_win,'\n'

        
        # Creating window
        self.chatWin = gui.Window(position = position_win, size = size_win, parent = desktopChat, text = '' ,style = win_style,closeable = False,shadeable = False,moveable = False)
        self.chatWin.surf.fill((0,0,0,140))
        self.chatWinFlag = True
        
        #NOTE: This part will be used once we know how to blit buttons on the chat window
        #self.button_skip = gui.Button(position = threades.resize_pos((500.0,10.0),(900.0,800.0),self.size_win), size = threades.resize_pos((80.0,30.0),(900.0,800.0),self.size_win), parent = self.chatWin, text = "Skip",style = self.button_style)
        #self.button_next = gui.Button(position = threades.resize_pos((200.0,10.0),(900.0,800.0),self.size_win), size = threades.resize_pos((80.0,30.0),(900.0,800.0),self.size_win), parent = self.chatWin, text = "Next >",style = self.button_style)
        #self.button_skip.onClick=self.closeChatWindow    
        #self.button_skip.onMouseOver=self.closeChatWindow  
        #print self.button_skip.enabled
        
        #creating label
        self.label = gui.Label(position = threades.resize_pos((100.0,760.0),(900.0,800.0),self.chatWin.size),size = threades.resize_pos((700.0,30.0),(900.0,800.0),self.chatWin.size), parent = self.chatWin, text = self.label_text, style = self.labelStyleCopy)
        
        
        
        
    def closeChatWindow(self,button = None):
        
        # Enable the gui
        
        gui_buttons.gui_obj.enable_buttons()
        #print 'before size is ',self.chatWin.size,'\n'
        self.chatWin.close()
        #print self.chatWin.size
        self.chatWinFlag=False
        threades.resume_update_thread()
        
        
    def addChat(self,playerName = None,message = ''):
        
        ''' Adds Chat to the chat window
            playerName tells the name of the character whose image to be used
            and message sends his mesage.
        '''
        
        #TODO: Make a list of all the characters and make their pics
        # and load them in a dictionary with their names as keys
        # Assuming the dictionary to be playerCharactersImages
        global clock
        global desktopChat
        global move_to_next_chatwin_flag
        global run
        self.myfont = pygame.font.Font("font.ttf",20)
        textColor = (0,0,0)
        textSurface = gui.renderText(message,self.myfont,True,textColor,(635,500),False,True)    #here 500(y-coordinate) doesn't make any difference , not used in gui.renderText
        #my_rect=pygame.Rect((0,0,500,500))
        #textSurface=render_textrect(message,self.myfont, my_rect, textColor, None, justification=0)
        tempsize = textSurface.get_size()
        #print tempsize[0],tempsize[1]
        tempsize2=tempsize[1]+50
        if tempsize2>120:
            tempSurface = pygame.transform.scale(self.chatBox,(720,tempsize[1]+50))
        else:
            tempSurface = pygame.transform.scale(self.chatBox,(720,120))
        #print 'color key is ',tempSurface.get_colorkey()
        tempSurface.blit(textSurface,(50,25))
        tempsize2=tempSurface.get_size()
        #print (tempSurface.get_size())[0],(tempSurface.get_size())[1]
        
        dim_y = 0
        if tempsize2[1]>120 :
            dim_y = tempsize2[1]
        else:
            dim_y = 120
            
        finalSurface = pygame.surface.Surface((870,dim_y+30)).convert_alpha()
        finalSurface.fill((0,0,0,0))
        #pos_of_image_on_finalsurface=(((dim_y)/2)-60)+15
        finalSurface.blit(self.imageBox,(15,15))
        finalSurface.blit(tempSurface,(135,15))
        #finalSurface.blit(playerCharactersImages[playerName],(24,24))
        finalSurface.blit(self.characterImage[str.upper(playerName)],(24,15+9))
        
        finalSurface = pygame.transform.scale(finalSurface,threades.resize_pos(finalSurface.get_size()))
        tempsize = finalSurface.get_size()
        dim_y = tempsize[1]
        #print 'self.position is',self.position[1]
        #print 'dim_y is',dim_y
        #print 'final position is',self.final_position[1]
        if (self.position[1]+ dim_y) > self.final_position[1]:
            #self.chatWin.size = threades.resize_pos((900,20))

            #print 'its in this time'
            #print 'self.position is',self.position[1]
            #print 'dim_y is',dim_y
            #print 'final position is',self.final_position[1]
            
            #code to ensure that a new window is not opened until the user presses enter/next again
            if show_whole_chat_flag==True:
                while move_to_next_chatwin_flag==False:
                    for e in gui.setEvents(pygame.event.get()):
                        chat_event_handle(e)
                        
                    
                    if background_image:
                        threades.screen.blit(surf_bckgnd,(0,0))
                        
                    desktopChat.update()
                    desktopChat.draw()
                    pygame.display.update() 
                    model.iteration_time = clock.tick()
                    model.global_time += model.iteration_time
                    if run==False:
                        
                        return
            
            self.closeChatWindow()
            self.chatWindow()
            self.position = self.initial_position
            self.chatWin.surf.blit(finalSurface,self.position)
            self.position=(self.position[0],self.position[1]+dim_y)
        else:
            #x_coordinate=threades.resize_pt_x(900)
            #y_coordinate=self.chatWin.size[1]+dim_y
            #self.chatWin.size=(x_coordinate,y_coordinate)
            self.chatWin.surf.blit(finalSurface,self.position)
           # self.position[1] += dim_y
            self.position=(self.position[0],self.position[1]+dim_y)
            
        
            
def chat_event_handle(e):
    global run
    global chatObject
    global show_whole_chat_flag
    global move_to_next_chatwin_flag
    if e.type == pygame.QUIT:
        pygame.mixer.quit()
        pygame.quit()
        exit()
    if e.type==KEYDOWN:
        if e.key==27:
            
            run=False
            
        if e.key==K_RETURN:
            if show_whole_chat_flag==False:
                show_whole_chat_flag=True
                chatObject.label.text='     ENTER : To move to next set of chats              ESC : To skip chat           '
            else:
                
                move_to_next_chatwin_flag=True


surf_bckgnd = None
def showChat(chatText,back_image=None):
    
    ''' Chat text should be a list with first the name
        of the character and then his dialogue,
    '''
    global run
    global chatObject
    global show_whole_chat_flag
    global move_to_next_chatwin_flag
    global clock
    global background_image
    global surf_bckgnd    
    
    background_image= back_image

    if back_image:
        surf_bckgnd = pygame.image.load(os.path.join('data',back_image)).convert()
        surf_bckgnd = pygame.transform.scale(surf_bckgnd,threades.resize_pos((1200,900)))
         
    chatObject = chat()
    chatObject.chatWindow()
    clock = pygame.time.Clock()
    show_whole_chat_flag=False
    move_to_next_chatwin_flag=False
    i = 0   
    i_incrementor =False
    run = True
    allowed=True
    global desktop2
    while run:
        if len(chatText)==0:
            break
        
        for e in gui.setEvents(pygame.event.get()):
            chat_event_handle(e)
        
        if back_image:
            threades.screen.blit(surf_bckgnd,(0,0))
            
        desktopChat.update()
        
        
        desktopChat.draw()
       
        pygame.display.update() 
        #print chatObject.button_skip.enabled
                
               
        if (model.global_time >= 10000) or (i==0 and allowed==True) or (show_whole_chat_flag==True):
                if i==0:
                    allowed=False
                if  i_incrementor==True:
                    i+=2
                model.global_time = 0
                
        #pygame.display.update()
                
                
                chatObject.addChat(chatText[i],chatText[i+1])
                if run==False:
                    print 'reaching here also finely'
                i_incrementor=True
            
        
       
        max_iterations=(len(chatText)-2)
        if i == max_iterations:
            while (model.global_time<10000 and show_whole_chat_flag==False) or (show_whole_chat_flag==True and move_to_next_chatwin_flag==False) :
                model.iteration_time = clock.tick()
                model.global_time += model.iteration_time
                for e in gui.setEvents(pygame.event.get()):
                    chat_event_handle(e)
                if back_image:
                    threades.screen.blit(surf_bckgnd,(0,0))
                    
                desktopChat.update()
                desktopChat.draw()
                pygame.display.flip()
                if run==False:
                    break
            run = False
                     
        
        model.iteration_time = clock.tick()
        model.global_time += model.iteration_time  
       
        
    surf_bckgnd = None
    chatObject.closeChatWindow()
    
        
