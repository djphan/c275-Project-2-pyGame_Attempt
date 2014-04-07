import sys 
import pygame, pygame.locals
import random
import maps

# Import various assets and modules for function
from ocempgui.widgets import *
from ocempgui.widgets.Constants import *
from ocempgui.draw import String, Image

from sounds import SoundManager

# GUI size information
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800

# Allows for pygame to render images onto the GUI
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# GUI Image File Maps 
HEALTH = ImageLabel ("asset/menu/health.png")
PEOPLE = ImageLabel ("asset/menu/person.png")
FOOD = ImageLabel ("asset/menu/soup.png")
WEAP = ImageLabel ("asset/menu/gun.png")

#------------

# Set the fonts to render in the GUI
FEAR_FONT = "asset/menu/FaceYourFears.tft"
pygame.font.init()

# RGB colors for the GUI
BASE_COLOUR = (230, 230, 230)

#---------------------------------


# Resource Values
HEALTH_VAL = 100
PEOPLE_VAL = 1
FOOD_VAL = 3
WEAP_VAL = 9

# Default Map size (30X20 TILES)
MAP_WIDTH = 960
MAP_HEIGHT = 640
TILE_DIMENSION = 32

def render_string(string, font, size):
    """
    This is a helper function to render strings as an image widget
    to be processed in the GUI.
    """
    text = String.draw_string(string, font, size, 1, (0,0,0))
    text = ImageLabel(text)
    return text

class GUI():
    """
    This is the core GUI class required to run the game.  It is responsible for 
    rendering all the objects on screen. It will interact with the units and the level
    updating the game's image side as the game is played.

    As well various tools will be used to keep track of map positions and other enviromental
    factors will be used to call on triggered events in the game.
    """
    # Number of GUI instances
    instance_num = 0
	

    def can_move(self):
        pass
    def avaliable_actions(self):
        pass

    def enviroment_update(self):
        pass

    def end_turn(self):
        pass

    def init_draw_window(self, string):
        """
        Initalize the GUI window using OceanGUI modules. This function
        takes in the title of the window as a string, and outputs 
        the base GUI window.
        """
        window = Renderer ()
        # Window size defined globally at the start of the map
        window.create_screen (WINDOW_WIDTH, WINDOW_HEIGHT)
        window.title = string
        # The GUI color is determined by RGB values
        window.color = BASE_COLOUR
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
        
            # Creates and sets the border
            res_frame = HFrame (Label ("Resource Summary"))
            table.add_child (0, 0, res_frame)

            # Add Graphical Components
            res_frame.add_child(HEALTH)
            # Pads text so updates to values keep the same positions
            text = render_string(": " + str(HEALTH_VAL).rjust(3, '0') + " ", FEAR_FONT, 30)
            res_frame.add_child(text)
            res_frame.add_child(PEOPLE)
            text = render_string(": " + str(PEOPLE_VAL).rjust(3, '0') + " ", FEAR_FONT, 30)
            res_frame.add_child(text)
            res_frame.add_child(FOOD)
            text = render_string(": " + str(FOOD_VAL).rjust(3, '0') + " ", FEAR_FONT, 30)
            res_frame.add_child(text)
            res_frame.add_child(WEAP)
            text = render_string(": " + str(WEAP_VAL).rjust(3, '0') + " ", FEAR_FONT, 30)
            res_frame.add_child(text)
        
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

    def load_map(self):
        for y in range(len(maps.MAP_node1)):
            for x in range(len(maps.MAP_node1[y])):
                location = (x*TILE_DIMENSION+100,y*TILE_DIMENSION+100)
                screen.blit(maps.parent_image,location,maps.MAP_node1[y][x])
                
        pygame.display.flip()
        return

    def load_unit(self):
        pass

    def load_items(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def fog_of_war(self):
        pass
       


