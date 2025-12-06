import fileinput
from functools import reduce
from operator import add, mul


def main():
    puzzle_input: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))


def part_1(puzzle_input: list[str]) -> int:
    return sum(reduce(add if operator == '+' else mul, map(int, operands), 0 if operator == '+' else 1)
               for *operands, operator in zip(*map(str.split, puzzle_input)))


def part_2(puzzle_input: list[str]) -> int:
    width = max(map(len, puzzle_input))
    op = add
    total = 0
    acc = 0

    for *digits, op_symbol in zip(*(line.ljust(width) for line in puzzle_input)):
        if digits := ''.join(digits).strip():
            if op_symbol == '+':
                op = add
                total += acc
                acc = 0
            elif op_symbol == '*':
                op = mul
                total += acc
                acc = 1
            acc = op(acc, int(digits))

    return total + acc


if __name__ == '__main__':
    main()
