import pygame
from pygame import *
from collections import namedtuple
from pygame.sprite import Sprite


# Default Map size (30X20 TILES)
MAP_WIDTH = 30
MAP_HEIGHT = 20
TILE_DIMENSION = 32

class MAP(Sprite):

    active_map = pygame.sprite.LayeredUpdates()

    # Assign a Parent Image 
    parent_image = pygame.image.load('asset/tiles.png')

    # A container class which stores information about a tile.
    Tile = namedtuple('Tile', ['area',
                               'passable'])
                           
    # Dictionary of tile types and associated information.
    TILES = {
        'cs':  Tile(pygame.Rect(256,   0, 32, 32), 'TRUE'),  # CobbleStone
        'wl':  Tile(pygame.Rect(320,   0, 32, 32), 'FALSE'), # Wall
        'gs':  Tile(pygame.Rect(384,   0, 32, 32), 'TRUE'),  # Grass
        'ib':  Tile(pygame.Rect(448,   0, 32, 32), 'TRUE'),  # Ice Brick
        'pf':  Tile(pygame.Rect( 32, 160, 32, 32), 'TRUE'),  # Planked Floor
        'gb':  Tile(pygame.Rect(320,  96, 32, 32), 'TRUE'),  # Grey Brick
        'hf':  Tile(pygame.Rect(128, 160, 32, 32), 'TRUE'),  # Hardwood Floor
        'dt':  Tile(pygame.Rect(256, 160, 32, 32), 'TRUE'),  # Dirt
        'sf':  Tile(pygame.Rect(448, 160, 32, 32), 'TRUE'),  # Steel Floor
        'wf':  Tile(pygame.Rect( 32, 320, 32, 32), 'TRUE'),  # Wheat Field
        'sp':  Tile(pygame.Rect( 96, 320, 32, 32), 'TRUE'),  # Steel Planking
        'f1':  Tile(pygame.Rect(160, 320, 32, 32), 'FALSE'), # Fire1
        'wr':  Tile(pygame.Rect(192, 320, 32, 32), 'FALSE'), # Water
        'ws':  Tile(pygame.Rect(256, 320, 32, 32), 'TRUE'),  # Weeds
        'bc':  Tile(pygame.Rect(352, 320, 32, 32), 'FALSE'), # Blue Crystal 
        'f2':  Tile(pygame.Rect(384, 320, 32, 32), 'FALSE'), # Fire2
        'pc':  Tile(pygame.Rect(448, 320, 32, 32), 'FALSE')  # Purple Crystal
    }

    def load_lvl_file(self, level_file):
        """
        Opens maps/level_.txt for specified level and stores number of nodes 
        and a list of their associated matrix files.
        Reworked from Assignment 4.
        """
        lvl_file = open(level_file, 'r')
        # Move up to the line with the Nodes Count
        line = lvl_file.readline()
        while line.find("Nodes: ") < 0:
            line = lvl_file.readline()
            if line == "":
                raise Exception ("Expected team count")
                
        # Get the number of Nodes
        line = line.lstrip("Nodes: ")
        self._node_count = int(line)    
         
        # Move up to the MAPS definitions
        while line.find("MAPS START") < 0:
            line = lvl_file.readline()
            if line == "":
                raise Exception ("Expected unit definitions")
        line = lvl_file.readline()
        
        # Store list of MAPS.
        maps = []
        while line.find("MAPS END") < 0:
            line = line.replace('\n', '')
            maps.append(line) 
            line = lvl_file.readline()
        
        return maps
        

    def load_mapfile(self, node):
        """
        Load mapfile by indexing to specific node within self._nodes list.
        
        load_mapfile(level_test) outputs this...
        
        matrix = [['wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','ws','ws','ws','ws','ws','ws','ws','ws','ws','ws','ws','ws','ws','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','pc','pc','pc','pc','pc','pc','pc','pc','pc','pc','pc','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','gb','gb','gb','gb','gb','wl','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','ws','gb','gb','gb','gb','gb','gb','gb','wl','pc','pc','pc','pc','pc','pc','pc','pc','pc','pc','pc','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
                     ['wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','gb','gb','gs','gs','gs','gs','gs','wl']] 
          
        """
        matrix = [[] for i in range(self._map_height)]
        map_file = open(self._nodes[node], 'r')
        # Move up to the line with the Nodes Count
        line = map_file.readline()
        for y in range(self._map_height):
            line = line.rstrip()
            line = line.split()
            for x in range(self._map_width):
                matrix[y].append(line[x])
            line = map_file.readline()
        
        self._map_matrix = matrix
        return matrix
        
    def __init__(self, level_file, tile_width=TILE_DIMENSION, tile_height=TILE_DIMENSION, map_width=MAP_WIDTH, map_height=MAP_HEIGHT):
        # Set up map info
        # self._sprite_sheet = pygame.image.load('/asset/tiles.png')
        self._tile_width = tile_width
        self._tile_height = tile_height
        self._map_width = map_width
        self._map_height = map_height
        self._node_count = None
        self._nodes = self.load_lvl_file(level_file)
        self._map_matrix = None
        
        Sprite.__init__(self)
        
        # These are required for a pygame Sprite
        self.image = None
        self._base_image = None
        self.rect = pygame.Rect(0, 0, 0, 0)  
