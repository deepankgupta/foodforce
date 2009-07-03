import pygame
import os

def load_sound(name):

    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join(name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:

        raise SystemExit, message
    return sound

class backgroundMusic:
    
    def start_music(self):
    
        run = True
        while run :
            try :
                
                pygame.mixer.init()
                self.soundtrack = load_sound(os.path.join('data', 'soundtrack.ogg'))
                self.soundtrack.play(-1)
                run = False
                
            except:
                run = True
                
                
    
    def stop_music(self):
        
        self.soundtrack.stop()
        pygame.mixer.quit()
        
objMusic = backgroundMusic()
        
        
    
    
    
    