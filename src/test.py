import pygame
from pygame.locals import *
from pygame import font
from sys import exit
from time import *
from threades import *
import threading
import gui
from gui import *
import defaultStyle


pygame.init()




# Initialisation of the screen

screen = pygame.display.set_mode((1200,900),DOUBLEBUF,32)
clock = pygame.time.Clock()

run = True

# For initialising the style of the gui
defaultStyle.init(gui)

# Initialisation of GUI elements with the desktop
desktop = Desktop()
update_thread = threading.Thread(target = update_turn, args=[]).start()

class indicators_panel:
    ''' Creates the indicator panel
    '''
    
    def __init__(self):
        self.label = Label(position = (900,600),size = (300,50), parent = desktop, text = "Facilities")
        self.list_name = ['Housing','Nutrition','Health','Education','Training']
        self.list_box_style = gui.defaultListBoxStyle.copy()
        self.list_box_style['item-height'] = 50
        self.label_box1 = ListBox(position = (900,630), size = (200, 250), parent = desktop,  items = self.list_name, style = self.list_box_style)
        self.list_value = []
        for i in range(5):
            self.list_value.append(str(int(indicators_list[i].get_value()))+'%')
        self.label_box2 = ListBox(position = (1100,630), size = (100, 250), parent = desktop,  items = self.list_value, style = self.list_box_style)
        
    def update_value(self):
        self.list_value = []
        for i in range(5):
            self.list_value.append(str(int(indicators_list[i].get_value()))+'%')
        self.label_box2.items = self.list_value
  
        
        
        
        
        
        
        
        
        
        
        
        
indian = indicators_panel()
while run:
    clock.tick()
    display.set_caption(str(int(clock.get_fps())))
    indian.update_value()
    #Just for exit        
    for e in gui.setEvents(pygame.event.get()):
        if e.type == pygame.QUIT:
            exit()            
            run = False
    
    #UPDATE YOUR LOGIC BEFORE UPDATING THE GUI
    #...
    
    #The desktop should be the last thing you update (for performance reasons)
    #First let the gui know events occurred
    
    indian.update_value()
    #Then update the desktop you're using
    desktop.update()
    
    #Here begins rendering
    screen.fill((20,40,50))               
    
    #YOUR RENDERING HERE!!!
    #screen.blit(back, (0,0))
    #END CUSTOM RENDERING
    
    #Last thing to draw, desktop
    desktop.draw()

    #Flips!
    pygame.display.flip()

#Bye bye
pygame.quit()
