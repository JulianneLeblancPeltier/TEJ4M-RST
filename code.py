#!/usr/bin/env python3

"""
Created by: Julianne Leblanc-Peltier
Created on: January 14
This program runs Tetris on the PyBadge
"""

import stage
import ugame
import time

def main_menu_scene() -> None:
    """
    This function is the main menu scene
    """

    # This bool variable checks if a button is active.
    #   Makes sure that the movement buttons aren't overly sensitive! (must CLICK each time to move)
    active_button = False

    # image banks for Circuit Python
    image_bank_background = stage.Bank.from_bmp16("/assets/tetris_background1.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("/assets/tetris_sprites.bmp")

    # set the background image to image on pybadge
    #    and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that wil be updated every frame
    # 1 = the index of the sprite in the bank, 75 = x axis, 66 = y axis
    tetris_block = stage.Sprite(image_bank_sprites, 1, 144, 0)
    
    # create a stage for the background to show up on
    #    and the size (10x8 tiles of size 16x16)
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites, items show up in order
    game.layers = [tetris_block] + [background]

    # render all sprites
    #    most likely you will only render the background one per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        elif keys & ugame.K_O:
            print("B")
        elif keys & ugame.K_START:
            print("Start")
        elif keys & ugame.K_SELECT:
            print("Select")
        elif keys & ugame.K_RIGHT:
            if active_button == False:
                tetris_block.move(tetris_block.x + 16, tetris_block.y)
                active_button = True
        elif keys & ugame.K_LEFT:
            if active_button == False:
                tetris_block.move(tetris_block.x - 16, tetris_block.y)
                active_button = True
        elif keys & ugame.K_UP:
            if active_button == False:
                tetris_block.move(tetris_block.x, tetris_block.y - 16)
                active_button = True
        elif keys & ugame.K_DOWN:
            if active_button == False:
                tetris_block.move(tetris_block.x, tetris_block.y + 16)
                active_button = True
        else:
            active_button = False

        # update game logic

        # redraw Sprite
        game.render_sprites([tetris_block])
        game.tick()  # wait until refresh rate finishes

if __name__ == "__main__":
    main_menu_scene()
