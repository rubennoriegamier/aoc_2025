import fileinput


def main():
    puzzle_input: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))


def part_1(puzzle_input: list[str]) -> int:
    dial = 50
    zeros = 0

    for direction, *rotation in puzzle_input:
        rotation = int(''.join(rotation))

        if direction == 'R':
            dial = (dial + rotation) % 100
        elif direction == 'L':
            dial = (dial - rotation) % 100

        if dial == 0:
            zeros += 1

    return zeros


def part_2(puzzle_input: list[str]) -> int:
    dial = 50
    zeros = 0

    for direction, *rotation in puzzle_input:
        rotation = int(''.join(rotation))

        if direction == 'R':
            zeros += (dial + rotation) // 100
            dial = (dial + rotation) % 100
        elif direction == 'L':
            zeros += (100 - dial + rotation) // 100 - (dial == 0)
            dial = (dial - rotation) % 100

    return zeros


if __name__ == '__main__':
    main()
