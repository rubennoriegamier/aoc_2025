import fileinput
from itertools import combinations, pairwise

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
    rects = sorted(combinations(tiles, 2), reverse=True,
                   key=lambda r: (abs(r[1][0] - r[0][0]) + 1) * (abs(r[1][1] - r[0][1]) + 1))
    sorted_segments = sorted(((min(x_3, x_4), min(y_3, y_4)),
                              (max(x_3, x_4), max(y_3, y_4)))
                             for (x_3, y_3), (x_4, y_4) in pairwise(tiles + [tiles[0]]))
    next_segments = {x: [sg for sg in sorted_segments if sg[1][0] > x]
                     for (_, _), (x, _) in sorted_segments}

    # noinspection PyInconsistentReturns
    for (x_1, y_1), (x_2, y_2) in rects:
        x_1, x_2 = sorted([x_1, x_2])
        y_1, y_2 = sorted([y_1, y_2])

        for (x_3, y_3), (_, y_4) in next_segments[x_1]:
            if x_3 < x_2 and y_4 > y_1 and y_3 < y_2:
                break
        else:
            return (x_2 - x_1 + 1) * (y_2 - y_1 + 1)


if __name__ == '__main__':
    main()
