"""
All game-wide constants and color definitions.
Imported by every other module to avoid circular dependencies.

Provided — do NOT modify
"""

# ── Timing ───────────────────────────────────────────────────────────────────
FPS = 15

# ── Window & Grid ─────────────────────────────────────────────────────────────
WINDOWWIDTH  = 640
WINDOWHEIGHT = 480
CELLSIZE     = 20

assert WINDOWWIDTH  % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."

CELLWIDTH  = WINDOWWIDTH  // CELLSIZE   # 32 columns
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE   # 24 rows

# ── Colors  (R, G, B) ─────────────────────────────────────────────────────────
WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (220,  30,  30)
APPLE_SHINE = (255, 160, 160)
LEAF_GREEN  = ( 34, 139,  34)
GREEN       = (  0, 220,   0)
DARKGREEN   = (  0, 120,   0)
HEADGREEN   = (  0, 180,   0)
DARKGRAY    = ( 40,  40,  40)
BGCOLOR     = BLACK

# ── Directions ────────────────────────────────────────────────────────────────
UP    = 'up'
DOWN  = 'down'
LEFT  = 'left'
RIGHT = 'right'

# ── Worm indexing ─────────────────────────────────────────────────────────────
HEAD = 0   # Index 0 in wormCoords is always the head