*********************************************************************************
FoodForce2 Installation Instructions
*********************************************************************************

Once you have downloaded the source and unzipped it, you need the following to run the game

1. Python : Python is generally present on all distributions of linux ( ver. 2.5.1 or greater). 
             If you are trying to run the game from source on windows, you can download python 
             from the following link: http://www.python.org/download/

2. Pygame : Pygame can be installed on any linux system. In ubuntu, you can install pygame from 
             synaptics, and on fedora, it can be installed as easily as " yum install pygame"
             For Windows, one can download pygame from here: http://www.pygame.org/download.shtml

After, installing the above two things, you can run the game by running the FoodForce2.py module
as "python FoodForce2.py" in your terminal.



*********************************************************************************
Creating a distribution for Windows
*********************************************************************************

1. You would be required to install, py2exe for making a windows distribution. One can get py2exe 
    from here: http://www.py2exe.org/

2. Once you have installed py2exe, the windows distribution can be made by running the setup.py file,
    with command line agruements as py2exe i.e. "python setup.py py2exe"
