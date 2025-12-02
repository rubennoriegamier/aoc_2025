from pytest import fixture

from aoc.day_02 import parse_range, invalid_ids_sum, part_1_invalid_ids, part_2_invalid_ids


@fixture
def ranges() -> list[range]:
    return list(map(parse_range, ['11-22',
                                  '95-115',
                                  '998-1012',
                                  '1188511880-1188511890',
                                  '222220-222224',
                                  '1698522-1698528',
                                  '446443-446449',
                                  '38593856-38593862',
                                  '565653-565659',
                                  '824824821-824824827',
                                  '2121212118-2121212124']))


def test_part_1(ranges) -> None:
    assert invalid_ids_sum(ranges, part_1_invalid_ids()) == 1227775554


def test_part_2(ranges) -> None:
    assert invalid_ids_sum(ranges, part_2_invalid_ids()) == 4174379265
