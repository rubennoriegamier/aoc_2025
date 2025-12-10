from pytest import fixture

from aoc.day_09 import Tile, parse_tile, part_1, part_2


@fixture
def tiles() -> list[Tile]:
    return list(map(parse_tile, ['7,1',
                                 '11,1',
                                 '11,7',
                                 '9,7',
                                 '9,5',
                                 '2,5',
                                 '2,3',
                                 '7,3']))


def test_part_1(tiles: list[Tile]):
    assert part_1(tiles) == 50


def test_part_2(tiles: list[Tile]):
    assert part_2(tiles) == 24
