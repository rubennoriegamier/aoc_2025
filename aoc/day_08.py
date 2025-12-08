import fileinput
from functools import reduce
from operator import mul

import numpy as np

type JunkBox = tuple[int, int, int]
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import DisjointSet


def main():
    junk_boxes: list[JunkBox] = list(map(parse_junk_box, fileinput.input()))

    print(*part_1_and_2(junk_boxes, 1_000), sep='\n')


def parse_junk_box(raw_value: str) -> JunkBox:
    # noinspection PyTypeChecker
    return tuple(map(int, raw_value.split(',')))


def part_1_and_2(junk_boxes: list[JunkBox], pairs_count: int) -> tuple[int, int]:
    distance_idxs = np.argsort(pdist(junk_boxes, metric='euclidean'))
    jb_a_idxs, jb_b_idxs = np.triu_indices(len(junk_boxes), 1)
    jb_a_idxs = jb_a_idxs[distance_idxs]
    jb_b_idxs = jb_b_idxs[distance_idxs]
    networks = DisjointSet(junk_boxes)
    part_1 = 0
    part_2 = 0

    for i in range(len(jb_a_idxs)):
        jb_a = junk_boxes[jb_a_idxs[i]]
        jb_b = junk_boxes[jb_b_idxs[i]]

        networks.merge(jb_a, jb_b)

        if i == pairs_count - 1:
            part_1 = reduce(mul, sorted(map(len, networks.subsets()))[-3:])
        elif networks.n_subsets == 1:
            part_2 = jb_a[0] * jb_b[0]
            break

    return part_1, part_2


if __name__ == '__main__':
    main()
