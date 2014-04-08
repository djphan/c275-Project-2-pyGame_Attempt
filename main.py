#!/usr/bin/python

import sys, pygame
from gui import GUI
from maps import MAP

from ocempgui.widgets import *
from ocempgui.widgets.Constants import *
from ocempgui.draw import String, Image

if __name__ == "__main__":
    # Initalize elements of the game
    pygame.mixer.pre_init(22050, -16, 2, 512) # Small buffer for less sound lag
    pygame.init()
    clock = pygame.time.Clock()

    # Initalize the GUI
    main_gui = GUI()
    main_menu = main_gui.init_draw_window('Zombie Survival Board Game')

    # Initalize the map
    main_gui.load_map()
    main_gui.def_unit('maps/level1.txt')
  
  
    node1 = Button ("Node %d" % 1)
    node2 = Button ("Node %d" % 2)
    node2.connect_signal(SIG_CLICKED, main_gui.load_map(1))
    #print(node2.connect_signal(SIG_CLICKED, main_gui.load_map(), node2))
    node3 = Button ("Node %d" % 3)
    main_menu.add_widget(main_gui.draw_frame('resources'))
    main_menu.add_widget(main_gui.draw_frame('main_menu'))
    main_menu.add_widget(main_gui.draw_frame('minimap'))
    main_menu.add_widget(main_gui.draw_frame('input',node1,node2,node3))

    main_menu.start ()

    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            # End if q is pressed
            elif (event.type == pygame.KEYDOWN and
            (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                pygame.display.quit()
                sys.exit()
            # Respond to clicks
            elif event.type == pygame.MOUSEBUTTONUP:
                main_gui.on_click(event)
        clock.tick(60)
 




