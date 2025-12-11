from pytest import fixture

from aoc.day_10 import Machine, part_1, part_2


@fixture
def machines() -> list[Machine]:
    return list(map(Machine.parse, ['[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}',
                                    '[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}',
                                    '[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}']))


def test_part_1(machines: list[Machine]):
    assert part_1(machines) == 7


def test_part_2(machines: list[Machine]):
    assert part_2(machines) == 33
