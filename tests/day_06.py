from pytest import fixture

from aoc.day_06 import part_1, part_2


@fixture
def puzzle_input() -> list[str]:
    return ['123 328  51 64',
            ' 45 64  387 23',
            '  6 98  215 314',
            '*   +   *   +']


def test_part_1(puzzle_input: list[str]):
    assert part_1(puzzle_input) == 4277556


def test_part_2(puzzle_input: list[str]):
    assert part_2(puzzle_input) == 3263827
