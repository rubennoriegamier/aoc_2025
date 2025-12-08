from pytest import fixture

from aoc.day_08 import JunkBox, parse_junk_box, part_1_and_2


@fixture
def junk_boxes() -> list[JunkBox]:
    return list(map(parse_junk_box, ['162,817,812',
                                     '57,618,57',
                                     '906,360,560',
                                     '592,479,940',
                                     '352,342,300',
                                     '466,668,158',
                                     '542,29,236',
                                     '431,825,988',
                                     '739,650,466',
                                     '52,470,668',
                                     '216,146,977',
                                     '819,987,18',
                                     '117,168,530',
                                     '805,96,715',
                                     '346,949,466',
                                     '970,615,88',
                                     '941,993,340',
                                     '862,61,35',
                                     '984,92,344',
                                     '425,690,689']))


def test_part_1(junk_boxes: list[JunkBox]):
    assert part_1_and_2(junk_boxes, 10)[0] == 40


def test_part_2(junk_boxes: list[JunkBox]):
    assert part_1_and_2(junk_boxes, 10)[1] == 25272
