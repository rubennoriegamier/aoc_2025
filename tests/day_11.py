from pytest import fixture

from aoc.day_11 import Devices, parse_devices, part_1, part_2


@fixture
def devices_part_1() -> Devices:
    return parse_devices(['aaa: you hhh',
                          'you: bbb ccc',
                          'bbb: ddd eee',
                          'ccc: ddd eee fff',
                          'ddd: ggg',
                          'eee: out',
                          'fff: out',
                          'ggg: out',
                          'hhh: ccc fff iii',
                          'iii: out'])


@fixture
def devices_part_2() -> Devices:
    return parse_devices(['svr: aaa bbb',
                          'aaa: fft',
                          'fft: ccc',
                          'bbb: tty',
                          'tty: ccc',
                          'ccc: ddd eee',
                          'ddd: hub',
                          'hub: fff',
                          'eee: dac',
                          'dac: fff',
                          'fff: ggg hhh',
                          'ggg: out',
                          'hhh: out'])


def test_part_1(devices_part_1: Devices):
    assert part_1(devices_part_1) == 5


def test_part_2(devices_part_2: Devices):
    assert part_2(devices_part_2) == 2
