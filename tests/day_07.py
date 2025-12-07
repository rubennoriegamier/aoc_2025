from pytest import fixture

from aoc.day_07 import part_1, part_2


@fixture
def diagram() -> list[str]:
    return ['.......S.......',
            '...............',
            '.......^.......',
            '...............',
            '......^.^......',
            '...............',
            '.....^.^.^.....',
            '...............',
            '....^.^...^....',
            '...............',
            '...^.^...^.^...',
            '...............',
            '..^...^.....^..',
            '...............',
            '.^.^.^.^.^...^.',
            '...............']


def test_part_1(diagram: list[str]):
    assert part_1(diagram) == 21


def test_part_2(diagram: list[str]):
    assert part_2(diagram) == 40
