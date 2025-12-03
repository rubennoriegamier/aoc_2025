from pytest import fixture

from aoc.day_03 import parse_bank, part_1, part_2


@fixture
def banks() -> list[list[int]]:
    return list(map(parse_bank, ['987654321111111',
                                 '811111111111119',
                                 '234234234234278',
                                 '818181911112111']))


def test_part_1(banks) -> None:
    assert part_1(banks) == 357


def test_part_2(banks) -> None:
    assert part_2(banks) == 3121910778619
