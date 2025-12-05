from pytest import fixture

from aoc.day_05 import parse_fresh_range, part_1, part_2


@fixture
def fresh_ranges() -> list[range]:
    return list(map(parse_fresh_range, ['3-5',
                                        '10-14',
                                        '16-20',
                                        '12-18']))


@fixture
def ingredient_ids() -> list[int]:
    return [1, 5, 8, 11, 17, 32]


def test_part_1(fresh_ranges: list[range], ingredient_ids: list[int]) -> None:
    assert part_1(fresh_ranges, ingredient_ids) == 3


def test_part_2(fresh_ranges: list[range]) -> None:
    assert part_2(fresh_ranges) == 14
