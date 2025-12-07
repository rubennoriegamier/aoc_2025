import fileinput
from functools import cache


def main():
    diagram: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(diagram))
    print(part_2(diagram))


def part_1(diagram: list[str]) -> int:
    splits = set()
    beams = {(0, diagram[0].find('S'))}

    while beams:
        if (beam := beams.pop()) not in splits:
            y, x = beam
            if 0 <= y < len(diagram) and 0 <= x < len(diagram[0]):
                if diagram[y][x] == '^':
                    splits.add(beam)
                    beams.add((y, x - 1))
                    beams.add((y, x + 1))
                else:
                    beams.add((y + 1, x))

    return len(splits)


def part_2(diagram: list[str]) -> int:
    @cache
    def move_downward(y: int, x: int) -> int:
        return next((move_downward(y, x - 1) + move_downward(y, x + 1)
                     for y in range(y, len(diagram)) if diagram[y][x] == '^'), 1)

    return move_downward(0, diagram[0].find('S'))


if __name__ == '__main__':
    main()
