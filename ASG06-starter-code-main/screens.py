""" ##
Screen management: start screen, game-over screen, and input helpers.

Provided — do NOT modify
"""

import pygame
from pygame.locals import *
from constants import WINDOWWIDTH, WINDOWHEIGHT, BGCOLOR, FPS, WHITE, GREEN


def checkForKeyPress(terminate_fn):
    """
    Return the first KEYUP event key found in the queue, or None.
    Terminates immediately on QUIT or ESC.

    Args:
        terminate_fn (callable): The terminate() function from wormy.py.
    """
    if pygame.event.get(QUIT):
        terminate_fn()
    keyUpEvents = pygame.event.get(KEYUP)
    if not keyUpEvents:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate_fn()
    return keyUpEvents[0].key


def showStartScreen(DISPLAYSURF, FPSCLOCK, BASICFONT, terminate_fn):
    """
    Display an animated rotating 'Wormy!' title until a key is pressed.

    Args:
        DISPLAYSURF  : Active pygame display surface.
        FPSCLOCK     : pygame.time.Clock instance.
        BASICFONT    : Loaded pygame font for UI text.
        terminate_fn : The terminate() function from wormy.py.
    """
    from graphics import drawPressKeyMsg

    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    surf1 = titleFont.render('Wormy!', True, WHITE, (0, 155, 0))
    surf2 = titleFont.render('Wormy!', True, GREEN)
    d1, d2 = 0, 0

    while True:
        DISPLAYSURF.fill(BGCOLOR)
        r1 = pygame.transform.rotate(surf1, d1)
        DISPLAYSURF.blit(r1, r1.get_rect(center=(WINDOWWIDTH // 2, WINDOWHEIGHT // 2)))
        r2 = pygame.transform.rotate(surf2, d2)
        DISPLAYSURF.blit(r2, r2.get_rect(center=(WINDOWWIDTH // 2, WINDOWHEIGHT // 2)))
        drawPressKeyMsg(DISPLAYSURF, BASICFONT)
        if checkForKeyPress(terminate_fn):
            pygame.event.get()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        d1 += 3
        d2 += 7


def showGameOverScreen(DISPLAYSURF, FPSCLOCK, BASICFONT, terminate_fn):
    """
    Display a full-screen 'Game Over' message and wait for a keypress.

    Args:
        DISPLAYSURF  : Active pygame display surface.
        FPSCLOCK     : pygame.time.Clock instance.
        BASICFONT    : Loaded pygame font for UI text.
        terminate_fn : The terminate() function from wormy.py.
    """
    from graphics import drawPressKeyMsg

    font     = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = font.render('Game', True, WHITE)
    overSurf = font.render('Over', True, WHITE)

    DISPLAYSURF.blit(gameSurf, gameSurf.get_rect(midtop=(WINDOWWIDTH // 2, 10)))
    DISPLAYSURF.blit(overSurf, overSurf.get_rect(
        midtop=(WINDOWWIDTH // 2, gameSurf.get_height() + 35)))
    drawPressKeyMsg(DISPLAYSURF, BASICFONT)
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress(terminate_fn)   # Flush keys buffered during gameplay

    while True:
        if checkForKeyPress(terminate_fn):
            pygame.event.get()
            return