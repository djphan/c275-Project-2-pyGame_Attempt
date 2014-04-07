import pygame
from pygame import *
from collections import namedtuple

# Assign a Parent Image 
parent_image = pygame.image.load('asset/tiles.png')

"""
Area of all tiles within parent_image.
"""
cs = pygame.Rect(256,   0, 32, 32) # CobbleStone
wl = pygame.Rect(320,   0, 32, 32) # Wall
gs = pygame.Rect(384,   0, 32, 32) # Grass
ib = pygame.Rect(448,   0, 32, 32) # Ice Brick
pf = pygame.Rect( 32, 160, 32, 32) # Planked Floor
gb = pygame.Rect(320,  96, 32, 32) # Grey Brick
hf = pygame.Rect(128, 160, 32, 32) # Hardwood Floor
dt = pygame.Rect(256, 160, 32, 32) # Dirt
sf = pygame.Rect(448, 160, 32, 32) # Steel Floor
wf = pygame.Rect( 32, 320, 32, 32) # Wheat Field
sp = pygame.Rect( 96, 320, 32, 32) # Steel Planking
f1 = pygame.Rect(160, 320, 32, 32) # Fire1
wr = pygame.Rect(192, 320, 32, 32) # Water
ws = pygame.Rect(256, 320, 32, 32) # Weeds
bc = pygame.Rect(352, 320, 32, 32) # Blue Crystal 
f2 = pygame.Rect(384, 320, 32, 32) # Fire2
pc = pygame.Rect(448, 320, 32, 32) # Purple Crystal

# Tiles that are passable.
TILES = {
    'cs': 'TRUE',
    'wl': 'FALSE',
    'gs': 'TRUE',
    'ib': 'TRUE',
    'pf': 'TRUE',
    'gb': 'TRUE',
    'hf': 'TRUE',
    'dt': 'TRUE',
    'sf': 'TRUE',
    'wf': 'TRUE',
    'sp': 'TRUE',
    'f1': 'FALSE',
    'wr': 'FALSE',
    'ws': 'TRUE',
    'bc': 'FALSE', 
    'f2': 'FALSE',
    'pc': 'FALSE'
}

# Matrix mapping tiles to background.
MAP_node1 = [[wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,ws,ws,ws,ws,ws,ws,ws,ws,ws,ws,ws,ws,ws,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,wr,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,wl,pc,pc,pc,pc,pc,pc,pc,pc,pc,pc,pc,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,wl,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,wl,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,dt,dt,dt,gb,gb,wl,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,gb,gb,gb,gb,gb,wl,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,pf,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,ws,gb,gb,gb,gb,gb,gb,gb,wl,pc,pc,pc,pc,pc,pc,pc,pc,pc,pc,pc,wl,gb,gb,gs,gs,gs,gs,gs,wl],\
             [wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,wl,gb,gb,gs,gs,gs,gs,gs,wl]] 
             

