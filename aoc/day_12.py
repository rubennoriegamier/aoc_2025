import fileinput


def main():
    regions: list[str] = [line.rstrip() for line in fileinput.input() if 'x' in line]

    print(part_1(regions))


def part_1(regions: list[str]) -> int:
    valid = 0

    for size, *counts in map(str.split, regions):
        width, height = map(int, size[:-1].split('x'))
        width = width // 3 * 3
        height = height // 3 * 3
        if width * height >= sum(map(int, counts)) * 9:
            valid += 1

    return valid


if __name__ == '__main__':
    main()
