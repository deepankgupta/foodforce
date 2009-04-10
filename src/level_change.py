
import gui
import pygame
#from threades import *
import threades
from Foodforce2 import safe_exit
#from gui import *
import threading
#from model import *
import load_images
import model
import os
from pygame.locals import *

desktop_level=gui.Desktop()
#level=1
animation_obj=None


class change_level:
    
    
    def __init__(self):
        self.level_no=-1
    def new_level_stats(self,data_file,graphics_file,level_no=-1):
        #global total_update_flag 
        global animation_obj
        threades.pause_update_thread()           #NOTE FOR ME: don't forget to start the update thread
        self.graphics()
        self.level_no=level_no
        self.data_file=data_file
        self.graphics_file=graphics_file
        self.run=True
        level_updater=threading.Thread(target=self.level_reinit,args=[]).start()
        
        
        
        while 1 :
            pygame.display.set_caption('FoodForce2')
            threades.screen.fill((0,0,0))
            threades.screen.blit(self.ff_logo,threades.resize_pos((40,50)))
        
            for e in gui.setEvents(pygame.event.get()):
                if e.type == pygame.QUIT:
                    print 'in pygame.quit'                    
                    safe_exit()
                if e.type == QUIT:
                    print 'in quit'
                    safe_exit()

            desktop_level.update()
            desktop_level.draw()
            pygame.display.update()
            #if level_updater.is_alive()==False:
               # self.run=False      GREAT THIS IS APPLICABLE ONLY WITH PYTHON 2.6, SO HAVE TO SEARCH SOME OTHER MEANS
            if self.run==False:
                break
           
        print 'now reached here\n'
        
            
        threades.initialize_facilities()
        animation_obj=threades.Animation()        #well, here i am making another instance of the animation_obj thinking we may be using another tileset,
        animation_obj.update()        #though I haven't added anything ryt now but we can now easily add them by making slight changes in the Environment2
          #NOTE: in case we want to just update the previous present animation_obj and not create a new one, then we are req not to empty the market
                 #group we are emptying in the level_reinit fn
                 
        threades.total_update_flag = True
        threades.resume_update_thread()

        
        
    def level_reinit(self):
        #global natural_calamities
        #global all_drawable
        #global villagers
        #global all
        #global facilities_group
        #global market            #do remember to initialise it again
        #global house_sprite_list
        #global House
        #from model import *
        #global Hospital
        #house_sprite_list=['name']
        #del model.house_sprite_list
        #print 'the value before deletion is ',House
        #del House
        #global House
        #print 'the value after new creation is ',House
        j=0
        for l in model.house_sprite_list:
            j+=1
        print 'j=',j
        #emptying all the groups present in threads.py
        local_list=threades.natural_calamities.sprites()
        #natural_calamities.clear()
        i=0
        for sprite in local_list:
            sprite.kill()
            i+=1
        threades.natural_calamities.empty()
        print i
        
        i=0
        local_list=threades.villagers.sprites()
        #villagers.clear()
        for sprite in local_list:
            sprite.kill()
            i+=1 
        threades.villagers.empty()
        print i
        
        
        local_list=threades.all.sprites()
        #all.clear()
        for sprite in local_list:
            sprite.kill()
        threades.all.empty()
        
        local_list=threades.facilities_group.sprites()
        #facilities_group.clear()
        for sprite in local_list:
            sprite.kill()
        threades.facilities_group.empty()
        
        local_list=threades.market.sprites()
        #market.clear()
        for sprite in local_list:
            sprite.kill()
        threades.market.empty()
        
        local_list=threades.all_drawable.sprites()
        #all_drawable.clear()
        for sprite in local_list:
            sprite.kill()
        threades.all_drawable.empty()
        
                
        model.init_cons(self.data_file)
        model.init_obj()
        load_images.graphics_layout(self.graphics_file)
        load_images.load_images()
       
        self.run=False
        print 'reached at last'
        
        
        
        
        
        
    def graphics(self):
        logo = pygame.image.load(os.path.join('data', 'logo.png')).convert()
        self.ff_logo = pygame.transform.scale(logo,threades.resize_pos((1111,250)))
        threades.screen.fill((0,0,0))
        threades.screen.blit(self.ff_logo,threades.resize_pos((40,50)))

        # Font type
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))

        # Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button_green.png')).convert_alpha()
        self.button_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)
        self.exit_button = gui.Button(position = threades.resize_pos((500,700)), size = threades.resize_pos((200,30)), parent = desktop_level, text = "Exit",style = self.button_style)
        #self.exit_button.onClick = safe_exit()  
        
        #creating new label showing loading of level
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont
        labelStyleCopy['font-color'] = (0,200,0)
        #labelStyleCopy['border-color'] = self.black_color
        
        if self.level_no==-1:
            text1='Loading New Level'
        else:
            text1='Loading Level No:'+str(self.level_no)
            
        #creating the label
        label = gui.Label(position = threades.resize_pos((500,600)), size = threades.resize_pos((200,30)), parent = desktop_level,style=labelStyleCopy,text=text1)
        
        #self.run=True
        
        