import fileinput

import numpy as np


def main():
    grid: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(grid))
    print(part_2(grid))


def part_1(grid: list[str]) -> int:
    grid = np.array([[cell == '@' for cell in row]
                     for row in grid], dtype=np.uint8)
    grid = np.pad(grid, 1)
    conv = np.lib.stride_tricks.sliding_window_view(grid, (3, 3)).sum(axis=(2, 3))
    le_4 = conv <= 4
    np.logical_and(le_4, grid[1:-1, 1:-1], out=le_4)

    return int(le_4.sum(dtype=np.uint32))


def part_2(grid: list[str]) -> int:
    grid = np.array([[cell == '@' for cell in row]
                     for row in grid], dtype=np.uint8)
    grid = np.pad(grid, 1)
    conv = np.empty_like(grid[1:-1, 1:-1])
    le_4 = np.empty_like(conv, dtype=bool)
    rolls = 0

    while True:
        np.lib.stride_tricks.sliding_window_view(grid, (3, 3)).sum(axis=(2, 3), out=conv)
        np.less_equal(conv, 4, out=le_4)
        np.logical_and(le_4, grid[1:-1, 1:-1], out=le_4)
        if (diff := le_4.sum(dtype=np.uint32)) == 0:
            return int(rolls)
        grid[1:-1, 1:-1][le_4] = 0
        rolls += diff


if __name__ == '__main__':
    main()
