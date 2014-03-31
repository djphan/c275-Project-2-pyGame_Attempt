#!/usr/bin/python

import sys, pygame
from gui import GUI

RESOLUTION = pygame.Rect(0, 0, 1080, 720)
BG_COLOR = (200, 200, 200)


class MainMenu:
    def loadLevel(self, filename):
        # If a filename was given, load that level. Otherwise, load a default.
        #level = "island"
        #if len(argv) > 0:
        #level = argv[0]
        #main_gui.load_level("maps/" + level + ".lvl")
        pass

    def initalize_game(self):
        """
        Initiallize the game with pygame material.
        """
        pygame.mixer.pre_init(22050, -16, 2, 512) # Small buffer for less lag
        pygame.init()
        pygame.display.set_caption("Zombie Survivors")
        main_gui = GUI(RESOLUTION, BG_COLOR)
        clock = pygame.time.Clock()

    def loadMenu(self, filename):
        pass

if __name__ == "__main__":
    argv = sys.argv[1:]
    self.initalize_game()

    # The main game loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            # Quit the game when Q or ESC is pressed
            elif (event.type == pygame.KEYDOWN and
            (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                pygame.display.quit()
                sys.exit()
            # Respond to clicks
            elif event.type == pygame.MOUSEBUTTONUP:
                main_gui.on_click(event)
        main_gui.update()
        main_gui.draw()
        clock.tick(60)




# The main game loop
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
    main_gui.update()
    main_gui.draw()
    clock.tick(60)

