import fileinput
from bisect import bisect
from itertools import combinations, islice

from shapely import Polygon, box, covers

type Tile = tuple[int, int]


def main():
    tiles: list[Tile] = list(map(parse_tile, fileinput.input()))

    print(part_1(tiles))
    print(part_2(tiles))


def parse_tile(raw_value: str) -> Tile:
    x, y = raw_value.split(',')

    return int(x), int(y)


def part_1(tiles: list[Tile]) -> int:
    return max((abs(x_2 - x_1) + 1) * (abs(y_2 - y_1) + 1)
               for (x_1, y_1), (x_2, y_2) in combinations(tiles, 2))


# noinspection PyTypeChecker
def part_2(tiles: list[Tile]) -> int | None:
    polygon = Polygon(tiles)
    rects = sorted(combinations(tiles, 2), reverse=True,
                   key=lambda r: (abs(r[1][0] - r[0][0]) + 1) * (abs(r[1][1] - r[0][1]) + 1))
    sorted_tiles = sorted(tiles)

    # noinspection PyInconsistentReturns
    for (x_1, y_1), (x_2, y_2) in rects:
        x_1, x_2 = sorted([x_1, x_2])
        y_1, y_2 = sorted([y_1, y_2])

        for x, y in islice(sorted_tiles, bisect(sorted_tiles, (x_1 + 1,)), None):
            if x < x_2 and y_1 < y < y_2:
                break
        else:
            if covers(polygon, box(x_1, y_1, x_2, y_2)):
                return (x_2 - x_1 + 1) * (y_2 - y_1 + 1)


if __name__ == '__main__':
    main()
