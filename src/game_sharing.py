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

import olpcgames.mesh as mesh
from sugar.presence import presenceservice
import sys
import types
import pygame
#from threades import *
import threades
import threading

from time import sleep,time,ctime
import gui
#from gui import *

presenceService = presenceservice.get_instance()

_is_shared=False
_is_connected=False
Flag_Trading_Unicast_Recieve_Sell = False
Flag_Trading_Unicast_Recieve_Buy = False
Flag_Trading_Unicast_Acknowledge = False

players_in_game={}
buddy=None
check_withBuddy=False

def withBuddy(buddy1):

    global buddy
    global check_withBuddy
    buddy=buddy1
    print buddy.props.nick
    print 'reached in withbuddy\n'
    check_withBuddy=True
                    
                        
    
class Player:
    def __init__(self,handle,buddy2):
        self.buddy=buddy2
        self.nick=buddy2.props.nick
        self.handle=handle


#these 3 fns will be useful if we decide to make the 3 global variables to be local to this file only
def test_sharing():
    global _is_shared
    return _is_shared

def test_connected():
    global _is_connected
    return _is_connected

def test_players_in_game():             #returns the dictionary of all the players in the game
    global players_in_game
    return players_in_game

def broadcast_msg(msg_content):
    print 'in game_sharing.broadcast_msg'
    mesh.broadcast(msg_content)

def unicast_msg(handle,msg_content):
    mesh.send_to(handle,msg_content)
    
#Functions been made by mohit, yet to be completed
def setUnicastTradingFlag(signal): 
    
    global Flag_Trading_Unicast_Recieve_Buy
    global Flag_Trading_Unicast_Recieve_Sell
    
    if signal=='buy':
        Flag_Trading_Unicast_Recieve_Buy = True
    if signal == 'sell':
        Flag_Trading_Unicast_Recieve_Sell = True
        
def setUncastTradingAcknowledgeFlag(signal):
    
    global Flag_Trading_Unicast_Acknowledge
    Flag_Trading_Unicast_Acknowledge = signal

def messageResponderBroadcast(handle,nick,message):

    global Flag_Trading_Unicast_Acknowledge
    if message[0] == 'Trade':
        object_trade = meshTrading()
        trade_thread = threading.Thread(target = object_trade.tradingWindow, args=[handle,nick,message[1],message[2],message[3],message[4]]).start()
        #object_trade.tradingWindow(handle,nick,message[1],message[2],message[3],message[4])
        #Flag_Trading_Unicast_Acknowledge = True
        
def messageResponderUnicast(handle,nick,message):
    
    global Flag_Trading_Unicast_Acknowledge
    global Flag_Trading_Unicast_Recieve_Buy
    global Flag_Trading_Unicast_Recieve_Sell
    
    if Flag_Trading_Unicast_Acknowledge:
        
        if message[0] == 'acknowledge_trade':
            res_name = message[1]
            quantity = int(message[2])
            price = int(message[3])
            buysell = message[4]
            for res in threades.resources:
                if res.get_name() == res_name:
                    break
            if buysell == 'sell':
                threades.buy_res(res,quantity,price)
            if buysell == 'buy':
                threades.sell_res(res,quantity,price)
            Flag_Trading_Unicast_Acknowledge = False
            threades.message.push_message('The Resources have been traded','low')
            
        if message[0] == 'decline_trade':
            threades.message.push_message('The Resources have already been traded with someone','medium')
                
    if Flag_Trading_Unicast_Recieve_Buy:
        if message[0] == 'TradeReply':
            res_name = message[1]
            quantity = int(message[2])
            price = int(message[3])
            for res in threades.resources:
                if res.get_name() == res_name:
                    break
            threades.buy_res(res,quantity,price)
            Flag_Trading_Unicast_Recieve_Buy = False
            threades.message.push_message('The Resources have been traded with '+nick,'low')
            message[0] = 'acknowledge_trade'            
            unicast_msg(handle,message)
            
    if Flag_Trading_Unicast_Recieve_Sell:
        if message[0] == 'TradeReply':
            res_name = message[1]
            quantity = int(message[2])
            price = int(message[3])
            for res in threades.resources:
                if res.get_name() == res_name:
                    break
            threades.sell_res(res,quantity,price)
            Flag_Trading_Unicast_Recieve_Sell = False
            threades.message.push_message('The Resources have been traded with '+nick,'low')
            message[0] = 'acknowledge_trade'
            unicast_msg(handle,message)
            
    
    if (not Flag_Trading_Unicast_Recieve_Buy) and (not Flag_Trading_Unicast_Recieve_Sell):
        if message[0] == 'TradeReply':
            message[0] = 'decline_trade'             
            unicast_msg(handle,message)
            
    
            
    

def sharing_handler(type,handle,content):
    global buddy
    global _my_handle
    global players_in_game
    global check_withBuddy
    global _is_shared
    global _is_connected
    
    if type == mesh.CONNECT:
            _is_shared=True
            print "Connected to the mesh."
            
    elif type == mesh.PARTICIPANT_ADD:
            mesh.lookup_buddy(handle,callback=withBuddy )
            while check_withBuddy==False:
                pass
            
            if handle == mesh.my_handle():
                
                _my_handle=mesh.my_handle()
                xoOwner = presenceService.get_owner()
                player=Player(handle,xoOwner)
                players_in_game[_my_handle]=player
                
                print "Me:", buddy.props.nick
                check_withBuddy=False
                
                
            else:
                _is_connected=True
                print "Join:", buddy.props.nick
                

                player = Player(handle,buddy)
                players_in_game[handle] = player
                
                #remove these in real game - just for testing
                # send a test message to the new player
                broadcast_msg(['Welcome player.nick' ,'get in the game'])
                # tell them which maze we are playing, so they can sync up
                unicast_msg(handle, ['Trying to send you personal msgs','hope you dont mind'])
                check_withBuddy=False

    elif type == mesh.PARTICIPANT_REMOVE:
            if players_in_game.has_key(handle):
                player = players_in_game[handle]
                print "Leave:", player.nick
                
                
                del players_in_game[handle]

                if handle==_my_handle:                       #XXX: not sure whether if we will leave the game, we ourselves will receive the message 
                    _is_shared=False                               #or not
                    _is_connected=False
                    players_in_game.clear()
                    
                elif len(players_in_game)==1:
                    _is_connected=False

            print 'someone is removed'


    elif type == mesh.MESSAGE_MULTI:
        if handle == mesh.my_handle():
                # ignore messages from ourselves
                print 'I have broadcasted '

        elif players_in_game.has_key(handle):
                player = players_in_game[handle]
                try:
                    
                    
                    print "got a broadcasted msg from %s" % (player.nick)
                    '''
                    if content==types.IntType:
                        pass
                    if content==types.FloatType:
                        pass
                    if content==types.LongType:
                        pass
                    #if content==types.StringType:
                    #    pass
                    if content==types.DictType:
                        pass
                    if content==types.TupleType:
                        pass
                    #if content==types.ListType:
                       # pass
                    for i,v in enumerate(content):
                        print i,v
                    
                    
                    #unicast the person who has broadcasted
                    
                    for p in players_in_game.itervalues():
                        if p==player:
                            unicast_msg(p.handle, "Succeeded in unicasting")
                    '''
                    for i,v in enumerate(content):
                        print i,v
                    messageResponderBroadcast(handle,player.nick,content)
                            
                except:
                    print "Error handling message: %s\n%s" % (type, sys.exc_info())
                    
        else:
                print "Message from unknown buddy?"

    elif type ==mesh.MESSAGE_UNI:
        if handle == mesh.my_handle():
                # ignore messages from ourselves
                print 'I have unicasted myself,might be of trouble'

        elif players_in_game.has_key(handle):
                player = players_in_game[handle]
                try:
                    
                    print "got a unicasted msg from %s" % (player.nick)

                    if content==types.IntType:
                        pass
                    if content==types.FloatType:
                        pass
                    if content==types.LongType:
                        pass
                    #if content==types.StringType:
                     #   pass
                    if content==types.DictType:
                        pass
                    if content==types.TupleType:
                        pass
                  #  if content==types.ListType:
                   #     pass
                    for i,v in enumerate(content):
                        print i,v

                    messageResponderUnicast(handle,player.nick,content)
                               
                except:
                    print "Error handling message: %s\n%s" % (type, sys.exc_info())
                    
        else:
                print "Message from unknown buddy?"
        
                








class meshTrading:
    '''Class which handles matters regarding the trading over
       Mesh Network
    '''    
    def tradingWindow(self,handle,buddyName = 'Friend',resource = 'Water', quantity = '0' ,price = '10',trade = 'sell'):
        '''Opens the trading window at the reciever end for trading
        '''        

        #self.font_color = (255,214,150) # Brown
        self.replyhandle = handle
        self.replymessage = ['TradeReply',resource,quantity,price,trade]
        color_blue = (0,0,250)
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))
        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['bg-color'] = (0,0,0)
        win_style['font-color'] = color_blue
        
        # Calculating position and size of window from the size of the desktop
        position_win =threades.resize_pos((725.0,42.0))
        size_win =threades.resize_pos((470.0,180.0))
    
        # Creating custom label style for the text to be displayed as a message
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont
        labelStyleCopy['font-color'] = color_blue
        #labelStyleCopy['font-color'] = font_color
    
        self.win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = "Trade " ,style = win_style,shadeable = False, moveable = False)
        # Creating label
        label_text = '\n'+buddyName + ' wants to ' + trade + ' ' + quantity + ' units of '+ resource + '\n at $ '+ price 
        message_label = gui.Label(position = threades.resize_pos((5,5),(470.0,180.0),self.win.size),size = threades.resize_pos((460,120),(470.0,180.0),self.win.size), parent = self.win, text = label_text, style = labelStyleCopy)
        
        # Creating button style
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(16))
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_accept = gui.Button(position = threades.resize_pos((100.0,130.0),(470.0,180.0),size_win), size = threades.resize_pos((100.0,40.0),(470.0,180.0),size_win), parent = self.win, text = " Accept ",style = button_style)
        self.button_reject = gui.Button(position = threades.resize_pos((300.0,130.0),(470.0,180.0),size_win), size = threades.resize_pos((100.0,40.0),(470.0,180.0),size_win), parent = self.win, text = " Reject ",style = button_style)
        
        self.button_accept.onClick = self.checkTrade
        self.button_reject.onClick = self.closeWin
        
        sleep(6)
        if self.win:
            self.win.close()
                    
    def checkTrade(self,button = None):
        ''' Sends an acceptance request to the person who tried to trade 
        '''
        
        unicast_msg(self.replyhandle,self.replymessage)
        setUncastTradingAcknowledgeFlag(True)
        self.closeWin()
        
            
    def closeWin(self,button = None):
        self.win.close()












                
    
