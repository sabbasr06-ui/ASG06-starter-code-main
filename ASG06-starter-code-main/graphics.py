"""
All Pygame drawing and rendering functions.
Surfaces and fonts are passed as parameters — no globals imported.
================================================================================
YOUR NAME  : ___________________________
STUDENT ID : ___________________________
================================================================================
Implement drawWorm() and drawApple() below (Tasks 8 and 9).
All other functions are provided — do NOT modify them.

All drawing functions receive DISPLAYSURF and BASICFONT as parameters.
Do NOT import or use global variables from wormy.py.
================================================================================
"""

import pygame
from constants import (
    CELLSIZE, WINDOWWIDTH, WINDOWHEIGHT,
    WHITE, BLACK, RED, APPLE_SHINE, LEAF_GREEN,
    GREEN, DARKGREEN, HEADGREEN, DARKGRAY,
    UP, DOWN, LEFT, RIGHT, HEAD,
)


# ─────────────────────────────────────────────────────────────────────────────
# TASK 8 — drawWorm()                                                 [15 pts]
# ─────────────────────────────────────────────────────────────────────────────
def drawWorm(DISPLAYSURF, wormCoords, direction=RIGHT):
    """
    Draw the worm on DISPLAYSURF.

    Each segment occupies one grid cell (CELLSIZE x CELLSIZE pixels).
    The pixel top-left corner of cell (col, row) is:
        px = col * CELLSIZE
        py = row * CELLSIZE

    MINIMUM requirement for full credit:
        - Each segment: dark-green outer rectangle + green inner rectangle.
          Suggested sizes:
            outer rect: (px+1, py+1, CELLSIZE-2, CELLSIZE-2)
            inner rect: (px+4, py+4, CELLSIZE-8, CELLSIZE-8)

    BONUS (+5 extra credit):
        - Rounded corners: use border_radius in pygame.draw.rect()
        - Head brighter than body (use HEADGREEN for segment at index HEAD)
        - Two eyes on the head with pupils facing the direction of travel

    Args:
        DISPLAYSURF  : Active pygame display surface.
        wormCoords (list): Current worm segments; index 0 is the head.
        direction  (str):  Current movement direction (for eye orientation).
    """
    # TODO: implement this function
    pass


# ─────────────────────────────────────────────────────────────────────────────
# TASK 9 — drawApple()                                                [15 pts]
# ─────────────────────────────────────────────────────────────────────────────
def drawApple(DISPLAYSURF, coord):
    """
    Draw the apple on DISPLAYSURF at the given grid coordinate.

    The pixel top-left corner of cell (col, row) is:
        px = coord['x'] * CELLSIZE
        py = coord['y'] * CELLSIZE

    MINIMUM requirement for full credit:
        - A filled RED rectangle covering the cell:
            pygame.draw.rect(DISPLAYSURF, RED, pygame.Rect(px, py, CELLSIZE, CELLSIZE))

    BONUS (+5 extra credit):
        - Circular apple body using pygame.draw.circle()
        - Darker lower ellipse for depth shading
        - Small LEAF_GREEN rectangle at the top as a stem/leaf
        - Small APPLE_SHINE circle for a specular highlight

    Args:
        DISPLAYSURF  : Active pygame display surface.
        coord (dict): {'x': int, 'y': int} grid position of the apple.
    """
    # TODO: implement this function
    pass


# ─────────────────────────────────────────────────────────────────────────────
# PROVIDED functions — Do NOT modify anything below this line.
# ─────────────────────────────────────────────────────────────────────────────

def drawGrid(DISPLAYSURF):
    """Draw subtle dark-gray grid lines across the entire window."""
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


def drawScore(DISPLAYSURF, BASICFONT, score):
    """Render the current score in the top-right corner."""
    surf = BASICFONT.render('Score: %s' % score, True, WHITE)
    rect = surf.get_rect()
    rect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(surf, rect)


def drawPressKeyMsg(DISPLAYSURF, BASICFONT):
    """Render a 'Press a key to play.' hint in the bottom-right corner."""
    surf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    rect = surf.get_rect()
    rect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(surf, rect)
