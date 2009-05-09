#! /usr/bin/env python
#

# ***** BEGIN LICENSE BLOCK *****
# Version: CPAL 1.0
#
# The contents of this file are subject to the Common Public Attribution
# License Version 1.0 (CPAL); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://opensource.org/licenses/cpal_1.0
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# ***** END LICENSE BLOCK ****
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
        
        