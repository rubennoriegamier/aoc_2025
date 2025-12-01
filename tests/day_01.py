from pytest import fixture

from aoc.day_01 import part_1, part_2


@fixture
def puzzle_input() -> list[str]:
    return ['L68',
            'L30',
            'R48',
            'L5',
            'R60',
            'L55',
            'L1',
            'L99',
            'R14',
            'L82']


def test_part_1(puzzle_input: list[str]) -> None:
    assert part_1(puzzle_input) == 3


def test_part_2(puzzle_input: list[str]) -> None:
    assert part_2(puzzle_input) == 6
