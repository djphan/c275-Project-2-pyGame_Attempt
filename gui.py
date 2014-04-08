import sys 
import pygame, pygame.locals
import random, unit
from maps import MAP

# Import various assets and modules for function
from pygame.sprite import LayeredUpdates
from ocempgui.widgets import *
from ocempgui.widgets.Constants import *
from ocempgui.draw import String, Image

# ***
# Import game assets handling modules
from unit import *
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

# Set the fonts to render in the GUI
FEAR_FONT = "asset/menu/FaceYourFears.tft"
pygame.font.init()

# RGB colors for the GUI
BASE_COLOUR = (230, 230, 230)

# Resource Values
HEALTH_VAL = 100
PEOPLE_VAL = 1
FOOD_VAL = 3
WEAP_VAL = 9

# Default Map size (30X20 TILES)
MAP_WIDTH = 960
MAP_HEIGHT = 640
TILE_DIMENSION = 32

# Names for the different factions in the game to control the units.
TEAM_NAME = {
    0: "survior",
    1: "zombie",
    2: "neutral"
}

def render_string(string, font, size):
    """
    This is a helper function to render strings as an image widget
    to be processed in the GUI.
    """
    text = String.draw_string(string, font, size, 1, (0,0,0))
    text = ImageLabel(text)
    return text

class GameStage:
    """
    Defined game phases taken from the resource in assignment 4:
    http://stackoverflow.com/questions/702834/whats-the-common-practice-
    for-enums-in-python
    """
    Exploration, Event, Combat, Sneak, GameOver = range(5)

class UnitRender:
    """
    This class contains all the functions required to render units
    onto the GUI. It is grouped together for ease.
    """
    def def_unit(self, file_name):
        """
        This class reads in a level and determines the unit information for that level
        to render the image. Load in the file_name/path and open it.  
        This was taken from assignment 4 and modified for the units.
        """
        # Open and read the file_name
        file_name = open(file_name, 'r')
        line = file_name.readline()

        # Move up to the unit definitions
        while line.find("UNITS START") < 0:
            line = file_name.readline()
            if line == "":
                raise Exception ("Expected unit definitions")
        line = file_name.readline()

        # Create the units
        while line.find("UNITS END") < 0:
            line = line.rstrip()
            line = line.split(' ')
            unit_name = line[0]
            unit_team = int(line[1])
            unit_x, unit_y = int(line[2]), int(line[3])
            unit_angle = int(line[4])
            
            if not unit_name in unit.unit_types:
                raise Exception("No unit of name {} found!".format(unit_name))

            new_unit = unit.unit_types[unit_name](team = unit_team,
                                                  tilex = unit_x,
                                                  tiley = unit_y,
                                                  angle = unit_angle,
                                                  activate = True)
            
            # Add the unit to the update group and set its display rect
            self.update_unit_rect(new_unit)
            
            line = map_file.readline()
            if line == "":
                raise Exception ("Expected end of unit definitions")

    def draw_unit(self, active_units):
        """
        This draws in the unit onto the screen for us.
        """
        for unit in active_units:
            active_units.draw(self.screen)

    def select_unit(self):
        """
        This draws a rectangle around our unit when selected.
        """
        pass

    def select_target(self):
        """
        This draws the target space that we select.
        """

        # If there's a selected unit, outline it
        if self.sel_unit:
            pygame.gfxdraw.rectangle(
                self.screen,
                self.sel_unit.rect,
                SELECT_COLOR)
                
        # Mark potential targets
        for tile_pos in self._attackable_tiles:
            screen_pos = self.map.screen_coords(tile_pos)
            self.draw_reticle(screen_pos)

    def update_unit_rect(self, unit):
        """
        Scales a unit's display rectangle to screen coordiantes.
        """
        x, y = unit.tilex, unit.tiley
        screen_x, screen_y = self.map.screen_coords((x, y))
        unit.rect.x = screen_x
        unit.rect.y = screen_y

class GUI(LayeredUpdates):
    """
    This is the core GUI class required to run the game.  It is responsible for 
    rendering all the objects on screen. It will interact with the units and the level
    updating the game's image side as the game is played.

    As well various tools will be used to keep track of map positions and other enviromental
    factors will be used to call on triggered events in the game.
    """
    # Number of GUI instances
    instance_num = 0

    def __init__(self):
        # Initalizes layered updates in the GUI to render all the images properly
        LayeredUpdates.__init__(self)

        # Error checking if you attempt to load multiple GUIs at once
        if GUI.instance_num != 0:
            raise Exception("Can only have one Zombie Survival Game up at a time.")
        GUI.instance_num = 1
	
        # Game properties selected by the GUI in reference to the game levels
        self.sel_level = None
        self.sel_unit = None 
        self.sel_tile = None 
        self.sel_event = None
        self.sel_gamestate = GameStage.Exploration

        
        # Initiate mapping
        self.current_node = None        
        level = 'level1'
        self.map = MAP("maps/" + level + ".txt")

    def select_mode(self, mode):
        """
        Using the predefined GameStates we will use this helper function to assist us 
        in setting the current game stage.
        """
        if self.gamestate == mode:
            return
        
        # Deal with the current mode
        if self.mode == GameStage.Exploration:
            # Add selection tile.
            pass
        
        # Deal with the current mode
        if self.mode == GameStage.Event:
            # Add selection tile.
            pass
            
        self.mode = mode
       
    # Think about placeholders for the unit actions for the other options.
    def can_move(self):
        """
        Checks whether we can move our unit
        """
        # If no unit is selected, we can't.
        if not self.sel_unit: return False
        
        # If the unit is done its move, we can't.
        return not self.sel_unit.turn_state[0]

    def can_action(self):
        """
        Checks whether we can move our unit
        """
        # If no unit is selected, we can't
        if not self.sel_unit: return False
        
        # If the unit is done its move, we can't.
        return not self.sel_unit.turn_state[0]

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
            outer_table = Table (1, 1)
            inner_table = Table (4, 2)
            # Set location based on x,y coordinates from top left - Graphical Notations.
            outer_table.topleft = 980, 5
            outer_table.spacing = 5
            inner_table.spacing = 5
        
            # Creates and sets the border
            res_frame = VFrame (Label ("Resource Summary"))
            outer_table.add_child (0, 0, res_frame)

            # Add Graphical Components
            inner_table.add_child (0, 0, HEALTH)
            # Pads text so updates to values keep the same positions    
            text = render_string(": " + str(HEALTH_VAL).rjust(3, '0') + " ", FEAR_FONT, 30)
            inner_table.add_child(0, 1, text)
            inner_table.add_child(1, 0, PEOPLE)
            text = render_string(": " + str(PEOPLE_VAL).rjust(3, '0') + " ", FEAR_FONT, 30)
            inner_table.add_child(1, 1, text)
            inner_table.add_child(2, 0, FOOD)
            text = render_string(": " + str(FOOD_VAL).rjust(3, '0') + " ", FEAR_FONT, 30)
            inner_table.add_child(2, 1, text)
            inner_table.add_child(3, 0, WEAP)
            text = render_string(": " + str(WEAP_VAL).rjust(3, '0') + " ", FEAR_FONT, 30)
            inner_table.add_child(3, 1, text)

            res_frame.add_child(inner_table)
            return outer_table

        elif menu_object == 'main_menu':
            mm_table = Table (2, 3)

            # Adjust
            mm_table.topleft = 980, 265
            mm_table.spacing = 5
            
            mm_frame = HFrame (Label ("main"))
            mm_frame.set_boarder = (BORDER_SUNKEN)
                
            mm_table.add_child (0, 0, mm_frame)

            for i in xrange(3):
                btn = Button ("Button %d" % i)
                mm_frame.add_child (btn)
            return mm_table    
       
        elif menu_object == 'input':
            inp_table = Table (2, 3)
            inp_table.topleft = 10, 655
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
            minimap_table = Table (1, 1)
            minimap_table.topleft = 980, 655
            minimap_table.spacing = 5
           
            # Create and display two 'standard' frames.
            minimap_frame = HFrame (Label ("Minimap"))
            minimap_frame.set_boarder = (BORDER_SUNKEN)
                            
            minimap_table.add_child (0, 0, minimap_frame)

            for i in xrange(3):
                btn = Button ("Button %d" % i)
                minimap_frame.add_child (btn)
            return minimap_table

        elif menu_object == 'txtstats':
            txtstats_table = Table (1, 1)
            txtstats_table.topleft = 1115, 5
            txtstats_table.spacing = 5
           
            # Create and display two 'standard' frames.
            txtstats_frame = VFrame ()
            txtstats_frame.set_boarder = (BORDER_SUNKEN)
                            
            txtstats_table.add_child (0, 0, txtstats_frame)

            for i in xrange(3):
                btn = Button ("Button %d" % i)
                txtstats_frame.add_child (btn)
            return txtstats_table

        else:
            # Add/overide for other modules.
            pass

    def load_unit(self):
        #***
        """
        This function draws the unit onto the screen.
        """
        for units in base_unit.UnitBase.active_units:
            self.update_unit_rect(u)
        base_unit.UnitBase.active_units.draw(self.screen)
        
        # units = UnitRender()
        # units.def_unit("maps/level1.txt")
        pass

    def load_map(self, node=0):
        """
        Loads the current map depending on the current node.
        """
        # Set current node to new loaded map.
        self.current_node = node
        
        for y in range(len(self.map._map_matrix)):
            for x in range(len(self.map._map_matrix[y])):
                location = (x*TILE_DIMENSION+10, y*TILE_DIMENSION+10)
                tile_key = self.map._map_matrix[y][x]
                tile_area = self.map.TILES[tile_key].area
                screen.blit(self.map.parent_image,location,tile_area)
                

        pygame.display.flip()
        return



    def load_items(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def fog_of_war(self):
        pass
       


