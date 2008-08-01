from distutils.core import setup
import py2exe

setup(windows = [{"script":"display_panel.py"}],
      data_files=[('data', ["data\earthquake1.png","data\earthquake2.png","data\earthquake3.png",'data\Farm.png','data\Fountain.png','data\hospital_upgrade0.png','data\hospital_upgrade1.png','data\hospital_upgrade2.png','data\hospital_upgrade3.png','data\house_upgrade0.png','data\house_upgrade1.png','data\house_upgrade2.png','data\house_upgrade3.png','data\school_upgrade0.png','data\school_upgrade1.png','data\school_upgrade2.png','data\school_upgrade3.png','data\workshop_upgrade0.png','data\workshop_upgrade1.png','data\workshop_upgrade2.png','data\workshop_upgrade3.png','data\market.png','data\people.png','data\Tileset.png','data\Top.png','data\soundtrack.ogg']),('art', ['art\Button.png', 'art\closebutton.png', 'art\optionbox.png','art\shadebutton.png','art\checkbox.png','art\combobox.png']),('.',['font.ttf']) ])
