#!/usr/bin/env python3

"""
Created by: Julianne Leblanc-Peltier
Created on: January 14
This program runs Tetris on the PyBadge
"""

import stage
import ugame

def main_menu_scene() -> None:
    """
    This function is the main menu scene
    """

    # image banks for Circuit Python
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    background = stage.Grid(image_bank_background, 10, 6)
    
    game = stage.Stage(ugame.display, 60)

    game.layers = [background]

    game.render_block()

    # repeat forever, game loop
    while True:
        pass # just a placeholder for now

if __name__ == "__main__":
    main_menu_scene()
