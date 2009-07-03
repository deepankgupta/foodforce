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





# Macros or say global variables for all the type of events in the game
BUILDFACILITYEVENT = 1
UPGRADEFACILITYEVENT = 2
STOPFACILITYEVENT = 3
RESUMEFACILITYEVENT = 4
DEMOLISHFACILITYEVENT = 5
BUYRESOURCESEVENT = 6
SELLRESOURCESEVENT = 7
ACTIONCOMPLETEEVENT = 8



class eventsQueue:
    ''' The class which will maintain a queue of all the game events
    '''
    
    queue = []
    def add(self,event):
        ''' Adds an event to the queue
        '''
        self.queue.append(event)
        
    def pop(self):
        ''' Pops an event from the queue
        '''
        val = self.queue.pop()
        return val
    
    def get_events(self):
        ''' Sends all the events in the event queue
            also empties the event queue
        '''
        val = self.queue
        self.queue = []
        return val
    
# Initialising an object of the events queue class
EventQueue = eventsQueue()

class Event:
    ''' Generic class for events, each event in 
        the event queue should be an object of this class 
    '''
    
    type = 0
    facility_name = ''
    res_name = ''
    res_quantity = 0
    
    def __init__(self, type = 0, facility_name = '', res_name = '' , res_quantity = 0):
        ''' Initialises the quantity of various variables
        '''
        
        self.type = type
        self.res_name = res_name
        self.facility_name = facility_name
        self.res_quantity = res_quantity
        
        