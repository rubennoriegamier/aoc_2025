from pytest import fixture

from aoc.day_04 import part_1_and_2


@fixture
def grid() -> list[str]:
    return ['..@@.@@@@.',
            '@@@.@.@.@@',
            '@@@@@.@.@@',
            '@.@@@@..@.',
            '@@.@@@@.@@',
            '.@@@@@@@.@',
            '.@.@.@.@@@',
            '@.@@@.@@@@',
            '.@@@@@@@@.',
            '@.@.@@@.@.']


def test_part_1(grid: list[str]) -> None:
    assert part_1_and_2(grid)[0] == 13


def test_part_2(grid: list[str]) -> None:
    assert part_1_and_2(grid)[1] == 43
