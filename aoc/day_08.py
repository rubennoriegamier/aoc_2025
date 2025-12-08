import fileinput
from dataclasses import dataclass
from functools import reduce
from itertools import combinations
from operator import mul
from time import perf_counter
from typing import Self


def main():
    junk_boxes: list[JunkBox] = list(map(JunkBox.parse, fileinput.input()))

    t_1 = perf_counter()
    print(*part_1_and_2(junk_boxes, 1_000), sep='\n')
    t_2 = perf_counter()
    print(round((t_2 - t_1) * 1_000, 3))


@dataclass(frozen=True, slots=True)
class JunkBox:
    x: int
    y: int
    z: int

    @classmethod
    def parse(cls, raw_value: str) -> Self:
        return cls(*map(int, raw_value.split(',')))

    def distance_to(self, other: Self) -> int:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2


def part_1_and_2(junk_boxes: list[JunkBox], pairs_count: int) -> tuple[int, int]:
    pairs = sorted(combinations(junk_boxes, 2), key=lambda pair: pair[0].distance_to(pair[1]))
    networks = []
    part_1 = 0
    part_2 = 0

    for i, (jb_a, jb_b) in enumerate(pairs, 1):
        networks_ = []
        network_a = {jb_a, jb_b}

        for network_b in networks:
            if network_a.isdisjoint(network_b):
                networks_.append(network_b)
            else:
                network_a.update(network_b)
        networks_.append(network_a)

        networks = networks_

        if i == pairs_count:
            part_1 = reduce(mul, sorted(map(len, networks))[-3:])
        elif len(networks[0]) == len(junk_boxes):
            part_2 = jb_a.x * jb_b.x
            break

    return part_1, part_2


if __name__ == '__main__':
    main()
