import fileinput
from collections import deque
from dataclasses import dataclass
from functools import reduce
from itertools import combinations
from operator import mul
from typing import Self


def main():
    junk_boxes: list[JunkBox] = list(map(JunkBox.parse, fileinput.input()))

    print(*part_1_and_2(junk_boxes, 1_000), sep='\n')


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
    networks = deque()
    part_1 = 0
    part_2 = 0

    for i, (jb_a, jb_b) in enumerate(pairs, 1):
        network = {jb_a, jb_b}

        for _ in range(len(networks)):
            if network.isdisjoint(networks[0]):
                networks.rotate(-1)
            else:
                network.update(networks.popleft())
        networks.append(network)

        if i == pairs_count:
            part_1 = reduce(mul, sorted(map(len, networks))[-3:])
        elif len(networks[0]) == len(junk_boxes):
            part_2 = jb_a.x * jb_b.x
            break

    return part_1, part_2


if __name__ == '__main__':
    main()
