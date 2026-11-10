"""
================================================================================
INSTRUCTOR TEST SUITE — Wormy
================================================================================
Run with:  pytest test_wormy.py -v
           pytest test_wormy.py -v --tb=short   (compact traceback)

Coverage:
  - getNewHead()          : all 4 directions
  - isWallCollision()     : all 4 walls, corners, safe interior positions
  - isSelfCollision()     : no collision, direct head-on-body, long snake spiral
  - hasEatenApple()       : hit, miss, adjacent cells
  - getScore()            : initial length, grown snake, minimum bound
  - isOppositeDirection() : all 6 direction pairs (4 opposites + 4 non-opposites)
  - Integration           : movement + growth + collision sequence
================================================================================

Provided — do not modify
"""

import pytest

# Import only the pure-logic functions — no Pygame display needed for these.
# Must NOT rename these functions.
from wormy import (
    getNewHead,
    isWallCollision,
    isSelfCollision,
    hasEatenApple,
    getScore,
    isOppositeDirection,
    CELLWIDTH,
    CELLHEIGHT,
    UP, DOWN, LEFT, RIGHT,
    HEAD,
)


# ─────────────────────────────────────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture
def short_worm():
    """A standard 3-segment horizontal worm at (10, 10)."""
    return [
        {'x': 10, 'y': 10},  # head
        {'x':  9, 'y': 10},
        {'x':  8, 'y': 10},
    ]

@pytest.fixture
def single_segment():
    """Edge case: worm with only one segment (the head)."""
    return [{'x': 5, 'y': 5}]

@pytest.fixture
def apple_at_head(short_worm):
    """Apple placed exactly where the head is."""
    return {'x': short_worm[HEAD]['x'], 'y': short_worm[HEAD]['y']}

@pytest.fixture
def apple_away(short_worm):
    """Apple placed far from the head."""
    return {'x': short_worm[HEAD]['x'] + 5, 'y': short_worm[HEAD]['y'] + 5}


# ─────────────────────────────────────────────────────────────────────────────
# Tests: getNewHead()
# ─────────────────────────────────────────────────────────────────────────────

class TestGetNewHead:

    def test_move_right(self, short_worm):
        """Moving RIGHT increments x by 1, y unchanged."""
        result = getNewHead(short_worm, RIGHT)
        assert result == {'x': 11, 'y': 10}

    def test_move_left(self, short_worm):
        """Moving LEFT decrements x by 1, y unchanged."""
        result = getNewHead(short_worm, LEFT)
        assert result == {'x': 9, 'y': 10}

    def test_move_up(self, short_worm):
        """Moving UP decrements y by 1 (y=0 is the top), x unchanged."""
        result = getNewHead(short_worm, UP)
        assert result == {'x': 10, 'y': 9}

    def test_move_down(self, short_worm):
        """Moving DOWN increments y by 1, x unchanged."""
        result = getNewHead(short_worm, DOWN)
        assert result == {'x': 10, 'y': 11}

    def test_returns_dict(self, short_worm):
        """Return type must be a dict with keys 'x' and 'y'."""
        result = getNewHead(short_worm, RIGHT)
        assert isinstance(result, dict)
        assert 'x' in result and 'y' in result

    def test_does_not_mutate_worm(self, short_worm):
        """getNewHead must not modify the original wormCoords list."""
        original = [dict(seg) for seg in short_worm]
        getNewHead(short_worm, UP)
        assert short_worm == original

    def test_move_from_origin(self):
        """Moving right from (0,0) gives (1,0)."""
        worm = [{'x': 0, 'y': 0}]
        assert getNewHead(worm, RIGHT) == {'x': 1, 'y': 0}


# ─────────────────────────────────────────────────────────────────────────────
# Tests: isWallCollision()
# ─────────────────────────────────────────────────────────────────────────────

class TestIsWallCollision:

    def test_no_collision_interior(self, short_worm):
        """Worm in the middle of the grid should not trigger wall collision."""
        assert isWallCollision(short_worm) is False

    def test_left_wall_exact(self):
        """x == -1 is out of bounds (just past the left wall)."""
        worm = [{'x': -1, 'y': 10}, {'x': 0, 'y': 10}]
        assert isWallCollision(worm) is True

    def test_right_wall_exact(self):
        """x == CELLWIDTH is out of bounds (just past the right wall)."""
        worm = [{'x': CELLWIDTH, 'y': 10}, {'x': CELLWIDTH - 1, 'y': 10}]
        assert isWallCollision(worm) is True

    def test_top_wall_exact(self):
        """y == -1 is out of bounds (just past the top wall)."""
        worm = [{'x': 10, 'y': -1}, {'x': 10, 'y': 0}]
        assert isWallCollision(worm) is True

    def test_bottom_wall_exact(self):
        """y == CELLHEIGHT is out of bounds (just past the bottom wall)."""
        worm = [{'x': 10, 'y': CELLHEIGHT}, {'x': 10, 'y': CELLHEIGHT - 1}]
        assert isWallCollision(worm) is True

    def test_top_left_corner_valid(self):
        """(0, 0) is the top-left cell — still inside the grid."""
        worm = [{'x': 0, 'y': 0}]
        assert isWallCollision(worm) is False

    def test_bottom_right_corner_valid(self):
        """(CELLWIDTH-1, CELLHEIGHT-1) is the bottom-right cell — still valid."""
        worm = [{'x': CELLWIDTH - 1, 'y': CELLHEIGHT - 1}]
        assert isWallCollision(worm) is False

    def test_top_left_corner_invalid(self):
        """(-1, -1) is outside the grid in both axes."""
        worm = [{'x': -1, 'y': -1}]
        assert isWallCollision(worm) is True

    def test_only_checks_head(self):
        """Wall collision is determined only by the head; body out-of-bounds is irrelevant."""
        # Head is valid; tail is out of bounds (shouldn't trigger collision)
        worm = [{'x': 5, 'y': 5}, {'x': -1, 'y': 5}]
        assert isWallCollision(worm) is False


# ─────────────────────────────────────────────────────────────────────────────
# Tests: isSelfCollision()
# ─────────────────────────────────────────────────────────────────────────────

class TestIsSelfCollision:

    def test_no_collision_normal(self, short_worm):
        """A straight 3-segment worm with no overlap."""
        assert isSelfCollision(short_worm) is False

    def test_head_on_body_segment(self):
        """Head overlaps a body segment — self collision detected."""
        worm = [
            {'x': 5, 'y': 5},  # head
            {'x': 6, 'y': 5},
            {'x': 6, 'y': 6},
            {'x': 5, 'y': 6},
            {'x': 5, 'y': 5},  # tail loops back to head position
        ]
        assert isSelfCollision(worm) is True

    def test_single_segment_no_collision(self, single_segment):
        """A single-segment worm cannot collide with itself."""
        assert isSelfCollision(single_segment) is False

    def test_two_segments_no_collision(self):
        """Two-segment worm; head ≠ tail."""
        worm = [{'x': 3, 'y': 3}, {'x': 2, 'y': 3}]
        assert isSelfCollision(worm) is False

    def test_head_does_not_collide_with_itself(self):
        """Head at index 0 must not be compared against index 0."""
        worm = [{'x': 5, 'y': 5}]
        assert isSelfCollision(worm) is False

    def test_long_worm_no_collision(self):
        """Straight 10-segment worm — no self overlap."""
        worm = [{'x': i, 'y': 0} for i in range(10, -1, -1)]
        assert isSelfCollision(worm) is False

    def test_collision_with_second_segment(self):
        """Head immediately collides with the segment right behind it."""
        worm = [
            {'x': 5, 'y': 5},
            {'x': 5, 'y': 5},  # same as head
        ]
        assert isSelfCollision(worm) is True


# ─────────────────────────────────────────────────────────────────────────────
# Tests: hasEatenApple()
# ─────────────────────────────────────────────────────────────────────────────

class TestHasEatenApple:

    def test_apple_at_head(self, short_worm, apple_at_head):
        """Apple on the exact same cell as the head → eaten."""
        assert hasEatenApple(short_worm, apple_at_head) is True

    def test_apple_away_from_head(self, short_worm, apple_away):
        """Apple far from the head → not eaten."""
        assert hasEatenApple(short_worm, apple_away) is False

    def test_apple_adjacent_right(self, short_worm):
        """Apple one cell to the right of the head → not eaten."""
        apple = {'x': short_worm[HEAD]['x'] + 1, 'y': short_worm[HEAD]['y']}
        assert hasEatenApple(short_worm, apple) is False

    def test_apple_adjacent_above(self, short_worm):
        """Apple one cell above the head → not eaten."""
        apple = {'x': short_worm[HEAD]['x'], 'y': short_worm[HEAD]['y'] - 1}
        assert hasEatenApple(short_worm, apple) is False

    def test_apple_at_body_not_head(self, short_worm):
        """Apple at a body segment (not head) → not eaten (head must touch)."""
        body_seg = short_worm[1]
        assert hasEatenApple(short_worm, body_seg) is False

    def test_apple_at_origin(self):
        """Edge case: apple and head both at (0, 0)."""
        worm  = [{'x': 0, 'y': 0}]
        apple = {'x': 0, 'y': 0}
        assert hasEatenApple(worm, apple) is True


# ─────────────────────────────────────────────────────────────────────────────
# Tests: getScore()
# ─────────────────────────────────────────────────────────────────────────────

class TestGetScore:

    def test_initial_score_zero(self, short_worm):
        """3-segment starting worm → score = 0."""
        assert getScore(short_worm) == 0

    def test_score_after_one_apple(self, short_worm):
        """4-segment worm (1 apple eaten) → score = 1."""
        short_worm.append({'x': 7, 'y': 10})  # grew by 1
        assert getScore(short_worm) == 1

    def test_score_after_five_apples(self, short_worm):
        """8-segment worm (5 apples eaten) → score = 5."""
        for i in range(5):
            short_worm.append({'x': 7 - i, 'y': 10})
        assert getScore(short_worm) == 5

    def test_score_never_negative(self):
        """Score of a 1-segment worm must not return negative."""
        worm = [{'x': 5, 'y': 5}]
        assert getScore(worm) >= 0


# ─────────────────────────────────────────────────────────────────────────────
# Tests: isOppositeDirection()
# ─────────────────────────────────────────────────────────────────────────────

class TestIsOppositeDirection:

    # True cases — genuine opposites
    def test_right_vs_left(self):
        assert isOppositeDirection(RIGHT, LEFT) is True

    def test_left_vs_right(self):
        assert isOppositeDirection(LEFT, RIGHT) is True

    def test_up_vs_down(self):
        assert isOppositeDirection(UP, DOWN) is True

    def test_down_vs_up(self):
        assert isOppositeDirection(DOWN, UP) is True

    # False cases — not opposites
    def test_right_vs_up(self):
        assert isOppositeDirection(RIGHT, UP) is False

    def test_right_vs_down(self):
        assert isOppositeDirection(RIGHT, DOWN) is False

    def test_up_vs_left(self):
        assert isOppositeDirection(UP, LEFT) is False

    def test_up_vs_right(self):
        assert isOppositeDirection(UP, RIGHT) is False

    def test_same_direction_not_opposite(self):
        """Moving in the same direction is NOT an opposite — allow it."""
        assert isOppositeDirection(RIGHT, RIGHT) is False

    def test_same_up_not_opposite(self):
        assert isOppositeDirection(UP, UP) is False


# ─────────────────────────────────────────────────────────────────────────────
# Integration tests — simulate game logic sequences
# ─────────────────────────────────────────────────────────────────────────────

class TestIntegration:

    def test_eat_apple_grows_worm(self):
        """
        Simulate one apple-eating cycle:
          getNewHead → prepend → detect eaten → do NOT delete tail.
        Worm length should increase by 1.
        """
        worm  = [{'x': 5, 'y': 5}, {'x': 4, 'y': 5}, {'x': 3, 'y': 5}]
        apple = {'x': 6, 'y': 5}   # one cell ahead (RIGHT)

        new_head = getNewHead(worm, RIGHT)
        worm.insert(0, new_head)   # prepend new head

        if hasEatenApple(worm, apple):
            apple = {'x': 10, 'y': 10}   # new apple (don't delete tail)
        else:
            del worm[-1]

        assert len(worm) == 4   # grew from 3 to 4
        assert getScore(worm) == 1

    def test_move_without_apple_same_length(self):
        """Normal move (no apple) keeps worm at the same length."""
        worm  = [{'x': 5, 'y': 5}, {'x': 4, 'y': 5}, {'x': 3, 'y': 5}]
        apple = {'x': 15, 'y': 15}  # far away

        new_head = getNewHead(worm, RIGHT)
        worm.insert(0, new_head)

        if not hasEatenApple(worm, apple):
            del worm[-1]

        assert len(worm) == 3   # unchanged
        assert worm[HEAD] == {'x': 6, 'y': 5}

    def test_wall_collision_after_move(self):
        """Worm at right edge moves RIGHT → wall collision on next check."""
        worm = [{'x': CELLWIDTH - 1, 'y': 5}, {'x': CELLWIDTH - 2, 'y': 5}]
        new_head = getNewHead(worm, RIGHT)
        worm.insert(0, new_head)
        del worm[-1]
        assert isWallCollision(worm) is True

    def test_self_collision_after_u_turn_sequence(self):
        """
        Worm doubles back: after adding a head that matches a body cell,
        isSelfCollision should return True.
        """
        # Create a worm shaped like a 'U' where the head is about to enter
        worm = [
            {'x': 3, 'y': 5},  # head
            {'x': 3, 'y': 6},
            {'x': 4, 'y': 6},
            {'x': 4, 'y': 5},  # this is where the new head will land
            {'x': 4, 'y': 4},
        ]
        # Simulate head moving LEFT into body cell at (3,5) — already the head,
        # so simulate the next step moving up to land on body
        new_head = getNewHead(worm, UP)  # {'x': 3, 'y': 4}
        worm.insert(0, new_head)
        del worm[-1]
        # Now manually place head on a body cell to confirm detection
        worm[0] = {'x': 4, 'y': 5}  # force overlap with index 3
        assert isSelfCollision(worm) is True

    def test_direction_guard_prevents_reversal(self):
        """
        Verify the direction-guard logic: if moving RIGHT, pressing LEFT
        should be ignored (isOppositeDirection returns True).
        """
        current_direction = RIGHT
        pressed_key_direction = LEFT
        if not isOppositeDirection(current_direction, pressed_key_direction):
            current_direction = pressed_key_direction
        assert current_direction == RIGHT   # direction must NOT have changed

        ##