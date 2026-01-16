#!/usr/bin/env python3

"""
Created by: Julianne Leblanc-Peltier
Created on: January 14
This program runs Tetris on the PyBadge using CircuitPython
"""

import stage
import ugame
import time
import constants

def main_menu_scene() -> None:
    """
    This function is the main menu scene
    """

    # This bool variable checks if a button is active.
    #   Makes sure that the movement buttons aren't overly sensitive! (must CLICK each time to move)
    active_button = False

    # This counter collects the iteration of the loop.
    #   Makes sure that once a second (60 ticks) the tetris block moves down by 1 block!
    game_loop_counter = 0

    # image banks for Circuit Python
    image_bank_background = stage.Bank.from_bmp16("/assets/tetris_background1.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("/assets/tetris_sprites.bmp")

    # set the background image to image on pybadge
    #    and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that wil be updated every frame
    # 1 = the index of the sprite in the bank, 144 = x axis, 0 = y axis
    tetris_block = stage.Sprite(image_bank_sprites, 1, 144, 0)
    
    # create a stage for the background to show up on
    #    and the size (10x8 tiles of size 16x16)
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers of all sprites, items show up in order
    game.layers = [tetris_block] + [background]

    # render all sprites
    #    most likely you will only render the background one per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # update game logic
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
                # rotates the block 90 degrees clockwise
                tetris_block.set_frame(None, 90)
                active_button = True
        elif keys & ugame.K_LEFT:
            if active_button == False:
                tetris_block.move(tetris_block.x - constants.ONE_BLOCK, tetris_block.y)
                active_button = True
        elif keys & ugame.K_UP:
            if active_button == False:
                tetris_block.move(tetris_block.x, tetris_block.y - constants.ONE_BLOCK)
                active_button = True
        elif keys & ugame.K_DOWN:
            if active_button == False:
                tetris_block.move(tetris_block.x, tetris_block.y + constants.ONE_BLOCK)
                active_button = True
        else:
            active_button = False

        # every 60 ticks (1 second), the sprite moves down one block (16 bits).
        if game_loop_counter % 60 == 0:
            tetris_block.move(tetris_block.x - 16, tetris_block.y)

        if tetris_block.x > 144:
            tetris_block.move(144, tetris_block.y)
        if tetris_block.x < 0:
            tetris_block.move(0, tetris_block.y)
        if tetris_block.y > 112:
            tetris_block.move(tetris_block.x, 112)
        if tetris_block.y < 0:
            tetris_block.move(tetris_block.x, 0)

        # counts the iteration of the loop
        game_loop_counter += 1

        # redraw Sprite
        game.render_sprites([tetris_block])
        game.tick()  # wait until refresh rate finishes

if __name__ == "__main__":
    main_menu_scene()
