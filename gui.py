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
        look nicer we will be hard coding values for these different frames.
        """
        table = Table (1,1)
        table.topleft = 5,5
        table.spacing = 5

        if menu_object == "resources":
            frame = HFrame (Label ("Resource Summary"))
            frame.set_boarder = (BORDER_SUNKEN)
            table.add_child = (1, 1, frame)

            for i in xrange(3):
                btn = Button ("Button %d" % i)
                frame.add_child (btn)
               
        elif menu_object == 'main_menu':
            frame.set_boarder = (BORDER_SUNKEN)
            pass
        elif menu_object == 'input':
            frame.set_boarder = (BORDER_SUNKEN)
            pass
        else:
            # Add/overide for other modules.
            pass
       
        return table

main_gui = GUI()

main_menu = main_gui.init_draw_window('Zombie Survival Board Game')
main_menu.add_widget(main_gui.draw_frame("resources"))
#button = Button ('HelloWorld')
#button.topleft=(100,50)
#main_menu.add_widget (button)

main_menu.start ()
