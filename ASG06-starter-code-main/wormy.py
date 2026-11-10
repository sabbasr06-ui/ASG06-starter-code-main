"""
================================================================================
PROJECT SPECIFICATION
================================================================================
Project Title : Wormy
Original Author: Al Sweigart 
Enhanced By    : Ri
Language       : Python 3.x
Library        : Pygame

Description:
    A classic snake/worm arcade game rendered in a Pygame window. The player
    controls a growing worm on a grid-based board. The objective is to eat as
    many red apples as possible without colliding with the walls or the worm's
    own body.

Controls:
    Arrow Keys / WASD  — Move the worm (Up, Down, Left, Right)
    ESC                — Quit the game at any time

Gameplay Rules:
    1. The worm starts with a length of 3 segments and moves continuously.
    2. Each apple eaten increases the worm's length by 1 and increments the score.
    3. Colliding with a wall or the worm's own body ends the game.
    4. After game over, the player may press any key to restart.

Graphics:
    - The worm is drawn with rounded pill-shaped segments; the head is
      distinguished by two white eyes with black pupils.
    - Apples are drawn as red circles with a green leaf highlight and a
      white specular shine dot for a 3-D appearance.
    - The background grid uses subtle dark-gray lines on a black field.

Configuration Constants (top of file):
    FPS          — Frames per second (game speed), default 15
    WINDOWWIDTH  — Display width in pixels, default 640
    WINDOWHEIGHT — Display height in pixels, default 480
    CELLSIZE     — Pixel size of each grid cell, default 20
================================================================================
================================================================================
WORMY — Main Entry Point
================================================================================
Course        : IST 242 — Intermediate Python Programming
Project       : Wormy Snake Game
Your Name     : ___________________________
Student ID    : ___________________________

Instructions:
    1. Implement all TODO functions in logic.py  (Tasks 1-6)
    2. Implement runGame() below                 (Task 7)
    3. Implement drawWorm() in graphics.py       (Task 8)
    4. Implement drawApple() in graphics.py      (Task 9)
    5. Do NOT modify constants.py, screens.py, or test_wormy.py

Install libraries/dependencies: pip install < requirements.txt 
Run the game  :  python wormy.py
Run the tests :  pytest test_wormy.py -v
================================================================================
"""

import random
import pygame
import sys
from pygame.locals import *

from constants import (
    FPS, WINDOWWIDTH, WINDOWHEIGHT, BGCOLOR, CELLSIZE,
    CELLWIDTH, CELLHEIGHT,
    UP, DOWN, LEFT, RIGHT, HEAD,
)
from logic import (
    getNewHead,
    isWallCollision,
    isSelfCollision,
    hasEatenApple,
    getScore,
    isOppositeDirection,
    getRandomLocation,
)
from graphics import drawGrid, drawWorm, drawApple, drawScore
from screens  import showStartScreen, showGameOverScreen, checkForKeyPress

# ── Pygame globals ─────────────────────────────────────────────────────────
FPSCLOCK    = None
DISPLAYSURF = None
BASICFONT   = None


def terminate():
    """Cleanly shut down Pygame and exit the process."""
    pygame.quit()
    sys.exit()


def main():
    """Initialise Pygame, show the start screen, then loop through game rounds."""
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK    = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT   = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    showStartScreen(DISPLAYSURF, FPSCLOCK, BASICFONT, terminate)
    while True:
        runGame()
        showGameOverScreen(DISPLAYSURF, FPSCLOCK, BASICFONT, terminate)


# ─────────────────────────────────────────────────────────────────────────────
# TASK 7 — runGame()                                                  [10 pts]
# ─────────────────────────────────────────────────────────────────────────────
def runGame():
    """
    Run one complete game round. Returns (ends the round) when the worm
    hits a wall or its own body.

    Step-by-step guide
    ------------------
    A. Pick a random starting position:
           startx = random.randint(5, CELLWIDTH  - 6)
           starty = random.randint(5, CELLHEIGHT - 6)

    B. Build the initial worm — a list of 3 dicts, head first:
           wormCoords = [
               {'x': startx,     'y': starty},   # head  (index 0)
               {'x': startx - 1, 'y': starty},   # body segment 1
               {'x': startx - 2, 'y': starty},   # body segment 2
           ]

    C. Set  direction = RIGHT  and place the first apple:
           apple = getRandomLocation()

    D. Enter the main while-True game loop. Each iteration is one frame:

       1. EVENT HANDLING — loop over pygame.event.get():
            - QUIT event            -> call terminate()
            - KEYDOWN event:
                Arrow Left  / K_a   -> direction = LEFT   (only if not opposite)
                Arrow Right / K_d   -> direction = RIGHT  (only if not opposite)
                Arrow Up    / K_w   -> direction = UP     (only if not opposite)
                Arrow Down  / K_s   -> direction = DOWN   (only if not opposite)
                K_ESCAPE            -> call terminate()
          Use isOppositeDirection(direction, new_dir) to guard each change.

       2. MOVE — prepend new head:
            wormCoords.insert(0, getNewHead(wormCoords, direction))

       3. WALL COLLISION — if isWallCollision(wormCoords): return

       4. SELF COLLISION — if isSelfCollision(wormCoords): return

       5. APPLE COLLISION:
            if hasEatenApple(wormCoords, apple):
                apple = getRandomLocation()   # new apple; tail stays -> worm grows
            else:
                del wormCoords[-1]            # remove tail -> worm stays same length

       6. RENDER (in this order):
            DISPLAYSURF.fill(BGCOLOR)
            drawGrid(DISPLAYSURF)
            drawWorm(DISPLAYSURF, wormCoords, direction)
            drawApple(DISPLAYSURF, apple)
            drawScore(DISPLAYSURF, BASICFONT, getScore(wormCoords))
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    """
    # TODO: implement this function
    pass


if __name__ == '__main__':
    main()
##