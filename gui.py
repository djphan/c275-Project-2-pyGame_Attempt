import sys, pygame
import random

# Import various assets and modules for function
from ocempgui.widgets import *
from ocempgui.widgets.Constants import *

from sounds import SoundManager

# GUI size information
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800

MAP_WIDTH = 800
BAR_WIDTH = 400
BUTTON_HEIGHT = 50
CENTER = 100

# Set the fonts
pygame.font.init()
FONT_SIZE = 16
BIG_FONT_SIZE = 42
FONT = pygame.font.SysFont("Arial", FONT_SIZE)
BIG_FONT = pygame.font.SysFont("Arial", BIG_FONT_SIZE)
BIG_FONT.set_bold(True)

# padding for left and top side of the bar
PAD = 6

# Speed of reticle blinking
RETICLE_RATE = 0.02

# RGBA colors for grid stuff
SELECT_COLOR = (255, 255, 0, 255)
UNMOVED_COLOR = (0, 0, 0, 255)
MOVE_COLOR_A = (0, 0, 160, 120)
MOVE_COLOR_B = (105, 155, 255, 160)
ATK_COLOR_A = (255, 0, 0, 140)
ATK_COLOR_B = (220, 128, 0, 180)

# RGB colors for the GUI
FONT_COLOR = (0, 0, 0)
BAR_COLOR = (150, 150, 150)
OUTLINE_COLOR = (50, 50, 50)
BUTTON_HIGHLIGHT_COLOR = (255, 255, 255)
BUTTON_DISABLED_COLOR = (64, 64, 64)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#GUI Image File Maps 
HEALTH = ImageLabel ("asset/menu/health.png")
PEOPLE = ImageLabel ("asset/menu/person.png")
FOOD = ImageLabel ("asset/menu/soup.png")
WEAP = ImageLabel ("asset/menu/gun.png")

class GUI:
    def init_draw_window(self, string):
        """
        Initalize the GUI window using OceanGUI modules. This function
        takes in the title of the window as a string, and outputs 
        the base winow GUI.
        """
        window = Renderer ()
        # Window size defined globally at the start of the map
        window.create_screen (WINDOW_WIDTH, WINDOW_HEIGHT)
        window.title = string
        # The GUI color is determined by RGB values
        window.color = (230, 230, 230)
        return window

    def draw_frame(self, menu_object):
        """
        Uses OceanGUI frames to partion the game menu into the three components:
        i. Resource header summary
        ii. Side bar.
        iii. Input window

        Each frame format is slightly different, therefore will take in an argument of the following
        keywords: resources, main_menu, input.

        Modularity can be accomplished if we used one general frame setting. However to make the GUI
        look nicer we will be hard coding values for these different frames. A detailed documentation   
        of the resource menu will be done, as all other menus are modified versions of this.
    
        Any unique changes to individual tables will be shown here.
        """
        if menu_object == "resources":
            # Set a table of row, column size to fill in
            table = Table (2, 2)
            # Set location based on x,y coordinates from top left - Graphical Notations.
            table.topleft = 5, 5
            table.spacing = 5
        
            res_frame = HFrame (Label ("Resource Summary"))
            res_frame.set_boarder = (BORDER_SUNKEN)
            
            table.add_child (0, 0, res_frame)
            res_frame.add_child(HEALTH)
            res_frame.add_child(PEOPLE)
            res_frame.add_child(FOOD)
            res_frame.add_child(WEAP)
        
            return table

        elif menu_object == 'main_menu':
            mm_table = Table (2, 3)

            # Adjust
            mm_table.topleft = 1000, 5
            mm_table.spacing = 5
            
            mm_frame = HFrame (Label ("LOL"))
            mm_frame.set_boarder = (BORDER_SUNKEN)
                
            mm_table.add_child (0, 0, mm_frame)

            for i in xrange(3):
                btn = Button ("Button %d" % i)
                mm_frame.add_child (btn)
            return mm_table    
       
        elif menu_object == 'input':
            inp_table = Table (2, 3)
            inp_table.topleft = 215, 600
            inp_table.spacing = 5
            
            # Create and display two 'standard' frames.
            inp_frame = HFrame (Label ("Input"))
            inp_frame.set_boarder = (BORDER_SUNKEN)
                
            inp_table.add_child (0, 0, inp_frame)

            for i in xrange(3):
                btn = Button ("Button %d" % i)
                inp_frame.add_child (btn)
            return inp_table

        elif menu_object == 'minimap':
            minimap_table = Table (2, 3)
            minimap_table.topleft = 5, 600
            minimap_table.spacing = 5
            
            # Create and display two 'standard' frames.
            minimap_frame = HFrame (Label ("Minimap"))
            minimap_frame.set_boarder = (BORDER_SUNKEN)
                
            minimap_table.add_child (0, 0, minimap_frame)

            for i in xrange(3):
                btn = Button ("Button %d" % i)
                minimap_frame.add_child (btn)
            return minimap_table

        else:
            # Add/overide for other modules.
            pass
       
main_gui = GUI()

main_menu = main_gui.init_draw_window('Zombie Survival Board Game')
main_menu.add_widget(main_gui.draw_frame('resources'))
main_menu.add_widget(main_gui.draw_frame('main_menu'))
main_menu.add_widget(main_gui.draw_frame('minimap'))
main_menu.add_widget(main_gui.draw_frame('input'))
#button = Button ('HelloWorld')
#button.topleft=(100,50)
#main_menu.add_widget (button)

main_menu.start ()
