import fileinput

import numpy as np


def main():
    grid: list[str] = list(map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(grid), sep='\n')


def part_1_and_2(grid: list[str]) -> tuple[int, int]:
    grid = np.array([[cell == '@' for cell in row]
                     for row in grid], dtype=np.int8)
    grid = np.pad(grid, 1)
    conv = np.lib.stride_tricks.sliding_window_view(grid, (3, 3)).sum(axis=(2, 3))
    le_4 = np.empty_like(conv, dtype=bool)
    rolls = []

    while True:
        np.less_equal(conv, 4, out=le_4)
        np.logical_and(le_4, grid[1:-1, 1:-1], out=le_4)
        if (diff := le_4.sum(dtype=np.uint32)) == 0:
            return rolls[0], sum(rolls)
        grid[1:-1, 1:-1][le_4] = 0

        y_a, y_z = np.flatnonzero(le_4.any(1))[[0, -1]]
        x_a, x_z = np.flatnonzero(le_4.any(0))[[0, -1]]

        conv_ = conv[max(0, y_a - 1):y_z + 2, max(0, x_a - 1):x_z + 2]
        le_4_ = le_4[max(0, y_a - 1):y_z + 2, max(0, x_a - 1):x_z + 2]

        conv_[:-1, :-1][le_4_[1:, 1:]] -= 1
        conv_[:-1, :][le_4_[1:, :]] -= 1
        conv_[:-1, 1:][le_4_[1:, :-1]] -= 1
        conv_[:, :-1][le_4_[:, 1:]] -= 1
        conv_[:, 1:][le_4_[:, :-1]] -= 1
        conv_[1:, :-1][le_4_[:-1, 1:]] -= 1
        conv_[1:, :][le_4_[:-1, :]] -= 1
        conv_[1:, 1:][le_4_[:-1, :-1]] -= 1

        rolls.append(int(diff))


if __name__ == '__main__':
    main()
