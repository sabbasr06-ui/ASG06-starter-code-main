## Objective
In this project you will complete a fully playable Wormy snake game using Python and the Pygame library. A working skeleton (wormy.py) has already been provided with constants, helper functions, and screen management code. Your job is to implement the 9 core functions that make the game run.

### This project reinforces:

- Function design and decomposition

- Boolean logic and conditional reasoning

- List manipulation (insert, delete, index)

- Coordinate-based 2D thinking

- Basic Pygame graphics with pygame.draw

- Writing code that can be automatically tested

### Learning Objectives
By completing this project, you will be able to:

- Implement game logic as small, independently testable pure functions

- Manipulate a list of dictionaries to simulate movement and growth

- Apply boundary and collision detection using coordinate comparisons

- Use pygame.draw primitives (rect, circle, ellipse) to render graphics

- Understand why separating logic from rendering makes code easier to test

## Project Structure
ASG06-starter-code/
├── wormy.py          ← main entry point (imports everything)
├── constants.py      ← all constants and colors
├── logic.py          ← pure game logic (tested by pytest)
├── graphics.py       ← all drawing/rendering functions
├── screens.py        ← start screen, game over screen, helpers
└── test_wormy.py     ← instructor pytest suite (48 tests)

Do not rename any function, change any function signature, or modify constants.py, screens.py, or test_wormy.py. The autograder depends on exact names and signatures.

 

## Implementation
All 9 tasks are marked with # TODO comments in the starter files. Here is a summary:

logic.py — 7 Functions (70 points)
These are pure functions — they take arguments and return a value. They do not use Pygame and can be fully unit-tested.

Task 1 — getNewHead(wormCoords, direction) — 10 pts
Calculate the grid cell the worm's head will move into next frame.

direction is one of UP, DOWN, LEFT, RIGHT

Important: In Pygame, y = 0 is the top of the screen. Moving UP means y - 1; moving DOWN means y + 1

Return a new {'x': int, 'y': int} dict

Do not modify wormCoords

text
Example: worm = [{'x': 5, 'y': 5}, {'x': 4, 'y': 5}] getNewHead(worm, RIGHT) → {'x': 6, 'y': 5} getNewHead(worm, UP) → {'x': 5, 'y': 4}
Task 2 — isWallCollision(wormCoords) — 10 pts
Return True if the worm's head has gone outside the grid.

Valid column range: 0 to CELLWIDTH - 1

Valid row range: 0 to CELLHEIGHT - 1

Only check the head (index 0) — body segments are always inside

Return False if the head is still within bounds

text
Example: worm = [{'x': -1, 'y': 10}, ...] → True (hit left wall) worm = [{'x': 32, 'y': 10}, ...] → True (hit right wall, CELLWIDTH=32) worm = [{'x': 10, 'y': 10}, ...] → False (safe)
Task 3 — isSelfCollision(wormCoords) — 10 pts
Return True if the worm's head overlaps any of its own body segments.

Compare head (index 0) against all segments from index 1 onward

A one-segment worm can never collide with itself

Return False if no overlap is found

text
Example: worm = [{'x':5,'y':5}, {'x':6,'y':5}, {'x':6,'y':6}, {'x':5,'y':6}, {'x':5,'y':5}] → True (head == tail)
Task 4 — hasEatenApple(wormCoords, apple) — 10 pts
Return True if the worm's head is on the same cell as the apple.

The apple is a {'x': int, 'y': int} dict

Only the head triggers eating — being on a body segment does not count

text
Example: worm = [{'x': 10, 'y': 10}, ...] apple = {'x': 10, 'y': 10} → True apple = {'x': 11, 'y': 10} → False
Task 5 — getScore(wormCoords) — 10 pts
Return the number of apples eaten so far.

The worm starts with 3 segments; every apple eaten adds 1

Score = len(wormCoords) - 3

Use max(0, ...) to ensure the score never goes negative

text
Example: len(wormCoords) == 3 → score = 0 (no apples eaten yet) len(wormCoords) == 7 → score = 4 (4 apples eaten)
Task 6 — isOppositeDirection(current, new) — 10 pts
Return True if new is the exact reverse of current.
This prevents the player from steering the worm directly into its own body.

Opposite pairs: UP ↔ DOWN, LEFT ↔ RIGHT

Moving in the same direction is not opposite — return False

text
Example: isOppositeDirection(RIGHT, LEFT) → True isOppositeDirection(UP, DOWN) → True isOppositeDirection(RIGHT, UP) → False isOppositeDirection(RIGHT, RIGHT) → False
Task 7 — runGame() in wormy.py — 10 pts
Wire all the logic functions together into the main game loop.

Your implementation must:

Pick a random starting position at least 5 cells from every edge

Create wormCoords as a list of 3 {'x', 'y'} dicts (head at index 0)

Set initial direction = RIGHT and place the first apple

Each frame:

Handle QUIT, KEYDOWN (WASD / arrow keys), and ESC events

Block direction reversals using isOppositeDirection()

Compute and prepend the new head with getNewHead()

Call isWallCollision() → return if True

Call isSelfCollision() → return if True

Call hasEatenApple() → if True, place a new apple and keep tail; else remove tail

Render: drawGrid, drawWorm, drawApple, drawScore, pygame.display.update, FPSCLOCK.tick

graphics.py — 2 Functions (30 points)
Task 8 — drawWorm(DISPLAYSURF, wormCoords, direction) — 15 pts
Render the worm on screen.

Minimum requirement (full credit):

Each segment is a filled green rectangle with a dark-green border

Bonus (up to 5 extra credit points):

Rounded corners using border_radius

Head visually distinct from body (brighter color)

Eyes on the head with pupils that face the direction of movement

Task 9 — drawApple(DISPLAYSURF, coord) — 15 pts
Render the apple on screen.

Minimum requirement (full credit):

A filled red rectangle covering the cell

Bonus (up to 5 extra credit points):

Circular apple shape using pygame.draw.circle

Leaf detail at the top

Shine/highlight dot for a 3-D effect

##  Grading Rubric
**Logic Functions — 70 pts**
Task	Function	Points	How It Is Graded
1	getNewHead()	10	7 automated test cases
2	isWallCollision()	10	9 automated test cases
3	isSelfCollision()	10	7 automated test cases
4	hasEatenApple()	10	6 automated test cases
5	getScore()	10	4 automated test cases
6	isOppositeDirection()	10	10 automated test cases
7	runGame()	10	5 integration test cases
Each task is all-or-nothing per test case: a test either passes or fails. Partial points are awarded proportionally within each task (e.g. 5/7 test cases passing = ~7/10 pts).

**Graphics — 30 pts**
Task	Function	Points	How It Is Graded
8	drawWorm()	15	Instructor visual inspection
9	drawApple()	15	Instructor visual inspection

## Running Your Code
Install libraries and dependencies 
`pip install < requirements.txt`

Play the game
`python wormy.py`

Run the test suite
`pytest test_wormy.py -v`