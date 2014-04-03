#!/usr/bin/python

import sys, pygame
from gui import GUI

class MainMenu:
    def loadLevel(self, filename):
        # If a filename was given, load that level. Otherwise, load a default.
        #level = "island"
        #if len(argv) > 0:
        #level = argv[0]
        #main_gui.load_level("maps/" + level + ".lvl")
        pass

    def loadMenu(self, filename):
        pass

if __name__ == "__main__":
    # Initalize elements of the game
    pygame.mixer.pre_init(22050, -16, 2, 512) # Small buffer for less sound lag
    pygame.init()
    clock = pygame.time.Clock()

    # Initalize the GUI
    main_gui = GUI()
    main_menu = main_gui.init_draw_window('Zombie Survival Board Game')

    main_menu.add_widget(main_gui.draw_frame('resources'))
    main_menu.add_widget(main_gui.draw_frame('main_menu'))
    main_menu.add_widget(main_gui.draw_frame('minimap'))
    main_menu.add_widget(main_gui.draw_frame('input'))

    main_menu.start ()

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





