"""
Pure game-logic functions — no Pygame dependency.

================================================================================
YOUR NAME  : ___________________________
STUDENT ID : ___________________________
================================================================================
Implement all 7 functions below. These are pure functions — they take
arguments and return values. They do NOT use Pygame and can be tested
independently with pytest.

Run the test suite at any time:
    pytest test_wormy.py -v
================================================================================

"""

import random
from constants import (
    CELLWIDTH, CELLHEIGHT,
    UP, DOWN, LEFT, RIGHT, HEAD,
)


# ─────────────────────────────────────────────────────────────────────────────
# TASK 1 — getNewHead()                                               [10 pts]
# ─────────────────────────────────────────────────────────────────────────────
def getNewHead(wormCoords, direction):
    """
    Return the {'x', 'y'} dict of the cell the head will enter next frame.

    IMPORTANT — Pygame y-axis convention:
        y = 0 is the TOP of the screen.
        Moving UP   means y decreases by 1.
        Moving DOWN means y increases by 1.

    Args:
        wormCoords (list): Current worm segments; index 0 is the head.
        direction  (str):  One of UP, DOWN, LEFT, RIGHT.

    Returns:
        dict: {'x': int, 'y': int} of the next head position.

    Examples:
        worm = [{'x': 5, 'y': 5}, {'x': 4, 'y': 5}]
        getNewHead(worm, RIGHT)  ->  {'x': 6, 'y': 5}
        getNewHead(worm, UP)     ->  {'x': 5, 'y': 4}

    Constraints:
        - Do NOT modify wormCoords.
        - Return a brand-new dict; do not reuse the existing head dict.
    """
    # TODO: implement this function
    pass


# ─────────────────────────────────────────────────────────────────────────────
# TASK 2 — isWallCollision()                                          [10 pts]
# ─────────────────────────────────────────────────────────────────────────────
def isWallCollision(wormCoords):
    """
    Return True if the worm's head has left the valid grid area.

    Valid range:
        x: 0  to  CELLWIDTH  - 1   (columns)
        y: 0  to  CELLHEIGHT - 1   (rows)

    Only check the HEAD (index 0). Body segments are always inside.

    Args:
        wormCoords (list): Current worm segments; index 0 is the head.

    Returns:
        bool: True if the head is out of bounds, False otherwise.

    Examples:
        worm = [{'x': -1, 'y': 10}, ...]   ->  True   (past left wall)
        worm = [{'x': 32, 'y': 10}, ...]   ->  True   (past right wall)
        worm = [{'x': 10, 'y': 10}, ...]   ->  False  (safe)
    """
    # TODO: implement this function
    pass


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3 — isSelfCollision()                                          [10 pts]
# ─────────────────────────────────────────────────────────────────────────────
def isSelfCollision(wormCoords):
    """
    Return True if the worm's head overlaps any of its own body segments.

    Compare head (index 0) against ALL segments from index 1 onward.
    A single-segment worm can never collide with itself.

    Args:
        wormCoords (list): Current worm segments; index 0 is the head.

    Returns:
        bool: True if the head position matches any body segment.

    Example:
        worm = [{'x':5,'y':5}, {'x':6,'y':5}, {'x':6,'y':6},
                {'x':5,'y':6}, {'x':5,'y':5}]
        isSelfCollision(worm)  ->  True   (head matches last segment)
    """
    # TODO: implement this function
    pass


# ─────────────────────────────────────────────────────────────────────────────
# TASK 4 — hasEatenApple()                                            [10 pts]
# ─────────────────────────────────────────────────────────────────────────────
def hasEatenApple(wormCoords, apple):
    """
    Return True if the worm's head is on the same cell as the apple.

    Only the HEAD triggers eating. Being on a body segment does NOT count.

    Args:
        wormCoords (list): Current worm segments; index 0 is the head.
        apple      (dict): {'x': int, 'y': int} apple grid position.

    Returns:
        bool: True if head position equals apple position.

    Examples:
        worm  = [{'x': 10, 'y': 10}, ...]
        apple = {'x': 10, 'y': 10}   ->  True
        apple = {'x': 11, 'y': 10}   ->  False
    """
    # TODO: implement this function
    pass


# ─────────────────────────────────────────────────────────────────────────────
# TASK 5 — getScore()                                                 [10 pts]
# ─────────────────────────────────────────────────────────────────────────────
def getScore(wormCoords):
    """
    Return the number of apples eaten so far.

    The worm starts with 3 segments. Each apple eaten adds 1 segment.
        Score = len(wormCoords) - 3

    Use max(0, ...) so the score never goes negative (e.g. in test fixtures
    that construct worms shorter than 3 segments).

    Args:
        wormCoords (list): Current worm segments.

    Returns:
        int: Current score (minimum 0).

    Examples:
        len(wormCoords) == 3  ->  0   (no apples eaten yet)
        len(wormCoords) == 7  ->  4   (4 apples eaten)
    """
    # TODO: implement this function
    pass


# ─────────────────────────────────────────────────────────────────────────────
# TASK 6 — isOppositeDirection()                                      [10 pts]
# ─────────────────────────────────────────────────────────────────────────────
def isOppositeDirection(current, new):
    """
    Return True if 'new' is the exact 180-degree reverse of 'current'.

    This prevents the player from steering the worm directly into its body.

    Opposite pairs:   UP <-> DOWN     LEFT <-> RIGHT
    Same direction:   NOT opposite -> return False

    Args:
        current (str): Current movement direction.
        new     (str): Proposed new direction from a key press.

    Returns:
        bool: True if the directions are exact opposites.

    Examples:
        isOppositeDirection(RIGHT, LEFT)   ->  True
        isOppositeDirection(UP,    DOWN)   ->  True
        isOppositeDirection(RIGHT, UP)     ->  False
        isOppositeDirection(RIGHT, RIGHT)  ->  False   (same is NOT opposite)
    """
    # TODO: implement this function
    pass


# ─────────────────────────────────────────────────────────────────────────────
# PROVIDED — getRandomLocation()    Do NOT modify.
# ─────────────────────────────────────────────────────────────────────────────
def getRandomLocation():
    """
    Return a random grid cell as {'x': int, 'y': int}.
    Used to place a new apple after one is eaten.
    """
    return {
        'x': random.randint(0, CELLWIDTH  - 1),
        'y': random.randint(0, CELLHEIGHT - 1),
    }

    """
    Return a random grid cell as {'x': int, 'y': int}.
    Used to place a new apple after one is eaten.

    Returns:
        dict: Random grid position within bounds.
    """
    return {
        'x': random.randint(0, CELLWIDTH  - 1),
        'y': random.randint(0, CELLHEIGHT - 1),
    }