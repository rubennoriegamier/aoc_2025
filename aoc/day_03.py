import fileinput
from functools import reduce


def main():
    banks: list[list[int]] = list(map(parse_bank, map(str.rstrip, fileinput.input())))

    print(part_1(banks))
    print(part_2(banks))


def parse_bank(raw_bank: str) -> list[int]:
    return list(map(int, raw_bank))


def bank_joltage(bank: list[int], size: int) -> int:
    batteries = reduce(lambda b, i: b + [max(range(b[-1] + 1, len(bank) - (size - i - 1)), key=bank.__getitem__)],
                       range(size), [-1])[1:]

    return sum(bank[batteries[i]] * 10 ** (size - i - 1) for i in range(size))


def part_1(banks: list[list[int]]) -> int:
    return sum(bank_joltage(bank, 2) for bank in banks)


def part_2(banks: list[list[int]]) -> int:
    return sum(bank_joltage(bank, 12) for bank in banks)


if __name__ == '__main__':
    main()
